#!/usr/bin/env python3
"""
A application for dealing with files in a variety of ways. Helpful for parsing 
and dealing with large numbers of files.
"""

import click
import logging
import os
import re

tag_regex = re.compile(r"^[a-zA-Z0-9_]+\=[a-zA-Z0-9_]+$")


@click.group()
def cli():
    pass


def verify_tag(tag):
    """
    Verify that the tag is in the correct format.
    """
    if not tag:
        return {"error": "Tag cannot be empty."}
    if len(tag) > 255:
        return {"error": "Tag cannot be longer than 255 characters."}
    if not tag_regex.match(tag):
        return {"error": "Tag must be in the format key=value."}

    return True


def add_tag_to_file(file, tag):
    """
    Add a tag to a file.
    """
    try:

        if os.path.exists(file):
            if os.path.exists(f"{file}.tagdata"):
                with open(f"{file}.tagdata", "r") as f:
                    if tag in f.read():
                        return {}

            with open(f"{file}.tagdata", "w") as f:
                # check to see if the tag is already in the file
                f.write(f"{tag}\n")
    except Exception as e:
        logging.error(e)


@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
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

    if not verify_tag(tag):
        return {"error": verify_tag(tag)}

    # check to see if the supplied path value is a file or a directory
    if os.path.isfile(path):
        # if it is a file then add the tag to the file
        add_tag_to_file(path, tag)


@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to remove.")
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
    
    #check to see if the tag is in the tagdata file
    if not os.path.exists(f".{path}.tagdata"):
        return {"error": f"File {path} does not have any tags."}
    
    #check to see if the tag is in the tagdata file
    if not tag in open(f".{path}.tagdata").read():
        return {"error": f"File {path} does not have the tag {tag}."}
    else:
        #remove the tag from the file
        with open(f".{path}.tagdata", "r") as f:
            lines = f.readlines()
        with open(f".{path}.tagdata", "w") as f:
            for line in lines:
                if line.strip("\n") != tag:
                    f.write(line)
    # if the length of the stripped file is 0 then remove the file
    if os.stat(f".{path}.tagdata").st_size == 0:
        os.remove(f".{path}.tagdata")

    
@cli.command()
@click.option("--path", default=".", help="Path to file.")
@click.option("--tag", default=".", help="Tag to add.")
def tagall(path: str, tag: str):
    """
    Tag all files in a directory with a keyword.

    path of the file to tag
    tag to add to the file

    """
    print("Tagging all files in a directory...")

    # check to see if the file exists is it doesnt then return an error
    if not os.path.exists(path):
        return {"error": f"File {path} does not exist."}

    if not verify_tag(tag):
        return {"error": verify_tag(tag)}

    # check to see if the supplied path value is a file or a directory
    if os.path.isdir(path):
        # if it is a directory then add the tag to all files in the directory
        for file in os.listdir(path):
            add_tag_to_file(file, tag)


def main():
    cli()

if __name__ == "__main__":
    cli()
