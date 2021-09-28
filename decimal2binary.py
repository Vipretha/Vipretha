decimalnumber=int(input("enter a number"))
binary=0 
mulvalue=1
while decimalnumber>0:
	rem=decimalnumber % 2
	mulvalue=mulvalue * 10
	binary=binary+(rem*mulvalue)
	decimalnumber=int(decimalnumber / 2)
print("binarynumber = ",binary)







