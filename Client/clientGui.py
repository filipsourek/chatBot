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
                
        def btnPress1_Clicked(self):
            if(self.input.text() != ""):
                
                self.textEdit.append("You: "+ self.input.text())
                self.network.send_msg(self.input.text())
                answer = self.network.recv_msg()
                self.textEdit.append("Bot: "+ answer)
                self.input.clear()
        
        def keyPressEvent(self, event):
            if event.key() == Qt.Key_Return:
                self.btnPress1_Clicked()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec_())