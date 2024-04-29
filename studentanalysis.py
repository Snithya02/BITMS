sub1=float(input())
sub2=float(input())
sub3=float(input())
sub4=float(input())
sub5=float(input())
percentage=((sub1+sub2+sub3+sub4+sub5)/500)*100
print(percentage)
if percentage>=75:
    print("grade A")
elif percentage>=60 and percentage<=74:
    print("grade B")
elif percentage>=35 and percentage<=59:
    print("grade c")
else:
    print("fail")

