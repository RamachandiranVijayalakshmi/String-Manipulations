#Palindrome
name=input('enter your world:')
a=name.lower()
if a==a[::-1]:
    print(a,'is palindrome')
else:
    print(a,'is not palindrome')
