import pytest
import os
import click
from pytest_click import cli_runner


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    if not os.path.exists("tests/"):
        os.mkdir("tests/")

    if os.path.exists("tests/testfile.txt"):
        print('Removing previous test files...')
        os.remove("tests/testfile.txt")

    with open("tests/testfile.txt", "w") as f:
        print('Creating a test file...')
        f.write("This is a test file.")

    yield

    if os.path.exists("tests/testfile.txt"):
        print('Removing the test file...')
        os.remove("tests/testfile.txt")
    
    if os.path.exists("tests/testfile.txt.tagdata"):
        print('Removing the test file...')
        os.remove("tests/testfile.txt.tagdata")


def test_verify_tag_empty():
    from src.swissfile.tagging import verify_tag

    result = verify_tag("")
    assert result["error"] == "Tag cannot be empty."


def test_verify_tag_too_long():
    from src.swissfile.tagging import verify_tag

    result = verify_tag("a" * 256)
    assert result["error"] == "Tag cannot be longer than 255 characters."


def test_verify_tag_invalid_format():
    from src.swissfile.tagging import verify_tag

    result = verify_tag("test")
    assert result["error"] == "Tag must be in the format key=value."


def test_verify_tag_valid():
    from src.swissfile.tagging import verify_tag

    result = verify_tag("test=test")
    assert result == True




def test_untag_missing_file(cli_runner):
    from src.swissfile.cli import tag

    result = cli_runner.invoke(
        tag, ["--path", "tests/testfile.txt", "--tag", "test=test"]
    )

    result = cli_runner.invoke(
        tag, ["--path", "tests/testfile.txt", "--tag", "test=test"]
    )
    # check that the test=test tag is not added twice
    with open("tests/testfile.txt.tagdata", "r") as f:
        assert f.read().count("test=test") == 1

def test_add_tag_to_all_files(cli_runner):
    from src.swissfile.cli import tagall

    result = cli_runner.invoke(
        tagall, ["--path", "tests", "--tag", "test=test"]
    )
    assert result.exit_code == 0

    with open("tests/testfile.txt.tagdata", "r") as f:
        assert "test=test" in f.read()