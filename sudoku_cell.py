from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtGui import QPainter, QPen, QFont
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
        self._draw_border(painter, rect)
        self._draw_number(painter, rect)

    def side(self):
        return self.width()

    def _draw_border(self, painter: QPainter, rect: QRect):
        # TODO 后续移动到 SudokuGridWidget 中
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)
        painter.drawRect(rect)

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
