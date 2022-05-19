from unittest import mock

#from requests import RequestException
import requests
import bot
import datetime
import pytest
from freezegun import freeze_time

def test_name():
    original = "Give me your name"
    expected = 1
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_time():
    original = "Whats the time"
    expected = 2
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_euro():
    original = "Whats the exchange rate of euro"
    expected = 3
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_help():
    original = "Help me"
    expected = 4
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_help():
    original = "Help me, name"
    expected = 0
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_buy():
    original = "buy"
    expected = 5
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_bu2():
    original = "name, buy"
    expected = 0
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_double_request():
    original = "Hgive me euro and time"
    expected = 0
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
def test_invalid_request():
    original = "ASD"
    expected = None
    b = bot.Bot()
    result = b.chooseRequestType(original)
    assert expected == result
@freeze_time("2022-01-01 18:43:20")
def test_time2():
        expected = "18:43:20"
        b = bot.Bot()
        result = b.getTime()
        assert expected == result
def test_name():
    expected = "Eduard"
    b = bot.Bot()
    result = b.getName()
    assert expected == result
        
def test_contains_date():
    expected = "02.04.2022"
    b = bot.Bot()
    result = b.containsDate("euro on date 2.4.2022")
    assert expected == result
def test_contains_date_invalid():
    expected = None
    b = bot.Bot()
    result = b.containsDate("Euro on date")
    assert expected == result
def test_getResponse_NotSure():
    expected = "I'm not sure which request you want"
    b = bot.Bot()
    result = b.getResponse("time and name")
    assert expected == result
def test_getResponse_Name():
    expected = "Eduard"
    b = bot.Bot()
    result = b.getResponse("name")
    assert expected == result
@freeze_time("2022-01-01 18:53:20")
def test_getResponse_Time():
    expected = "18:53:20"
    b = bot.Bot()
    result = b.getResponse("time")
    assert expected == result
def test_getResponse_Euro():
    expected = 5
    b = bot.Bot()
    b.addEuro("28.04.2022", 5)
    result = b.getResponse("euro on date 28.4.2022")
    assert expected == result
def test_getResponse_Error():
    expected = "I don't understand"
    b = bot.Bot()
    result = b.getResponse("ASD")
    assert expected == result
def test_getResponse_Help():
    expected = "List of requests: \n time - returns current time \n name - returns name \n euro - returns current euro rate \n euro 'date' - returns euro on date \n euro all - returns all dates \n help - returns list of requests"
    b = bot.Bot()
    result = b.getResponse("help")
    assert expected == result
def test_getResponse_BuyError():
    expected = "Not enough euro data"
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    result = b.getResponse("buys")
    assert expected == result
def test_getResponse_Buy1():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 19)
    b.addEuro("30.04.2022", 18)
    expected = "Buy, euro is lower by {:.2f}".format(20-18)

    result = b.getResponse("buy")
    assert expected == result
def test_getResponse_Buy2True():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    b.addEuro("30.04.2022", 22)
    expected = "Buy, euro is higher only by {:.2f} which is less than {:.2f}".format(22-20, round(b.euroAvg()/10, 3))

    result = b.getResponse("buy")
    assert expected == result
def test_getResponse_Buy2False():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    b.addEuro("30.04.2022", 23)
    expected = "Don't buy, euro is higher by {:.2f} which is more than {:.2f}".format((23-20), round(b.euroAvg()/10, 3))
    result = b.getResponse("buy")
    assert expected == result
def test_getEuroData():  
    with mock.patch('requests.get', side_effect=requests.RequestException('Failed Request')) as mock_request_post:
        b = bot.Bot()
        with pytest.raises(requests.exceptions.RequestException):
            b.getEuroData()
def test_getPriceOnDate():
    expected = "Date not found"
    b = bot.Bot()
    with pytest.raises(Exception):
        b.getPriceOnDate("1.1.1000")
def test_euroAvg():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    b.addEuro("30.04.2022", 22)
    result = b.euroAvg()
    assert 21 == result
def test_euroAvg_False():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    result = b.euroAvg()
    assert False == result
def test_recmEuro():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    result = b.recmEuro()
    assert (False, 0, 0) == result
def test_recmEuro_True():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 19)
    b.addEuro("30.04.2022", 18)
    result = b.recmEuro()
    assert (True, 1, 20-18) == result
def test_recmEuro_True2():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 21)
    b.addEuro("30.04.2022", 22)
    result = b.recmEuro()
    assert (True, 2, 2) == result
def test_recmEuro_False2():
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("29.04.2022", 25)
    b.addEuro("30.04.2022", 28)
    result = b.recmEuro()
    assert (False, 2, 8) == result
def test_getResponse_recm():
    expected = "Not enough euro data"
    b = bot.Bot()
    b.addEuro("28.04.2022", 20)
    b.addEuro("28.04.2022", 22)

    result = b.getResponse("buy")
    assert expected == result



