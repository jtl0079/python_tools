from dataclasses import dataclass, field
from typing import Generic, TypeVar

from .ClassMap import ClassMap
from .Dataset import Dataset

"""
====================================
    variables
====================================

VisionDataset
│
├── name: str
│
├── class_map: ClassMap
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

TInput = TypeVar("TInput")
TTarget = TypeVar("TTarget")


@dataclass
class VisionDataset(
    Dataset[TInput, TTarget],
    Generic[TInput, TTarget],
):
    """
    ====================================
    variables
    ====================================

        name: str

        splits: dict[str, DatasetSplit[TInput, TTarget]]

        class_map: ClassMap

        .
    """

    class_map: ClassMap = field(default_factory=ClassMap)