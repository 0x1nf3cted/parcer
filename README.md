# Parcer: C parser written in Python


Parcer is a simple C parser implemented in Python. This parser is designed to tokenize C code and construct an Abstract Syntax Tree (AST).

## Features

- Tokenizes C code files.
- Recognizes delimiters, keywords, operators, and more.
- Constructs an Abstract Syntax Tree (AST) from the parsed tokens.
- Handles multi-line comments.
- Provides detailed information about each token and AST node.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/duckduckcodes/parcer
    ```
2.  
    ```bash
    cd parcer
    ```
3.    
    ```bash
    python3 src/c_ast.py [file]
    ```


## Example:

1.  **String** format

### Input:

```c

for (int i = 0; i < 10; i += 1) {
    printf("%d", i);
}

```

### Output:

```
Entry:: Program
  For Loop:  body: ['{', 'printf', '(', '"', '%', 'd', '"', ',', 'i', ')', ';', '}']

    Assignement:
    left: 
      Variable:
      type: int, identifier: i
    operator: =
    right: ['0']

    Loop Condition:
    left: ['i'], comparator: <, right: ['10']

    Assignement:
    left: i
    operator: =
    right: 
      Binary Expression:
      left: i, operator: +, right: 1
```

2.  **JSON** format:

```json
{
  "node_type": "Entry",
  "value": "Program",
  "parent": null,
  "children": {
    "node_type": "For Loop",
    "body": ["{", "printf", "(", "\"", "%", "d", "\"", ",", "i", ")", ";", "}"],
    "Initialization": {
      "node_type": "Assignement",
      "operator": "=",
      "left": { "node_type": "Variable", "value": "i", "parent": null },
      "right": ["0"]
    },
    "Condition": {
      "node_type": "Loop Condition",
      "comparator": "<",
      "left": ["i"],
      "right": ["10"]
    },
    "Update": {
      "node_type": "Assignement",
      "operator": "=",
      "left": "i",
      "right": {
        "node_type": "Binary Expression",
        "operator": "+",
        "left": "i",
        "right": "1"
      }
    }
  }
}
```


## ⚠️ Warnings

### Important Information

Please be aware that this project is still in development and may not be stable for production use. Use it at your own risk.

### Contribution

This project is actively under development. You're encouraged to explore, test, and provide feedback. Contributions in the form of bug reports, feature requests, or code contributions are welcome. Please see our [contribution guidelines](https://github.com/duckduckcodes/parcer/blob/main/CONTRIBUTING.md) for more details on how to get involved.
