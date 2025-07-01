from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit


class SudokuCell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 设置布局边距为0，让单元格紧贴
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.line_edit = QLineEdit()
        self.line_edit.setFixedSize(30, 30)
        self.layout.addWidget(self.line_edit)

    def set_value(self, value):
        self.line_edit.setText(str(value))

    def get_value(self):
        return int(self.line_edit.text())

    def set_editable(self, editable):
        self.line_edit.setReadOnly(not editable)
