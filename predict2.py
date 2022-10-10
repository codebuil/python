import matplotlib.pyplot as p, numpy
from sklearn import linear_model
a=[]
b=[]
c=0
bb=range(10)
print ("\033c\033[42;30m wait...\n")

for n in bb:
	a=a+[[n,2]]
	c=n*2-30
	b=b+[c]
	
print (a)
print (b)

regr= linear_model.LinearRegression()
regr.fit(a,b)
predic=regr.predict([[12,2]])
print (predic)
