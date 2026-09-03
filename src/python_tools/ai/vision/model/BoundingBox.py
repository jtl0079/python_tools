from dataclasses import dataclass


@dataclass
class BoundingBox:
    x_min: float = 0.0
    y_min: float = 0.0
    x_max: float = 0.0
    y_max: float = 0.0

    @property
    def width(self) -> float:
        return self.x_max - self.x_min

    @property
    def height(self) -> float:
        return self.y_max - self.y_min

    @property
    def center_x(self) -> float:
        return (self.x_min + self.x_max) / 2

    @property
    def center_y(self) -> float:
        return (self.y_min + self.y_max) / 2

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def is_empty(self) -> bool:
        return self.width == 0 or self.height == 0

    def intersection_over_union(self, other: "BoundingBox") -> float:
        intersection_x_min = max(self.x_min, other.x_min)

        intersection_y_min = max(self.y_min, other.y_min)

        intersection_x_max = min(self.x_max, other.x_max)

        intersection_y_max = min(self.y_max, other.y_max)

        intersection_width = max(0.0, intersection_x_max - intersection_x_min)

        intersection_height = max(0.0, intersection_y_max - intersection_y_min)

        intersection_area = intersection_width * intersection_height

        union_area = self.area + other.area - intersection_area

        if union_area <= 0.0:
            return 0.0

        return intersection_area / union_area
