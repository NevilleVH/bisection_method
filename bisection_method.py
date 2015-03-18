import random

num = 0
cont = 'Y'
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
    while f(x_0) > 0 or f(x_1) < 0:   
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