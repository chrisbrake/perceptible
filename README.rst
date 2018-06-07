perceptible
===========

Observable versions of python data structures

|Build Status| |Coverage Status| |Docs Status| |Package Status|

.. |Build Status| image:: https://travis-ci.org/chrisbrake/perceptible.svg?branch=master
   :target: https://travis-ci.org/chrisbrake/perceptible
.. |Coverage Status| image:: https://coveralls.io/repos/github/chrisbrake/perceptible/badge.svg?branch=master
   :target: https://coveralls.io/github/chrisbrake/perceptible?branch=master
.. |Docs Status| image:: https://readthedocs.org/projects/perceptible/badge/?version=latest
   :target: https://perceptible.readthedocs.io/en/latest/
.. |Package Status| image:: https://badge.fury.io/py/perceptible.svg
    :target: https://badge.fury.io/py/perceptible

.. quick-start-section-marker

This library is meant to be API compatible with standard Python objects, but with the addition of observability.  Currently supports Lists and Dictionaries.

A simple use looks like this:

.. code-block:: python

    >>> from perceptible import ObservableDictionary
    >>> def observer(o):
    ...     print('observer was called with', o)
    ...
    >>> o_dict = ObservableDictionary()
    >>> o_dict.add_observer(observer)
    >>> o_dict['key'] = 'value'
    observer was called with {'key': 'value'}


Installation is as simple as installing via pip.

.. code-block:: bash

    pip install perceptible
