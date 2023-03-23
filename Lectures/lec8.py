'''
function
lec8
'''

#def cal_plus(input1,input2=0): #the input2=0 makes it to where if you don't put an value for input 2 it will default to 0/(whatever number you put in as defualt)
#    return input1+input2
#    print(input1)
#    print(input2)
#    result=input1+input2
#    
#    return result #will print the reuslt of the function meaning if you have 1+2 it will print 3
#
#print(cal_plus(1,3))
#print(cal_plus(2,7))
#
#print(cal_plus(input2=1,input1=3))
#print(cal_plus(2))

#def cal_abs(a):
#    
#    if type(a)is str:
#        return ('wrong datatype')
#    
#    elif a>0:
#        return a
#    else:
#        return-a
#print(cal_abs(468))

#Ex2 Sigma and Pi
def cal_sigma(m,n):
    result=0
    for i in range(1,6):
        result=result+i
        #n+(n+1)+(n+2)..+m
        
    return(result)

print(cal_sigma(10,3))


def cal_pi(m,n):
    result=1
    for i in range(n,m+1):
        result=result*i
        
    return(result)

print(cal_pi(10,3))
#-------------------------------------#

#Ex3
def cal_f(m):
    if m==0:
        return 1
    else:
        return m*cal_f(m-1)

#print(cal_f(5))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)

print(cal_p(5,3))

import lec9
print(my_highlander.report())