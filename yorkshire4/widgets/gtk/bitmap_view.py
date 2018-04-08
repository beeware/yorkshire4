from gi.repository import Gtk, Gdk, GdkPixbuf
from travertino.size import at_least

# from toga_gtk.keys import toga_key
from toga_gtk.widgets.base import Widget


class BitmapView(Widget):
    COMPONENTS_PER_PIXEL = 3

    def create(self):
        # Allocate a memory buffer to store pixel data.
        self.memory_stride = self.interface.size[0] * self.COMPONENTS_PER_PIXEL
        self.memory_size = self.memory_stride * self.interface.size[1]
        self.memory = bytearray(self.memory_size)

        # Create an image from the pixel buffer.
        self.native = Gtk.Image.new_from_pixbuf(self.create_pixbuf())

        # Current state of redraw updates
        self._suspended = 0
        self._update_pending = False

    def create_pixbuf(self):
        pixbuf = GdkPixbuf.Pixbuf.new_from_data(
            data=self.memory,
            colorspace=GdkPixbuf.Colorspace.RGB,
            has_alpha=False,
            bits_per_sample=8,
            width=self.interface.size[0],
            height=self.interface.size[1],
            rowstride=self.memory_stride,
            destroy_fn=None,
            destroy_fn_data=None,
        )
        return pixbuf

    def _key_press(self, widget, ev, data=None):
        if self.interface.on_key_press:
            pass
            # self.interface.on_key_press(
            #     self.interface,
            #     **toga_key(event.keyCode, event.modifierFlags)
            # )

    def set_on_key_press(self, handler):
        pass

    def rehint(self):
        self.interface.intrinsic.width = at_least(self.interface.size[0])
        self.interface.intrinsic.height = at_least(self.interface.size[1])

    def set(self, x, y, color):
        offset = (
            x * self.COMPONENTS_PER_PIXEL + (y * self.memory_stride)
        )
        self.memory[offset] = color.r
        self.memory[offset + 1] = color.g
        self.memory[offset + 2] = color.b

        self.update_display()

    def get(self, x, y, color):
        offset = (
            x * self.COMPONENTS_PER_PIXEL + (y * self.memory_stride)
        )
        return (
            int(self.memory[offset]),
            int(self.memory[offset + 1]),
            int(self.memory[offset + 2]),
        )

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
            self.native.set_from_pixbuf(self.create_pixbuf())
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
                self.native.set_from_pixbuf(self.create_pixbuf())
                self._update_pending = False
