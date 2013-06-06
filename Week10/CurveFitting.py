def LinearLeastSquaresFit(x,y):
    """Take in arrays representint (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slop and intercept
    parameters of the best fit line with their uncertainties."""
    x_a = average(x)
    y_a = average(y)
    x2 = average(x**2)
    xy = average(x*y)
    m = (xy - (x_a*y_a))/(x2 - x_a**2)
    b = (x2*y_a - x_a*xy)/(x2 - x_a**2)
    s2 = average( (y-(m*x+b))**2 )
    slerr = ( (1.0/(len(x)-2)) * (s2/((x2 - x_a**2))) )**(0.5)
    interr = ( (1.0/(len(x)-2)) * ((s2*x2)/((x2 - x_a**2))) )**(0.5)
    return m, b, slerr, interr

def WeightedLinearLeastSquaresFit(x,y,w):
	"""Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w. Perform a weighted linear least squares regression. Return the resulting slope and intercept parameters of the best fit line with their uncertainties.
	If the weights are all equal to one, the uncertainties on the parameters are calculated using the non-weight least squares equations."""
	import math
	import numpy as np
	for i in range(len(x)-1): 
           sw = sum(w)
           wx = sum(w*x)
           wy = sum(w*y)
           wx2 = sum(w*(x**2))
           wxy = sum(w*x*y)

           if w[i] == 1:
              m,b, slerr, interr = LinearLeastSquaresFit(x,y)
           else:
              m = (sw*wxy - wx*wy)/(sw*wx2 - wx*wx)
              b = (wx2*wy - wx*wxy)/(sw*wx2 - wx**2)
              slerr = ( sw/(sw*wx2-wx**2) )**(0.5)
              interr = ( wx2/(sw*wx2-wx**2) )**(0.5)
        return m, b, slerr, interr
