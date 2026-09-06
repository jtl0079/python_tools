from dataclasses import dataclass, field
from typing import Generic, TypeVar

from .DatasetSplit import DatasetSplit

TInput = TypeVar("TInput")
TTarget = TypeVar("TTarget")

"""
====================================
    variables
====================================

Dataset
│
├── name: str
│
└── splits: dict[str, DatasetSplit[TInput, TTarget]]
    │
    ├── "train"
    │   └── DatasetSplit[TInput, TTarget]
    │       └── samples: list[Sample[TInput, TTarget]]
    │           ├── Sample[TInput, TTarget]
    │           │   ├── input: TInput
    │           │   └── target: TTarget
    │           │
    │           └── ...
    │
    ├── "validation"
    │   └── DatasetSplit[TInput, TTarget]
    │       └── samples: list[Sample[TInput, TTarget]]
    │
    ├── "test"
    │   └── DatasetSplit[TInput, TTarget]
    │       └── samples: list[Sample[TInput, TTarget]]
    │
    └── ...

"""


@dataclass
class Dataset(Generic[TInput, TTarget]):
    """
    ====================================
    variables
    ====================================
        name: str

        splits: dict[str, DatasetSplit[TInput, TTarget]]

        .
    """

    name: str = ""

    splits: dict[str, DatasetSplit[TInput, TTarget]] = field(default_factory=dict)
