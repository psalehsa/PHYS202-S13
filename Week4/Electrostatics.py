def pointPotential(x,y,q,posx,posy):
    k=8987551787
    Vxy= (k*q)/((((x-posx)**(2.))+((y-posy)**(2.)))**(1/2.))
    return Vxy

def dipolePotential(x,y,q,d):
    k=8987551787
    Vxy=pointPotential(x,y,q,-d,0.)-pointPotential(x,y,q,d,0.)
    return Vxy
def pointField(x,y,q,Xq,Yq):
    k=8987551787
    Ex_xy= (k*q)(x-Xq)/((((x-Xq)**(2.))+((y-Yd)**(2.)))**(1/2.))
    Ey_xy=(k*q)(y-Yq)/((((x-Xq)**(2.))+((y-Yd)**(2.)))**(1/2.))
    return Ex_xy,Ey_xy
