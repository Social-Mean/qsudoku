from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSizePolicy


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(30, 30)

    def paintEvent(self, event):
        from PySide6.QtGui import QPainter, QPen
        from PySide6.QtCore import Qt

        painter = QPainter(self)
        pen = QPen(Qt.black, 2)  # 1像素黑色画笔
        painter.setPen(pen)

        # 绘制正方形边框
        painter.drawRect(0, 0, self.width(), self.height())
