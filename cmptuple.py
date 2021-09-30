Tuple1 + Tuple2 = (123 , 'XYZ' ),(456 , 'ABC')
print cmp(Tuple1 , Tuple2)
print cmp(Tuple2 , Tuple1)
Tuple3 = Tuple2 + (789,);
print cmp(Tuple2 , Tuple3)