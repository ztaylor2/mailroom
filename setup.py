"""The setup for mailroom project in python."""
from setuptools import setup

setup(
    name="mailroom",
    description="A Python implementation of a mailroom donation tracking app.",
    version=0.1,
    author="Zach Taylor & Michael Shinners",
    author_email="zacharymtaylor3@gmail.com & michaelshinners@gmail.com",
    license='MIT',
    py_modules=['mailroom'],
    install_requires=['tabulate'],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
        ]
    }
)
