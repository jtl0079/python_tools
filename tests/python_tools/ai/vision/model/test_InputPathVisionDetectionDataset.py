import pytest

from python_tools.ai.vision.model.BoundingBox import BoundingBox
from python_tools.ai.vision.model.ClassMap import ClassMap
from python_tools.ai.vision.model.DatasetSplit import DatasetSplit
from python_tools.ai.vision.model.DetectionObject import DetectionObject
from python_tools.ai.vision.model.InputPathVisionDetectionDataset import (
    InputPathVisionDetectionDataset,
)
from python_tools.ai.vision.model.Sample import Sample


def create_sample(
    path: str,
    class_id: int = 0,
) -> Sample[str, list[DetectionObject]]:
    return Sample(
        input=path,
        target=[
            DetectionObject(
                class_id=class_id,
                bbox=BoundingBox(
                    x_min=0,
                    y_min=0,
                    x_max=100,
                    y_max=100,
                ),
            )
        ],
    )


def create_dataset(
    class_names: list[str],
    train_samples: list[Sample[str, list[DetectionObject]]] | None = None,
) -> InputPathVisionDetectionDataset:
    dataset = InputPathVisionDetectionDataset(
        class_map=ClassMap(class_names),
    )

    if train_samples is not None:
        dataset.splits["train"] = DatasetSplit(
            samples=train_samples,
        )

    return dataset


def test_merge():
    # ------------------------------------
    # Dataset A
    # ------------------------------------

    sample_a = create_sample("cat.jpg")

    dataset_a = create_dataset(
        ["cat"],
        [sample_a],
    )

    # ------------------------------------
    # Dataset B
    # ------------------------------------

    sample_b = create_sample("dog.jpg")

    dataset_b = create_dataset(
        ["cat", "dog"],
        [sample_b],
    )

    # ------------------------------------
    # Merge
    # ------------------------------------

    dataset_a.merge(dataset_b)

    # ------------------------------------
    # Assert
    # ------------------------------------

    assert dataset_a.class_map.names == [
        "cat",
        "dog",
    ]

    assert "train" in dataset_a.splits

    assert len(dataset_a.splits["train"].samples) == 2

    assert sample_a in dataset_a.splits["train"].samples
    assert sample_b in dataset_a.splits["train"].samples