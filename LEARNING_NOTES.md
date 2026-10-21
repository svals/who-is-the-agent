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

## Python basics

### Functions

A function is a reusable capability.

In this project:

`get_calendar()`

is a function that returns calendar data.

### Lists and loops

`get_calendar()` currently returns a list of meetings.

A loop lets me do something with each item in that list:

`for meeting in get_calendar():`

Here, `meeting` is a variable. Each time through the loop, it temporarily represents one meeting from the list.

### Conditional logic

The first version of the program uses an `if` statement to decide whether to call the calendar function.

If the request contains "meeting" or "calendar", the program calls `get_calendar()`.

This is not AI. I explicitly programmed the rule.

## Git workflow

`git status` — shows what has changed.

`git add .` — stages the current changes for the next commit.

`git commit -m "message"` — saves a checkpoint in the local Git history.

`git push` — sends my local commits to GitHub.

So my basic workflow is:

edit → add → commit → push

## V0: Calendar assistant

The first version can:

1. Accept a request from a user.
2. Look for specific words in that request.
3. Decide whether to call `get_calendar()`.
4. Return fake calendar data.

Architecture:

User → request → hard-coded decision → calendar function → calendar data

### Identity question

V0 has no authentication or authorization. Anyone who can ask for calendar information can receive it.

As I replace the hard-coded decision with an AI model that can choose when to call tools, this raises a bigger question:

**Who is allowed to call a tool, and who decides?**

I'm exploring this further in the companion Substack.

The next version will replace the hard-coded decision with an AI model that can decide when it needs to use the calendar tool.