def Factorial(n):
    'Calculates n!'
    if (n == 0 or n == 1):
        return (1)
    else:
        return (n*Factorial(n-1))
def Permutation(n,k):
    'Calculates n! / (n-k)!'
    return int((Factorial(n) / Factorial(n-k)))
def Combination(n,k):
    'Calculates n! / ((n-k)! * k!)'
    return int((Factorial(n) / (Factorial(n-k) * Factorial(k))))
def Repeated_Permutation(arr1):
    'For example, MEHMET contains two Ms, two Es, one H, and one T. RP can be calculated as 6! / (2!*2!*1!*1!)'
    nf = Factorial(len(arr1))
    setarr1 = set(arr1)
    for i in setarr1:
        nf = nf / Factorial(arr1.count(i))
    return (int(nf))
def At_Least_to_Split(n,k):
    'When to use while sharing identical objects'
    return int((Factorial(n-1) / Factorial(k-1) * Factorial(n-k)))
def Different_Ways_to_Split(n,k):
    return int((Factorial(n+k-1) / Factorial(k-1) * Factorial(n)))
def Relation_Numbers(n,k):
    'b^a'
    return int((k**n))
def Conditional_Probability(a,b):
    'P(B/A) = P(AnB) / P(A)'
    return int((a*b / a))
def Binomial_Coefficients_Sum(a,b,n): 
    return int(((a + b)**n))
def Binomial_Expansion(a,b,n):
    for i in range (0,n+1):
        print(str(int(Combination(n,i))) + "x" + "^" + str(n-i) + "y" + "^" + str(i), end= " + ")


        
    
    
    
    
