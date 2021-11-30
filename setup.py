from setuptools import find_packages, setup

with open("requirements.txt", "r") as fp:
    reqs = fp.read().split("\n")[:-1]


setup(
    name="mlutils",
    packages=find_packages(include=["mlutils"]),
    version="1.0.0",
    description="MLUtils release 1.0.0",
    author="GAVB Servicos de Informatica LTDA",
    install_requires=reqs,
    setup_requires=["pytest_runner"],
    tests_require=["pytest== 6.2.4"],
    tests_suite="tests",
)
