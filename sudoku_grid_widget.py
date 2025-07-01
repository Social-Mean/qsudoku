from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QMainWindow,
)
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数独")
        self.sudoku_widget = SudokuGridWidget()
        self.setCentralWidget(self.sudoku_widget)
        # 创建右侧控制面板
        self.right_panel = QWidget()
        right_layout = QVBoxLayout()
        self.right_panel.setLayout(right_layout)

        # 创建主布局并添加数独网格和右侧面板
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.sudoku_widget)
        main_layout.addWidget(self.right_panel)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        # self.setFixedSize(self.sudoku_widget.size())


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
