from setuptools import setup

setup(
    name="swissfile",
    version="0.1",
    py_modules=["swissfile"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        swissfile=swissfile:cli
    """,
)
