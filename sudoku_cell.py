from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QSizePolicy


class SudokuCell(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(30, 30)

    def set_value(self, value):
        self.setText(str(value))

    def get_value(self):
        return int(self.text())

    def set_editable(self, editable):
        self.setReadOnly(not editable)