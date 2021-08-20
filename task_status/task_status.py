#!/usr/bin/env python
""" Get completed tasks from taskwarrior and output a simple report """
import subprocess
import json
from datetime import date
from dateutil.relativedelta import relativedelta, MO
import click

__version__ = "0.2.0"


@click.command()
@click.version_option(__version__, prog_name="task-status")
@click.option("--uuid", is_flag=True, help="Display the task UUID")
@click.option("--header", is_flag=True, help="Display date header")
def main(uuid, header):
    """Main function that does all the work for task_status"""
    today = date.today()
    last_monday = today + relativedelta(weekday=MO(-2))

    tasks = subprocess.run(
        [
            "task",
            f"end.after:{last_monday}",
            "export",
            "-home",
            "status_report:display",
        ],
        capture_output=True,
        check=True,
    )

    entries = json.loads(tasks.stdout.decode())
    last_project = ""
    if header:
        print(f"Reporting from: {last_monday}")
    for entry in entries:
        if entry["project"] != last_project:
            last_project = entry["project"]
            print(f"* {entry['project']}")
        if uuid:
            print(f"\t* {entry['description']} ({entry['uuid']})")
        else:
            print(f"\t* {entry['description']}")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
