def same_source(allocation,max,all):
    already = sum(allocation)
    safe_list = []
    need_list = [max[i] - allocation[i] for i in range(len(max))]
    free = all - already
    for i in range(len(need_list)):
        if need_list[i] <= free:
            safe_list.append(i)
    # print(safe_list)
    
if __name__ == '__main__':
    same_source([1,4,5],[2,4,8],12)