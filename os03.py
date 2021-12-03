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
    
def get_last(name,size):
    global table_free,table_used
    if table_free == []:
        return "Absolutely No Space !"
    maxitem = table_free[0]
    for item in table_free:
        if item[1] > maxitem[1]:
            maxitem = item
    ### 得到了最大的
    if maxitem[1] == size:
        temp = maxitem.copy()
        table_free.remove(maxitem)
        temp.extend([name])
        table_used.append(temp)
        return "="
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
        return ">"
    else:
        return "No Space!"

def get_best(name,size):
    global table_free,table_used
    flag = 0
    if table_free == []:
        return "Absolutely No Space !"
    maxitem = [-1,10000000000000000]
    for item in table_free:
        if item[1] >= size:
            if item[1] < maxitem[1]:
                maxitem = item
    if maxitem[0] == -1:
        return "No Space!"
    elif maxitem[1] == size:
        temp = maxitem.copy()
        table_free.remove(maxitem)
        temp.append(name)
        table_used.append(temp)
        return '='
    elif maxitem[1] > size:
        temp = maxitem.copy()
        num1 = temp[0]
        num2 = temp[1]
        num11 = num1 + size
        num22 = num2 - size
        maxitem[0] = num11
        maxitem[1] = num22
        table_used.append([num1,size,name])
        return '>'
    else:
        pass
    return "Done !"

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
            return ">"
        elif item[1] == size:
            temp = item.copy()
            table_free.remove(item)
            temp.append(name)  
            table_used.append(temp)
            flag = 1
            return "="
        else:
            pass
    return "No Space!"
    
def get_fit_space(name,size):
    global name_table,status_global,table_free,table_used
    if name in name_table:
        return "Already Exists!"
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
    if temp != "No Space!":
        name_table.append(name)
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
    get_fit_space(name,size)

def mm_release(name):
    global table_used,table_free
    for item in table_used:
        if item[2] == name:
            temp = item.copy()
            table_used.remove(item)
            name_table.remove(name)
            list1 = [temp[0],temp[1]]
            break
        else:
            return "Find Nothing!"
    table_free.append(list1)
    table_free.sort(key = lambda x: x[0])
    closure_()
    # pjiougyuutgjyvfhgujhilkjo;ihghikjol;hkhh;j
    
    
if __name__ == '__main__':
    mm_init(100)
    mm_request('aa',10)
    print(table_free)
    print(table_used)
    mm_request('bb',30)
    print(table_free)
    print(table_used)
    mm_release('bb')
    print(table_free)
    print(table_used)
    mm_request('cc',20)
    print(table_free)
    print(table_used)
    
    # print(mem)
    # print(table_free)
    # table_used = [[20,10,"a"],[40,30,'bb']]
    # status_global = 0
    
    # name = "sss"
    # size = 10
    # types = get_fit_space(name,size)
    # get_fit_space('1222',15)
    # # squeeze() # 40  60  0 10 a  10 30 bb
    # print(table_used)
    # print(table_free)