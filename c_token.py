class Token:
    def __init__(self, token_type, value, line_number, position):
        self.type = token_type 
        self.value = value           
        self.line_number = line_number   
        self.position = position     

    def __str__(self):
        return f"Token(type='{self.type}', value='{self.value}', line_number={self.line_number}, position={self.position})"
