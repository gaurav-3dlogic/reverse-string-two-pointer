def reverse(a):
    b = list(a)
    s = 0
    e = len(a) - 1
    while(s < e):
        b[s] , b[e] = b[e], b[s]
        s += 1
        e -= 1
        z = ""
        return(z.join(b))
    
    
    
    
a = "abc"
print(reverse(a))



