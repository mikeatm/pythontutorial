try:
    print a
except NameError:
    print "Error: NameError"
try:
    print 1/0
except ZeroDivisionError:
    print "undefined"
try:
    print 1 + 'hello'
except Exception as e:
    print  repr(e.args)

