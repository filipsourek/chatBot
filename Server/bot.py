from datetime import datetime


URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

class Bot:
    def __init__(self):
        self.name = "Eduard"
        self.values = dict()

    def getTime(self):
        return datetime.now().strftime("%X")
    def getName(self):
        return self.name