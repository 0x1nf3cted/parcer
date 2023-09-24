import os
from c_token import Token
from c_utils import IS_DELIMITER, IS_KEYWORD, IS_COMPARATOR, IS_OPERATOR
from c_types import TokenType



# < > = !
def tokenize(line: str, lineNumber: int):
    tokens: Token = []
    i = 0
    index = 1
    length = len(line)
    
    while i < length:
        if line[i].isspace():
            index += 1
            i += 1
            continue
        
		# check if token is a delimeter
        if IS_DELIMITER(line[i]):
            token = Token(TokenType.TOKEN_DELIMITER, line[i], lineNumber, index-len(line[i]))
            tokens.append(token)
        
        elif IS_COMPARATOR(line[i]):
            temp = line[i]
            index += 1
            
            if i + 1 < length and line[i + 1] == '=':
                temp += '='
                i += 1
                index += 1
            
            token = Token(TokenType.TOKEN_COMPARATOR, temp, lineNumber, index-len(temp))
            tokens.append(token)
			
        
        elif IS_OPERATOR(line[i]):
            temp = line[i]
            index += 1
            temp_type = TokenType.TOKEN_OPERATOR
            if(line[i] == '/' and line[i+1] == '/'):
                break
			
            
            if i + 1 < length and line[i + 1] == '=':
                temp += '='
                i += 1
                index += 1
            
            if temp == '->':
                temp_type = TokenType.TOKEN_PTR_CALL
                i += 1
                index += 1
            
            
            token = Token(temp_type, temp, lineNumber, index-len(temp))
            tokens.append(token)
        
        elif line[i].isnumeric():
            num = line[i]
            index += 1
            temp = i + 1
            
			#check if token is number (int, float, ect....)
            while temp < length and (line[temp].isdigit() or line[temp] == '.'):
                num += line[temp]
                temp += 1
                i += 1
                index += 1
            
            token = Token(TokenType.TOKEN_NUMBER, num, lineNumber, index-len(num))
            tokens.append(token)
        
        elif line[i].isalpha() or line[i] == '#':
            word = line[i]
            index += 1
            temp = i + 1
            token_type = TokenType.TOKEN_IDENTIFIER
            
            while temp < length and (line[temp].isalpha() or line[temp] == '_'):
                word += line[temp]
                temp += 1
                i += 1
                index += 1
            
            if IS_KEYWORD(word):
                token_type = TokenType.TOKEN_KEYWORD
            
            token = Token(token_type, word, lineNumber, index-len(word))
            tokens.append(token)
        else:
            tokens.append(Token(TokenType.TOKEN_UNKNOWN, line[i], lineNumber, index-len(line[i])))

        i += 1   

    for tok in tokens:
        print(tok)

    return tokens





file1 = open("test/main.c", "r")

inside_multi_line_comment = False
lineNumber = 1
while True:
    line = file1.readline()
    if not line:
        break

 
    if inside_multi_line_comment:
 
        if "*/" in line:
            inside_multi_line_comment = False
 
            line = line.split("*/", 1)[1]
        else:
            lineNumber+=1
            continue  # Skip this line if still inside a comment
    else:
        # Check if the line starts a multi-line comment
        if "/*" in line:
            inside_multi_line_comment = True
            # Remove everything before and including "/*"
            line = line.split("/*", 1)[0]
            

    # Tokenize the line (outside of comments)
    tokenize(line, lineNumber)
    lineNumber += 1

file1.close()
