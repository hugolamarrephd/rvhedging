import os
from setuptools import setup, find_packages

# Cython and numpy must be installed first!
from Cython.Build import cythonize
import numpy as np


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# All directories containing Cython code
extensions_dir = []

setup(
    name="rvhedging",
    version="0.0.0",
    author="Hugo Lamarre",
    author_email="hugolamarre.phd@gmail.com",
    description='Code for "The Economic Value of Volatility Timing using Realized Volatility for Hedged S&P 500 Index Options"',
    license="MIT",
    keywords=[
        "quantitative finance",  "GARCH",
        "volatility", "arch", "ARCH",
        "option", "derivatives",
        "call", "put",
        "volatility risk premium",
        "hedging", "risk",
        "realized volatility", "realized variance",
        "MEM", "HEAVY"
    ],
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers="""
            Development Status :: 1 - Planning
            Intended Audience :: Science/Research
            Intended Audience :: Financial and Insurance Industry
            License :: OSI Approved :: MIT License
            Programming Language :: Python :: 3.7 :: Only
            Programming Language :: Cython
            Topic :: Scientific/Engineering :: Mathematics
            """,
    project_urls={
        "Source Code": "https://github.com/hugolamarrephd/rvhedging"
    },
    setup_requires=[
        'cython',
        'numpy'
    ],
    python_requires='>=3.7',
    install_requires=[],  # Dependencies handled by Pipfile (via pipenv install)
    ext_modules=cythonize(
        [x + '*.pyx' for x in extensions_dir],
        annotate=True
    ),
    include_dirs=[np.get_include()]
)
