leveldict
=========

LevelDB dict-like wrappers.

Requirements
------------

* `LevelDB`_
* `py-leveldb`_

Usage
-----

Basic usage::

  >>> from leveldict import LevelDict
  >>> db = LevelDict('mydb')
  >>> db['key'] = 'value'

Storing serialized values::

  >>> import json
  >>> from leveldict import LevelDictSerialized
  >>> db = LevelDictSerialized('mydb', serializer=json)
  >>> db['key'] = {'foo': [True, None]}

DBM-like interface::

  >>> import leveldbm
  >>> db = leveldbm.open('mydb', 'c')

Write batch support::

  >>> with db.write_batch() as wb:
  ...   wb['foo'] = 'bar'
  ...   del wb['baz']
  ...   wb['bob'].pop()


.. note:: This code haven't been used in production. Use at your own risk!

.. _LevelDB: http://code.google.com/p/leveldb/
.. _py-leveldb: http://code.google.com/p/py-leveldb/

