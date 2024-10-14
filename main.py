a=input()  #экстриситет

print(a[0])
print(a[-1])
print(len(a))
dlina= len(a)
polovina = len(a)//2
d= (dlina-polovina)
if d%2==0:print(a[polovina+1:])
else: print(a[polovina:])
print(a[::-1])
print(a[1::2])