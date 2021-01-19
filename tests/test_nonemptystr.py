import pytest

from nonemptystr import EmptyString, nonemptystr


class NE:
    def __str__(self) -> str:
        return "NE"


class E:
    def __str__(self) -> str:
        return ""


@pytest.mark.parametrize("obj", ["hi", 1.5, [], NE()])
def test_normal(obj: object) -> None:
    nes = nonemptystr(obj)
    assert isinstance(nes, nonemptystr)
    assert isinstance(nes, str)
    assert nes == str(nes) == str(obj)


@pytest.mark.parametrize("obj", ["", E()])
def test_empty_string(obj: object) -> None:
    with pytest.raises(EmptyString):
        nonemptystr(obj)
