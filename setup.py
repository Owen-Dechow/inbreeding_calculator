from setuptools import setup
from pathlib import Path

long_description = Path("README.md").read_text(encoding="utf-8")

setup(
    name="inbreeding_calculator",  # str
    version="1.0.0",  # str
    description="Calculate the inbreeding coefficient of a pedigree in Python.",  # str
    long_description=long_description,  # str
    long_description_content_type="text/markdown",  # str
    author="Owen Dechow",  # str
    author_email="owen.dechow@gmail.com",  # str
    url="https://github.com/Owen-Dechow/inbreeding-python",  # str
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    py_modules=["inbreeding_calculator"],
    license="MIT license",  # str
)
