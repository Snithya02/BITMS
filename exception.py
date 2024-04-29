l=[1,2,3,4,5]
def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print('error')
    finally:
        print("end of fun")
try:
    fun(l,5)
except IndexError:
    print("indexerror")
finally:
    print("End of blocks")