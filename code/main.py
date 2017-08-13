import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)
from parse_file import get_itinerary


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FTF Itinerary Generator")
        self.setGeometry(300, 300, 700, 600)
        self.initUI()
    def initUI(self):
        source_label = QLabel('Input Addresses')
        optimized_label = QLabel('Optimized Route')

        self.source_file = QTextEdit()
        self.source_file.setFixedHeight(500)

        self.optimized_output = QTextEdit()
        self.optimized_output.setFixedHeight(500)
        self.optimized_output.setReadOnly(True)

        generate_file = QPushButton("Generate Ordered Addresses")
        generate_file.setFixedHeight(50)
        generate_file.clicked.connect(self.handleButton)

        clear_text = QPushButton("Clear Text")
        clear_text.setFixedHeight(50)
        clear_text.clicked.connect(self.clearOptimizedPanel)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(source_label, 0, 0)
        grid.addWidget(self.source_file, 1, 0)

        grid.addWidget(optimized_label, 0, 1)
        grid.addWidget(self.optimized_output, 1, 1)

        grid.addWidget(generate_file)
        grid.addWidget(clear_text)

        self.setLayout(grid)

        self.show()

    def handleButton(self):
        address_string = self.source_file.toPlainText()
        addresses = address_string.split(",")

        #strings are immutable
        for i in range(0, len(addresses)):
            addresses[i] = addresses[i].strip().strip("\n")
        print(addresses)

        ordered_addresses = get_itinerary(addresses)

        output_string = ""
        for address in ordered_addresses:
            output_string += address + "\n\n"

        self.optimized_output.setText(output_string)

    def clearOptimizedPanel(self):
        self.optimized_output.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


