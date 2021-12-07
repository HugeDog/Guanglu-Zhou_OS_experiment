# 第三次实验

table_free = []
# 【始址，长度】
# 【20，30】
# [0,20],[30,10]
table_used = []
# 【始址，长度，标志】
# 【0，100，a】
name_table = []
mem = []
mem_size = 100
status_global = 0  # 最差 -1    最先  0     最佳 1
busy_table = []

def change_status():
    global status_global
    while True:
        inputs = input("Input Your Status:")
        if inputs.digit() and inputs in ['0','-1','1']:
            break
    inputs = int(inputs)
    status_global = inputs
    
def mm_init(size):
    global mem,mem_size,table_free,table_used
    mem_size = size
    mem = [0 for i in range(size)]
    table_free = []
    table_used = []
    table_free.append([0,size])
    return table_free[0][0]

def get_last(name,size):
    global table_free,table_used
    if table_free == []:
        return ""
    maxitem = table_free[0]
    for item in table_free:
        if item[1] > maxitem[1]:
            maxitem = item
    ### 得到了最大的
    if maxitem[1] == size:
        ret = maxitem[0]
        temp = maxitem.copy()
        table_free.remove(maxitem)
        temp.extend([name])
        table_used.append(temp)
        return ret
    elif maxitem[1] > size:
        temp = maxitem
        list1 = []
        temp_num0 = maxitem[0]
        list1.append(temp_num0)
        list1.extend([size,name])
        temp_num1 = maxitem[1]
        temp_num0 = temp_num0 + size
        temp_num1 = temp_num1 - size
        maxitem[0] = temp_num0
        maxitem[1] = temp_num1
        # table_free.remove(temp)
        # table_free.append([temp_num0,temp_num1])
        table_used.append(list1)
        return temp_num0
    else:
        return ""

def get_best(name,size):
    global table_free,table_used
    flag = 0
    if table_free == []:
        return ""
    maxitem = [-1,10000000000000000]
    for item in table_free:
        if item[1] >= size:
            if item[1] < maxitem[1]:
                maxitem = item
    if maxitem[0] == -1:
        return ""
    elif maxitem[1] == size:
        temp = maxitem.copy()
        table_free.remove(maxitem)
        temp.append(name)
        table_used.append(temp)
        return temp[0]
    elif maxitem[1] > size:
        temp = maxitem.copy()
        num1 = temp[0]
        num2 = temp[1]
        num11 = num1 + size
        num22 = num2 - size
        maxitem[0] = num11
        maxitem[1] = num22
        table_used.append([num1,size,name])
        return num1
    else:
        pass
    return ""

def get_fit(name,size):
    global table_free,table_used
    flag = 0
    for item in table_free:
        if item[1] > size:
            flag = 1
            temp = item
            num0 = temp[0]
            num1 = temp[1]
            num00 = num0 + size
            num11 = num1 - size
            table_used.append([num0,size,name])
            item[0] = num00
            item[1] = num11 
            return num0
        elif item[1] == size:
            temp = item.copy()
            table_free.remove(item)
            temp.append(name)  
            table_used.append(temp)
            flag = 1
            return temp[0]
        else:
            pass
    return ""
    
def get_fit_space(name,size):
    global name_table,status_global,table_free,table_used
    if name in name_table:
        return "?"
    status = status_global
    table_free.sort(key = lambda x:x[0])
    table_used.sort(key = lambda x:x[0])
    if status == -1:
        temp = get_last(name,size)
    elif status == 0:
        temp = get_fit(name,size)
    elif status == 1:
        temp = get_best(name,size)
    else:
        print("Error!!")
    if temp != "":
        name_table.append(name)
    else:
        temps = [name,size]
        if temps not in busy_table:
            busy_table.append(temps)
    return temp 

def closure_():
    global table_free
    flag = 0
    while True:
        flag = 0
        lens = len(table_free) - 1
        for i in range(lens):
            if table_free[i][0] + table_free[i][1] == table_free[i+1][0]:
                flag = 1
                num0 = table_free[i][0]
                num1 = table_free[i][1] + table_free[i+1][1]
                temp1 = table_free[i]
                temp2 = table_free[i+1]
                table_free.remove(temp1)
                table_free.remove(temp2)
                table_free.append([num0,num1])
                break

        if flag == 0:
            return "Done!"

def squeeze():
    global table_free,table_used
    index = 0
    if table_free == []:
        return "Absolutely No Space !"
    # table_free.sort(key = lambda x:x[0])
    table_used.sort(key = lambda x:x[0])
    table_used_new = []
    for item in table_used:
        temp = [index,item[1],item[2]]
        index = index + item[1]
        table_used_new.append(temp)
    table_used = table_used_new.copy()
    table_free = [[index,mem_size-index]]
    return "Done !"

def mm_request(name,size):
     return get_fit_space(name,size)

def mm_release(name):
    global table_used,table_free
    flag = 0
    for item in table_used:
        if item[2] == name:
            flag = 1
            temp = item.copy()
            table_used.remove(item)
            name_table.remove(name)
            list1 = [temp[0],temp[1]]
            table_free.append(list1)
            table_free.sort(key = lambda x: x[0])
            closure_()
            break
        else:
            pass
    if flag == 0:
        return "Find Nothing!"
    if busy_table != []:
        k = mm_request(busy_table[0][0],busy_table[0][1])
        if k == "?":
            busy_table.pop(0)
        elif k != "":
            busy_table.pop(0)
        else:
            pass
    
def print_status():
    f = 0
    print("空闲区间_ ，使用区间 ×")
    for i in table_free:
        x_temp = i[0] - f
        print("%s%s"%(x_temp*"×",i[1]*"_"),end = "")
        f = i[0] + i[1]

if __name__ == '__main__':
    mm_init(100)
    change_status()
    mm_request('a',20)
    mm_request('b',30)
    print(name_table)
    mm_request('c',10)
    print(name_table)
    mm_release('b')
    print(name_table)
    print(table_free)
    # print(print_status())