#!/usr/bin/env python

from setuptools import setup


# Modified from http://stackoverflow.com/questions/2058802/
# how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
def version():
    import os
    import re

    init = os.path.join('gor4', '__init__.py')
    with open(init) as fp:
        initData = fp.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]",
                      initData, re.M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError('Unable to find version string in %r.' % init)


setup(name='gor4',
      version=version(),
      packages=['gor4'],
      include_package_data=True,
      url='https://github.com/acorg/gor4',
      download_url='https://github.com/acorg/gor4',
      author='Terry Jones, Barbara Muehlemann',
      author_email='tcj25@cam.ac.uk',
      keywords=['GOR4 amino acid structure prediction'],
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT',
      description=('Python class providing an interface to GOR4 amino acid '
                   'structure prediction C code.'),
      install_requires=['cffi>=1.0.0'],
      setup_requires=['cffi>=1.0.0'],
      cffi_modules=['./src/build.py:ffi'])
