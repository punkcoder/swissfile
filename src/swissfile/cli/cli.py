#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""
import click
from tagging import tagall, tag, untag

@click.group()
def cli():
    pass

@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
def tag(path: str, tag: str):
   tag(path, tag)


@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to remove.")
def untag(path: str, tag: str):
    untag(path, tag)

    
@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
def tagall(path: str, tag: str):
    tagall(path, tag)


def main():
    cli()

if __name__ == "__main__":
    cli()
