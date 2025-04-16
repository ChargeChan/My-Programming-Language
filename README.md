# EpicSwag

Ultimate is a stack-based esoteric programming language inspired by [BeeScript](https://esolangs.org/wiki/BeeScript).

| Instruction | Description |
| ------ | ------ |
| UNSUBSCRIBE | Clear the stack of everything |
| UPLOAD {value}| push a value onto the stack |
| UPLOAD_NUM {value}| push a value onto the stack as an integer|
| SHOUT_OUT >{value} | prints everything after the > to the screen |
| ADD | Pops A and then B from the stack and pushes A + B to the stack |
| SUBTRACT | Pops A and then B from the stack and pushes B - A to the stack |
| MULTIPLY | Pops A and then B from the stack and pushes B * A to the stack |
| DIVIDE | Pops A and then B from the stack and pushes B / A to the stack |
| PROMPT [type] | Asks the user to enter a value specified by type. See table below |
| IF_GREATER_THAN {value} {value} | checks if the first value is larger than the second. Allows variables in place of the values. If false, it will skip the line of code directly below it. Otherwise, it will run |
| IF_EQUAL_TO {value} {value} | Same as greater than but checks if values are equal |
| SKIP_TO {timestamp} | skips to the line of code that matches the timestamp name |
| REWIND | Pops everything off the stack then back onto it, reversing the order |
| REWIND COMBO | Pops everything off the stack then pushes it back as a combined string |
| LIKE {variable} | Increments the variable by 1 |
| DISLIKE {variable} | Decrements the variable by 1 |
| PRINT POP | Removes the top value of the stack and displays it |
| PRINT PEEK | Displays the top value of the stack |
| PRINT ALL | Displays all values in the stack |
| PRINT VAR {variable} | Displays the value of the given variable |
| OUTTRO | Terminate program execution |

## Prompt types
| Instruction | Description |
| ------ | ------ |
| string | adds user input to the stack as a string, includes all white space |
| number | adds user input to the stack as an int |
| char | adds user input to the stack as a single char |
| stringArray | pushes each character the user typed into the stack in the order typed |
ex: `PROMPT number` will stop the code to ask for user input


## Variables
Two kinds of variables: Standard python variables and integers.
Here's how to assign a value to a variable in some different ways  
`var awesome = swag`
`int counter =1`
`var message =i love you`  
It will automatically truncate any spaces in between the = and after your input

## Timestamps
Timestamps are just labels like in Assembly
You make them like this:
`!label`

## Comments
You can leave a comment using this symbol: 
Because I thought it'd be funny if most people in my class couldn't type that easily but I could

