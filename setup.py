# setup.py

from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='0.1',
    author = 'Aishik Ghosh',
    packages=find_packages(),
    install_requires=[ 'pandas==1.4.4'
        # Add any dependencies here if needed
    ],
)
