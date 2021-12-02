#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random,re

id_num = 1
process_list = ["process"]
ready_list = ["ready"]
block_list = ["block"]
source_list= []
run_list = ["run"]
prio = []
a0 = [0,'Q0']
a1 = [1,'Q1']
a2 = [2,'Q2']

class Process:
    mes = [] #内存
    ots = [] #其他资源
    gentree = []
    
    status = [] #前者是状态码，后者是状态队列指针 0
    # 0  阻塞   Q0
    # 1  就绪   Q1
    # 2  运行   Q2
    def __init__(self,name,id,pri):
        self.__name = name
        self.__id = id
        self.__pri = pri
        self.status = [1,"Q1"]
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_pri(self):
        return self.__pri
    def set_pri(self,n):
        self.__pri = n
class Source:
    def __init__(self,rid):
        self.__rid = rid
        self.status = 1
        # 0 ---- 忙
        # 1 ---- 空闲
        self.wq = []
        # 有谁在等待本资源
    def get_rid(self):
        return self.__rid

def create_process(pname,ppri):
    global id_num
    ram = id_num
    p = Process(pname,ram,ppri)
    process_list.append(p)
    id_num = id_num + 1
    return p

def find_in_list(id,listname):
    for i in range(1,len(listname)):
        if listname[i].get_id() == id:
            pos = i
            return pos
    return 0        

def delete_status(id):
    for i in range(1,len(source_list)):
        temp = source_list[i]
        try:
            temp.wq.remove(id)
            if temp.wq == []:
                temp.status = 1
        except:
            pass
        source_list[i] = temp
        
def del_process(id):
    # 根据id删除进程
    flag = 0
    for i in range(1,len(process_list)):
        if process_list[i].get_id() == id:
            pos = i
            flag = 1
            break
        else:
            flag = 0
    if flag:
        prio.remove(process_list[pos].get_pri())
        process_list.pop(pos)
        delete_status(id)
        
#          根据id删除进程
def get_all_id():
    results = []
    for i in range(1,len(process_list)):
        results.append(process_list[i].get_id())
    return results
def print_name(lists,flag):
    if flag == 1:
        strs = " is Ready !"
    else:
        strs = " is Blocked !"
    temp = lists[1:].copy()
    for term in temp:
        name = get_obj_name(term)
        print(name+"("+str(term)+")"+strs)

def get_obj_name(id):
    temp = process_list[1:].copy()
    for term in temp:
        if term.get_id() == id:
            return term.get_name()
    return 0
def get_obj_id(name):
    temp = process_list[1:].copy()
    for term in temp:
        if term.get_name() == name:
            return term.get_id()
    return 0

def create_source(): 
    global source_list
    # 在这里，将返回一个形如["source",S1,S2,S3,S4,S5,S6]的资源列表，其中，该列表的下标即表示source的编号
    sources_list = []
    sources_list.append("source")
    for i in range(6):
        sources_list.append(Source(i+1))
    source_list = sources_list.copy()
    return sources_list

def input_part():
    back = []
    inputs = input("python >>> ")
    inputs = re.sub(' +', ' ', inputs).split(" ")
    if inputs[0] == "cr" and inputs[1] != "" and inputs[2].isdecimal() and int(inputs[2]) not in prio:
        back.append(1)
        back.append(inputs[1])
        back.append(inputs[2])
        prio.append(int(inputs[2]))
    elif inputs[0] == "del" :
        back.append(2)
        back.append(inputs[1])    
    elif inputs[0] == "req" and inputs[1].isdecimal() and int(inputs[1])<7:
        back.append(3)
        back.append(int(inputs[1]))  
    elif inputs[0] == "rel" and inputs[1].isdecimal()and int(inputs[1])<7:
        back.append(4)
        back.append(int(inputs[1]))
    elif len(inputs) == 2 and inputs[0] == "ls" and inputs[1] == "-p" :
        back.append(5)
    elif len(inputs) == 2 and inputs[0] == "ls" and inputs[1] == "-s" :
        back.append(6)
    elif inputs[0] == "bye":
        exit(0)
    else:
        back.append(0)
    return back

if __name__ == "__main__":
    create_source()
    while True:
        showflag = 1
        inputs = input_part()
        if inputs[0] == 0:
            print("ERROR!")
            continue
        elif inputs[0] == 1:
            create_process(inputs[1],int(inputs[2]))      
        elif inputs[0] == 2:
            temp1 = get_obj_id(inputs[1])
            if temp1 ==0:
                print("No such process!")
                continue
            del_process(temp1)
        elif inputs[0] == 3:
            run_number = run_list[1].get_id()
            index = inputs[1]
            temp = source_list[index]
            if temp.status == 1:
                temp.status = 0
            if run_number not in temp.wq:
                temp.wq.append(run_number)
            source_list[index] = temp
        elif inputs[0] == 4:
            run_number = run_list[1].get_id()
            index = inputs[1]
            temp = source_list[index]
            if temp.status != 1:
                try:
                    temp.wq.remove(run_number)
                except:
                    pass
                if len(temp.wq ) == 0:
                    temp.status = 1
                source_list[index] = temp
            else:
                pass
        elif inputs[0] == 5:
            lens = len(process_list)
            if lens == 1:
                print("None!")
                continue
            for i in range(1,lens):
                term = process_list[i]
                print(term.get_name()," ",term.get_id()," ",term.get_pri())
                
        elif inputs[0] == 6:
            for i in range(1,len(source_list)):
                term = source_list[i]
                print(" Source",term.get_rid()," ",term.status," ",term.wq)
                showflag = 0
        else:
            pass
        
        ############################
        temp_lists = process_list[1:].copy()
        if len(temp_lists) == 0:
            continue
        
        work_lists = sorted(temp_lists,key = lambda a:a.get_pri(),reverse = True)
        if len(run_list) == 1:
            temps= work_lists[0]
            temps.status = a2
            temp_num = temps.get_id()
            k = find_in_list(temp_num,process_list)
            process_list[k] = temps
            run_list.append(temps)
            work_lists.pop(0)
            print(temps.get_name()+'('+str(temps.get_id())+')'+" is Running !")
            
        else:
            kills = run_list[1].get_id()
            kill_pos = -1
            for i in range(0,len(work_lists)):
                if kills == work_lists[i].get_id():
                    kill_pos = i
                    break
            if kill_pos == -1:
                    run_list[1].set_pri(-1)
            else:
               work_lists.pop(kill_pos)
            try:
                if(run_list[1].get_pri()<work_lists[0].get_pri()):
                    l1 = run_list[1]
                    l2 = work_lists[0]
                    l1.status = a1
                    l2.status = a2
                    k1 = find_in_list(l1.get_id(),process_list)
                    k2 = find_in_list(l2.get_id(),process_list)
                    process_list[k1] = l1
                    process_list[k2] = l2
                    run_list[1] = l2
                    print(l2.get_name()+'('+str(l2.get_id())+')'+" is Running !")
                else:
                    print(run_list[1].get_name()+'('+str(run_list[1].get_id())+')'+" is Running !")
            except:
                print(run_list[1].get_name()+'('+str(run_list[1].get_id())+')'+" is Running !")
        status =["source_status"]
        ready_list = ["ready"]
        ready_list.extend(get_all_id())
        block_list = ["block"]
        for i in range(1,len(source_list)):
            status.append(source_list[i].wq)
        status_copy = status.copy()
        running_id = run_list[1].get_id()
        running_lists = ["running"]
        running_lists.append(running_id)
        try:
            
            ready_list.remove(running_id)
        except:
            pass
        for i in range(1,len(status)):
            temp = status_copy[i].copy()
            if running_id in temp :
                temp.remove(running_id)
                for term in temp:
                    if term not in block_list:
                        block_list.append(term)
                    try:
                        ready_list.remove(term)
                    except:
                        pass
        if showflag:           
            print_name(ready_list, 1)
            print_name(block_list, 2)
        # work_lists 按优先级排序后的 process_list
        
                
# 所有进程的列表 process_list = ["process",P1,P2,P3,P4,......]          NO!    后续加入
# 所有资源的列表 source_list  = ["source",S1,S2,S3,S4,S5,S6] 有且只有六个 NO!   已有六个
# 所有就绪的列表 ready_list   = ["ready",P1,PX,.........]                      后续加入
# 所有阻塞的列表 block_list   = ["block",P1,PX,.........]                      后续加入
# 所有运行的列表 run_list = ["run",P1]                                         后续加入

    # process : __name str, __id int, __pri int, status [int,listname] 0阻 block_list , 1就 ready_list , 2运 run_list
    # source: __rid int, status 0忙1闲 int, wq [process_name]谁在等待这个资源？

'''


    # p1 = Process("P1",22322,2)
    # print(p1.get_name(),"   ",p1.get_pri(),)


'''
