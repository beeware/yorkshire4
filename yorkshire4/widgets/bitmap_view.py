from travertino.colors import rgb

import toga
from toga.handlers import wrapped_handler

from .platform import get_platform_factory


class BitmapView(toga.Widget):
    def __init__(self, id=None, size=(320, 200), style=None,
                 on_key_press=None, enabled=True, factory=None):
        super().__init__(
            id=id, enabled=enabled, style=style,
            factory=get_platform_factory(factory=factory)
        )

        self._size = size
        self._impl = self.factory.BitmapView(interface=self)
        self.on_key_press = on_key_press

    @property
    def size(self):
        return self._size

    def set(self, x, y, color):
        self._impl.set(x, y, color)

    def get(self, x, y):
        return rgb(self._impl.get(x, y))

    def __enter__(self):
        self._impl.suspend_updates()
        return self

    def __exit__(self, type, value, traceback):
        self._impl.resume_updates()

    @property
    def on_key_press(self):
        """The handler to invoke when a key is pressed.

        Returns:
            The function ``callable`` that is called on key press.
        """
        return self._on_key_press

    @on_key_press.setter
    def on_key_press(self, handler):
        """Set the handler to invoke when a key is pressed.

        Args:
            handler (:obj:`callable`): The handler to invoke when a key
            is pressed.
        """
        self._on_key_press = wrapped_handler(self, handler)
        self._impl.set_on_key_press(self._on_key_press)
