from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from sudoku_grid_widget import SudokuGridWidget
from sudoku import Sudoku

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

        # 设置初始窗口大小
        screen_smaller_side = min(
            self.screen().size().width(), self.screen().size().height()
        )
        height = screen_smaller_side * 0.6
        width = screen_smaller_side * 0.8
        self.resize(width, height)

        self._init_board()

    def _init_board(self):
        puzzle = Sudoku(3).difficulty(0.5)
        # 将None转换为0
        board = [
            [cell if cell is not None else 0 for cell in row] for row in puzzle.board
        ]
        self.sudoku_widget.set_board(board)