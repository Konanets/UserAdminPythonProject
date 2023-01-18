from enum import Enum


class RegExEnum(Enum):
    OnlyWord = (r'^[a-zA-Zа-яА-ЯїЇ]*$', 'enter only alphanumeric characters')
    ContainOneNumber = (r'\d', 'must contain 1 number (0-9)')
    ContainUpperCaseLetter = (r'[A-ZА-ЯЇ]', 'must contain 1 uppercase letter')
    ContainerLowerCaseLetter = (r'[a-zа-яї]', 'must contain 1 lowercase letter')
    ContainNonAlphaNumeric = (r'[^a-zA-Z\d\s:]', 'must contain 1 non-alpha numeric')
    WhiteSpace = (r'\s', 'must not contain white spaces')
    PhoneNumber = (r'^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$', 'invalid phone number')

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
