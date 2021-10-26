# Changelog

## v0.3.0 (2021-10-26)

#### New Features

* add --bullet option to change char in front of list items

Full set of changes: [`v0.2.4...v0.3.0`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.2.4...v0.3.0)

## v0.2.4 (2021-10-25)

#### Fixes

* correct the -deleted to -DELETED to filter out tasks that were deleted

Full set of changes: [`v0.2.3...v0.2.4`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.2.3...v0.2.4)

## v0.2.3 (2021-10-18)

#### Fixes

* correct issue causing the status_report filter to not apply
#### Others

* added tests and configs for linting and coverage
* Updated dependant packages
* removed coveage of main in the if __name__ test

Full set of changes: [`v0.2.2...v0.2.3`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.2.2...v0.2.3)

## v0.2.2 (2021-08-26)

#### Fixes

* Corrected a missing elif that was causing duplicated output when --uuid was specified
* fixed duplicate project adding
#### Refactorings

* remove test dep on build task
#### Others

* Added coverage tests
* Added header and sort tests

Full set of changes: [`v0.2.1...v0.2.2`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.2.1...v0.2.2)

## v0.2.1 (2021-08-23)

#### Fixes

* corrected the issue causing split project entries closes [#1](https://git.admin.franklin.edu/kellya/task-status/issues/1)
* Added handling for empty/no project name
#### Others

* cleanup for linting errors
* Add directory to correct flakes flakiness
* attempt to fix [#1](https://git.admin.franklin.edu/kellya/task-status/issues/1), but instead made it fail the same way with completely different logic
* hopefully fixed tests adding ci tasks to my taskwarrior
* fixed the forced bad entry
* checking in invalid code to force a build fail

Full set of changes: [`v0.2.0...v0.2.1`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.2.0...v0.2.1)

## v0.2.0 (2021-08-19)

#### New Features

* added --header option to display start date of report
#### Others

* added taskrc config for base configuration
* added makefile
* Added __init__.py to try to clean up build errors
* added a useless --help test to verify commit message hook is working

Full set of changes: [`v0.1.1...v0.2.0`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.1.1...v0.2.0)

## v0.1.1 (2021-08-18)


Full set of changes: [`v0.1.0...v0.1.1`](https://git.admin.franklin.edu/kellya/task-status/compare/v0.1.0...v0.1.1)

## v0.1.0 (2021-08-18)

#### New Features

* Added click and --uuid to display task's uuid to aid in cleanup of tasks
