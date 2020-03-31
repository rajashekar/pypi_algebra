# Pypi publish
The purpose of this project is to understand how python is created and published to Pypi.

## To create environment 
python -m venv basic_algebra

## Activating environment
source basic_algebra/bin/activate

## Building distribution
```
python setup.py sdist

running sdist
running egg_info
creating raj_algebra.egg-info
writing raj_algebra.egg-info/PKG-INFO
writing dependency_links to raj_algebra.egg-info/dependency_links.txt
writing top-level names to raj_algebra.egg-info/top_level.txt
writing manifest file 'raj_algebra.egg-info/SOURCES.txt'
reading manifest file 'raj_algebra.egg-info/SOURCES.txt'
writing manifest file 'raj_algebra.egg-info/SOURCES.txt'
running check
warning: check: missing required meta-data: url

warning: check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) must be supplied

creating raj_algebra-0.1
creating raj_algebra-0.1/raj_algebra
creating raj_algebra-0.1/raj_algebra.egg-info
copying files to raj_algebra-0.1...
copying README.md -> raj_algebra-0.1
copying setup.py -> raj_algebra-0.1
copying raj_algebra/Algebra.py -> raj_algebra-0.1/raj_algebra
copying raj_algebra/__init__.py -> raj_algebra-0.1/raj_algebra
copying raj_algebra.egg-info/PKG-INFO -> raj_algebra-0.1/raj_algebra.egg-info
copying raj_algebra.egg-info/SOURCES.txt -> raj_algebra-0.1/raj_algebra.egg-info
copying raj_algebra.egg-info/dependency_links.txt -> raj_algebra-0.1/raj_algebra.egg-info
copying raj_algebra.egg-info/not-zip-safe -> raj_algebra-0.1/raj_algebra.egg-info
copying raj_algebra.egg-info/top_level.txt -> raj_algebra-0.1/raj_algebra.egg-info
Writing raj_algebra-0.1/setup.cfg
creating dist
Creating tar archive
removing 'raj_algebra-0.1' (and everything under it)
```

## Installing twine
pip install twine


## Testing without installation 
```
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from raj_algebra import Algebra
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'raj_algebra'
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
```

# Commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ distributions

```
Python 3.7.4 (default, Aug 13 2019, 15:17:50)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from raj_algebra import Algebra
>>> a = Algebra()
>>> a.addition(1,2)
3
>>> a.subtraction(22,2)
20
>>> a.multiplication(2,3)
6
>>> a.division(6,2)
3.0
>>> exit()
```


## Command to upload to the pypi repository
twine upload dist/*
pip install distributions

## Test cases
```
 python -m unittest test

 ....
----------------------------------------------------------------------
Ran 4 tests in 0.013s

OK
```
