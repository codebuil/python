import matplotlib.pyplot as p, numpy
print ("\033c\033[42;30m wait...\n")
x=numpy.random.uniform(-25,25.0,100)
y=numpy.random.uniform(-25,25.0,100)
p.scatter(x,y)
p.show()
