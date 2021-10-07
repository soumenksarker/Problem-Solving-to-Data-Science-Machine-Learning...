def table(expr):
    """ print truth table for logical expression

    >>> table('and(A,or(A,B))')
    A     B     and(A,or(A,B))
    True  True  True
    True  False True
    False True  False
    False False False
    """
    # uppercase functions to avoid name clashes with
    #   python reserved words
    def AND(a,b):
        return a and b
    def NAND(a,b):
        return not (a and b)
    def OR(a,b):
        return a or b
    def NOR(a,b):
        return not (a or b)
    def XOR(a,b):
        return a ^ b
    def EQU(a,b):
        return not (a^b)
    def IMP(a,b):
        return not a or b
    # print a nice header
    format = "%-5s %-5s --%5s"
    print(format%('A','B',expr))
    # convert the expression to uppercase and
    # compile it for later 'eval' call
    expr = compile(expr.upper(),'<expression>','eval')

    for A in (True, False):
        for B in (True, False):
            print(format%(A, B, eval(expr, locals())))
    
