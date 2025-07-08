from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtGui import QPainter, QFont
from PySide6.QtCore import QRect, Qt


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(30, 30)

        self.number = 1

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(0, 0, self.width(), self.height())
        self._draw_number(painter, rect)

    def side(self):
        return self.width()

    def _draw_number(self, painter: QPainter, rect: QRect):
        font_size = self.side() * 0.618
        painter.setFont(QFont("Arial", font_size))
        if self.number > 0:
            painter.drawText(rect, Qt.AlignCenter, str(self.number))

    def set_number(self, number: int):
        self.number = number
        self.update()

    def get_number(self) -> int:
        return self.number
