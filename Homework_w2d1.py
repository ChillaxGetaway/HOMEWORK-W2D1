#QUESTION 1
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... Loop until the user chooses not to perform any more calculations

a=input("GIMME YO FIRST NUMBER...\n")
d="Your result is  "
o="y"
i=0
while o=="y":
    c=input("What operation are we doing ?  '+','-','*' or '/' \n")
    b=input("GIMME YO SECOND DIGIT...\n")
    print("\n\n")
    if c=="+":
        i = int(a)+int(b)
        print(d,i)
    elif c=="-":
        i = int(a)-int(b)
        print(d,i)
    elif c=="*":
        i = int(a)*int(b)
        print(d,i)
    elif c=="/":
        i = int(a)//int(b)
        ii= int(a)%int(b)
        print(d, i," and your remainder is " , ii)
    print("\n\n")
    a=i
    print("Do you want to keep going?")
    print("Press Y for yes, or N for no")
    o=input("Y/N...\n")
    print("Your curent digit is ", a)
    print("\n\n")


# QUESTION 2
#Create a pyramid of X's for n number of levels.

a=input("How tall do you want your pyrimid? ")
i=0
c=0

for b in range(1, int(a)+1): 
    for c in range(b): 
         print("X", end=' ') 
    print("")
