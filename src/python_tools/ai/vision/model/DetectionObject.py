from dataclasses import dataclass
from python_tools.ai.vision.model.BoundingBox import BoundingBox


@dataclass
class DetectionObject:
    class_id: int
    bbox: BoundingBox
