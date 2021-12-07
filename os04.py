def compares(list1,list2):
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            return False
    return True

def plus(list1,list2):
    temp = []
    for i in range(len(list1)):
        temps = list1[i] + list2[i]
        temp.append(temps)
    return temp

def print_list(lists):
    for item in lists:
        print("---",item, end = "")
    print()
def same_source(allocation,max,all):
    already = sum(allocation)    
    all_list = [0,1,2]
    safe_list = []
    seq_list = []
    need_list = [max[i] - allocation[i] for i in range(len(max))]
    free = all - already
    leng = len(need_list)
    while True:
        flag = 0
        for i in range(len(need_list)):
            if need_list[i] <= free:
                safe_list.append(i)
        for i in safe_list:
            if all_list[i] != -1:
                flag = 1
                seq_list.append(i + 1)
                free = free + allocation[i]
                all_list[i] = -1
                leng  = leng - 1
        safe_list = []
        if leng == 0:
            print("safe!" ,end = "")
            print_list(seq_list)
            return "1"
        elif flag == 0 :
            print("unsafe!")
            return ""
        else:
            pass

def diff_source(allo,maxs,remain):
    need_list = []
    safe_list = []
    res = []
    for i in range(len(allo)):
        temp = [maxs[i][j] - allo[i][j] for j in range(4)]
        need_list.append(temp)
    number_process = len(allo)
    flag_list = [i for i in range(number_process)]
    while True:
        flag = 0
        for i in range(len(allo)):
            if compares(need_list[i],remain):
                safe_list.append(i)
        for i in safe_list:
            if flag_list[i] != -1:
                res.append(i + 1)
                flag = 1
                flag_list[i] = -1
                number_process = number_process - 1
                remain = plus(allo[i],remain)
        if number_process == 0:
            print("safe!",end = "")
            print_list(res)  
            return 1
        elif flag == 0:
            print("unsafe!")
            return -1
        else:
            pass
    
if __name__ == '__main__':
    same_source([1,4,6],[4,4,8],12)
    diff_source([[0,0,1,2],[1,0,0,0],[1,3,5,4],[0,6,3,2],[0,0,1,4]],[[0,0,1,2],[2,7,5,0],[20,3,5,6],[0,6,5,2],[0,6,5,6]],[1,5,2,0])