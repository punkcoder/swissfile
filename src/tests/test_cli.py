import pytest
import os
import click
from pytest_click import cli_runner


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
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



def test_tag_import():
    from src.swissfile.cli import tag



def test_untag_import():
    from src.swissfile.cli import untag



def test_untag_missing_file(cli_runner):
    from src.swissfile.cli import untag

    result = cli_runner.invoke(untag, ["--path", "tests/missing.txt", "--tag", "test"])
    assert result.exit_code == 0


def test_tag_missing_file(cli_runner):
    from src.swissfile.cli import tag

    result = cli_runner.invoke(tag, ["--path", "tests/missing.txt", "--tag", "test"])
    assert result.exit_code == 0


def test_add_tag_to_file(cli_runner):
    from src.swissfile.cli import tag

    result = cli_runner.invoke(tag, ["--path", "tests/testfile.txt", "--tag", "test=test"])

    with open("tests/testfile.txt.tagdata", "r") as f:
        assert "test=test" in f.read()
