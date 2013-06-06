function [ output_args ] = untitled5( input_args )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here


end
def WeightedLinearLeastSquaresFit(x,y, w): 
   
    sw = sum(w)
    wx = sum(w*x)
    wy = sum(w*y)
    wx2 = sum(w*(x**2))
    wxy = sum(w*x*y)

    if w[i] == 1:
        x_a = average(x)
        y_a = average(y)
        x2 = average(x**2)
        xy = average(x*y)
        m = (xy - (x_a*y_a))/(x2 - x_a**2)
        b = (x2*y_a - x_a*xy)/(x2 - x_a**2)
        s2 = average( (y-(m*x+b))**2 )
        slerr = ( (1.0/(len(x)-2)) * (s2/((x2 - x_a**2))) )**(0.5)
        interr = ( (1.0/(len(x)-2)) * ((s2*x2)/((x2 - x_a**2))) )**(0.5)
    else:
        m = (sw*wxy - wx*wy)/(sw*wx2 - wx*wx)
        b = (wx2*wy - wx*wxy)/(sw*wx2 - wx**2)
        slerr = ( sw/(sw*wx2-wx**2) )**(0.5)
        interr = ( wx2/(sw*wx2-wx**2) )**(0.5)
    return m, b, slerr, interr    