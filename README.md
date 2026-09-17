# quantum-computing-playground

Scratch space for the *Introduction to Quantum Computing* lab (INBPA9963-21, Fall 2026).
Python 3.11.3 + qiskit 2.1.2 in a conda env, run inside Docker so nothing has to be installed locally.

## Setup

Requires Docker Desktop running.

```sh
docker compose build                       # first time, and after editing environment.yml
```

## Daily use

```sh
docker compose run --rm app                # interactive shell inside the env
docker compose run --rm app ipython        # IPython REPL
docker compose run --rm app python labs/<file>.py
docker compose run --rm app pytest         # smoke test: Python 3.11.3 + qiskit 2.1.2 import
```

The repo is bind-mounted at `/app`, so edits on the host are visible immediately.

## Layout

```
labs/             one file (or folder) per lab session
tests/            smoke test for the environment
environment.yml   conda env — add packages here, then `docker compose build`
Dockerfile        miniconda image, conda-forge only
compose.yaml      single `app` service, defaults to a bash shell
```

## Without Docker

```sh
conda env create -f environment.yml && conda activate quantum
```
