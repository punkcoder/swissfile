#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""

import click
import logging


@click.group()
def cli():
    pass


@cli.command()
@click.option("--path", default=".", help="Path to file.")
def tag(path: str, tag: str) -> dict:
    """
    Tag a file with a keyword.

    path of the file to tag
    tag to add to the file

    """
    print("Tagging a file...")


if __name__ == "__main__":
    cli()
