from setuptools import setup
from Cython.Build import cythonize
setup(version="0.0.1", name="fastadd", ext_modules=cythonize("fastadd.pyx"))