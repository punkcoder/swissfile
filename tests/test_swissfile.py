import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    if os.path.exists("tests/testfile.txt"):
        os.remove("tests/testfile.txt")

    with open("tests/testfile.txt", "w") as f:
        f.write("This is a test file.")

    yield

    if os.path.exists("tests/testfile.txt"):
        os.remove("tests/testfile.txt")


def test_tag():
    from swissfile.swissfile import tag


def test_untag():
    from swissfile.swissfile import untag


def test_tagged_missing_file():
    from swissfile.swissfile import tagged
