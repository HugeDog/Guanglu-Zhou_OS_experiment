# 实验五
req_list = [55,58,39,18,90,160,150,38,184]

def find_min(num,list_r):
    dist = 1000000000000
    res = -1
    for item in list_r:
        if abs(item - num) < dist:
            dist = abs(item - num)
            res = item
    return res

def FCFS(start):
    list_r = req_list.copy()
    if list_r == []:
        return [],[],0,0
    res = []
    sums = 0
    pos = start
    for item in list_r:
        temp = abs(pos - item)
        sums += temp
        res.append(temp)
        pos = item
    return list_r,res,sums,round(sums/len(list_r),1)

def ret(start,lists):
    sums = 0
    seq = []
    res = []
    pos = start
    for item in lists:
        temp = abs(item - pos)
        sums += temp
        seq.append(item)
        res.append(temp)
        pos = item
    return seq,res,sums,pos
              
def SSTF(start):
    list_r = req_list.copy()
    lenth = len(list_r)
    if list_r == []:
        return [],[],0,0
    pos = start
    seq = []
    res = []
    sums = 0
    while True:
        if list_r == []:
            break
        min = find_min(pos,list_r)
        temp = abs(min - pos)
        sums += temp
        res.append(temp)
        seq.append(min)
        pos = min
        list_r.remove(min)
    return seq,res,sums,round(sums/lenth,2)
        
def elevator(start):
    list_r = req_list.copy()
    if list_r ==[]:
        return [],[],0,0
    list_r.sort()
    for i in range(len(list_r)):
        if list_r[i] >= start:
            pos = i
            break
    list1 = list_r[0:pos]
    list1.reverse()
    list2 = list_r[pos:]
    x1, x2, x3, pos = ret(100,list2) 
    y1, y2, y3, _ = ret(pos,list1)
    x1.extend(y1)
    x2.extend(y2)
    sums = x3 + y3
    avg = round((sums/len(list_r)),1)
    return x1, x2, sums, avg
        
if __name__ == '__main__':
    a,b,c,d= elevator(100)
    print(a)
    print(b)
    print(c)
    print(d)
    