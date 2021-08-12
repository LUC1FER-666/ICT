num=int(input("ENTER NUMBER:"))
temp=num
rev=0
while(num!=0):
      n=num%10
      rev=rev*10+n
      num=num//10
if(rev==temp):
      print("PALINDROME NUMBER")
else:
      print("NOT A PALINDROME NUMBER")
