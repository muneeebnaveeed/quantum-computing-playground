# quantum-computing-playground

Scratch space for the *Introduction to Quantum Computing* lab (INBPA9963-21, Fall 2026).
Python 3.11.3 + qiskit 2.1.2 + qiskit-aer 0.17.2 + matplotlib in a conda env, run inside Docker so nothing has to be installed locally.

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
docker compose run --rm app pytest         # smoke test: pinned Python, every dep imports, mpl drawer works
```

The repo is bind-mounted at `/app`, so edits on the host are visible immediately.

## Notebooks in VS Code

`main.ipynb` is the scratch notebook. To run it inside the container:

```sh
docker compose up -d                       # container idles on a bash shell
```

Then in VS Code: Dev Containers → *Attach to Running Container…* →
`quantum-computing-playground-app-1` → File → Open Folder → `/app`. Open `main.ipynb`
and pick the kernel at `/opt/miniconda3/envs/quantum/bin/python` (`ipykernel` is in the env).
Stop with `docker compose down`.

## Layout

```
main.ipynb        scratch notebook (Bell state demo)
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
