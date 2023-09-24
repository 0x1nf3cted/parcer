def IS_DELIMITER(token: str) -> bool:
    return token in '()[]{|_,;}:'

def IS_OPERATOR(token: str) -> bool:
    return token in '+-*/%'

def IS_COMPARATOR(token: str) -> bool:
    return token in '=<>!'

def IS_KEYWORD(token: str) -> bool:
    c_keywords = {
        "#include", "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
        "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register",
        "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
        "union", "unsigned", "void", "volatile", "while"
    }

    return token in c_keywords
