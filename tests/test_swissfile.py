import pytest
import os
import click
from pytest_click import cli_runner


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    if os.path.exists("tests/testfile.txt"):
        os.remove("tests/testfile.txt")

    with open("tests/testfile.txt", "w") as f:
        f.write("This is a test file.")

    yield

    if os.path.exists("tests/testfile.txt"):
        os.remove("tests/testfile.txt")


def test_tag_import():
    from swissfile.swissfile import tag

def test_untag_import():
    from swissfile.swissfile import untag


def test_untag_missing_file(cli_runner):
    from swissfile.swissfile import untag
    result = cli_runner.invoke(untag, ["--path", "tests/missing.txt", "--tag", "test"])
    assert result.exit_code != 0 
    
    
def test_tag_missing_file(cli_runner):
    from swissfile.swissfile import tag
    result = cli_runner.invoke(tag, ["--path", "tests/missing.txt", "--tag", "test"])
    assert result.exit_code != 0
    
    
