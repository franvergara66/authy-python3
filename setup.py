from authy import __version__
from setuptools import setup, find_packages

# to install authy type the following command:
#     python setup.py install
#

setup(
    name = "authy",
    version = __version__,
    description = "Authy API Client",
    author = "Authy Inc",
    author_email = "dev-support@authy.com",
    url = "https://github.com/smontoya/authy-python3",
    keywords = ["authy", "two factor", "authentication", "python3"],
    install_requires = ["requests>=2.2.1", "simplejson>=3.4.0"],
    packages = find_packages(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security"
        ],
    long_description = """\
    Authy API Client for Python
""" )
