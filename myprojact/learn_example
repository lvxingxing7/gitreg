def filedoc(filename:str,doc:bool = False) -> str:
    finddoc = filename.rfind('.')
    if not doc :
        finddoc += 1
    return filename[finddoc:] if finddoc > 0 else ''
# if __name__ == '__main__':
#      print(filedoc('asc.py'))

def calcu ( init_value:int , fn , *args:int , **kwargs:int ) -> int:
    total = init_value
    for arg in args:
        if type(arg) in (int,float):
            total = fn(total,arg)
    for varg in kwargs.values():
        if type(varg) in (int,float):
            total = fn(total,varg)
    return total
# if __name__ == '__main__':
#      print(calcu(100,lambda x , y : x + y ,111))

def sort(lst:list,fn=lambda x , y : x > y ,resver:bool=False) -> list:
    new_lst = lst[:]
    for i in range (1,len(new_lst)):
        swap = False
        for j in range (0,len(new_lst) - i ):
            if fn (new_lst[j],new_lst[j + 1]):
                new_lst[j],new_lst[j+1] = new_lst[j+1],new_lst[j]
                swap = True
        if not swap :
            break
    return new_lst
# if __name__ == '__main__':
#      print(sort([11,53,73,24,73,57,64,23,78]))

def midfind(lst:list,nmb:int) -> int:
    start ,end = 0 ,len(lst) -1
    while start <= end:
        mid = (start + end) // 2
        if nmb > lst[mid]:
            start = mid + 1
        elif nmb < lst[mid]:
            end = mid - 1
        else:
            return mid
    return -1
# if __name__ == '__main__':
    # print(midfind([11, 23, 24, 53, 57, 64, 73, 73, 78],78))