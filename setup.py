from setuptools import setup

setup(
    name = 'leveldict',
    version = '0.2',
    description = 'LevelDB dict-like wrappers.',
    author = 'Rolando Espinoza La fuente',
    author_email = 'darkrho@gmail.com',
    url = 'https://github.com/darkrho/leveldict',
    license = 'BSD',
    py_modules = ['leveldict', 'leveldbm'],
    install_requires = ['leveldb'],
    classifiers = [
      'Programming Language :: Python',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
    ],
)
