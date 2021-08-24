#!/usr/bin/env python
""" Get completed tasks from taskwarrior and output a simple report """
import subprocess
import json
import itertools
import operator
from datetime import date
from dateutil.relativedelta import relativedelta, MO
import click

__version__ = "0.2.1"


@click.command()
@click.version_option(__version__, prog_name="task-status")
@click.option("--uuid", is_flag=True, help="Display the task UUID")
@click.option("--header", is_flag=True, help="Display date header")
def main(uuid, header):
    """Main function that does all the work for task_status"""
    today = date.today()
    last_monday = today + relativedelta(weekday=MO(-2))

    task_command = [
        "task",
        f"end.after:{last_monday}",
        "export",
        "status_report:display",
        "-home",
        "-deleted",
    ]
    tasks = subprocess.run(
        task_command,
        capture_output=True,
        check=True,
    )

    entries = json.loads(tasks.stdout.decode())
    output_list = []
    project_list = []
    if header:
        print(f"Reporting from: {last_monday}")
    for status_projects, status_entries in itertools.groupby(
        entries, key=operator.itemgetter("project")
    ):
        project_list.append(status_projects)
        output_list.append(list(status_entries))
    for project in project_list:
        print(f"* {project}")
        for entry in entries:
            if entry["project"] == project and uuid:
                print(f'\t* {entry["description"]} ({entry["uuid"]})')
            if entry["project"] == project:
                print(f'\t* {entry["description"]}')


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
