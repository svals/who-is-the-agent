# Learning Notes

Notes from building this project from scratch. This is a chronological record of what I tried, what worked, and what I learned—not a comprehensive AI textbook.

## Setup

### What I installed

- **VS Code** — where I write and work with the project.
- **Python** — the programming language I use for the experiments.
- **Git** — tracks changes and connects my local project to GitHub.

### Terminal, PowerShell, and Python

The **terminal** is the text-based window where I give the computer commands. On my Windows computer, the terminal uses **PowerShell**. Python is a separate program that PowerShell can run.

For example, `python --version` asks Python to report its version.

### Getting the GitHub project onto my computer

I first moved to my Coding folder:

```powershell
cd C:\Coding
```

`cd` means **change directory**: move to a folder.

Then I cloned the repository:

```powershell
git clone https://github.com/svals/who-is-the-agent.git
```

`git clone` creates a local copy of a GitHub repository and sets up a connection to its remote.

Then:

```powershell
cd who-is-the-agent
code .
```

`cd who-is-the-agent` moves into the project folder. `code .` opens the current folder in VS Code; `.` means **the current folder**.

## Things I understand so far

- A **repository (repo)** is a project folder and its version history.
- **GitHub** hosts the remote repository.
- **Git** runs locally and tracks changes.
- **Cloning** creates a local copy of the repository.
- `README.md` is the project's introductory documentation.
- `main` is the primary branch in this project.
- A **commit** is a saved checkpoint in Git history.

## Python basics

### Functions

A **function** is a reusable piece of code. In this project, `get_calendar()` returns fake calendar data.

`get_calendar` refers to the function without running it. `get_calendar()` **calls** the function.

### Lists and loops

`get_calendar()` returns a list of meetings. A loop lets me process each item:

```python
for meeting in get_calendar():
    print(meeting)
```

`meeting` is a variable. On each iteration it represents one item from the list.

### Conditional logic

In V0, I explicitly programmed when to show the calendar:

```python
if "meeting" in request.lower() or "calendar" in request.lower():
    ...
```

This is ordinary rule-based programming, not AI. It misses requests such as “Am I free at 11 tomorrow?” because neither keyword appears.

### Indentation and debugging

Python uses indentation to group statements inside functions, loops, and conditionals. When the second model response initially did not appear, I checked the code, saved the file, and reran it. Before guessing at a bug, I should check whether I saved the latest changes and where execution stops.

## Git workflow

- `git status` — see what has changed.
- `git add .` — stage current changes for a commit.
- `git commit -m "message"` — save a local checkpoint.
- `git push` — send local commits to GitHub.

My basic workflow: **edit → add → commit → push**.

## V0: Rule-based calendar assistant

The first version could:

1. Accept a user's request.
2. Look for specific words in the request.
3. Decide whether to call `get_calendar()`.
4. Return fake calendar data.

**Architecture:** User → request → hard-coded decision → calendar function → calendar data.

### Identity question

V0 has no authentication or authorization. Anyone who can run the program and ask for calendar information can receive the fake data.

**Who is allowed to call a tool, and who decides?**

This is one topic to explore in the companion Substack, but the broader learning project focuses on practical AI and AI product management. V1 replaces the keyword decision with a local LLM that can request a tool.

---

## V1: First local LLM-powered calendar assistant — October 20, 2026

### AI models, LLMs, tokens, and parameters

An **AI model** is a system trained on data to recognize patterns and produce predictions or outputs. Rather than writing every rule, developers use training to adjust the model based on examples.

A **large language model (LLM)** is a type of AI model that processes and generates language. Examples include GPT, Claude, Gemini, Llama, and Qwen. It generates outputs by predicting tokens from the context and learned patterns.

A **token** is a unit of data a model processes—often a word, part of a word, or punctuation in text. Training on trillions of tokens means processing an enormous amount of tokenized material, not keeping a searchable copy of all of it.

**Parameters**, also called weights, are numerical values adjusted during training. Qwen3 1.7B has roughly **1.7 billion parameters**.

### Training, inference, and extra information

- **Training:** Learning patterns by changing model weights.
- **Fine-tuning:** Additional training of an existing model; weights change.
- **Inference:** Using a trained model to answer a request; weights do not change.
- **Prompting:** Supplying instructions or context at inference time; weights do not change.
- **Tool calling:** The model requests a function or external capability; the application executes it if appropriate. No retraining is required.
- **RAG (Retrieval-Augmented Generation):** Retrieving relevant external information and giving it to the model as context. No retraining is required. We'll explore it later.

When Qwen receives our fake calendar data, it can use it for that response, but **we are not training it on the calendar**. Giving a model information during a conversation is different from a provider potentially collecting that conversation for separate future training, depending on its policies and settings.

### Local versus hosted models

A **local model** runs on my computer. It avoids per-request API fees and can keep inference local, but uses my computer's RAM and processing power. Performance depends on hardware.

A **hosted model** runs on a provider's infrastructure. My application sends requests over an API. It can offer more capable models without needing powerful local hardware, but usually has usage charges and sends request data to the provider.

I have **8 GB RAM**, so I started with a small local model. Later I want to compare the same tasks on local and hosted models: accuracy, speed, reliability, privacy, and cost.

### Ollama and Qwen

**Ollama** is software that downloads, runs, and provides an interface to local models. **Qwen** is the LLM family, developed by Alibaba's Qwen team. They are not the same thing.

I selected **Qwen3 1.7B** as a small, tool-capable starting model—not because it is universally the best model. Model selection should depend on the task and constraints.

Commands I used:

```powershell
ollama --version
ollama pull qwen3:1.7b
ollama run qwen3:1.7b
```

`--version` checks the installed version; `pull` downloads a model; `run` starts an interactive session. I exited the session using `/bye`.

I installed the Ollama Python library with:

```powershell
python -m pip install ollama
```

**Model provenance matters:** Prefer trustworthy sources, keep runtime software updated, and remember that running locally does not make model outputs inherently accurate or safe.

### Calling Qwen from Python

I created `test_llm.py` and used:

```python
from ollama import chat

response = chat(
    model="qwen3:1.7b",
    messages=[
        {"role": "user", "content": "Am I free at 11 AM tomorrow?"}
    ]
)

print(response.message.content)
```

- `from ollama import chat` imports a function from the Python library.
- `model` selects which local model to use.
- `messages` supplies the conversation.
- `role` indicates who is speaking, such as `user` or `system`.
- `response` stores Ollama's reply.

**Observation:** Qwen understood that “Am I free at 11?” was a calendar question, even without the word *calendar*. But it could not actually know my availability until we connected a tool.

### System prompts

I added a system message telling Qwen to act as a calendar assistant, say when it lacks calendar access, and keep answers brief.

Its response became more focused. **System prompts guide model behavior without retraining the model**, but they do not guarantee compliance. The model also gave different responses to the same question on separate runs: LLM output can vary.

### Tool calling: from language to action

I reused the original `get_calendar()` function in `agent.py` and registered it as a tool:

```python
tools = [get_calendar]
```

I passed `tools=tools` into the Ollama `chat()` request. Qwen then requested `get_calendar` when I asked “Am I free at 11am tomorrow?”

**Important:** A tool request is **not** the same as tool execution. The model proposes a call; Python decides whether and how to run it.

Our application checked the tool name and executed the function:

```python
if response.message.tool_calls:
    for tool_call in response.message.tool_calls:
        if tool_call.function.name == "get_calendar":
            meetings = get_calendar()
```

Then we made a **second call** to Qwen, sending the original user request, Qwen's tool-call message, and the calendar data as a `tool` message. Qwen used that information to produce the final answer.

**Full loop:** User → Python → Qwen → tool request → Python executes `get_calendar()` → calendar result → Qwen → natural-language answer.

**Successful result:** Qwen answered that I was **not free at 11 AM** because of the Identity roadmap review in our fake calendar.

### Unexpected behavior worth investigating

**1. Invented tool argument.** On one run, Qwen requested:

```python
arguments={"time": "tomorrow 11am"}
```

But `get_calendar()` takes **no arguments**. Our code happened to work because Python called the function without passing that argument. A robust application should validate tool names and arguments against the expected schema and handle errors.

**2. Unsupported capability.** Qwen offered to reschedule a meeting, even though we built no rescheduling tool. Model-generated suggestions should not imply capabilities the application lacks.

**3. Variability.** Responses differed between runs. One successful request is not proof of reliability.

**4. No real calendar integration.** The meetings are hard-coded fake data. We have not granted Qwen access to any real calendar or account.

### AI product management questions

The next stage is not simply adding features. I want to **evaluate** the feature:

- **Task success:** Did it correctly answer the availability question?
- **Tool selection:** Did it request the right tool when needed, and avoid unnecessary calls?
- **Argument validity:** Did it supply arguments that match the tool schema?
- **Answer accuracy:** Did the final answer agree with the returned data?
- **Latency:** How long did the whole request take?
- **Reliability:** Does it work across varied phrasing and repeated trials?
- **Cost:** What compute resources or API charges does each request require?
- **Guardrails:** Does it avoid unauthorized or unsupported actions?

For each metric we eventually choose, I want to define the **numerator, denominator, instrumentation, and acceptable threshold** rather than use vague labels like “works well.”

### Milestone

**I built my first local LLM-powered, tool-using calendar assistant with Python, Ollama, and Qwen3 1.7B.** It recognizes an availability question, requests a calendar tool, receives fake calendar data through Python, and generates an answer. This is a learning prototype—not a production-ready autonomous agent.

### Next experiments

1. Commit the V1 milestone to GitHub (`Build first local LLM calendar agent`).
2. Try varied questions, including ones that should **not** call the calendar.
3. Create a small evaluation set and measure success rates.
4. Validate tool arguments and handle failures.
5. Compare the local model with a hosted model.
6. Later: explore RAG, MCP, and more complex agent workflows.

**Writing connection:** The interesting material for *Who Is the Agent?* is not just that the code works. It's that the model can choose a tool, invent an argument, and offer an action it cannot perform. Those observations can lead to broader posts about reliable AI products, with identity and authorization as one part of the story.
