"""Smoke test: the container's env is the one environment.yml declares."""
import sys


def test_python_version_is_pinned():
    assert sys.version_info[:3] == (3, 11, 3), sys.version


def test_ipython_importable():
    import IPython  # noqa: F401


def test_qiskit_pinned():
    import qiskit

    assert qiskit.__version__ == "2.1.2", qiskit.__version__


def test_qiskit_aer_importable():
    from qiskit_aer import AerSimulator  # noqa: F401


def test_matplotlib_importable():
    import matplotlib  # noqa: F401


def test_qiskit_mpl_drawer_works(tmp_path):
    import matplotlib

    matplotlib.use("Agg")
    from qiskit import QuantumCircuit

    qc = QuantumCircuit(1)
    qc.h(0)
    qc.draw(output="mpl").savefig(tmp_path / "c.png")


def test_ipykernel_importable():
    import ipykernel  # noqa: F401
