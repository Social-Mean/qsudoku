from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import QRect, Qt


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(30, 30)

        self.number = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 2)  # 1像素黑色画笔
        painter.setPen(pen)

        rect = QRect(0, 0, self.width(), self.height())
        painter.drawRect(rect)

        if self.number > 0:
            painter.drawText(rect, Qt.AlignCenter, str(self.number))

    def set_number(self, number: int):
        self.number = number
        self.update()

    def get_number(self) -> int:
        return self.number
