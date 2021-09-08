Name=input("enter the name ")
Mark1=int(input("enter the mark in Tamil "))
Mark2=int(input("enter the mark in English "))
Mark3=int(input("enter the mark in Maths "))
Mark4=int(input("enter the mark in Science "))
Mark5=int(input("enter the mark in Soical "))
percentage=((Mark1+Mark2+Mark3+Mark4+Mark5)/5)
print("Student mark detail")
print("Student Name",Name)
print("Tamil",Mark1)
if(Mark1>=35):
	print("pass")
else:
		print("fail")
print("English",Mark2)
if(Mark2>=35):
	print(" pass ")
else:
		print(" fail ")
print("Maths",Mark3)
if(Mark3>=35):
	print(" pass ")
else:
		print(" fail ")
print("Science",Mark4)
if(Mark4>=35):
	print(" pass ")
else:
		print(" fail ")
print("social",Mark5)
if(Mark5>=35):
	print(" pass ")
else:
		print(" fail ")
print("Total percentage",percentage)


 