from dataclasses import dataclass, field
from typing import Generic, TypeVar

from .Sample import Sample

TInput = TypeVar("TInput")
TTarget = TypeVar("TTarget")

"""
====================================
    variables
====================================

DatasetSplit
│
├── name: str
│
└── samples: list[Sample[TInput, TTarget]]
    │
    ├── Sample[TInput, TTarget]
    │   ├── input: TInput
    │   └── target: TTarget
    │
    ├── Sample[TInput, TTarget]
    │   ├── input: TInput
    │   └── target: TTarget
    │
    └── ...

"""
@dataclass
class DatasetSplit(Generic[TInput, TTarget]):
    """
    ====================================
    variables
    ====================================
        name: str

        samples: list[Sample[TInput, TTarget]]

        .

    """

    name: str = ""

    samples: list[Sample[TInput, TTarget]] = field(default_factory=list)
