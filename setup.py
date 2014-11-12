__author__ = 'wnilsen'

from setuptools import setup

long_descr = open('README.MD').read()

setup(
    name='python-c3',
    version='0.0.1',
    description="Python wrapper for the C3js D3 plotting library.",
    long_description=long_descr,
    author='Wayne Nilsen',
    author_email='waynenilsen@gmail.com',
    license='MIT',
    packages=['pyc3'],
    zip_safe=False,
    install_requires=[]
)