from setuptools import setup

setup(
    name='rtb', # research toolbox
    version='0.0.1',
    description='Tools I found useful during my research',
    url='https://github.com/ruchtem/toolbox',
    author='Michael Ruchte',
    author_email='ruchtem@cs.uni-freiburg.de',
    packages=[
        'rtb',
    ],
    install_requires=[
        "numpy",
    ],
    license='MIT',
    zip_safe=False,
    test_suite = 'tests',
)