from setuptools import find_packages, setup


VERSION = open('VERSION').read()
LONG_DESCRIPTION = open('README.md').read()


with open("requirements.txt", "r") as fp:
    reqs = fp.read().split("\n")


setup(
    name="gumly",
    packages=find_packages(include=["gumly"]),
    version=VERSION,
    description="Gumly",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="GAVB Servicos de Informatica LTDA",
    install_requires=reqs,
    setup_requires=["pytest_runner"],
    tests_require=["pytest== 6.2.4"],
    tests_suite="tests",
)
