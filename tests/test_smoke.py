"""Smoke test: the container's env is the one environment.yml declares."""
import sys


def test_python_version_is_pinned():
    assert sys.version_info[:3] == (3, 11, 3), sys.version


def test_ipython_importable():
    import IPython  # noqa: F401
