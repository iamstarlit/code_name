from setuptools import setup

__project__ = "mood"
__version__ = "0.0.1"
__description__ = "A Python sentiment module that responds depending on your state"
__packages__ = ["sentiment"]
__author__ = "namestarlit"
__author_email__ = "rainson.work@gmail.com"
__classifiers__ = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: Freeware",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Education :: Testing",
        ]
__keywords__ = ["sentiment", "mood", "learning", "motivation"]
__url__ = "https://github.com/namestarlit/mood"


setup(
    name=__project__,
    version=__version__,
    description=__description__,
    packages=__packages__,
    author=__author__,
    author_email=__author_email__,
    classifiers=__classifiers__,
    keywords=__keywords__,
    url=__url__,
)
