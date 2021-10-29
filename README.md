# task-status

This utility allows you to generate a list of tasks completed from task warrior
over the last week.

# Installation

Task-status is published in PyPi, so to install you just need to run `pip
install task-status`.  This will give you the `task-status` entry point to
execute.

## Prerequirements

In order for this to work, you need to have taskwarrior installed to track
tasks.  Addtitionally, taskwarrior needs an additiona "User Defined
Attribute"(UDA) to define the boolean for displaying a task in the report

### Taskwarrior

All of the data comes from taskwarrior, so In order for this to work, [Taskwarrior](https://taskwarrior.org/download/) must
be set up first.

### User-Defined Attribute

The following must be added to your taskrc file.

```
uda.status_report.type=string
uda.status_report.label=status_report
uda.status_report.values=display,hide
uda.status_report.default=display
```

You may either do that by copying and pasting that directly in your taskrc file,
or by running the following:

`task config uda.status_report.type string`

`task config uda.status_report.label status_report`

`task config uda.status_report.values display,hide`

`task config uda.status_report.default display`

This will create the attribute that is used to filter out tasks that are not
desired to show on the report

## Usage

The general usage is to just run `task-status`.  It will automatically create a
list of tasks completed from last monday to the time the script is run.  You may
run `task-status --help` to see the complete list of options and their
explanation
