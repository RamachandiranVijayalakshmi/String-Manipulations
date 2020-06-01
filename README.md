# String-Manipulations
Sample code to check whether a word is Palindrome or not
From user we getting Input
Both integer value & string value can get as Input.
In if condition we getting string value equals to reverse a string.
If the condition is true it is a palindrome.
In else, its is not a palindrome.



Sample code to check whether a word is Palindrome or not:


name=input('enter your world:')
a=name.lower()
if a==a[::-1]:
    print(a,'is palindrom')
else:
    print(a,'is not palindrom')
