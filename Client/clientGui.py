from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import client

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("ChatBot")
                
                self.resize(300,270)
                self.network = client.Client()

                self.textEdit = QTextEdit()
                self.textEdit.setReadOnly(True)
                
                self.input = QLineEdit()
                
                self.btnPress1 = QPushButton("Send")

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                layout.addWidget(self.input)
                layout.addWidget(self.btnPress1)
                self.setLayout(layout)

                self.btnPress1.clicked.connect(self.btnPress1_Clicked)
