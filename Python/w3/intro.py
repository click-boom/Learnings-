print('Hello World')
# ======================================================================  garbage collection  ====================================================================


def garb():
    print('\n 5')
    a = 200           # GArbage collection deleted above value of a
    print(a)


# ====================================================================  Comments =================================================================================
"""
 Pascal= 1st letter of each word capital
Snake= each word separated by underscore
Camel= 1st letter of each word capital except 1st letter 
"""

# Above is multiline and this is single line comment, this can also be used as multi line
# ======================================================================  Variables  ==================================================================


def assign():
    print('\n Direct multi assignment 22')
    a, b, c = 10, 20, 30
    print(a)
    print(b)
    print(c)

# ------------------------------------------------------------------------


def conc():
    print('\nConcatenation types 32')
    a = 'Rohan'
    b = 'Chaulagain'
    print('Rohan', 'Chaulagain')
    print(a+b)
    print(a, b)

# ------------------------------------------------------------------------


def multi():
    print('\nSame assignment 44')
    a = b = c = 20
    print(a, b, c)


"""------------------------------------------------------------ Unpack """


def unpack():
    print('\nUnpacking: 53')
    fruits = ['apple', 'orange', 'avocado']
    a, b, c = fruits
    print('a='+a, 'b='+b, 'c='+c)


"""------------------------------------------------------------ Variable/ namespace """


def fx():
    print('\nGlobal variable:  63')
    print('\n Local Variable:  73')
    print('\n Global keyword:  87')
    a = 'Chaulagain'        # Global Variable

    def my_func():
        return ('Rohan '+a)

    print(my_func())
    # -----------------------------
    a = 'Rai'        # Local Variable

    def my_func():
        a = 'Chaulagain'        # Local Variable
        return ('Inside: Rohan '+a)

    print(my_func())
    print('Outside: Rohan '+a)

    # -----------------------------
    a = 'Rai'        # Global Variable

    def my_func():
        global a
        a = 'Chaulagain'        # Explicit Global Variable
        return ('Inside: Rohan '+a)

    print(my_func())
    print('Outside: Rohan '+a)


# ========================================================================  Datatypes in brief =================================================
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
# ========================================================================  Numeric literals ============================================


def sc():
    print('\n Scientific numbers:  167')
    a = 23e3
    print(a)
    a = 12E4
    print(a)
    a = -97.7e100
    print(a)
    a = 10_00_000  # _ works like comma for clear visual bt wont be printed
    print(a)


""" e/E= +ve power 
    complex is the only type that cant be converted to other types
"""
# ========================================================================  Ways to print =============================================


def w_t_p():
    print('\n Ways to print:  184')
    a = 'A paragraph is defined as “a group of sentences or a single sentence that forms a unit”\
    (Lunsford and Connors 116). Length and appearance do not determine whether a section in \
    a paper is a paragraph. For instance, in some styles of writing, particularly journalistic\
    styles, a paragraph can be just one sentence long.'

    print(a)  # output will be single lined string
    print('\n')

    a = '''A paragraph is defined as “a group of sentences or a single sentence that forms a unit”
        (Lunsford and Connors 116). Length and appearance do not determine whether a section in 
        a paper is a paragraph. For instance, in some styles of writing, particularly journalistic
        styles, a paragraph can be just one sentence long.'''

    print(a)  # output will be as it is given in input

# ========================================================================  String literals =============================================


def string():
    print('\nString''    205')
    a = 'Rohan'
    print(a*3)  # PRINTS A 3x without spaces
    # cheking if a word is available or not in sentence using membership opertor: in / not in

    print('\nSlicing:' '     210')
    print(a[1:4])
    print(a[:4])
    print(a[2:])
    print(a[-5:-3])
    print(a[-3:])
    print(a[:-3])   # 0 dekhi -3 samma


def str_op():
    a = 'Rohan Chaulagain'
    # 1st letter of 1st word is made capital ani if 1st baek aru word ko ni leter capital xa vane ni sano banaidinx
    print('Calitalize:', a.capitalize(), '    222')
    print('Casefold:', a.casefold(), '    223')  # sablai sano banaidinx

    """ Puts given strings in center by putting spaces on fromt and back, priority front fills while dividing the spaces/characters.
    If possible divides the spaces equally front and back, else back will have more sapces.
    if you want to fill something else instead of space, add extra string parameter as shown below """
    print('\nCenter:', a.center(30, '0'), '    228')
    print('Center:', a.center(20), '    229')
    print('\n')
    """ optional parameters, start and end index. Default start=0 and end=last. So, if only 1 optional parameter put, then its considered start index"""
    b = "I love apples, apple are my favorite fruit"
    print('COunt', b.count('apple'), '          233')
    print('COunt', b.count('apple', 10), '          234')
    print('COunt', b.count('apple', 10, 14), '          235')

    """ optional parameters, same as count------231"""
    print('\n', 'Ends with', b.endswith(',', 1, 14), '       238')
    print('Ends with', b.endswith('t'), '       239')
    print('Ends with', b.endswith('t', 10), '       240')

    """ Default size 8 ho but can be changed if added int parameter """
    c = 'r\to\th\ta\tn'
    print('\n', 'expandtabs', c.expandtabs(), '       244')
    print('expandtabs', c.expandtabs(2), '       245')

    """ FIND chercks the first occurance of the target, has the start and end index, same rules as aboves
        returns -1 if a value is not found, while index throws error
    """
    print('\nfind', b.find('apples'), '       250')
    # apple khojda apples ko ans dinxa bt apples khojda apple ko didaina
    print('find', b.find('apple', 9, ), '       252')
    print('find', b.find('apple', 9, 13),
          '           253', 'look at 228 for index')

    # print('index', b.index('apple', 9, 13), '       256')

    b = "I love apples, apple apples are my favorite fruit"

    print('\nrfind', b.rfind('apples'), '       260')
    print('rfind', b.rfind('apple', 9, ), '       261')
    print('rfind', b.rfind('apple', 9, 13), '       262')

    txt1 = "My name is {fname}, I'm {age}".format(
        fname="John", age=36)  # keyword placeholder
    txt2 = "My name is {0}, I'm {1}".format(
        "John", 36)  # positional placeholder
    txt3 = "My name is {}, I'm {}".format("John", 36)  # empty placeholder

    print('\nformat1', txt1, '       264')
    print('format2', txt2, '       266')
    print('format3', txt3, '       268\n')

    # print('index', b.rindex('apple', 9, 13), '       256')
    """ Except isacii, isspace, istitle,islower, isupper if u put escape seq and check, it returns False  """
    a = 'Rohan123'
    print('a=', a)
    print('alnum:', a.isalnum(), '        278')          # allows alphamumeric
    print('alpha:', a.isalpha(), '        279')          # allows only alphabet
    # allows only decimal numbers string (0-9)
    print('decimal:', a.isdecimal(), '        281')
    print('ascii:', a.isascii(), '        282')          # allows everything
    # allows decimals, subscripts, superscripts
    print('digit:', a.isdigit(), '        284')
    # checks if value stored in passed variable can be an identifier
    print('identifier:', a.isidentifier(), '        286')
    # returns true only if all characters are lowercase and false if no character available
    print('islower:', a.islower(), '        288')
    print('isnumeric:', a.isnumeric(), '        289')
    print('isprintable:', a.isprintable(), '        290')
    print('issapce:', a.isspace(), '        291')
    print('istitle:', a.istitle(), '        292')
    # returns true only if all characters are uppercase and false if no character available
    print('isupper:', a.isupper(), '        294')
    fruits = ['apple', 'orange', 'avocado']
    print('\njoin', '=='.join(fruits), '        296')
    myDict = {"name": "John", "country": "Norway"}
    # when we use join in dictionary, it returns the keys, not values
    print('dictionary join', '---'.join(myDict), '        299')
    # ljust is the same as center, just indented to left
    print('\nljust:', a.ljust(20), '        301')
    print('ljust optional:', a.ljust(20, '0'), '        302')
    # casefold is stronger than lower as it translates other langs as well.
    print('lower:', a.lower(), '        304')
    # removes all spaces on the left
    print('lower:', a.lstrip(), '        306')
    a = '    Rohan'
    print('\nlstrip:', a.lstrip(), '        308 look this line')
    a = 'hswa....Rohan'
    print('lstrip:', a.lstrip('whas.'), '        310')
    """ trans replaces the sepcified values in translation table concept and 3rd arg is for deletion value
        Eg: 'Rn''Nr' gives Nohar """
    print(a.translate(str.maketrans('a', 'P')), '        312')
    print(a.translate(str.maketrans('a', 'P', 'h')), '        313')
    """ partition checks for the 1st occurance, if taget not found returns 1st value= whole string, 2nd and 3rd value=empty string """
    a = 'Rohan Rohan Rohan'
    print('\npartition:', a.partition('h'), '        317')
    print('partition:', a.partition('q'), '        318')
    # rpartition is same as partition but just works in reverse
    print('\nrpartition:', a.rpartition('h'), '        320')
    print('rpartition:', a.rpartition('q'), '        321')

    # replace wiil replace all the available values, if the 3rd arg, i.e. count isn't specified
    print('\nreplace:', a.replace('Rohan', 'haseena'), '        324')
    print('replace:', a.replace('Rohan', 'haseena', 2), '        325')
    print('\nrjust:', a.rjust(20), '        326')
    print('rjust:', a.rjust(20, 'h'), '        327')
    fruits = 'apple, orange, banana'
    print('\nrsplit', fruits.rsplit(', '), '        329')
    print('rsplit', fruits.rsplit(', ', 1), '        330')
    a = 'Rohan    '
    print('\nrstrip:', a.rstrip(), '        332')
    a = 'Rohanhswa....'
    print('rstrip:', a.rstrip('awhs.'), '        334')
    a = 'Rohan is a good boy'
    print('\nsplit:', a.split(), '        336')
    print('split:', a.split('a'), '        337')  # puts comma innplace of a
    print('split:', a.split('a', 1), '        338')  # puts comma innplace of a
    a = "Thank you for the music\nWelcome to the jungle"
    # default value is False
    print('\nsplitlines:', a.splitlines(), '             340')
    print('splitlines:', a.splitlines(1), '             341')
    a = '     Rohan    '
    print('\nstrip:', a.strip(), '        343')
    a = 'hswa....Rohanhswa....'
    print('strip:', a.strip('awhs.'), '        345')
    print('\nswapcase:', a.swapcase(), '        347')
    """ Generally, makes each 1st letter of each word capital.title will convert 1 letter after a number into capital irrespective of position  """
    txt = "hello b2b2b2 and 3g3g3g"
    print('\ntitle:', txt.title(), '        350')
    a = 'Rohan'
    # takes ascii for translation, or u can use maketrans instead coz both are same
    print('translate:', a.translate({82: 80}), '        353')
    print('upper:', a.upper(), '        354')
    # the parameter number is length and can fill only 0
    print('zfill:', a.zfill(10), '        356')
    print('startswith:', a.startswith('R'), '               357')

    """ String operations used:
        1. capitalize
        2. Casefold
        3. center
        4. count
        5. endswith
        6. expandtabs
        7. find
        8. format
        9.index
        10. isalnum
        11. isalpha
        12. isascii
        13. isdecimal
        14. isdigit
        15, isidentifier
        16. islower
        17. isnumeric
        18. isprintable
        19. isspace
        20. istitle
        21. isupper
        22. join
        23. ljust
        24. lower
        25. lstrip
        26. maketrans
        27. partition
        28. replace
        29. rfind
        30. rindex
        31. rjust
        32. rpartition
        33. rsplit
        34. rstrip
        35. split
        36. splitlines
        37. startswith
        38. strip
        39. swapcase
        40. title
        41. translate 
        42. upper
        43.zfill 
        """


def list_op():
    fruits = ['apple', 'banana', 'cherry']
    """ list of list or list of tuple also appendable """
    fruits.append('orange')
    print('append:', fruits, '                409')

    fruits.clear()
    print('clear:', fruits, '                412')

    fruits = ['apple', 'banana', 'cherry']
    y = fruits.copy()
    print('copy:', y, '                416')

    fruits.append('apple')
    print('count:', fruits.count('apple'), '                419')

    fruits = ['apple', 'banana', 'cherry']
    cars = ['Ford', 'BMW', 'Volvo']   # tupe or set can also be instead of list
    fruits.extend(cars)
    # if append was used instead of extend, list of list would have been appended, we can also use + between two list to directly extend
    print('Extend:', fruits, '                424')

    fruits = [4, 55, 64, 32, 16, 32]
    # returns 1st occrance if repeat
    print('index:', fruits.index(32), '                430')

    fruits = ['apple', 'banana', 'cherry']
    fruits.insert(1, "orange")
    print('insert:', fruits, '                433')

    fruits = ['apple', 'banana', 'cherry']
    x = fruits.pop(1)  # if parameter not passed, removes last value
    print('\npopped list:', fruits, '                437')
    print('popped value:', x, '                437')

    fruits = ['apple', 'banana', 'cherry']
    fruits.remove("apple")
    print('after remove:', fruits, '                442')
    fruits.reverse()
    print('reverse:', fruits, '                444')

    cars = ['Ford', 'BMW', 'Volvo']
    cars.sort()
    print('\nsort:', cars, '                448')
    cars.sort(reverse=True)
    print('sort reverse:', cars, '                450')

    def myFunc(e):
        # e is the length of input of each element from the list
        return len(e)

    cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
    cars.sort(key=myFunc)
    print('\nsort function:', cars, '            453')

    def myFunc(e):
        return e['year']

    cars = [
        {'car': 'Ford', 'year': 2005},
        {'car': 'Mitsubishi', 'year': 2000},
        {'car': 'BMW', 'year': 2019},
        {'car': 'VW', 'year': 2011}
    ]
    cars.sort(key=myFunc)
    print(cars, '            460  look at line 472 and 473')

    del cars
    # print('del:', cars, '                472')

    """ List operations used:
        1. append
        2. clear
        3. copy
        4. count
        5.extend
        6. insert
        7. index
        8. pop
        7. remove 
        9. reverse
        10. sort
        11.del
        """


def tuple_op():
    thistuple = ("apple",)
    print(type(thistuple), 'look at line 492')

    # NOT a tuple
    thistuple = ("apple")
    print(type(thistuple), 'look at line 496')

    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
    # counts repeated elements
    print('count:', thistuple.count(5), '           499')

    thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)   # 1st occurance only
    print('index:', thistuple.index(5), '           499')

    print('len:', len(thistuple))

    """ To do any sort of CRUD thing in list first convert it to list, do the operation and reconvert to tuple
        printing of elements via indexing is also possble
        CONCATENATION OF two tuples is possible
        unpacking is also possible 
    """

    """ Operations:
        1. Count
        2. Index
        3. len
    """


def dict_op():
    info = {
        'name': 'Rohan',
        'age': 20,
        'classs': 13
    }
    y = info.copy()
    print('copy:', y, '               528')

    info.clear()
    print('clear:', info, '           533')

    a = ('key1', 'key2', 'key3')
    y = ('Rohan')  # if y wasnt defined, the value would have been None
    print('from keys:', dict.fromkeys(a, y), '           536,   look at 535')

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print('\nget:', car.get('brand'), '           543')
    print('if key not exist, get:', car.get('brand1'), '           544')
    print('if key not exist value can be specified, get:',
          car.get('brand1', 'KIA'), '           545')
    print('\nitems:', car.items(), '           547')  # gives list of tuples
    car['price'] = 120000
    print('items after update:', car.items(),
          '           548')

    print('\nkeys:', car.keys(), '           552')  # returns list

    """ If given key not exist, throws error. if default value parameter passed ,returns that value
         works same as list but needs key para, not index  """
    print('\npopped value:', car.pop('price'), '           556')
    # print('popped value:',car.pop('price1')) will give error
    print('\npopitem value not available, default parameter added:',
          car.pop('price1', 200000), '           559   look at 557')
    print('dictionary after pop:', car)

    # returns tuple of key-value pair
    print('popitem:', car.popitem(), '           563 ')
    print('dict after popitem:', car)
    car.update({'brand': 'BMW'})
    print('\nupdate:', car, '               565')

    print('values:', car.values(), '            568')  # returns list


# garb()
# assign()
# conc()
# multi()
# unpack()
# fx()
# sc()
# w_t_p()
# string()
# str_op()
# list_op()
# tuple_op()
dict_op()

"""                 References:
    String operations: https://www.w3schools.com/python/python_ref_string.asp 
    List operations: https://www.w3schools.com/python/ref_list_append.asp
    Tuple operations:
    """
