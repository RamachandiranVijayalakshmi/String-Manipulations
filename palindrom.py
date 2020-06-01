#student mark list
name=input('enter your world:')
a=name.lower()
if a==a[::-1]:
    print(a,'is palindrom')
else:
    print(a,'is not palindrom')
