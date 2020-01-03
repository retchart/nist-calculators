#!/usr/bin/python
"""
"""
import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fh:
    long_description = fh.read()

NUMPY_MIN_VERSION = '1.8.2'
SCIPY_MIN_VERSION = '1.3.1'
# PANDAS_MIN_VERSION = ''
MATPLOTLIB_MIN_VERSION = '3.1.1'
PYTABLES_MIN_VERSION = '3.5.1'

setuptools.setup(
    name="nist-calculator",
    version="0.0.2",
    author="Mikhail Zelenyi",
    author_email="mihail.zelenyy@phystech.edu",
    url='http://npm.mipt.ru/',
    description="Python implementaion of NIST XCOM",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="phd",
    packages=["xcom"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    # project_urls={
    #     "Bug Tracker": "",
    #     "Documentation": "",
    #     "Source Code": "",
    # },
    install_requires=[
        'numpy>={0}'.format(NUMPY_MIN_VERSION),
        'scipy>={0}'.format(SCIPY_MIN_VERSION),
        'matplotlib>={0}'.format(MATPLOTLIB_MIN_VERSION),
        'tables>={0}'.format(PYTABLES_MIN_VERSION),

    ],
    test_suite='tests',
    package_data = {
        'xcom' : ["data/NIST_XCOM.hdf5"]
    }
)
