import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("isort nonemptystr tests")
    c.run("black nonemptystr tests")
    c.run("flake8 nonemptystr tests")
    c.run("mypy nonemptystr tests")
    c.run("pytest tests")
