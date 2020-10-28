from fakeproj.fakedir.fakemodule import fakefunc

def dummyfunc() -> int:
    mylist = [1, 2, 3, 4, 5]
    myarray = fakefunc(mylist)
    return len(myarray)