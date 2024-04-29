l=[2,3,4,5,6]
try:
    try:
        a=l.copy()
        a[0]=l[0]/l[5]
    except ValueError:
        print("abc")
    finally:
        print("end of fun")
except IndexError:
    print("index")