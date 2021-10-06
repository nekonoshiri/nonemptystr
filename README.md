# nonemptystr

[![PyPI](https://img.shields.io/pypi/v/nonemptystr)](https://pypi.org/project/nonemptystr/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nonemptystr)](https://pypi.org/project/nonemptystr/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/github/license/nekonoshiri/nonemptystr)](https://github.com/nekonoshiri/nonemptystr/blob/main/LICENSE)

Non-empty string.

## Usage

```Python
from nonemptystr import EmptyString, nonemptystr

name: nonemptystr = nonemptystr("John")

try:
    name = nonemptystr("")
except EmptyString:
    print("The name is empty.")
```

### ... with [pydantic](https://github.com/samuelcolvin/pydantic)

```Python
from nonemptystr import nonemptystr
from pydantic import BaseModel, ValidationError

class Request(BaseModel):
    user_id: nonemptystr

try:
    request = Request.parse_obj({"user_id": ""})
    print(f"user_id: {request.user_id}")
except ValidationError:
    print("user_id is empty")
```

Caveat: Currently it does NOT seem to work properly
when it is used with field constraints of pydantic
as: `user_id: nonemptystr = Field(..., max_length=10)`
[(#1)](https://github.com/nekonoshiri/nonemptystr/issues/1)

## API

### Module `nonemptystr`

#### *class* `nonemptystr(obj: object)`

Subclass of `str`.
Raise `EmptyString` exception if `str(obj)` is empty string.

#### *class* `EmptyString`

Subclass of `ValueError`.

