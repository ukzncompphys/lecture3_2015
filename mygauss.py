import numpy
import matplotlib.pyplot as plt
print __name__
def gauss(x,x0=0.0,sig=1.0):
    y=numpy.exp(-0.5/(sig**2)*(x-x0)**2)
    return y
if __name__=="__main__":
    x=numpy.arange(-10,10,0.1)
    y=gauss(x)
    plt.plot(x,y)
    plt.show()



