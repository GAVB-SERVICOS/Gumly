from setuptools import find_packages, setup


VERSION = open('VERSION').read()
LONG_DESCRIPTION = open('README.md').read()


with open("requirements.txt", "r") as fp:
    reqs = fp.read().split("\n")[:-1]


setup(
    name="mlutils",
    packages=find_packages(include=["mlutils"]),
    version=VERSION,
    description="MLUtils release 1.0.0",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="GAVB Servicos de Informatica LTDA",
    install_requires=reqs,
    setup_requires=["pytest_runner"],
    tests_require=["pytest== 6.2.4"],
    tests_suite="tests",
)
