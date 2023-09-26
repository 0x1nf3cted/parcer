# ****************************************************************************
# File: c_token.py
# Author: Duckduckcodes (https://github.com/duckduckcodes)
# Date: 26/09/2023
#
# Description:
# This Python file contains the implementation of various classes related to
# tokenization, abstract syntax trees (AST), and other language processing
# constructs
#
# ****************************************************************************



class Token:
    def __init__(self, token_type, value, line_number, position):
        self.type = token_type 
        self.value = value           
        self.line_number = line_number   
        self.position = position     

    def __str__(self):
        return f"Token(type='{self.type}', value='{self.value}', line_number={self.line_number}, position={self.position})"


class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def __str__(self):
        return f"AST(node_type='{self.node_type}', value='{self.value}', children={self.children}, parent={self.parent})"

    def to_json(self):
        ast = {}
        ast["children"] = []
        if(type(self) is ASTNode):
            ast["node_type"] = self.node_type
            ast["value"] = self.value
            ast["parent"] = None
            for child in self.children:
                ast["children"].append(child.to_json())

        return ast
        

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        if self.value is not None:
            node_str += f": {self.value}"
        result = [node_str]

        # Recursively add child nodes
        print(type(self.children))
        for child in self.children:
            child_str = child.to_string(level + 1)
            result.extend(child_str.split('\n'))

        
        return '\n'.join(result)

# class for Number nodes
class BinaryOperatorNode(ASTNode):
    def __init__(self, operator, left, right, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.operator = operator
        self.left = left
        self.right = right


    def to_json(self):
        BinaryOperatorAST = {}
        
        BinaryOperatorAST["node_type"] = self.node_type
        BinaryOperatorAST["operator"] = self.operator
        
        if isinstance(self.left, ASTNode):
            BinaryOperatorAST["left"] = self.left.to_json()
        else:
            BinaryOperatorAST["left"] = self.left.value

        if isinstance(self.right, ASTNode):
            BinaryOperatorAST["right"] = self.right.to_json()
        else:
            BinaryOperatorAST["right"] = self.right.value
 
        return BinaryOperatorAST
    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        node_str += f"{indent}left: {self.left.value}, operator: {self.operator}, right: {self.right.value}\n"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.left, ASTNode):
 
                child_str = self.left.to_string(level + 1)
                result.append(f"{indent}left: ")
                result.extend(child_str.split('\n'))

        if isinstance(self.right, ASTNode):
                
                child_str = self.right.to_string(level + 1)
                result.append(f"{indent}right: ")
                result.extend(child_str.split('\n'))


        return '\n'.join(result)

# class for Array nodes 
class ArrayNode(ASTNode):
    def __init__(self, name: str, size: int, elements, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.size = size
        self.elements = elements


    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        node_str += f"{indent}name: {self.name}, size: {self.size}"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.elements, ASTNode):
 
                child_str = self.elements.to_string(level + 1)
                result.append(f"{indent}elements: ")
                result.extend(child_str.split('\n'))

        return '\n'.join(result)



# class for Struct nodes 
class StructNode(ASTNode):
    def __init__(self, name,  elements, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.elements = elements


# class for Macro nodes
class MacroNode(ASTNode):
    def __init__(self, name, macro_body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.body = macro_body


# class for nodes (character, int, float, string, ect...)
class VariableNode(ASTNode):
    def __init__(self, value, varType, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.varType = varType
        self.value = value

    def to_json(self, level=0):
        VariableAST = {}
 
        VariableAST["Type"] = self.node_type
        VariableAST["VariableType"] = self.varType.value
        VariableAST["Value"] = self.value.value

 

        return VariableAST

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:\n"
        
        node_str += f"{indent}type: {self.varType.value}, identifier: {self.value.value}"

        result = [node_str]

        return '\n'.join(result)



# class for Asignements
class AssignmentNode(ASTNode):
    def __init__(self, left, right, operator, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.left = left
        self.right = right
        self.operator = operator


    def to_json(self):
        AssignmentAST = {}
        
        AssignmentAST["node_type"] = self.node_type
        AssignmentAST["operator"] = self.operator
        
        if isinstance(self.left, ASTNode):
            AssignmentAST["left"] = self.left.to_json()
        else:
            AssignmentAST["left"] = self.left.value

        if isinstance(self.right, ASTNode):
            AssignmentAST["right"] = self.right.to_json()
        else:
            
            AssignmentAST["right"] = self.right.value
 
        return AssignmentAST
    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        result = [node_str]

        # Recursively add child nodes
 
        if isinstance(self.left, ASTNode):
            child_str = self.left.to_string(level + 1)
            result.append(f"{indent}left: ")
            result.extend(child_str.split('\n'))
        else:
            result.append(f"{indent}left: {self.left.value}")
        
        result.append(f"{indent}operator: {self.operator}")
 
        if isinstance(self.right, ASTNode):
            child_str = self.right.to_string(level + 1)
            result.append(f"{indent}right: ")
            result.extend(child_str.split('\n'))
        else:
            
            result.append(f"{indent}right: {self.right.value}")
 

        return '\n'.join(result)


# class for Conditionals
class IfStatementNode(ASTNode):
    def __init__(self, condition, body, node_type, elif_num, children=[], parent=None):
        super().__init__(node_type)
        self.node_type = node_type
        self.condition = condition
        self.parent=parent
        self.children = children
        self.body = body
        self.elif_num = elif_num
        self.else_body = []

    def to_json(self):
        IfStatementAST = {}
        
        IfStatementAST["node_type"] = self.node_type
        IfStatementAST["elif_num"] = self.elif_num
        IfStatementAST["else_body"] = []  # (for now), later, it will be populated with other if block data

        
        if isinstance(self.condition, ASTNode):
            IfStatementAST["condition"] = self.condition.to_json()


        if type(self.children) == 'list' and isinstance(self.children[0], ASTNode):
            IfStatementAST["children"] = self.children.to_json()
        else:
            IfStatementAST["Children"] = self.children[0].value
 
        return IfStatementAST
    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}Node type: {self.node_type}, Else num: {self.elif_num}"
        
        result = [node_str]

        # Recursively add child nodes
 
        if isinstance(self.condition, ASTNode):
            child_str = self.condition.to_string(level + 1)
            result.append(f"{indent}condition: ")
            result.extend(child_str.split('\n'))



        if type(self.children) == 'list' and isinstance(self.children[0], ASTNode):
            for ch in self.children:
                child_str = ch.to_string(level + 1)
                result.extend(child_str.split('\n')) 
        else:
            result.append(f"{indent}children: {self.children}")
 
 

        return '\n'.join(result)



# class for While loop
class WhileLoopNode(ASTNode):
    def __init__(self, condition, body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.condition = condition
        self.body = body


# class for Function declaration
class FunctionDeclarationNode(ASTNode):
    def __init__(self, return_type, name, parameters, body, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body


# class for Function calls
class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.name = name
        self.arguments = arguments

# class for For loop
class ForLoopNode(ASTNode):
    def __init__(self, initialization, condition, update, body, node_type, children=[], parent=None):
        super().__init__(node_type)
        self.node_type = node_type
        self.parent = parent
        self.initialization = initialization
        self.condition = condition
        self.update = update
        self.children = children
        self.body = body


    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def to_json(self):
        ForLoopAST = {}
        
        ForLoopAST["node_type"] = self.node_type
        local_body = []
        for i in self.body:
            local_body.append(i.value)
        ForLoopAST["body"] = local_body
        
        if isinstance(self.initialization, ASTNode):
            ForLoopAST["Initialization"] = self.initialization.to_json()
        
        if type(self.children) == 'list' and isinstance(self.children[0], ASTNode):
            ForLoopAST["Children"] = self.children.to_json()
        else:
            ForLoopAST["Children"] = self.children[0].value

        if isinstance(self.condition, ASTNode):
            ForLoopAST["Condition"] = self.condition.to_json()
 
        if isinstance(self.update, ASTNode):
            ForLoopAST["Update"] = self.update.to_json()
 
        return ForLoopAST

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:"
        
        node_str += f"{indent}body: {self.body}\n"
        result = [node_str]

        # Recursively add child nodes
 
        if isinstance(self.initialization, ASTNode):
            child_str = self.initialization.to_string(level + 1)
            result.extend(child_str.split('\n'))
 
        if isinstance(self.condition, ASTNode):
            child_str = self.condition.to_string(level + 1)
            result.extend(child_str.split('\n'))

        if type(self.children) == 'list' and isinstance(self.children[0], ASTNode):
            for ch in self.children:
                child_str = ch.to_string(level + 1)
                result.extend(child_str.split('\n')) 
            
 
        if isinstance(self.update, ASTNode):
            child_str = self.update.to_string(level + 1)

            result.extend(child_str.split('\n'))

        if isinstance(self.body, ASTNode):
            child_str = self.body.to_string(level + 1)
            
            result.extend(child_str.split('\n'))
            
        

        return '\n'.join(result)



class LoopConditionNode(ASTNode):
    def __init__(self, right, comparator, left, node_type):
        super().__init__(node_type)
        self.node_type = node_type
        self.right = right
        self.comparator = comparator
        self.left = left

    def to_json(self):
        LoopConditionAST = {}
        
        LoopConditionAST["node_type"] = self.node_type
        LoopConditionAST["comparator"] = self.comparator.value
        
        if isinstance(self.left, ASTNode):
            LoopConditionAST["left"] = self.left.to_json()
        else:
            LoopConditionAST["left"] = self.left.value

        if isinstance(self.right, ASTNode):
            LoopConditionAST["right"] = self.right.to_json()
        else:
            LoopConditionAST["right"] = self.right.value

 
        return LoopConditionAST

    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}:\n"
        
        node_str += f"{indent}left: {self.left.value}, comparator: {self.comparator.value}, right: {self.right.value}"
        result = [node_str]

        # Recursively add child nodes
        if isinstance(self.left, list)  == True:
        
            for child in self.left:
                if isinstance(child, ASTNode):
                    child_str = child.to_string(level + 1)
                    result.extend(child_str.split('\n'))

        if isinstance(self.right, list)  == True:
        
            for child in self.right:
                if isinstance(child, ASTNode):
                    child_str = child.to_string(level + 1)
                    
                    result.extend(child_str.split('\n'))


        return '\n'.join(result)

