class SchdeuleParserException(Exception):
    pass

class NotFoundGroupException(SchdeuleParserException):
    pass

class NotFoundWeekdayException(SchdeuleParserException):
    pass

class SundayWorkDayException(SchdeuleParserException):
    pass