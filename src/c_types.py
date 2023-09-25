from enum import Enum

class TokenType(Enum):
    TOKEN_NUMBER = 1,
    TOKEN_DEFAULT_KEY = 3,
    TOKEN_OPTION = 4,
    TOKEN_COMPARATOR = 5,
    TOKEN_IDENTIFIER = 6,
    TOKEN_OPERATOR = 7,
    TOKEN_KEYWORD = 8,
    TOKEN_DELIMITER = 9,
    TOKEN_UNKNOWN = 10,
    TOKEN_PTR_CALL = 11,
    TOKEN_LOOP_OPERATOR = 12, # ex: i++, t--
    TOKEN_PREASSIGN_INCREMENTER = 12, # ex: --a, ++b