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
    pass
#  累了，爬不动了，先写到这里吧
#  想摸鱼了
#  先打一把游戏，和平精英 乖巧大狗狗

if __name__ == '__main__':
    a,b,c,d= SSTF(100)
    print(a)
    print(b)
    print(c)
    print(d)