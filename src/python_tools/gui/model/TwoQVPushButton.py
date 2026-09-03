from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
)
from PySide6.QtCore import Qt


class TwoQVPushButton:
    top_button: QPushButton
    bottom_button: QPushButton
    layout: QVBoxLayout

    def __init__(
        self,
        top_text: str = "Top Button",
        bottom_text: str = "Bottom Button",
        window=None,
    ):
        # ====================================
        # Parameters
        # ====================================
        if window is not None:
            self.layout = QVBoxLayout(window)
        else:
            self.layout = QVBoxLayout()

        # ====================================
        # Logic
        # ====================================
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.top_button = QPushButton(top_text)
        self.bottom_button = QPushButton(bottom_text)

        self.layout.addWidget(self.top_button, alignment=Qt.AlignmentFlag.AlignBottom)

        self.layout.addWidget(self.bottom_button, alignment=Qt.AlignmentFlag.AlignTop)
