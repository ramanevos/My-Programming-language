author: 100488290
PROGRAMMING LANGUAGE RULES:
Space between the tokens does not make a difference  Ex: 2+2  is the same as 2 + 2

Arithmetic:
To insert a number: insert the number in the format 4 or -4(for integers), 4.5 or -4.5(for floats)
Operation allowed: +, -, *, /
Brackets operation are supported: ex: (10 + 10) /2

Logical:
Supported: >, <, >=, <=, !, !=, |, &, false, true
| = OR
& = AND
false(lowercase) = Boolean FALSE
true(lowercase) = Boolean TRUE

Strings:
To insert a string: all the text insert between a opening and closing '"' is considered as string ex: "this is a string 4"
If a string contains a single backslash followed by n ex:"\n" then a newline is added"
If a string contains a double backslash followed by n or any other character ex:"\\n" then "\n" is printed with the rest of the string
string contactation allowed in format: "string" + "string"

Global variables:
variable are represented as a text without bracket
Format of variable assignment has as initial part "variablename =". After the "=" any number, string, arithmetic or logical operation
can be inserted. This will be stored in the variablename. 
The content of variablename can be used to assign other variables. Ex: variablename2 = variablenam
To print the content of a variable, the keyword "Display" is used. Ex: Display variablename

Input:
To insert a input the following format is needed: 
variablename = input "text to display with the input"
or
variablename = input      This second option doesn't print any text before the input