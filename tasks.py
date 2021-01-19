import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("isort nonemptystr.py tests")
    c.run("black nonemptystr.py tests")
    c.run("flake8 nonemptystr.py tests")
    c.run("mypy nonemptystr.py tests")
    c.run("pytest tests")
