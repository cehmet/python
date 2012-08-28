def regularfalsi(eps,xa,xu):
   
    while not(f(xa)*f(xu))<0:
        xa=input("degerlerin carpimi 0 dan kucuk olmali tekrar float bir deger giriniz:   ")
        xu=input("degerlerin carpimi 0 dan kucuk olmali tekrar deger giriniz:   ")
    adim=0
    while not (abs(xa-xu)<eps):
        fxa=float(f(xa))
        fxu=float(f(xu))
        xy=((fxa*xu)-(fxu*xa))/(fxa-fxu)
        print "xy=",xy
        if (f(xa)*f(xy))<0:
            xu=xy
            print "xu=",xu,"  atamasi \n",adim+1,"nci. adim"
        else:
            xa=xy
            print "xa=",xa
            print adim,"nci. adim \n"
        adim=adim+1
    
    print "program",adim,"adimda sonlanir ben regular gencler"
    return xy

import math
def f(x):
    return (x*x*x)+(0.2923*x*x)-(0.3902*x)-3.0
        
