def evaluation(expression):
   stack = []
   for i in expression:
     if i in ["+"]:
       operand1 = stack.pop()
       operand2 = stack.pop()
       if i == "+":
         stack.append(operand1 + operand2)
     else:
        stack.append(int(i))
   
   return stack.pop()
  
