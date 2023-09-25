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


    def to_string(self, level=0):
        indent = "  " * level
        node_str = f"{indent}{self.node_type}"
        if self.value is not None:
            node_str += f": {self.value}"
        if self.position is not None:
            node_str += f" ({self.position})"
        result = [node_str]
        for child in self.children:
            result.extend(child.to_string(level + 1).split('\n'))
        return '\n'.join(result)

# class for Number nodes
class BinaryOperatorNode(ASTNode):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

# class for Array nodes 
class ArrayNode(ASTNode):
    def __init__(self, name: str, size: int, elements):
        self.name = name
        self.size = size
        self.elements = elements

# class for Struct nodes 
class StructNode(ASTNode):
    def __init__(self, name,  elements):
        self.name = name
        self.elements = elements


# class for Macro nodes
class MacroNode(ASTNode):
    def __init__(self, name, macro_body):
        self.name = name
        self.body = macro_body


# class for nodes (character, int, float, string, ect...)
class VariableNode(ASTNode):
    def __init__(self, value, varType):
        self.varType = varType
        self.value = value


# class for Asignements
class AssignmentNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

# class for Conditionals
class IfStatementNode(ASTNode):
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body


# class for While loop
class WhileLoopNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


# class for Function declaration
class FunctionDeclarationNode(ASTNode):
    def __init__(self, return_type, name, parameters, body):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body


# class for Function calls
class FunctionCallNode(ASTNode):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

# class for For loop
class ForLoopNode(ASTNode):
    def __init__(self, initialization, condition, update, body):
        self.initialization = initialization
        self.condition = condition
        self.update = update
        self.body = body


class LoopConditionNode(ASTNode):
    def __init__(self, right, comparator, left):
        self.right = right
        self.comparator = comparator
        self.left = left

