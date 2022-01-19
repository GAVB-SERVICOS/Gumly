# CHANGELOG

This file follows [semantic versioning 2.0.0](https://semver.org/). Given a version number MAJOR.MINOR.PATCH, increment
the:

- **MAJOR** version when you make incompatible API changes,
- **MINOR** version when you add functionality in a backwards compatible manner, and
- **PATCH** version when you make backwards compatible bug fixes.

As a heuristic:

- if you fix a bug, increment the PATCH
- if you add a feature (add keyword arguments with default values, add a new object, a new mechanism for parameter setup
  that is backwards compatible, etc.), increment the MINOR version
- if you introduce a breaking change (removing arguments, removing objects, restructuring code such that it affects
  imports, etc.), increment the MAJOR version

The general format is:

```

# VERSION - DATE (dd/mm/yyyy)
### Features and improvements
- module alpha.py
  - A: brief description of A.
  - B: brief description of B.
- module beta.py
  - C: brief description of C.

### Fixes
- module alpha.py:
  - New fixed behavior #1 
  - New fixed behavior #2

### Deprecated
- module alpha.py
  - function A
  - argument B of function C

```

# 0.1.0 - DATE (xx/xx/2022)

### Added

- ..features added..