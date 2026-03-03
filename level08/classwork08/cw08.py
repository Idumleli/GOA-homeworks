# 1)

print(True and False)
print(False and True)
print(True and True)
print(False and False)

print(True or False)
print(False or True)
print(True or True)
print(False or False)


#2) რას გამოიტანს ეს კოდი? True and False or False or True and True and False or True
                               #False  or False     or      True   and    False   or  True
                                   #    False        or            False   or True    
                                   # საბოლოო ჯამში პასუხი იქნება True
print(True and False or False or True and True and False or True)

print( '--------')
#3)

people = 4
thief = 5

thief_detected = thief > people 
print(thief_detected)
