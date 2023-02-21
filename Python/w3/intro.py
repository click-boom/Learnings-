print('Hello World')
#======================================================================  garbage collection  ====================================================================
def garb():
    print('\n 3')
    a=200           # GArbage collection deleted above value of a
    print(a)

#====================================================================  Comments =================================================================================
"""
 Pascal= 1st letter of each word capital
Snake= each word separated by underscore
Camel= 1st letter of each word capital except 1st letter 
"""

# Above is multiline and this is single line comment, this can also be used as multi line
#======================================================================  Variables  ==================================================================
def assign():
    print('\n Direct multi assignment 17')
    a, b,c=10, 20, 30
    print(a)
    print(b)
    print(c)

#------------------------------------------------------------------------
def conc():   
    print('\nConcatenation types 25')
    a='Rohan'
    b='Chaulagain'
    print('Rohan','Chaulagain')
    print(a+b)
    print(a, b)

#------------------------------------------------------------------------
def multi():
    print('\nSame assignment 34')
    a=b=c=20
    print(a, b, c)

"""------------------------------------------------------------ Unpack """
def unpack():
    print('\nUnpacking: 41')
    fruits=['apple','orange','avocado']
    a, b,c= fruits
    print('a='+a, 'b='+b, 'c='+c)

"""------------------------------------------------------------ Variable/ namespace """
def fx():
    print('\nGlobal variable:  47')
    print('\n Local Variable:  57')
    print('\n Global keyword:  69')
    a='Chaulagain'        # Global Variable

    def my_func():
        return('Rohan '+a)

    print(my_func())
    #-----------------------------
    a='Rai'        # Local Variable

    def my_func():
        a='Chaulagain'        # Local Variable
        return('Inside: Rohan '+a)

    print(my_func())
    print('Outside: Rohan '+a)

    #-----------------------------
    a='Rai'        # Global Variable
    def my_func():
        global a
        a='Chaulagain'        # Explicit Global Variable
        return('Inside: Rohan '+a)

    print(my_func())
    print('Outside: Rohan '+a)

#========================================================================  Datatypes in brief =================================================
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
    x=bytearray(5)
    x=memoryview(bytes(5))

 """
#========================================================================  Numeric literals ============================================
def sc():
    print('\n Scientific numbers:  147')
    a= 23e3
    print(a)
    a=12E4
    print(a)
    a=-97.7e100
    print(a)
    a=10_00_000 # _ works like comma for clear visual bt wont be printed
    print(a)

""" e/E= +ve power 
    complex is the only type that cant be converted to other types
"""
#========================================================================  Ways to print =============================================
def w_t_p():
    print('\n Ways to print:  162')
    a='A paragraph is defined as “a group of sentences or a single sentence that forms a unit”\
    (Lunsford and Connors 116). Length and appearance do not determine whether a section in \
    a paper is a paragraph. For instance, in some styles of writing, particularly journalistic\
    styles, a paragraph can be just one sentence long.'

    print(a) # output will be single lined string
    print('\n')

    a='''A paragraph is defined as “a group of sentences or a single sentence that forms a unit”
        (Lunsford and Connors 116). Length and appearance do not determine whether a section in 
        a paper is a paragraph. For instance, in some styles of writing, particularly journalistic
        styles, a paragraph can be just one sentence long.'''

    print(a) # output will be as it is given in input

#========================================================================  String literals =============================================
def string():
    print('\nString''    180')
    a='Rohan'
    print(a*3) # PRINTS A 3x without spaces
    # cheking if a word is available or not in sentence using membership opertor: in / not in 

    print('\nSlicing:' '    186')
    print(a[1:4])
    print(a[:4])
    print(a[2:])
    print(a[-5:-3])
    print(a[-3:])
    print(a[:-3])   # 0 dekhi -3 samma

def str_op():
    a='Rohan Chaulagain'
    print('Calitalize:',a.capitalize(), '    196')  #1st letter of 1st word is made capital ani if 1st baek aru word ko ni leter capital xa vane ni sano banaidinx 
    print('Casefold:',a.casefold(), '    197')  #sablai sano banaidinx 
    
    """ Puts given strings in center by putting spaces on fromt and back, priority front fills while dividing the spaces/characters.
    If possible divides the spaces equally front and back, else back will have more sapces.
    if you want to fill something else instead of space, add extra string parameter as shown below """
    print('\nCenter:',a.center(30, '0'), '    203')  
    print('Center:',a.center(20), '    204')  
    print('\n')
    """ optional parameters, start and end index. Default start=0 and end=last. So, if only 1 optional parameter put, then its considered start index"""
    b = "I love apples, apple are my favorite fruit"
    print(b.count('apple'),'          207')
    print(b.count('apple', 10),'          208')
    print(b.count('apple', 10, 14),'          209')
    
    """ optional parameters, same as count------205"""
    print('\n',b.endswith(',', 1,14 ),'       212')
    print(b.endswith('t' ),'       213')
    print(b.endswith('t', 10 ),'       214')
    
    """ Default size 8 ho but can be changed if added int parameter """
    c='r\to\th\ta\tn'
    print('\n',c.expandtabs(),'       218')
    print(c.expandtabs(2),'       219')

# garb()
# assign()
# conc() 
# multi()
# unpack()
# fx()
# sc()
# w_t_p()
# string()
str_op()