class Yigit:
    def __init__(self):
        self.items=[]
    def it(self,item):
        self.items.append(item)
    def cek(self):
        return self.items.pop()
    def bosmu(self):
        return self.items==[]
    def tgoster(self):
        return self.items[len(self.items)-1]
    def boy(self):
        return len(self.items)

   
import string   
def infixtopostfix(infislem):
    prec = {}
    prec["/"] = 3
    prec["*"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opstack = Yigit()
    postfixlist = []
    
    if kontrol(infislem):
        tokenlist =parcala(infislem)
        
    else:
        print "hatali ifade"
        return 1
    
    for token in tokenlist:
       
        if isFloat(token):
            postfixlist.append(token)
            
        elif token == '(':
            opstack.it(token)
            
        elif token == ')':
            toptoken = opstack.cek()
            
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.cek()
        
        else:
            while (not opstack.bosmu()) and \
                  (prec[opstack.tgoster()] >= prec[token]):
                    postfixlist.append(opstack.cek())
            opstack.it(token)
     
    while not opstack.bosmu():
        postfixlist.append(opstack.cek())
    x=string.join(postfixlist)

    return postfixeval(x)
    
       
def postfixeval(postfixexpr):
    operandstack = Yigit()
    tokenlist =postfixexpr.split()
    
    for token in tokenlist:
        if isFloat(token):
            operandstack.it(float(token))
            
        else:
            operand2 = operandstack.cek()
            operand1 = operandstack.cek()
            result = domath(token,operand1,operand2)
            operandstack.it(result)

    return operandstack.cek()

def domath(op,op1,op2):
    if op == "*":
        return op1 * op2
    
    else:
        if op == "/":
            return op1 / op2
        
        else:
            if op == "+":
                return op1 + op2
            
            else:
                return op1 - op2

def parcala(x):
    yeni=""
    news=[]
    i=0
    op="-+*/()"
    
    while i<len(x):

        try:
            if x[i] in "0123456789":
                while x[i] not in op:
                    yeni=yeni+x[i]
                    i=i+1
                news.append(yeni)

            else:
                if x[i] in op:
                    news.append(x[i])  
                    i=i+1
   
        except IndexError:
            news.append(yeni)    
        yeni=""
        
    return news  


def kontrol(x):
    dengeli=True
    sayi="0123456789()"
    op="+-*/"
    k=0
    t=0
    
    for i in range(len(x)):
    
            if x[i]=="(":
                k=k+1
            if x[i]==")":
                t=t+1
         
            if (x[i]=="(" and x[i-1]==")" and i>0)or(x[i]=="(" and x[i-1] in sayi and i>0):
                        dengeli=False
                        break
            elif t!=k:
                dengeli=False
                
            else:
                if not x[0] in sayi:
                    dengeli=False
                      
                else:
                    if x[i] in op and   (x[i-1] in op or x[i-1]=="(")  :
                        
                        dengeli=False
                        break
                    
                        
                    elif x[len(x)-1] in op or x[len(x)-1]=="(":
                        dengeli=False
                        
                    else:
                        dengeli=True
                        
       
                
    return dengeli   

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
