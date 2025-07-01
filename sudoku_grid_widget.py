from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
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


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = SudokuGridWidget()
    window.show()
    app.exec()
