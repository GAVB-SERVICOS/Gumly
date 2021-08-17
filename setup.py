from setuptools import find_packages, setup
import mlutils


with open('requirements.txt', 'r') as f:
    reqs = f.read().split('\n')

setup(
    name='mlutils',
    packages=find_packages(include=['mlutils']),
    version=mlutils.__version__,
    description='My first Python library test',
    author='GAVB',
    install_requires=[],
    setup_requires=['pytest_runner'],
    tests_require=reqs,
    tests_suite='tests',
)