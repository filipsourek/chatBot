from datetime import datetime
import requests
from dateutil import parser
import re
from apscheduler.schedulers.background import BackgroundScheduler


URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
HELP_MSG = "List of requests: \n time - returns current time \n name - returns name \n euro - returns current euro rate \n euro 'date' - returns euro on date \n euro all - returns all dates \n help - returns list of requests"

class Bot:
    def __init__(self):
        self.name = "Eduard"
        self.values = dict()
        
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.addPrice, 'cron', day_of_week = 'mon-fri', hour=14, minute=31, second=0, timezone='Europe/Prague')
        self.scheduler.start()

    def getTime(self):
        return datetime.now().strftime("%X")
    def getName(self):
        return self.name
    def getEuroData(self):
        try:
            site = requests.get(URL).text            
        except requests.exceptions.RequestException as e:
            raise  (e)
        date = site.split(" ", 1)[0]
        exchRate = site.partition("EUR|")[2][0:6]
        exchRate = round(float(exchRate.replace(",",".")), 3)
        return date, exchRate
    def addEuro(self, date, value):
        self.values[date] = value
    def addPrice(self):
        try:
            date, exchRate = self.getEuroData()
        except requests.RequestException as e:
            pass
        else:
            if(date not in self.values):
                self.values[date] = exchRate
            
    def getPriceOnDate(self, date):
        if(date in self.values):
            return self.values[date]
        raise Exception("Date not found")
     
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
            text += "{} EUR/CZK {:.2f}\n".format(key, self.values[key])
        return text
    
    def euroAvg(self):
        numOfDates = 3
        if len(self.values) < numOfDates:
            return False

        sumVal = 0
        x = list(self.values.items())
        for i in range(len(x)-numOfDates, len(x)):
            sumVal += x[i][1]  
        return round(sumVal/numOfDates, 3)
    
    def recmEuro(self):
        P = 10
        avg = self.euroAvg()
        if avg == False:
            return False, 0, 0
        val3 = [*self.values.values()][-3]
        val2 = [*self.values.values()][-2]
        val1 = [*self.values.values()][-1]
        
        if val3 > val1:
            return True, 1, val3 - val1
        else:
            if(((val1 - val3)) < avg/P):
                return True, 2, round((val1 - val3), 3)
            return False, 2, round(((val1 - val3)), 3)
        
    def chooseRequestType(self, text):
        flag = None
        
        name_arr = ["name", "nick"]
        time_arr = ["time", "o'clock", "clock"]
        euro_arr = ["eur", "euro", "exchange"]
        help_arr = ["help"]
        buy_help = ["buy"]
 
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
        if re.compile('|'.join(buy_help)).search(text):
            if(flag != None):
                flag = 0
                return flag
            flag = 5
        return flag
    def getResponse(self, text):
        req_type = self.chooseRequestType(text)
        
        match req_type:
            case 0:
                return "I'm not sure which request you want"
            case 1:
                return self.getName()
            case 2:  
                return self.getTime()
            case 3:
                if not len(self.values) == 0:
                    date = self.containsDate(text)
                    if ('date' in text):
                        if(self.containsDate(text) != None):
                            try:
                                return self.getPriceOnDate(date)
                            except Exception as e:
                                return e
                    elif('all' in text):
                        return self.dictToString()
                    return [*self.values.keys()][-1] + " EUR/CZK = " + str(self.values[[*self.values.keys()][-1]]) 
                return "I don't have any data"
            case 4:
                return HELP_MSG
            case 5:
                buy, type, val = self.recmEuro()
                if type == 0:
                    return "Not enough euro data"
                if type == 1:
                    if buy == True:
                        return "Buy, euro is lower by {:.2f}".format(val)
                if type == 2:
                    if buy == True:
                        return "Buy, euro is higher only by {:.2f} which is less than {:.2f}".format(val, round(self.euroAvg()/10, 3))
                    return "Don't buy, euro is higher by {:.2f} which is more than {:.2f}".format(val, round(self.euroAvg()/10, 3))
            case _:
                return "I don't understand"

