from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtGui import QPainter, QPen, QBrush
from PySide6.QtCore import Qt
from sudoku_cell import SudokuCell


class SudokuGridWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cells = []
        self._insert_cells()

    def _insert_cells(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        # 设置网格间距为0，让单元格紧贴
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        for i in range(9):
            for j in range(9):
                cell = SudokuCell()
                self.layout.addWidget(cell, i, j)
                self.cells.append(cell)

    def resizeEvent(self, event):
        side = min(self.width(), self.height())
        self.resize(side, side)
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        self._draw_box_background(painter)
        self._draw_grid(painter)
        super().paintEvent(event)

    def _draw_box_background(self, painter: QPainter):
        pass

    def _draw_grid(self, painter: QPainter):
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)
        # 画外边框
        rect = self.rect()
        painter.drawRect(rect.adjusted(0, 0, -1, -1))

        cell_size = self.width() // 9

        # 画粗线（3x3宫格）
        thick_pen = QPen(Qt.black, 3)
        painter.setPen(thick_pen)
        for i in range(10):
            if i % 3 == 0:
                # 竖线
                painter.drawLine(i * cell_size, 0, i * cell_size, self.height())
                # 横线
                painter.drawLine(0, i * cell_size, self.width(), i * cell_size)

        # 画细线（单元格）
        thin_pen = QPen(Qt.black, 1)
        painter.setPen(thin_pen)
        for i in range(10):
            if i % 3 != 0:
                # 竖线
                painter.drawLine(i * cell_size, 0, i * cell_size, self.height())
                # 横线
                painter.drawLine(0, i * cell_size, self.width(), i * cell_size)

    def set_board(self, board: list[list[int]]):
        for i in range(9):
            for j in range(9):
                self.cells[i * 9 + j].set_number(board[i][j])
                if board[i][j] != 0:
                    self.cells[i * 9 + j].set_editable(False)

    def get_board(self) -> list[list[int]]:
        board = []
        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(self.cells[i * 9 + j].get_number())
        return board
