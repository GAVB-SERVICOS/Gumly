from setuptools import find_packages, setup

# Read requirements.txt and transform in a list.
with open("requirements.txt", "r") as fp:
    reqs = fp.read().split("\n")[:-1]


setup(
    name="mlutils",
    packages=find_packages(include=["mlutils"]),
    version="0.1.0",
    description="My first Python library test",
    author="GAVB",
    install_requires=reqs,
    setup_requires=["pytest_runner"],
    tests_require=["pytest== 6.2.4"],
    tests_suite="tests",
)
