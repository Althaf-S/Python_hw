def evaluation(expression):
   stack = []
   valid = "123456789+-*/"
   for i in expression:
     if i not in valid:
       return False
     elif i in ["+","-","*","/"] and len(stack) < 2:
       return False
     elif i in ["+","-","*","/"]:
       operand1 = stack.pop()
       operand2 = stack.pop()
       if i == "+":
         stack.append(operand2 + operand1)
       elif i == "-":
         stack.append(operand2 - operand1)
       elif i == "*":
         stack.append(operand2 * operand1)
       elif i == "/":
         stack.append(operand2 // operand1)
       elif i == "%":
         stack.append(operand2 % operand1)
     else:
        stack.append(int(i))
   
   return stack.pop()

def main():
  evaluation(expressions)
  
  
if __name__ == "__main__":
   main()
