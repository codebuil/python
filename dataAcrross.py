import matplotlib.pyplot as p, numpy,sklearn
a=[]
b=[]
c=0
bb=range(10)
print ("\033c\033[42;30m wait...\n")

for n in bb:
	a=a+[[2,n]]
	c=n*2
	b=b+[c]
	
for n in bb:
	print (a[n])
	print (b[n])
