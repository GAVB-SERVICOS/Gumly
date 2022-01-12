## Contributing to MLUtils

**Thank you for considering contributing to MLUtils! You can contribute in so many ways like: code, answering questions, implementing functions, examples and documentation.**

Please keep in mind the following guidelines and practices when contributing:

1. For new features create a PR to `dev` branch. In case of hotfix create a PR to `main` branch.
1. Use `make format` to format the repository code. `make format` maps to a usage of
   [black](https://github.com/psf/black), and the repository adheres to whatever `black` uses as its strict pep8 format.
   No questions asked
1. Use `make verify` to lint, run tests, and typecheck on the project
1. Add unit tests for any new code you write
1. Add an example, or extend an existing example, with any new features you may add
1. For hotfix increment the version in the [VERSION](https://github.com/GAVB-SERVICOS/mlutils/blob/main/VERSION) file. A
   [CHANGELOG](https://github.com/GAVB-SERVICOS/mlutils/blob/main/CHANGELOG.md) entry is expected along with
   version increases! For new features that will be done in the next releases by one of our engineers.
