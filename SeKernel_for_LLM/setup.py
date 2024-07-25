from setuptools import setup

setup(
    author="Perpendicular AI",
    author_email = "support@perpendicular.web.za",
    name="sekernel",
    version="0.0.1",
    long_description=open('README.md').read(),
    install_requires=[
        'bs4',
        'nltk',
    ],
)