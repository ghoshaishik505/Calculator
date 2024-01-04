# setup.py

from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='0.3',
    author = 'Aishik Ghosh',
    packages=find_packages(),
    install_requires=[ 'pandas'
        # Add any dependencies here if needed
    ],
)
