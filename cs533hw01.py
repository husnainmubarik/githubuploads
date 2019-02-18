#r=[2,3,5,7]
#for s in r:
# print s
#print ("how you doin!")

     
#for i in range(1,10):
#   print i

from math import sqrt
print("sppedup for n=4")
n=4.0
for r in range(1,5):  
 speedup=(10.0/(100*max(1.0,sqrt(r))))+(50.0/(100*(n-r+1)))+(40.0/(100*(min(n-r+1,4))))
 print ("%f, " % (1/(speedup)),file=open("what.csv" , "a"))

print("sppedup for n=16")
n=16.0
for r in range(1,17):
 speedup=(10.0/(100*max(1.0,sqrt(r))))+(50.0/(100*(n-r+1)))+(40.0/(100*(min(n-r+1,4))))
 print ("%f, " % (1/(speedup)),file=open("what.csv" , "a"))

n=64.0
print("sppedup for n=64")
for r in range(1,65):
 speedup=(10.0/(100*max(1.0,sqrt(r))))+(50.0/(100*(n-r+1)))+(40.0/(100*(min(n-r+1,4))))
 print ("%f, " % (1/(speedup)),file=open("what.csv" , "a"))




#for r in range(1,5):
# print max(n,r)
# print min(n,r)

