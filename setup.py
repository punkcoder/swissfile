from setuptools import setup

setup(
    name="swissfile",
    version="0.1",
    py_modules=["src.swissfile.cli", "src.swissfile.tagging"],
    packages=["src.swissfile", "src.tests"],
    entry_points={
        "console_scripts": [
            "swissfile = src.swissfile.cli:cli",
        ]
    },
    install_requires=[
        "Click",
    ],
    test_suite="src.tests",
)
