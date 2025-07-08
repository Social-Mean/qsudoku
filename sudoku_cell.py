from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtGui import QPainter, QFont, QPen
from PySide6.QtCore import QRect, Qt


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(30, 30)

        # 设置焦点策略，允许通过点击获得焦点
        self.setFocusPolicy(Qt.StrongFocus)

        self.number = 0
        self.editable = True

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(0, 0, self.width(), self.height())
        self._draw_number(painter, rect)
        self._draw_border(painter, rect)

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

    def keyPressEvent(self, event):
        if not self.editable:
            return
        if event.key() == Qt.Key_Backspace or event.key() == Qt.Key_Delete:
            self.set_number(0)
        elif event.key() == Qt.Key_1:
            self.set_number(1)
        elif event.key() == Qt.Key_2:
            self.set_number(2)
        elif event.key() == Qt.Key_3:
            self.set_number(3)
        elif event.key() == Qt.Key_4:
            self.set_number(4)
        elif event.key() == Qt.Key_5:
            self.set_number(5)
        elif event.key() == Qt.Key_6:
            self.set_number(6)
        elif event.key() == Qt.Key_7:
            self.set_number(7)
        elif event.key() == Qt.Key_8:
            self.set_number(8)
        elif event.key() == Qt.Key_9:
            self.set_number(9)

    def set_editable(self, editable: bool):
        self.editable = editable
        self.update()

    def is_editable(self) -> bool:
        return self.editable

    def mousePressEvent(self, event):
        # 点击时获得焦点
        self.setFocus()
        super().mousePressEvent(event)

    def focusInEvent(self, event):
        # 获得焦点时重新绘制
        self.update()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        # 失去焦点时重新绘制
        self.update()
        super().focusOutEvent(event)

    def _draw_border(self, painter: QPainter, rect: QRect):
        # 只在获得焦点时绘制边框
        if self.hasFocus():
            painter.setPen(QPen(Qt.blue, 10))
            painter.drawRect(rect)