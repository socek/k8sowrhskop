from setuptools import find_packages
from setuptools import setup

setup(
    name="Faker",
    version="0.1",
    description="",
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    long_description=__doc__,
    author='Dominik "Socek" Długajczyk',
    author_email="dominik.dlugajczyk@netguru.com",
    license="Apache 2.0",
    zip_safe=False,
    url="http://github.com/socek/iep",
    entry_points={
        "paste.app_factory": ["main = faker:main"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
