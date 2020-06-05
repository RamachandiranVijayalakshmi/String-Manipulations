#Palindrome
def n(name):
   a=name.lower()
   if a==a[::-1]:
       print(a,'is palindrome')
   else:
       print(a,'is not palindrome')
d=input('enter your world:')
n(d)
