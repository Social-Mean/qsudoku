from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from sudoku_cell import SudokuCell


class SudokuGridWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.cells = []
        for i in range(9):
            row = QGridLayout()
            for j in range(9):
                cell = SudokuCell()
                row.addWidget(cell, i, j)
                self.cells.append(cell)
            self.layout.addLayout(row)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = SudokuGridWidget()
    window.show()
    app.exec()
