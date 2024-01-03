from setuptools import setup

setup(
    name="swissfile",
    version="0.1",
    py_modules=["src.swissfile.cli"],
    packages=[
        "src.swissfile.cli",
        "src.swissfile.tagging", 
        "src.tests"
        ],
    entry_points={
        "console_scripts": [
            "swissfile = src.swissfile.cli:main",
        ]
    },
    install_requires=[
        "Click",
    ],
    test_suite="src.tests",
)
