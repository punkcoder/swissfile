#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""

import click
import logging
import os


@click.group()
def cli():
    pass


@cli.command()
@click.option("--path", default=".", help="Path to file.")
def tag(path: str, tag: str):
    """
    Tag a file with a keyword.

    path of the file to tag
    tag to add to the file

    """
    print("Tagging a file...")

    # check to see if the file exists is it doesnt then return an error
    if not os.path.exists(path):
        return {"error": f"File {path} does not exist."}


@cli.command()
@click.option("--path", default=".", help="Path to file.")
def untag(path: str, tag: str):
	"""
	Remove a tag from a file.

	path of the file to tag
	tag to add to the file

	"""
	print("Removing a tag from a file...")

	# check to see if the file exists is it doesnt then return an error
	if not os.path.exists(path):
		return {"error": f"File {path} does not exist."}

if __name__ == "__main__":
    cli()
