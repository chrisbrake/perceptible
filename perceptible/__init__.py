from .observable import Observable
from .observableDictionary import ObservableDictionary
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = ['Observable', 'ObservableDictionary']
