__author__ = 'wnilsen'

from setuptools import setup

setup(
    name='python-c3',
    version='0.0.1',
    description="Python wrapper for the C3js D3 plotting library.",
    long_description="",
    author='Wayne Nilsen',
    author_email='waynenilsen@gmail.com',
    license='MIT',
    packages=['pyc3'],
    zip_safe=False,
    install_requires=[
        'numpy'
        , 'pandas'
    ]
)