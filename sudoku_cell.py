from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(30, 30)
        self.layout.addWidget(self.line_edit)

    def set_value(self, value):
        self.line_edit.setText(str(value))

    def get_value(self):
        return int(self.line_edit.text())

    def set_editable(self, editable):
        self.line_edit.setReadOnly(not editable)
