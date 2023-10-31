#first python program
def fizzbizz(n):
  for i in range (1,n+1):
    if i % 15 == 0:
      print("fizzbizz")
    elif i % 5 == 0:
      print("bizz")
    elif i % 3 == 0 :
      print("fizz")
    else :
      print(i)

#program to find whether given string is palindrome or not
def palindrome(s):
  return s == s[::-1]

#program to find whether provided string is panagaram
def panagram(s):
  c = 0
  s = s.lower()
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  for i in alphabets: 
    if i in s:
      c += 1
  if c == len(alphabets):
    return True
  return False
    

#program to print the key value dictionary
def freq(s):
 dicti = {} 
 for i in s:
   if i in dicti:
     dicti[i] += 1
   else:
     dicti[i] = 1
 return dicti


if __name__ == "__main__":
   fizzbizz(n = int(input("Enter any number to do operations : ")))
   print(palindrome(s = input("Enter your string to check if it is palindrome: "))) 
   print(panagram(s = input("Enter your string here to check if it is panagram: ")))
   print(freq(s = input("Enter your string : ")))




