#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""
import click
from .tagging import command_tagall, command_tag, command_untag

@click.group()
def cli():
    pass

@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
def tag(path: str, tag: str):
   command_tag(path, tag)


@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to remove.")
def untag(path: str, tag: str):
    command_untag(path, tag)

    
@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
def tagall(path: str, tag: str):
    command_tagall(path, tag)


def main():
    cli()

if __name__ == "__main__":
    cli()
