from PySide6.QtWidgets import QWidget, QGridLayout
from sudoku_cell import SudokuCell


class SudokuGridWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.cells = []

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
