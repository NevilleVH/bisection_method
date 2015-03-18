import random
import math #so the user can specify functions like math.sin(x) or math.sqrt(x)

def has_roots(s): #descarte's rule of signs: won't work for transcendentals
    def check_signs(s, sign):
        count = 0
        if sign == '+':
            sign = '-'
        else:
            sign = '+'
        pos = s.find(sign)
        if pos > -1:
            count += 1 + check_signs(s[pos:],sign)
        return count
    
    result = [0,0]
    
    s = s.replace(' ','') 
    if s.find('-') > s.find('x') or s.find('-') == -1: 
        s = '+' + s    
        result[0] = check_signs(s, '+')
    else:
        result[0] = check_signs(s,'-')
    
    func = (s.replace('+','&')).replace('-','&') + '&'
    
    new = ''
    while func != '&':
        pos = func.find('&',1)
        substr = s[: pos]
        if substr.find('x') != -1:
            substr = substr[:substr.find('x')] + '(x)' + substr[1+substr.find('x'):]
        func = func[pos:]
        s = s[pos:]
        f1 = lambda x : eval (substr)
        f2 = lambda x : eval (substr.replace('x','-x'))
        if f1(1) != f2(1):
            substr = substr.replace('x','-x')
        new += substr
    func = new
    while  ((new.find('+') > new.find('-') and new.find('+') < new.find('x')) or  (new.find('-') > new.find('+') and new.find('-') < new.find('x'))) and  (func.find('-') != -1 and func.find('+') != -1):
        if (new.find('-') > new.find('+') and new.find('-') < new.find('x')):
            new = new[new.find('-'):]
            func = func[1+new.find('-'):]
        else: #(new.find('+') > new.find('-') and new.find('+') < new.find('x')) and new.find('-') > -1 and new.find('+') > -1:
            new =  new[new.find('+'):]
            func = func[1+new.find('+'):]            
    if new.find('-') > new.find('x') or new.find('-') == -1: 
        new = '+' + new    
        result[1] = check_signs(new, '+')
    else:
        result[1] = check_signs(new,'-')
    return result

def get_init_values():
    max_iter = 1e5 
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
    if i == max_iter:
        x_0 = x_1 = None
    return x_0, x_1
    
msg = 'Enter your function. Remember to specify any modules as needed (e.g. math.pi).'
print('*'*len(msg),msg, '*'*len(msg), sep = '\n')
cont = 'Y'
while cont == 'Y':
    #user inputs function, try fix formatting
    s = input('f(x) = ').replace('^','**')
    for i in range(len(s)-2,-1,-1):
        if s[i].isdigit() and s[i+1] == 'x':
            s = s[:i+1] + '*' + s[i+1:]
    try:
        f = eval('lambda x : ' + s) 
        f(0)
    except:
        print('Invalid function: Please try again.')
        continue
    
    #if the function is a polynomial, determine whether it has real roots <- only correct if tpt on same side as real roots (picks up complex roots)
    
    roots = has_roots(s)
    if roots[0] or roots[1]:
        print('Upper bounds for real roots: {} positive and {} negative'.format(roots[0], roots[1]))
    elif s.find('math.') == -1 and f(0) != 0:
            print('Your function has no real roots! Try another one.')
            continue    
    
    #check if a function without real roots slipped through; generate initial values
    x_0,x_1 = get_init_values()
    
    if x_0 == x_1 == None: #loop terminated, couldn't cross x-axis
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
    cont = (input('\nTry a new function? (Y/N) ').upper())[0]
print('*'*6)