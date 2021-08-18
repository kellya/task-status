from task_status.task_status import main as task_main
from task_status.task_status import __version__ as task_version
from click.testing import CliRunner

runner = CliRunner()


def test_main():
    if task_main:
        response = runner.invoke(task_main)
        assert response.exit_code == 0


def test_version():
    response = runner.invoke(task_main, ["--version"])
    assert response.exit_code == 0
    assert task_version in response.output


def test_uuid():
    response = runner.invoke(task_main, ["--uuid"])
    assert response.exit_code == 0
