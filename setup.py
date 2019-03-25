import sys
from setuptools import setup

setup(name='python3-cycler' if sys.argv[1] == "bdist_rpm" else "cycler",
      version='0.10.0',
      author='Thomas A Caswell',
      author_email='matplotlib-users@python.org',
      py_modules=['cycler'],
      description='Composable style cycles',
      url='http://github.com/matplotlib/cycler',
      platforms='Cross platform (Linux, Mac OSX, Windows)',
      install_requires=['six'],
      license="BSD",
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
      keywords='cycle kwargs',
      )
