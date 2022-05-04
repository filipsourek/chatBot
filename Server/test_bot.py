import bot
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
    original = "Help me"
    expected = 4
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

