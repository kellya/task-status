#!/usr/bin/env python
import subprocess
import json
from datetime import date
from dateutil.relativedelta import relativedelta, MO


def main():
    today = date.today()
    last_monday = today + relativedelta(weekday=MO(-2))

    tasks = subprocess.run(
        ["task", "+status", f"end.after:{last_monday}", "export"], capture_output=True
    )

    entries = json.loads(tasks.stdout.decode())
    last_project = ""
    for entry in entries:
        if entry["project"] != last_project:
            last_project = entry["project"]
            print(f"* {entry['project']}")
        print(f"\t* {entry['description']}")


if __name__ == "__main__":
    main()
