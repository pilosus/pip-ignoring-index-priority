from setuptools import setup
from pathlib import Path

current_dir = Path(__file__).resolve().parent

try:
    readme = current_dir.joinpath('README.md').read_text()
except FileNotFoundError:
    readme = "Dependency confusion attack for PyPI (proof of concept)"

setup(
    name="anna_risk_score_client",
    version="666.777.2",
    author="pilosus",
    author_email="vrs@pilosus.org",
    packages=["anna_risk_score_client"],
    package_dir={"anna_risk_score_client": "./index_priority"},
    url="https://github.com/pilosus/pip-ignoring-index-priority",
    description="PoC for pip v21 ignoring index priorities",
    long_description=readme,
    zip_safe=False,
)
