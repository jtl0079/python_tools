from copy import deepcopy
from dataclasses import dataclass

from .DetectionObject import DetectionObject
from .InputPathVisionDataset import InputPathVisionDataset

"""
====================================
    variables
====================================

InputPathVisionDetectionDataset
│
├── name: str
│
├── class_map: ClassMap
│
└── splits: dict[str, DatasetSplit[str, list[DetectionObject]]]
    │
    ├── "train"
    │   └── DatasetSplit[str, list[DetectionObject]]
    │       └── samples: list[Sample[str, list[DetectionObject]]]
    │           ├── Sample[str, list[DetectionObject]]
    │           │   ├── input: str
    │           │   └── target: list[DetectionObject]
    │           │       ├── DetectionObject
    │           │       ├── DetectionObject
    │           │       └── ...
    │           │
    │           └── ...
    │
    ├── "validation"
    │   └── DatasetSplit[str, list[DetectionObject]]
    │       └── samples: list[Sample[str, list[DetectionObject]]]
    │
    ├── "test"
    │   └── DatasetSplit[str, list[DetectionObject]]
    │       └── samples: list[Sample[str, list[DetectionObject]]]
    │
    └── ...

"""


@dataclass
class InputPathVisionDetectionDataset(
    InputPathVisionDataset[list[DetectionObject]],
):
    """
    ====================================
    variables
    ====================================

        name: str

        splits: dict[str, DatasetSplit[str, list[DetectionObject]]]

        class_map: ClassMap

        .
    """

    def merge(
        self,
        *others: "InputPathVisionDetectionDataset",
    ) -> None:
        """
        ====================================
        Description
        ====================================

        Merge other datasets into itself.

        ====================================
        Rules
        ====================================

        1. Merge ClassMap using ClassMap.merge().
        2. Merge splits with the same name.
        3. Remove duplicate samples.
        4. Add new splits directly.
        5. The merge is atomic.

        ====================================
        Returns
        ====================================

            None
        """

        # Create temporary copies.
        merged_class_map = deepcopy(self.class_map)
        merged_splits = deepcopy(self.splits)

        # Merge ClassMaps first.
        for other in others:
            merged_class_map.merge(other.class_map)

        # Merge splits.
        for other in others:
            for split_name, other_split in other.splits.items():
                if split_name not in merged_splits:
                    merged_splits[split_name] = deepcopy(other_split)
                    continue

                merged_samples = merged_splits[split_name].samples

                for sample in other_split.samples:
                    if sample not in merged_samples:
                        merged_samples.append(deepcopy(sample))

        # Commit only after the entire merge succeeds.
        self.class_map = merged_class_map
        self.splits = merged_splits