loop=1
l=[]
n=int(input("enter number:"))
for x in range(n):
 try: l.append(int(input("enter elements:")))
 except ValueError:print("enter a number plz...")
 #l.append(int(input("enter elements 2:")))
   
while loop == 1:
   print("1.total")
   print("2.count")
   print("3. max")
   print("4.min")
   print("5.Avg")
   print("6.exit")
   ch=int(input("enter ur choice:"))
   if ch==1:print(sum(l))
   elif ch==2:print(len(l))
   elif ch==3:print(max(l))
   elif ch==4:print(min(l))
   elif ch==5:print(sum(l)/len(l))
   elif ch==6:loop=0

