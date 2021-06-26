

for i in range(5):
    for j in range( i):
        print("*")
    print("\n")

name=['mayank','anuj','pranjal','chetan','yogesh']
for i in name:
    print(i)    

number=int(input("Enter a number"))
for i in range(1,10):
    print(f" { number} x {i} = {number*1}")




l1 = ["mayank","Shalini","Shivani","Anmol"]

for name in l1:
    if name.startswith("S"):
        print(f"Hello {name} ")

# WAP TO CHECK WHETHER A GIVEN NO. IS PRIME OR NOT

num = int(input("Enter the number:"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime = False
        break

if prime:
    print(f"{num}  is Prime")
else:
    print(f"{num}  is not prime")
########## program to find the factorail of no.###########
