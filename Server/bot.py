from datetime import datetime
import requests
from dateutil import parser
import re

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

class Bot:
    def __init__(self):
        self.name = "Eduard"
        self.values = dict()

    def getTime(self):
        return datetime.now().strftime("%X")
    def getName(self):
        return self.name
    def getEuroData(self):
        try:
            site = requests.get(URL).text            
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        date = site.split(" ", 1)[0]
        exchRate = site.partition("EUR|")[2][0:6]
        return date, exchRate
    def addPrice(self):
        date, exchRate = self.getEuroData()
        if(date not in self.values):
            self.values[date] = exchRate
    def getPriceOnDate(self, date):
        if(date in self.values):
            return self.values[date]
        return "This date is not stored"  
    def containsDate(self, text):
        try:
            res = parser.parse(text, fuzzy=True, dayfirst=True)
            date = res.strftime("%d.%m.%Y")
            return date
        except:
            return None
    def dictToString(self):
        text = ""
        for key in self.values:
            text += key + " EUR/CZK " + self.values[key] + "\n"
        return text
    
    def chooseRequestType(self, text):
        flag = None
        
        name_arr = ["name", "nick"]
        time_arr = ["time", "o'clock", "clock"]
        euro_arr = ["eur", "euro", "exchange"]
        help_arr = ["help"]
        
        text = text.lower()
        
        if re.compile('|'.join(name_arr)).search(text):
            flag = 1
        if re.compile('|'.join(time_arr)).search(text):
            if(flag != None):
                flag = 0
                return flag
            flag = 2
        if re.compile('|'.join(euro_arr)).search(text):
            if(flag != None):
                flag = 0
                return flag
            flag = 3
        if re.compile('|'.join(help_arr)).search(text):
            if(flag != None):
                flag = 0
                return flag
            flag = 4
        return flag
