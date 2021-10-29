""" Validate task-status options """
from click.testing import CliRunner
from task_status.task_status import main as task_main
from task_status.task_status import __version__ as task_version

runner = CliRunner()


def test_main():
    """Validate the basic command runs with a successful response"""
    response = runner.invoke(task_main)
    assert response.exit_code == 0


def test_version():
    """Verify that --version outputs the version and it matches
    what the code says it should be"""
    response = runner.invoke(task_main, ["--version"])
    assert response.exit_code == 0
    assert task_version in response.output


def test_uuid():
    """Validate the --uuid option returns successfully"""
    response = runner.invoke(task_main, ["--uuid"])
    assert response.exit_code == 0


def test_sort():
    """Validate --sort returns successfully"""
    response = runner.invoke(task_main, ["--sort"])
    assert response.exit_code == 0


def test_header():
    """Validate --header returns successfully"""
    response = runner.invoke(task_main, ["--header"])
    assert response.exit_code == 0


def test_help():
    """Validate --help returns successfully"""
    response = runner.invoke(task_main, ["--help"])
    assert response.exit_code == 0


def test_invalid_option():
    """Validate pasing a bad option returns an error"""
    # check that task fails successfully!"
    response = runner.invoke(task_main, ["--invalid"])
    assert response.exit_code == 2
