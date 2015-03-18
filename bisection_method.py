import random
import math #so the user can specify functions like math.sin(x) or math.sqrt(x)
cont = 'Y'
max_iter = 1e5 #limits the number of tries for finding starting values in case function has no real roots
while cont == 'Y':
    #user inputs function
    try:
        f = eval('lambda x : ' + input('f(x) = ').replace('^','**')) 
        f(0)
    except:
        print('Invalid function: Please try again.')
        continue
    
    #generates initial values (can get stuck if the function has many tpts)
    x_0 = x_1 = 0
    i = 0
    while (f(x_0) > 0 or f(x_1) < 0) and (i < max_iter):   
        num = random.random() * 100 # using random nums can help escape local minima; not ideal
        if f(x_0) > 0 : #*
            if f(x_0) > f(x_0 - num):
                x_0 -= num
            else:
                x_0 += num
        if f(x_1) < 0: #* cheaper than using separate while loops
            if f(x_1) < f(x_1 - num):
                x_1 -= num
            else:
                x_1 += num
        i += 1
        
    if i == max_iter: #loop terminated, couldn't cross x-axis
        print('Either your function has no real roots or they\'re really far away. Try another one!')
        continue
    
    #bisect, iterate
    w = (x_0+x_1)/2
    while abs(f(w)) > 1e-10 :
        
        if f(w) > 0 :
            x_1 = w
        else:
            x_0 = w
        w = (x_0+x_1)/2
        
    print('The graph cuts the x-axis near {0:0.5f}'.format(w))
    cont = (input('Try a new function? (Y/N) ').upper())[0]
print('*'*6)