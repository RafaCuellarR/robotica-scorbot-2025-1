from setuptools import find_packages
from setuptools import setup

setup(
    name='scorbot_bringup',
    version='0.0.0',
    packages=find_packages(
        include=('scorbot_bringup', 'scorbot_bringup.*')),
)
