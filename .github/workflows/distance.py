#Batch_02
#two_point_Distance
X1=int(input("please input point x1="))
Y1=int(input("please input point y1="))
A="point A"+"("+str(X1)+","+str(Y1)+")"
print(A)

X2=int(input("please input point x2="))
Y2=int(input("please input point y2="))
B="point B"+"("+str(X2)+","+str(Y2)+")"
print(B)

Distce=((((X2-X1))**2)+(((Y2-Y1))**2))**(1/2)
print (" Distance of two points "+A+" "+"&"+" "+B+" "+"is="+str(Distce))