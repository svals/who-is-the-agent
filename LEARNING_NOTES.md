# Learning Notes

Notes from building this project from scratch.

## Setup

### What I installed

- VS Code — where I write and work with the project
- Python — the programming language I'll use for the experiments
- Git — keeps track of changes to the project and connects my local project to GitHub

### Terminal, PowerShell and Python

The terminal is the text-based window where I give the computer commands.

On my Windows computer, the terminal is using PowerShell.

Python is a separate program that PowerShell can run.

For example:

`python --version`

asks Python to tell me which version is installed.

### Getting the GitHub project onto my computer

I first moved to my Coding folder:

`cd C:\Coding`

`cd` means "change directory" — essentially, go to this folder.

Then I ran:

`git clone https://github.com/svals/who-is-the-agent.git`

`git clone` creates a local copy of the GitHub repository and connects the local copy to the GitHub repository.

Then:

`cd who-is-the-agent`

moved me inside the new project folder.

Finally:

`code .`

opened the current folder in VS Code. The `.` means "the current folder."

## Things I understand so far

- A repository (repo) is the project folder plus its version history.
- GitHub stores the remote copy of the repo.
- Git runs on my computer and tracks changes.
- Cloning created a local copy of my GitHub repo.
- README.md is the front page/documentation for the project.
- `main` is the primary branch.
- A commit is a saved checkpoint in the project's history.