def finiteDifference(x,y):
	dy=diff(y)
	dx=diff(x)
	dydx=zeros(y.shape,float)
	dydx[1:-1]=(y[2:]-y[:-2])/(x[2:]-x[:-2])
	dydx[0]=(y[1]-y[0])/(x[1]-x[0])
	dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
	return dydx
def fourPtFiniteDiff(x,y):
	dydx=zeros(y.shape,float)
	dydx[2:-2]=(y[3:]-y[:-3])/(x[3:]-x[:-3])
	dydx[0]=(y[1]-y[0])/(x[1]-x[0])
	dydx[-1]=(y[-1]-y[-2])/(x[-1]-x[-2])
	dydx[-2]=(y[-2]-y[-3])/(x[-2]-x[-3])
	dydx[1]=(y[2]-y[1])/(x[2]-x[1])
	return dydx
