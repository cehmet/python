def kes(a,b):
    liste=[]
    bulundu=False
    if a<b:
        while not bulundu:
            oran=b/a
            c=oran+1
            liste.append(c)
            
            if  a==1 or (b*c)%(a*c-b)==0:
                liste.append((b*c)/(a*c-b))
                print "cik artik liste elemanlari",liste
                bulundu=True
            else :
                a=a*c-b
                b=b*c
                print "yeni a ve b degerleri ",a,b
        #return liste
def katimi(a,b):
    if a==0:
        return True
    elif a<0:
        return False
    else:
        return katimi(a-b,b)



#def obeb_bul(a,b):
 #   if b == 0:
#        return a
#    elif a < b:
#        return obeb_bul(b,a)
#    else:
 #       return obeb_bul(a-b,b)

            
            
            
