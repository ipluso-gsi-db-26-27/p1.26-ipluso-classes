# Python 2026/2027 — Codespace Environment

Everything you need for the practical classes runs inside a **GitHub Codespace**.  
Nothing needs to be installed on your own machine, and it works identically on Windows, macOS and Linux.

The environment is prepared with:

- **Python 3.14**
- A Python virtual environment (`.venv`)
- The **Python extension for Visual Studio Code**
- An `exercises/` folder where your Python programs should be stored

---

## 1. Get your own copy of the repository

**Do this before anything else.** You need your *own* repository — working directly in the class repository is not possible and your work may be lost.

> Log in to your Github account before proceding

**If you have a GitHub Classroom link:** click it, accept the assignment, and GitHub creates a private repository for you automatically.  
Skip to step 2 — the link takes you to your new repository.

**Otherwise:** open the class repository, click the green **Use this template** button → **Create a new repository**. Give it a meaningful name and create it.  
You now own a full copy of the classroom environment in your own repository.

> Do **not** use Fork, and do not create a codespace directly on the class repository.  
> Both leave your work somewhere you cannot properly commit to.

Everything below happens in **your** repository, not the class one.

---

## 2. Start the environment

Click **Code → Codespaces → Create codespace on main**.

On the first launch GitHub builds the development environment defined in `.devcontainer/devcontainer.json`.

During setup:

- Python 3.14 is installed as part of the development container;
- the Python extension for Visual Studio Code is installed;
- a `.venv` Python virtual environment is created automatically.

The first launch can take a few minutes while the development container is downloaded and configured.

Setup runs in the background, **not** in the terminal, so an empty terminal does not mean nothing is happening.

If necessary, you can follow the setup process by opening the Command Palette (`F1` or `Ctrl+Shift+P`) and selecting:

```text
Codespaces: View Creation Log
```

After completing environment setup, you can close the browser tab and return to the codespace whenever you like — the codespace stops automatically when inactive and resumes with your files intact... kind of!

> A codespace that goes untouched for an extended period can be deleted by GitHub, along with anything you never pushed.  
> So **COMMIT OFTEN**. Do it at the end of each class and whenever you make significant changes to your work.

Commit in the codespace, then push to your GitHub repository.

It is important to remember that the Codespace is **not a backup** — it is just a convenient place to work.  
Your GitHub repository is your backup.

When using GitHub Classroom, you may also have a **Submit** option available for grading.

---

## 3. Check the Python environment

If you do not have the Terminal open, select:

**Terminal → New Terminal**

Check the installed Python version:

```bash
python --version
```

You should get a result similar to:

```text
Python 3.14.x
```

The repository also creates a Python virtual environment named:

```text
.venv
```

Normally VS Code detects and activates it automatically.

You can check which Python executable is currently being used with:

```bash
which python
```

When the virtual environment is active, the result should point to something similar to:

```text
/workspaces/<repository-name>/.venv/bin/python
```

The terminal prompt may also start with:

```text
(.venv)
```

If `.venv` exists but is not active, activate it manually:

```bash
source .venv/bin/activate
```

To leave the virtual environment:

```bash
deactivate
```

---

## 4. Test the environment

A simple Python example is included in:

```text
exercises/myfirst.py
```

The program contains:

```python
print("Hello, World")
```

From the repository root, run:

```bash
python exercises/myfirst.py
```

The expected result is:

```text
Hello, World
```

You can also open `exercises/myfirst.py` in the editor and run it using the **Run Python File** button in the top-right corner of the editor.

If both methods work, your Python environment is ready.

---

## 5. Working with Python files

Keep your Python examples and exercises inside the `exercises/` folder.

For example:

```text
exercises/
├── myfirst.py
├── exercise01.py
├── exercise02.py
└── exercise03.py
```

To execute a program from the repository root:

```bash
python exercises/exercise01.py
```

### Installing additional Python packages

Packages required by your programs should be installed inside the virtual environment.

For example:

```bash
pip install requests
```

To see the packages currently installed:

```bash
pip list
```

If a project later provides a `requirements.txt` file, install all its dependencies with:

```bash
pip install -r requirements.txt
```

Packages installed inside `.venv` are specific to this Codespace environment and are not stored in the Git repository.

---
## 6. Leaving the Codespace


Before leaving the Codespace, make sure your work is saved and stored in your GitHub repository or you risk loosing it permanently.

Follow this workflow:

### 1. Save all your work

Save all open files before doing anything else.

If the **Explorer** icon shows a number, there are files with unsaved changes.

You can save the current file with:

```text
Ctrl+S
```

or save all files with:

```text
Ctrl+K S
```

Make sure there are no unsaved files before continuing.

---

### 2. Commit your saved work

Open the **Source Control** panel.

If the Source Control icon shows a number - ![uncommitted changes](./assets/sourcecontrol.png) - there are changes that have not yet been committed.

Review the changed files and create a commit.

A **commit message is mandatory** and should briefly explain what was changed.

For example:

```text
Add exercise 03
```

or:

```text
Complete list processing exercises
```

Avoid meaningless messages such as:

```text
new file
```

or:

```text
changes
```

A good commit message should help you understand later what was done in that commit.

---

### 3. Push or synchronize your work

After committing, send the commit to your GitHub repository.

Use **Push**, **Sync Changes**, or the equivalent option shown in the Source Control panel.

If you are working on a branch that must be merged, complete the required merge into your repository according to the workflow being used in class.

Wait until the push or synchronization finishes successfully before closing the Codespace.

Your latest work should now be visible in your GitHub repository.

> Remember: a commit only saves the work inside the local Git repository in the Codespace.  
> **Push** sends that commit to GitHub.

---

### 4. Stop the Codespace

Once your files are saved, committed and pushed, stop the Codespace.

Open the Command Palette with:

```text
Ctrl+Shift+P
```

or:

```text
F1
```

Then run:

```text
Codespaces: Stop Current Codespace
```

Stopping the Codespace releases the running environment while keeping it available for the next class.

When you return, you can restart the same Codespace and continue working.

> Do not simply rely on closing the browser tab as your normal workflow.  
> Always save, commit and push your work first, then stop the Codespace.
---

## 7. Folder Layout

```text
.
│   .gitignore
│   README.md
│
├───.devcontainer
│       devcontainer.json
│
└───exercises
        myfirst.py
```

### `.venv/`

The Python virtual environment is created automatically when the Codespace is first configured.

It does not appear in the repository layout above because it is excluded through `.gitignore` and should **never be committed to Git**.

Each copy of the repository creates its own `.venv`.

### `exercises/`

This is where your work goes.

Keep the Python source files you want to preserve inside this folder and commit them regularly to your repository.

---

## Troubleshooting

### `python: command not found`

Run:

```bash
python --version
```

If Python is not available, the Codespace may not have been created successfully from the `.devcontainer/devcontainer.json` configuration.

Open the Command Palette (`F1`) and select:

```text
Codespaces: View Creation Log
```

Check for errors during creation.

If the Codespace was created before the current `.devcontainer` configuration existed, the simplest solution is usually to delete that Codespace and create a new one from the repository.

Push or commit any work you want to preserve before deleting it.

---

### `.venv` does not exist

Check the files in the repository root:

```bash
ls -la
```

You should see:

```text
.venv
```

If the environment was not created automatically, create it manually:

```bash
python -m venv .venv
```

Then activate it:

```bash
source .venv/bin/activate
```

---

### The wrong Python interpreter is being used

Open the Command Palette:

```text
F1
```

or:

```text
Ctrl+Shift+P
```

Run:

```text
Python: Select Interpreter
```

Select the interpreter inside:

```text
.venv/bin/python
```

You can verify it from the terminal with:

```bash
which python
```

---

### `Python: Select Interpreter` does not appear

The Visual Studio Code Python extension may not be loaded.

Open the **Extensions** panel and search for:

```text
Python
```

The Microsoft Python extension should be installed:

```text
ms-python.python
```

The extension is normally installed automatically from `.devcontainer/devcontainer.json`.

If it is missing, install it manually from the Extensions panel.

For a newly created Codespace, a missing extension may indicate that part of the Codespace configuration did not complete correctly. Check:

```text
Codespaces: View Creation Log
```

for setup errors.

---

### `myfirst.py` does not run

Make sure you are at the repository root and run:

```bash
python exercises/myfirst.py
```

Check that the file exists:

```bash
ls exercises
```

You should see:

```text
myfirst.py
```

The expected output is:

```text
Hello, World
```

---

### Packages installed with `pip` cannot be imported

First check that the virtual environment is active:

```bash
which python
```

and:

```bash
which pip
```

Both should point inside `.venv`.

If necessary, activate the environment:

```bash
source .venv/bin/activate
```

Then install the package again:

```bash
pip install <package-name>
```

---

### Everything is broken and I do not know why

First make sure all your work has been committed and pushed to GitHub.

From the **Codespaces** page on GitHub, delete the Codespace and create a new one from your repository.

The new Codespace will rebuild the complete Python environment from `.devcontainer/devcontainer.json`.

Your committed files remain in the GitHub repository; the development environment itself is disposable.
