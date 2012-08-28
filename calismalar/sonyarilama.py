import math
import time
def yarilama(e,xa,xu):
    bas=time.clock()
    adim=0
    while not f(xa)*f(xu)<0:
        xa=input("degerlerin carpimi 0 dan kucuk bir daha giriniz.  ")
        xu=input("degerlerin carpimi 0 dan kucuk bir daha giriniz.  ")
    while(abs(xa-xu)>e):
        xy=(xa+xu)/( 2.0)
        print "xy atamasinda"
        print xy
        if f(xa)*f(xy)<0:
             xu=xy
             print "xu atamasinda"
             print xu
        else:
             xa=xy
             print "xa atamasinda"
             print xa
        adim=adim+1
    print "program",adim ,"adimda sonlanir"
    son=time.clock()
    print "program " ,son-bas,"saniye de sonuc uretir"
    return xy

def f(x):
    return (x*x*x)+(0.2923*x*x)-(0.3902*x)-3.0

        
        
        
