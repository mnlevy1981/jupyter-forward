#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.rst') as f:
    long_description = f.read()

setup(
    maintainer='Xdev',
    maintainer_email='xdev@ucar.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='Jupyter Port Forwarding Utility',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description=long_description,
    include_package_data=True,
    keywords='jupyter-forward',
    name='jupyter-forward',
    packages=find_packages(include=['jupyter_forward', 'jupyter_forward.*']),
    entry_points={
        'console_scripts': [
            'jupyter-forward = jupyter_forward.core:main',
            'jlab-forward = jupyter_forward.core:main',
        ]
    },
    url='https://github.com/NCAR/jupyter_forward',
    project_urls={
        'Documentation': 'https://github.com/NCAR/jupyter_forward',
        'Source': 'https://github.com/NCAR/jupyter_forward',
        'Tracker': 'https://github.com/NCAR/jupyter_forward/issues',
    },
    zip_safe=False,
)