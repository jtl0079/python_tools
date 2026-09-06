from dataclasses import dataclass
from typing import Generic, TypeVar

from .VisionDataset import VisionDataset

"""
====================================
    variables
====================================

InputPathVisionDataset
│
├── name: str
│
├── class_map: ClassMap
│
└── splits: dict[str, DatasetSplit[str, TTarget]]
    │
    ├── "train"
    │   └── DatasetSplit[str, TTarget]
    │       └── samples: list[Sample[str, TTarget]]
    │           ├── Sample[str, TTarget]
    │           │   ├── input: str
    │           │   └── target: TTarget
    │           │
    │           ├── Sample[str, TTarget]
    │           │   ├── input: str
    │           │   └── target: TTarget
    │           │
    │           └── ...
    │
    ├── "validation"
    │   └── DatasetSplit[str, TTarget]
    │       └── samples: list[Sample[str, TTarget]]
    │
    ├── "test"
    │   └── DatasetSplit[str, TTarget]
    │       └── samples: list[Sample[str, TTarget]]
    │
    └── ...

"""

TTarget = TypeVar("TTarget")


@dataclass
class InputPathVisionDataset(
    VisionDataset[str, TTarget],
    Generic[TTarget],
):
    """
    ====================================
    variables
    ====================================

        name: str

        splits: dict[str, DatasetSplit[str, TTarget]]

        class_map: ClassMap

        .
    """

    pass