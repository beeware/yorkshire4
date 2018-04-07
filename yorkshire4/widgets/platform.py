import sys
from functools import lru_cache

import toga


@lru_cache(maxsize=8)
def get_platform_factory(factory=None):
    """ This function figures out what the current host platform is and
    imports the adequate factory. The factory is the interface to all platform
    specific implementations.

    Args:
        factory (:obj:`module`): (optional) Provide a custom factory that is automatically returned unchanged.

    Returns: The suitable factory for the current host platform
        or the factory that was given as a argument.

    Raises:
        RuntimeError: If no supported hots platform can be identified.
    """
    if factory is not None:
        return factory

    if sys.platform == 'ios':
        from . import iOS as factory
    elif sys.platform == 'tvos':
        from . import tvOS as factory
    elif sys.platform == 'watchos':
        from . import watchOS as factory
    elif sys.platform == 'android':
        from . import android as factory
    elif sys.platform == 'darwin':
        from . import cocoa as factory
    elif sys.platform == 'linux':
        from . import gtk as factory
    elif sys.platform == 'win32':
        from . import winforms as factory
    else:
        raise RuntimeError("Couldn't identify a supported host platform.")

    return factory
