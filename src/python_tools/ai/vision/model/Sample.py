from dataclasses import dataclass
from typing import Generic, TypeVar

TInput = TypeVar("TInput")
TTarget = TypeVar("TTarget")


@dataclass
class Sample(Generic[TInput, TTarget]):
    """
    ====================================
    variables
    ====================================
        input: TInput | None = None

        target: TTarget | None = None

    """

    input: TInput | None = None

    target: TTarget | None = None
