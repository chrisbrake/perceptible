"""
.. automodule:: perceptible.observableDictionary
    :members:
    :undoc-members:
    :show-inheritance:
"""
from .observableDictionary import ObservableDictionary
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = [ObservableDictionary]
