print('Hello World')
print('\n 4')
#======================================================================  garbage collection  ============================================================================================================
a='Rohan'
a=200           # GArbage collection deleted above value of a
print(a)
print('\n Direct multi assignment 16')
#====================================================================  Comments ============================================================================================================
"""
 Pascal= 1st letter of each word capital
Snake= each word separated by underscore
Camel= 1st letter of each word capital except 1st letter 
"""
#======================================================================  Variables  =================================================================================================================

a, b,c=10, 20, 30
print(a)
print(b)
print(c)

print('\nConcatenation types 23')
#------------------------------------------------------------------------
a='Rohan'
b='Chaulagain'
print('Rohan','Chaulagain')
print(a+b)
print(a, b)

print('\nSame assignment 31')
#------------------------------------------------------------------------
a=b=c=20
print(a, b, c)
print('\nUnpacking: 36')

"""------------------------------------------------------------ Unpack """
fruits=['apple','orange','avocado']
a, b,c= fruits
print('a='+a, 'b='+b, 'c='+c)

print('\nGlobal variable:  41')
"""------------------------------------------------------------ Variable/ namespace """
a='Chaulagain'        # Global Variable

def my_func():
    return('Rohan '+a)

print(my_func())
print('\n Local Variable:  50')
#-----------------------------
a='Rai'        # Local Variable

def my_func():
    a='Chaulagain'        # Local Variable
    return('Inside: Rohan '+a)

print(my_func())
print('Outside: Rohan '+a)

print('\n Global keyword:  61')
#-----------------------------
a='Rai'        # Global Variable
def my_func():
    global a
    a='Chaulagain'        # Explicit Global Variable
    return('Inside: Rohan '+a)

print(my_func())
print('Outside: Rohan '+a)
#=================================================================================================================================================================================================
""" 
    text type: str
    numeric type: int, float, complex
    sequence type: list, tuple, range
    mapping type: dict
    set type: set, frozenset
    boolean  type: bool
    binary type: bytes, bytearray, memoryview
    Nonetype: None

    Mutable:

    (b)ytearray
    (d)ict
    (s)et
    (l)ist

    Immutable:
    
    string
    int 
    float
    complex
    tuple
    range
    frozenset
    bool
    bytes
    memoryview
    None

    to check the type, use print(type('variable name'))
 """


"""                    Datatype examples
    a='Rohan' --------------------------------str
    a=30       --------------------------------int
    a=30.5        --------------------------------float
    a=1j/ 1J/ 2+3(j/J)     --------------------------------complex
    a=['apple','orange', 'cherry']    -------------------------list
    a=('apple','orange', 'cherry)    -------------------------tuple
    a=range(10)     ------------------------------------------range
    a={'name':'John', 'age':35}   ---------------------------- dict
    a={'apple','orange', 'cherry}    -------------------------set
    a=frozenset({'apple','orange', 'cherry})    -------------------------set
    a=True/ False       --------------------------------------------------Bool
    a=b'Rohan' --------------------------------------------------------------bytes
    a=bytearray(5) ----------------------------------------------------------bytearray
    a=None     ----------------------------------------------------------Nonetype

    a=memoryview(bytes(5))
"""

""" 
    ways to explicitly declare:
    a=list(('APPLE', 'ORANGE', 'AVOCADO'))
    a=tuple(('APPLE', 'ORANGE', 'AVOCADO'))
    a=range(5)  gives range(0, 5) output
    a=dict(name='Rohan', age=20)
    a=set(('APPLE', 'ORANGE', 'AVOCADO'))
    a=frozenset(('APPLE', 'ORANGE', 'AVOCADO'))
    a=bool(5)       vitrw 0 rakhyo vane matrw false else true
    x=bytes(5)
    x=bytes(5)
    x=memoryview(bytes(5))


 """
