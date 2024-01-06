import pytest
from pydantic import BaseModel, Field, ValidationError

from nonemptystr import nonemptystr


class Model(BaseModel):
    nes: nonemptystr


@pytest.mark.parametrize(
    "model",
    [
        Model(nes="hello"),  # type: ignore
        Model(nes=nonemptystr("hello")),
        Model.model_validate({"nes": "hello"}),
        Model.model_validate_json('{"nes": "hello"}'),
    ],
)
def test_normal(model: Model) -> None:
    assert model.nes == nonemptystr("hello")
    assert type(model.nes) is nonemptystr


def test_validation_error() -> None:
    with pytest.raises(ValidationError):
        Model(nes="")  # type: ignore
    with pytest.raises(ValidationError):
        Model.model_validate({"nes": ""})
    with pytest.raises(ValidationError):
        Model.model_validate_json('{"nes": ""}')


def test_schema() -> None:
    assert Model.model_json_schema()["properties"]["nes"]["minLength"] == 1


def test_nonemptystr_can_be_used_with_constraints() -> None:
    class ModelWithConstraints(BaseModel):
        nes: nonemptystr = Field(..., max_length=5)

    assert type(ModelWithConstraints(nes="hello").nes) is nonemptystr  # type: ignore
    assert type(ModelWithConstraints(nes=nonemptystr("hello")).nes) is nonemptystr

    with pytest.raises(ValidationError):
        ModelWithConstraints(nes="")  # type: ignore
    with pytest.raises(ValidationError):
        ModelWithConstraints(nes="thanks")  # type: ignore
    with pytest.raises(ValidationError):
        ModelWithConstraints(nes=nonemptystr("thanks"))
