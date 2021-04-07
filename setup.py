from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.0.1'

setup(
    name='toolbox',
    version=_VERSION,
    description='Tools I found useful during my research',
    long_description=_README_MD,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/ruchtem/toolbox',
    author='Michael Ruchte',
    author_email='ruchtem@cs.uni-freiburg.de',
    packages=find_packages(),
    package_dir = {"":"toolbox"},
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=[
        "numpy",
        "fvcore",
        "pillow",
    ],
    include_package_data=True,
    license='MIT',
    python_requires=">=3.6",
)