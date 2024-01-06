import invoke


@invoke.task()
def check(c):
    """Run formatting, linting and testing."""
    c.run("ruff format")
    c.run("ruff check --fix")
    c.run("mypy nonemptystr tests")
    c.run("pytest tests")
