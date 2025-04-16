import sys
fileName = ""
lines = []
try:
   fileName = sys.argv[1]
   file = open(fileName)
   lines = file.read().split("\n")
   file.close()
except Exception as e:
   print(f"Error while opening file:\n{e}")
   sys.exit(0)

stack = []
cursor = 0 #what line the program is reading
label_tracker = {}
variables = {}
outtroMessage = "\n\nThanks for watching!\nRemember to [👍like] and 🆂 🆄 🅱 🆂 🅲 🆁 🅸 🅱 🅴"

def err(str):
   print("\n💀 " + str + f" at line {cursor+1} 💀")
   sys.exit(0)

# initialize labels and stuff
while cursor < len(lines):
   parts = lines[cursor].split(" ")
   instr = parts[0]

   if instr.startswith("!"):
       a = parts[0].removeprefix("!")
       label_tracker[a] = cursor
   cursor += 1
print(f"Hey guys, welcome back to Chandler's Programming House. Today, we'll be checking out this awesome viewer submitted program to me called {fileName}\nSo let's go ahead and jump into it!\n\n")
cursor = 0
while cursor < len(lines):
    parts = lines[cursor].split(" ")
    instr = parts[0]
    if instr.startswith(''):
        pass
    elif instr == "UNSUBSCRIBE":
       stack = []
    elif instr == "":
       pass
    elif instr.startswith("!"):
       pass
    elif instr == "HELLO_WORLD":
       print("Hello stupid! i mean world")


    elif instr == "UPLOAD_NUM":
        try:
          stack.append(int(parts[1]))
        except:
          err("You forgot to upload a number")
    elif instr == "UPLOAD":
        try:
          stack.append(parts[1])
        except:
          err("You forgot to upload something")
          
    elif instr == "SHOUT_OUT":#print
        try:
          print(lines[cursor].split('>')[1])
        #   stack.append(parts[1])
        except:
          err("Needs something to print >")



    elif instr == "ADD":
        try:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        except:
           err("adding didn't work. use better numbers next time buddy")
    elif instr == "SUBTRACT":
        try:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        except:
           err("subtracting didn't work. use better numbers next time buddy")
    elif instr == "MULTIPLY":
        try:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)
        except:
           err("multiplying didn't work. use better numbers next time buddy")
    elif instr == "DIVIDE":
        try:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b / a)
        except:
           err("dividing didn't work. use better numbers next time buddy")



    elif instr == "PROMPT":
       try:
        if(parts[1] == "string"):
           stack.append(0)
        elif(parts[1] == "number"):
           stack.append(1) #set to number mode
        elif(parts[1] == "char"):
            stack.append(2) #set to char mode
        elif(parts[1] == "stringArray"):
            stack.append(3) #set to char mode
        else:
           err("Specify type of input. can be string, number, char, or stringArray")
       except:
        err("No prompt given")
    # elif instr == "INPUT":
       inputMode = stack.pop()
       #STRING MODE
       if(inputMode == 0):
            try:
                stack.append((input("String: ")))
            except:
                err("Invalid input buddy")
       #NUMBER MODE
       elif(inputMode == 1):
            try:
                stack.append(int(input("Number: ")))
            except:
                err("Invalid input buddy")
       #1 CHAR MODE
       elif(inputMode == 2):
            try:
                stack.append(ord(input("One char: ")[0]))
            except:
                err("Invalid input buddy")
       #char array mode
       elif(inputMode == 3):
            try:
                user_input = list(input("String: "))
                for x in user_input:
                   stack.append(x)
            except:
                err("Invalid input buddy")         
# CONDITIONAL
    elif instr == "IF_GREATER_THAN":
       firstValue = 0
       secondValue = 0
       
       try:
          if variables.get(parts[1]) != None:
             firstValue = variables.get(parts[1])
          else: firstValue = parts[1]
          if variables.get(parts[2]) != None:
             secondValue = variables.get(parts[2])
          else: secondValue = parts[2]
       except:
          err("Error setting up conditional")

       try:
         # print(firstValue > secondValue)
         if(firstValue <= secondValue): 
            cursor += 2
            continue
       except:
          try:
            #  print("Trying again")
             if(int(firstValue) <= int(secondValue)): 
               cursor += 2
               continue
          except:
            err("error comparing values")

    elif instr == "IF_EQUAL_TO":
       firstValue = 0
       secondValue = 0
       
       try:
          if variables.get(parts[1]) != None:
             firstValue = variables.get(parts[1])
          else: firstValue = parts[1]
          if variables.get(parts[2]) != None:
             secondValue = variables.get(parts[2])
          else: secondValue = parts[2]
       except:
          err("Error setting up conditional")

       try:
         if(firstValue != secondValue): 
            cursor += 2
            continue
       except:
          try:
            #  print("Trying again")
             if(int(firstValue) != int(secondValue)): 
               cursor += 2
               continue
          except:
            err("error comparing values")

    elif instr == "JUMP" or instr == "SKIP_TO":
       try:
            a = parts[1]
            cursor = label_tracker[a]
            continue
       except:
            err("Jumping failed") 
       
       #reverse
    elif instr == "REWIND":
       if len(parts) > 1:
          if parts[1] == "COMBO":
             temp = []
             while(len(stack) > 0):
                temp.append(stack.pop())
             stack.append("".join(temp))
          else:  #see if there's a variable name to use
            try:
                temp = list(variables.get(parts[1]))
                temp2 = []
                while(len(temp) > 0):
                   temp2.append(temp.pop())
                stack.append("".join(temp2))
            except:
               err("Variable not found")
       else:
        temp = []
        while(len(stack) > 0):
            temp.append(stack.pop())
        stack = temp
       


    elif instr == "var":
      try:
        a = lines[cursor].split("=")[1]
      #   print(parts[1])
        if a.strip() == "POP":
           variables[parts[1]] = stack.pop()
        else:   
         variables[parts[1]] = a.strip()   
      except:
         err("Variable not declared right")
    elif instr == "int":
      try:
        a = lines[cursor].split("=")[1]
        if a.strip() == "POP":
           variables[parts[1]] = int(stack.pop())
        else:
            variables[parts[1]] = int(a.strip())
      except:
         err("Variable not declared right")

    elif variables.get(instr) != None:
       if parts[1] == "++":
          variables[instr] = variables[instr]+1
       else:
          err("you need to do something with the variable")   

    elif instr == "LIKE":
         if variables.get(parts[1]) != None:
            variables[parts[1]] = variables[parts[1]]+1
    elif instr == "DISLIKE":
         if variables.get(parts[1]) != None:
            variables[parts[1]] = variables[parts[1]]-1

    elif instr == "WHAT?":
       print(stack)
    elif instr == "PRINT":
      #  try:
          if len(parts) == 1:
             err("Missing argument for print")
          elif parts[1] == "POP":
             print(stack.pop())
          elif parts[1] == "PEEK":
             a = stack.pop()
             print(a)
             stack.append(a)
          elif parts[1] == "ALL":
             print(stack)
          elif parts[1] == "VAR":
             try:
                print(variables.get(parts[2]))
             except:
                err("Could not get variable")
          else:
             err("Invalid argument")
      #  except:
      #     err("Printing error")
    elif instr == "OUTTRO":
       print(outtroMessage)
       sys.exit(0)
    else:
       err("stupid. Not even a real function")
    cursor+=1

# print(variables)
print(outtroMessage)