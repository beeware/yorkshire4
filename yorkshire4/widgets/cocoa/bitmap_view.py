from ctypes import (
    c_double, c_void_p, c_ubyte, c_size_t, c_bool, c_ulong, POINTER, c_long
)

from rubicon.objc import CGRect, objc_method
from rubicon.objc.types import register_preferred_encoding
from travertino.size import at_least

from toga_cocoa.keys import toga_key
from toga_cocoa.libs import core_graphics, NSView, NSRect, NSGraphicsContext
from toga_cocoa.widgets.base import Widget


######################################################################
# CoreGraphics constants
######################################################################

kCGBitmapByteOrderDefault = 0
kCGImageAlphaNone = 0
kCGRenderingIntentDefault = 0

######################################################################
# CoreGraphics data types
######################################################################

CGFloat = c_double
CGBitmapInfo = c_ulong
CGColorRenderingIntent = c_long

CGContextRef = c_void_p
register_preferred_encoding(b'^{__CGContext=}', CGContextRef)

CGDataProviderRef = c_void_p
register_preferred_encoding(b'^{__CGDataProvider=}', CGDataProviderRef)

CGColorSpaceRef = c_void_p
register_preferred_encoding(b'^{__CGColorSpace=}', CGColorSpaceRef)

CGImageRef = c_void_p
register_preferred_encoding(b'^{__CGImage=}', CGImageRef)

######################################################################
# CoreGraphics methods
######################################################################

core_graphics.CGDataProviderCreateWithData.argtypes = [
    c_void_p, c_void_p, c_size_t, c_void_p
]
core_graphics.CGDataProviderCreateWithData.restype = CGDataProviderRef

core_graphics.CGColorSpaceCreateDeviceRGB.argtypes = []
core_graphics.CGColorSpaceCreateDeviceRGB.restype = CGColorSpaceRef

core_graphics.CGImageCreate.argtypes = [
    c_size_t, c_size_t, c_size_t, c_size_t, c_size_t,
    CGColorSpaceRef, CGBitmapInfo, CGDataProviderRef,
    POINTER(CGFloat), c_bool, CGColorRenderingIntent
]
core_graphics.CGImageCreate.restype = CGImageRef

core_graphics.CGContextDrawImage.argtypes = [
    CGContextRef, CGRect, CGImageRef
]
core_graphics.CGContextDrawImage.restype = None


######################################################################
# Cocoa native widget implementation
######################################################################

class TogaBitmapView(NSView):
    @objc_method
    def drawRect_(self, rect: NSRect) -> None:
        cg_context = NSGraphicsContext.currentContext.CGContext

        data_provider = core_graphics.CGDataProviderCreateWithData(
            None, self._impl.memory, self._impl.memory_size, None
        )
        image = core_graphics.CGImageCreate(
            self.interface.size[0],
            self.interface.size[1],
            self._impl.BITS_PER_COMPONENT,
            self._impl.BITS_PER_COMPONENT * self._impl.COMPONENTS_PER_PIXEL,
            self._impl.COMPONENTS_PER_PIXEL * self.interface.size[0],
            self._impl.rgb_colorspace,
            kCGBitmapByteOrderDefault | kCGImageAlphaNone,
            data_provider, None, False, kCGRenderingIntentDefault)

        core_graphics.CGContextDrawImage(cg_context, rect, image)

    @objc_method
    def acceptsFirstResponder(self) -> bool:
        return True

    @objc_method
    def isFlipped(self) -> bool:
        return True

    @objc_method
    def keyDown_(self, event) -> None:
        if self.interface.on_key_press:
            self.interface.on_key_press(
                self.interface,
                **toga_key(event.keyCode, event.modifierFlags)
            )

    # @objc_method
    # def flagsChanged_(self, event) -> None:
    #     if self.interface.on_key_press:
    #         old_modifiers = self.modifiers
    #         self.modifiers = toga_modifiers(event.modifierFlags)
    #         mods_press = self.modifiers - old_modifiers
    #         # mods_release = old_modifiers - self.modifiers

    #         if mods_press:
    #             self.interface.on_key_press(
    #                 self.interface,
    #                 modifiers=self.modifiers
    #             )
    #         elif mods_release:
    #             self.interface.on_key_release(
    #                 self.interface,
    #                 modifiers=self.modifiers
    #             )

######################################################################
# Cocoa widget implementation
######################################################################

class BitmapView(Widget):
    COMPONENTS_PER_PIXEL = 3
    BITS_PER_COMPONENT = 8

    def create(self):
        self.native = TogaBitmapView.alloc().init()
        self.native._impl = self
        self.native.interface = self.interface

        self.rgb_colorspace = core_graphics.CGColorSpaceCreateDeviceRGB()

        # Current state of redraw updates
        self._suspended = 0
        self._update_pending = False

        # Allocate a memory buffer, initialized to 0
        self.memory_stride = self.interface.size[0] * self.COMPONENTS_PER_PIXEL
        self.memory_size = self.interface.size[1] * self.memory_stride
        self.memory = (self.memory_size * c_ubyte)()

        # Add the layout constraints
        self.add_constraints()

    def set_on_key_press(self, handler):
        pass

    def rehint(self):
        self.interface.intrinsic.width = at_least(self.interface.size[0])
        self.interface.intrinsic.height = at_least(self.interface.size[1])

    def set(self, x, y, color):
        offset = (
            x * self.COMPONENTS_PER_PIXEL + (
                (self.interface.size[1] - y - 1) * self.memory_stride
            )
        )

        self.memory[offset] = color.r
        self.memory[offset + 1] = color.g
        self.memory[offset + 2] = color.b
        self.update_display()

    def get(self, x, y, color):
        offset = (
            x * self.COMPONENTS_PER_PIXEL + (
                (self.interface.size[1] - y - 1)
                * (self.COMPONENTS_PER_PIXEL * self.interface.size[0])
            )
        )
        return (self.memory[offset], self.memory[offset + 1], self.memory[offset + 2])

    def suspend_updates(self):
        """Temporarily suspend updates on the bitmap view.

        Operates as a stack; multiple suspend operations will
        increase the suspension "depth". Updates will only
        resume when the depth returns to 0.
        """
        self._suspended += 1

    def update_display(self):
        """Request an update of the bitmap display.

        The update may be suspended if the
        """
        if self._suspended:
            self._update_pending = True
        else:
            self.native.needsDisplay = True
            self._update_pending = False

    def resume_updates(self):
        """Reduce the suspension depth by 1 level.

        Operates as a stack; multiple suspend operations will
        increase the suspension "depth". Updates will only
        resume when the depth returns to 0.
        """
        if self._suspended > 0:
            self._suspended -= 1

        if self._suspended == 0:
            if self._update_pending:
                self.native.needsDisplay = True
                self._update_pending = False
