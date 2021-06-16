from setuptools import find_packages, setup
setup(
    name='mlutils',
    packages=find_packages(include=['mlutils']),
    version='0.1.0',
    description='My first Python library test',
    author='GAVB',
    install_requires=[],
    setup_requires=['pytest_runner'],
    tests_require=['pytest== 6.2.4'],
    tests_suite='tests',
)