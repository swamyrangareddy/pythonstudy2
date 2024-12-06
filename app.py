import streamlit as st
from streamlit_option_menu import option_menu


class PythonApp:
    def __init__(self):
        self.title = "Python App"

    def Basics(self):
        st.title("Python Basics Quiz")

        # Quiz data with options and correct answers
        questions = [
                    {
                "number": 1,
                "question": "What type of programming language is Python?",
                "options": [
                    "Low-level, compiled",
                    "High-level, interpreted",
                    "High-level, compiled",
                    "Low-level, interpreted"
                ],
                "answer": "High-level, interpreted"
            },
            {
                "number": 2,
                "question": "Which of the following is NOT a feature of Python?",
                "options": [
                    "Easy syntax",
                    "Dynamically typed",
                    "Extensive libraries",
                    "Limited support for AI applications"
                ],
                "answer": "Limited support for AI applications"
            },
            {
                "number": 3,
                "question": "Where can you install Python from?",
                "options": [
                    "python.org",
                    "pyinstaller.com",
                    "pypi.org",
                    "anaconda.com"
                ],
                "answer": "python.org"
            },
            {
                "number": 4,
                "question": "Which of the following IDEs is commonly used for Python?",
                "options": [
                    "Eclipse",
                    "VSCode",
                    "Xcode",
                    "NetBeans"
                ],
                "answer": "VSCode"
            },
            {
                "number": 5,
                "question": "Which domain does Python NOT actively serve?",
                "options": [
                    "Web Development",
                    "Game Development",
                    "Embedded Systems",
                    "Data Science"
                ],
                "answer": "Embedded Systems"
            },
            {
                "number": 6,
                "question": "What is Python widely used for in data science?",
                "options": [
                    "Building predictive models",
                    "Analyzing large datasets",
                    "Developing AI systems",
                    "All of the above"
                ],
                "answer": "All of the above"
            },
            {
                "number": 7,
                "question": "Which Python library would you use for scientific computing?",
                "options": [
                    "NumPy",
                    "Django",
                    "Flask",
                    "Pygame"
                ],
                "answer": "NumPy"
            },
            {
                "number": 8,
                "question": "What does the following Python code do?\n```python\nprint(\"Hello World!\")\n```",
                "options": [
                    "Displays an error",
                    "Prints the message Hello World!",
                    "Executes the print function",
                    "Runs without output"
                ],
                "answer": "Prints the message Hello World!"
            },
            {
                "number": 9,
                "question": "How does Python handle the expression `5 + 5` without quotes?",
                "options": [
                    "Prints '5 + 5' as a string",
                    "Throws a syntax error",
                    "Prints the numerical result 10",
                    "Returns the value as a float"
                ],
                "answer": "Prints the numerical result 10"
            },
            {
                "number": 10,
                "question": "Which of the following is NOT a career opportunity for Python developers?",
                "options": [
                    "Data Scientist",
                    "Machine Learning Engineer",
                    "Web Developer",
                    "Database Administrator"
                ],
                "answer": "Database Administrator"
            },
            {
                "number": 11,
                "question": "How can multi-line comments be implemented in Python?",
                "options": [
                    "Using multiple # symbols at the start of each line",
                    "Using triple quotes (''' or \")",
                    "Using /* and */",
                    "Python does not support multi-line comments"
                ],
                "answer": "Using triple quotes (''' or \")"
            },
            {
                "number":12,
                "question": "What happens to text after the # symbol on the same line in Python?",
                "options": [
                    "It is executed as code",
                    "It is ignored by the Python interpreter",
                    "It causes a syntax error",
                    "It is treated as a string"
                ],
                "answer": "It is ignored by the Python interpreter"
            }
        ]

        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    def DataTypes(self):
        st.title("Data Types Quiz")

            # Quiz data with options and correct answers
        questions = [
        {
            "number": 1,
            "question": "Which of the following is a valid string in Python?",
            "options": ['"Hello World"', "'Hello World'", 'Hello World', '123'],
            "answer": '"Hello World"'
        },
        {
            "number": 2,
            "question": "What type of data is 5 in Python?",
            "options": ["String", "Integer", "Float", "Boolean"],
            "answer": "Integer"
        },
        {
            "number": 3,
            "question": "Which data type would be used to represent the value 3.14 in Python?",
            "options": ["String", "Integer", "Float", "Boolean"],
            "answer": "Float"
        },
        {
            "number": 4,
            "question": "Which of the following is a Boolean value in Python?",
            "options": ["True", "None", "5", "Hello"],
            "answer": "True"
        },
        {
            "number": 5,
            "question": "What type of data is the value '123' in Python?",
            "options": ["String", "Integer", "Float", "Boolean"],
            "answer": "String"
        },
        {
            "number": 6,
            "question": "Which of the following is a valid way to declare a float in Python?",
            "options": ["3", "3.0", "'3.0'", "True"],
            "answer": "3.0"
        },
        {
            "number": 7,
            "question": "What is the output of the expression: `print(type(5))`?",
            "options": ["<class 'String'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"],
            "answer": "<class 'int'>"
        },
        {
            "number": 8,
            "question": "Which of the following is the correct way to check if a variable is of type 'str'?",
            "options": ["type(variable) == 'str'", "type(variable) == str", "type(variable) == 'string'", "str(variable)"],
            "answer": "type(variable) == str"
        },
        {
            "number": 9,
            "question": "Which of these is NOT a valid way to declare a string in Python?",
            "options": ['"Hello"', "'Hello'", 'Hello', '"""Hello"""'],
            "answer": 'Hello'
        },
        {
            "number": 10,
            "question": "What will the following code print?\n```python\nx = True\nprint(type(x))\n```",
            "options": ["<class 'str'>", "<class 'bool'>", "<class 'int'>", "<class 'float'>"],
            "answer": "<class 'bool'>"
        }
        ]

        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    def Operators(self):
        st.title("Operators Quiz")

        # Quiz data with options and correct answers
        questions = [
        {
            "number": 1,
            "question": "What is the result of `5 + 3` in Python?",
            "options": ["5", "8", "53", "35"],
            "answer": "8"
        },
        {
            "number": 2,
            "question": "What is the result of `10 - 4` in Python?",
            "options": ["6", "14", "40", "4"],
            "answer": "6"
        },
        {
            "number": 3,
            "question": "What is the result of `6 * 7` in Python?",
            "options": ["42", "13", "63", "56"],
            "answer": "42"
        },
        {
            "number": 4,
            "question": "What is the result of `10 / 2` in Python?",
            "options": ["5", "2", "10", "20"],
            "answer": "5"
        },
        {
            "number": 5,
            "question": "What is the result of `10 % 3` in Python?",
            "options": ["1", "3", "2", "0"],
            "answer": "1"
        },
        {
            "number": 6,
            "question": "Which of the following is the correct operator for modulus in Python?",
            "options": ["%", "//", "/=", "^"],
            "answer": "%"
        },
        {
            "number": 7,
            "question": "What will the following code print?\n```python\nx = [1, 2, 3]\nprint(x[1])\n```",
            "options": ["1", "2", "3", "Error"],
            "answer": "2"
        },
        {
            "number": 8,
            "question": "What is the result of `5 // 2` in Python?",
            "options": ["2", "2.5", "2.0", "3"],
            "answer": "2"
        },
        {
            "number": 9,
            "question": "Which operator is used for division in Python that returns a float result?",
            "options": ["/", "//", "%", "*"],
            "answer": "/"
        },
        {
            "number": 10,
            "question": "What will the following code print?\n```python\nx = [5, 10, 15]\nprint(x[2])\n```",
            "options": ["5", "10", "15", "Error"],
            "answer": "15"
    },
    {
        "number": 11,
        "question": "What is the correct syntax to format a string in Python using placeholders?",
        "options": [
            "'Hello {}'.format(name)",
            "'Hello {name}'.format()",
            "'Hello {}'.format()",
            "'Hello {}.format(name)'"
        ],
        "answer": "'Hello {}'.format(name)"
    },
    {
        "number": 12,
        "question": "Which of the following does NOT require type conversion when using string formatting?",
        "options": [
            "String",
            "Integer",
            "Boolean",
            "None of the above"
        ],
        "answer": "None of the above"
    },
    {
        "number": 13,
        "question": "What is the output of the following code?\n```python\nname = 'Alice'\nprint('Hello {}'.format(name))\n```",
        "options": [
            "'Hello Alice'",
            "'Hello {}'",
            "'Hello name'",
            "'Alice Hello'"
        ],
        "answer": "'Hello Alice'"
    },
    {
        "number": 14,
        "question": "How can you add multiple placeholders in a string and format them in Python?",
        "options": [
            "'Hello {} and {}'.format(name, age)",
            "'Hello {} and {}'.format()",
            "'Hello {name} and {age}'.format(name, age)",
            "'Hello {name, age}'.format()"
        ],
        "answer": "'Hello {} and {}'.format(name, age)"
    }
        ]

        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    def Conditionals(self):
        st.title("Conditionals Quiz")

        # Quiz data with options and correct answers
        questions = [
        {
            "number": 1,
            "question": "What will the result of the comparison `5 > 3` be?",
            "options": ["True", "False", "Error", "None"],
            "answer": "True"
        },
        {
            "number": 2,
            "question": "What is the result of `7 == 8` in Python?",
            "options": ["True", "False", "Error", "None"],
            "answer": "False"
        },
        {
            "number": 3,
            "question": "Which operator is used to check if two values are not equal in Python?",
            "options": ["==", "!=", ">", "<", "<="],
            "answer": "!="
        },
        {
            "number": 4,
            "question": "What will the result of the expression `4 >= 4` be?",
            "options": ["True", "False", "Error", "None"],
            "answer": "True"
        },
        {
            "number": 5,
            "question": "Which of the following is the correct operator for 'less than or equal to' in Python?",
            "options": [">", "<", "==", "<="],
            "answer": "<="
        },
        {
            "number": 6,
            "question": "What will the result of `10 != 5` be?",
            "options": ["True", "False", "Error", "None"],
            "answer": "True"
        },

        # Conditional Statements
        {
            "number": 7,
            "question": "Which of the following keywords is used to check multiple conditions in Python?",
            "options": ["if", "else", "elif", "for"],
            "answer": "elif"
        },
        {
            "number": 8,
            "question": "What is the result of the following code?\n```python\nx = 5\nif x > 3:\n    print('Greater')\nelse:\n    print('Lesser')\n```",
            "options": ["Greater", "Lesser", "Error", "None"],
            "answer": "Greater"
        },
        {
            "number": 9,
            "question": "Which of the following is used to start a conditional block in Python?",
            "options": ["{", "if", "while", ":"],
            "answer": "if"
        },
        {
            "number": 10,
            "question": "How is indentation used in Python?",
            "options": ["To separate code blocks", "To comment code", "To define functions", "To define variables"],
            "answer": "To separate code blocks"
        },
        {
            "number": 11,
            "question": "What will the following code output?\n```python\nx = 4\nif x > 5:\n    print('Greater')\nelse:\n    print('Lesser')\n```",
            "options": ["Greater", "Lesser", "Error", "None"],
            "answer": "Lesser"
        },
        {
            "number": 12,
            "question": "Which of the following is a correct Python if-else structure?",
            "options": [
                "if x > 5 {print('Greater')}",
                "if x > 5: print('Greater')",
                "if x > 5 then: print('Greater')",
                "if (x > 5) then print('Greater')"
            ],
            "answer": "if x > 5: print('Greater')"
        },
        {
            "number": 13,
            "question": "What will the following code print?\n```python\nx = 10\nif x > 5:\n    print('Greater')\nelif x == 10:\n    print('Equal')\nelse:\n    print('Lesser')\n```",
            "options": ["Greater", "Equal", "Lesser", "Error"],
            "answer": "Greater"
        },
        {
            "number": 14,
            "question": "What is the result of `5 < 10 and 10 > 5`?",
            "options": ["True", "False", "None", "Error"],
            "answer": "True"
        },
        {
            "number": 15,
            "question": "What will the following code print?\n```python\nx = 7\nif x < 5:\n    print('Less')\nelif x == 7:\n    print('Equal')\nelse:\n    print('Greater')\n```",
            "options": ["Less", "Equal", "Greater", "None"],
            "answer": "Equal"
        }
        ]

        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    def Loops(self):
        st.title("Python Basics Quiz")
    
        # Quiz data with options and correct answers
        questions = [
        {
            "number": 1,
            "question": "Which of the following is the correct syntax for a `for` loop in Python?",
            "options": [
                "for i in range(10):",
                "for (i=0; i<10; i++):",
                "for i = 0 to 10:",
                "for i in 10:"
            ],
            "answer": "for i in range(10):"
        },
        {
            "number": 2,
            "question": "What will the following code output?\n```python\nfor i in range(3):\n    print(i)\n```",
            "options": ["0", "1", "2", "0 1 2", "0 1 2 3"],
            "answer": "0 1 2"
        },
        {
            "number": 3,
            "question": "What is the correct way to stop a `while` loop in Python?",
            "options": ["exit", "end", "break", "continue"],
            "answer": "break"
        },
        {
            "number": 4,
            "question": "What will the following code output?\n```python\nx = 0\nwhile x < 3:\n    print(x)\n    x += 1\n```",
            "options": ["0", "1", "2", "0 1 2", "Error"],
            "answer": "0 1 2"
        },
        {
            "number": 5,
            "question": "Which loop will execute at least once, even if the condition is false?",
            "options": ["for", "while", "do-while", "None"],
            "answer": "do-while"
        },
        {
            "number": 6,
            "question": "What will the following code output?\n```python\nfor i in range(2, 6, 2):\n    print(i)\n```",
            "options": ["2 4", "2 3 4 5", "2 4 6", "3 4 5"],
            "answer": "2 4"
        },
        {
            "number": 7,
            "question": "What will happen if the condition in a `while` loop is always true?",
            "options": ["The loop will execute forever", "The loop will execute once", "The loop will not execute", "The code will raise an exception"],
            "answer": "The loop will execute forever"
        },
        {
            "number": 8,
            "question": "Which of the following will make a `for` loop skip the current iteration?",
            "options": ["continue", "break", "exit", "pass"],
            "answer": "continue"
        },
        {
            "number": 9,
            "question": "What will the following code output?\n```python\nfor i in range(3):\n    if i == 1:\n        break\n    print(i)\n```",
            "options": ["0", "0 1", "0 1 2", "None"],
            "answer": "0"
        },
        {
            "number": 10,
            "question": "How would you print the numbers from 1 to 5 using a `while` loop?",
            "options": [
                "while i <= 5: print(i); i += 1",
                "while i < 5: print(i); i += 1",
                "while i = 1 to 5: print(i)",
                "while i <= 5: print(i)"
            ],
            "answer": "while i <= 5: print(i); i += 1"
        }
        ]
        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    def Functions(self):
        st.title("Python Basics Quiz")

        # Quiz data with options and correct answers
        questions = [
         {
        "number": 1,
        "question": "What is the purpose of defining a function in Python?",
        "options": [
            "To store data", 
            "To perform a specific task repeatedly", 
            "To create a variable", 
            "To create a loop"
        ],
        "answer": "To perform a specific task repeatedly"
    },
    {
        "number": 2,
        "question": "Which of the following is the correct way to define a function in Python?",
        "options": [
            "function myFunction():", 
            "def myFunction():", 
            "def function myFunction():", 
            "function: myFunction()"
        ],
        "answer": "def myFunction():"
    },
    {
        "number": 3,
        "question": "What does the following code do?\n```python\ndef greet():\n    print('Hello World')\ngreet()```",
        "options": [
            "Creates a function and prints 'Hello World'", 
            "Defines a function called greet", 
            "Creates a variable and prints 'Hello World'", 
            "Creates an error"
        ],
        "answer": "Creates a function and prints 'Hello World'"
    },
    {
        "number": 4,
        "question": "How do you call a function named `myFunction` in Python?",
        "options": [
            "call myFunction()", 
            "myFunction()", 
            "function myFunction()", 
            "invoke myFunction()"
        ],
        "answer": "myFunction()"
    },
    {
        "number": 5,
        "question": "What will be the output of the following code?\n```python\ndef add(x, y):\n    return x + y\nadd(3, 4)```",
        "options": ["3", "4", "7", "None"],
        "answer": "7"
    },
    {
        "number": 6,
        "question": "What is the correct way to pass arguments to a function in Python?",
        "options": [
            "pass values as arguments inside parentheses", 
            "pass values as a string", 
            "pass values as return statements", 
            "pass values in a list"
        ],
        "answer": "pass values as arguments inside parentheses"
    },

    # Predefined functions
    {
        "number": 7,
        "question": "Which of the following is a pre-defined function in Python?",
        "options": [
            "function()", 
            "len()", 
            "print()", 
            "sum()"
        ],
        "answer": "len()"
    },
    {
        "number": 8,
        "question": "What does the `print()` function do in Python?",
        "options": [
            "Executes the code", 
            "Displays a message or variable value", 
            "Returns the value of a variable", 
            "Stops the program"
        ],
        "answer": "Displays a message or variable value"
    },
    {
        "number": 9,
        "question": "Which of the following will return the total number of elements in a list named `numbers`?",
        "options": [
            "len(numbers)", 
            "numbers.len()", 
            "count(numbers)", 
            "sum(numbers)"
        ],
        "answer": "len(numbers)"
    },
    {
        "number": 10,
        "question": "What will the following code output?\n```python\nnumbers = [1, 2, 3, 4]\nprint(sum(numbers))```",
        "options": ["1", "10", "4", "None"],
        "answer": "10"
    },
    {
        "number": 11,
        "question": "What is the purpose of the `return` statement in a function?",
        "options": [
            "To stop the function execution", 
            "To return a value from the function", 
            "To print output", 
            "To define a function"
        ],
        "answer": "To return a value from the function"
    },

    # Function usage and parameters
    {
        "number": 12,
        "question": "What will the following code output?\n```python\ndef multiply(x, y=2):\n    return x * y\nprint(multiply(4))```",
        "options": ["6", "8", "4", "Error"],
        "answer": "8"
    },
    {
        "number": 13,
        "question": "Which keyword is used to define a function in Python?",
        "options": ["define", "function", "def", "func"],
        "answer": "def"
    },
    {
        "number": 14,
        "question": "Which of the following can be used to call a function with named parameters in Python?",
        "options": [
            "myFunction(x=5, y=10)", 
            "myFunction(5, 10)", 
            "myFunction(5, y=10)", 
            "None of the above"
        ],
        "answer": "myFunction(x=5, y=10)"
    },
    {
        "number": 15,
        "question": "What will the following code print?\n```python\ndef greet(name='User'):\n    print('Hello', name)\ngreet()```",
        "options": ["Hello User", "Hello", "Error", "Hello Name"],
        "answer": "Hello User"
    }
        ]

        
        # Store the user's answers
        user_answers = {}

        # Loop through each question
        for idx, q in enumerate(questions):
            st.write(f'{idx + 1}. {q["question"]}')
            
            # Radio buttons with no default selection
            selected_option = st.radio(
                f"Choose an answer for Question {idx + 1}:",
                q["options"],
                key=idx,
                index=None
            )
            user_answers[idx] = selected_option

        # Submit button
        if st.button("Submit"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["answer"]:
                    st.success(f"Correct! {idx}. {q['question']} -> {user_answers[idx]}")
                    score += 1
                else:
                    st.error(f"Incorrect. {idx}. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")
            st.info(f"Total score is: {score} / {len(questions)}")


    
    def main(self):
        with st.sidebar:
            selected = option_menu(
                menu_title="Select a Page",
                options=["Basics", "Data Types", "Operators", "Conditionals", "Loops", "Functions"],
                icons=["book", "book", "book", "book", "book", "book"],
                menu_icon="cast",
                default_index=0
            )

        if selected == "Basics":
            self.Basics()
        elif selected == "Data Types":
            self.DataTypes()
        elif selected == "Operators":
            self.Operators()    
        elif selected == "Conditionals":
            self.Conditionals()
        elif selected == "Loops":
            self.Loops()
        elif selected == "Functions":
            self.Functions()
        
if __name__ == "__main__":
    app = PythonApp()
    app.main()