import matplotlib.pyplot as p, numpy,sklearn
a=[]
b=[]
c=0
f=[4]
bb=range(10)
print ("\033c\033[42;30m wait...\n")

for n in bb:
	a=a+[[1,n]]
	c=n*1
	b=b+[c]
	a=a+[[2,n]]
	c=n*2
	b=b+[c]
	a=a+[[3,n]]
	c=n*3
	b=b+[c]
	a=a+[[4,n]]
	c=n*4
	b=b+[c]
	
for n in range(len(b)):
	c=a[n][0]
	if c==4:
		print (a[n])
		print (b[n])
