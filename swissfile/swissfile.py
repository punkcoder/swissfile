#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""

import click


@click.group()
def cli():
	pass


@cli.command()
def tag():
	"""
	Tag a file with a keyword.
	"""
	print("Tagging a file...")
	pass

cli.add_command(tag)