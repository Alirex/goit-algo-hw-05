# Homeworks

Course: "Basic algorithms and data structures"

Topic: 5. "Search algorithms"

---

## Check

[//]: # "### Task 1"
[//]: #
[//]: # "Check the code:"
[//]: #
[//]: # "- [main.py](src/goit_algo_hw_04/task_1/main.py)"
[//]: #
[//]: # "Read the comparison results:"
[//]: #
[//]: # "- [comparison.md](src/goit_algo_hw_04/task_1/comparison.md)"
[//]: #
[//]: # "Run comparison by `timeit`:"
[//]: #
[//]: # "```shell"
[//]: # "uv run task_1"
[//]: # "```"
[//]: #
[//]: # "Run comparison by `pytest-benchmark` (with colorized output):"
[//]: #
[//]: # "```shell"
[//]: # "uv run pytest -k test_sorting_benchmark --verbose"
[//]: # "```"
[//]: #
[//]: # "### Task 2"
[//]: #
[//]: # "Check the code:"
[//]: #
[//]: # "- [main.py](src/goit_algo_hw_04/task_2/main.py)"
[//]: #
[//]: # "Run tests:"
[//]: #
[//]: # "```shell"
[//]: # "uv run pytest -k test_merge_k_lists --verbose"
[//]: # "```"

---

## Dev

### Uv install or update

https://docs.astral.sh/uv/getting-started/installation/

```bash
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh;
else
    uv self update;
fi

uv --version
```

### Ruff install or update

https://docs.astral.sh/ruff/installation/

```bash
if ! command -v ruff &> /dev/null; then
    uv tool install ruff
else
    uv tool upgrade ruff
fi

ruff --version
```

### Install prek for pre-commit hooks

Needed for automatic linting.

```shell
if ! command -v prek &> /dev/null; then
    curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/download/v0.2.19/prek-installer.sh | sh &&\
    prek self update
else
    prek self update
fi

prek --version
```

Note: Run with self-update for installing the latest version of prek. Maybe they will provide a better script later.

### Create venv

```bash
uv sync --all-packages
```

### Register pre-commit hooks

Make this after cloning the repository.

```shell
prek install
```

or, if you have pre-commit hooks installed before prek:

```shell
prek install --overwrite
```

Make this each time after cloning the repository.

Don't need to do it after changing the hooks, commit or pull.

## Homework

Download the archive with a specific name:

```shell
bash scripts/download_homework.sh ДЗ5_СОВ
```

---

## Extra

- Why is the `.idea` folder is partially stored in the repository?
  - [read (UKR)](https://github.com/Alirex/notes/blob/main/notes/ignore_or_not_ide_config/ukr.md)
- Why `py.typed`?
  - [mypy (ENG)](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages)
  - [typing (ENG)](https://typing.python.org/en/latest/spec/distributing.html#packaging-type-information)

### Create a new project

In case, if you need to create a new project with `src-layout` instead of default, created by PyCharm,
use the following command inside the project directory:

```shell
rm --recursive --force src pyproject.toml &&\
uv init --package --vcs none &&\
touch src/$(basename $PWD | tr '-' '_')/py.typed &&\
uv sync
```

### Reinit .idea folder for git for better gitignore support

If you created a new project with JetBrains IDE and automatically created git repository,
before providing more granular `.gitignore` file, you need to reinit `.idea` folder.

```shell
git rm -r --force --cached .idea &&\
git add .idea
```

### Create layout for tasks

Use a number of tasks, if needed:

```shell
bash scripts/create_tasks_layout.sh 3
```
