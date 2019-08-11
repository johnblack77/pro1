import copy
def loadData():
    # data_set = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
    #         ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
    #         ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    data_set=[[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    return data_set


#生成首个候选项集
def createC(data_set):
    C=list()
    for i in data_set:
        for j in i:
            if [j] not in C:
                C.append([j])
    C.sort()
    return list(map(set,C))


#统计候选集生成频繁项集
def statisticsC_getL(data_set,C,minSupport):
    dataLen=float(len(data_set))
    d=dict()
    retList=[]
    for i in data_set:
        for j in C:
            if str(j) not in d:
                d[str(j)] = 0
            if j.issubset(i):
                d[str(j)]=d[str(j)]+1

    for i in C:
        d[str(i)] = d[str(i)] / dataLen
        if d[str(i)]>=minSupport:
            retList.append(i)

    return retList,d


#根据频繁集生成候选项集
def createC_byL(LK,K):
    retList=[]
    lenLk=len(LK)

    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(LK[i])[:K-2]
            L2=list(LK[j])[:K-2]
            L1.sort()
            L2.sort()
            if L1==L2:
                Ck_item=LK[i]|LK[j]
                if pruning(Ck_item,LK):
                    retList.append(LK[i]|LK[j])
    return retList


#判断候选集中子集是否为频繁项集
def pruning(Ck_item,LK):
    for i in Ck_item:
        temp=Ck_item-{i}
        if temp not in LK:
            return False
    return True


#生成频繁项目集的子集
def generatingSubset (itemSet,retList):
    ret=copy.deepcopy(retList)
    s=[]
    while ret:
        t=ret.pop(0)
        if t not in s:
            s.append(t)
        for i in t:
            temp=t-{i}
            if temp in itemSet:
                ret.append(temp)
    return s


def generatingRules(supportSet,retList,itemSet,min_conf):
    result=[]
    for i in retList:
        s=generatingSubset(itemSet,[i])
        for j in s:
            if j!=i:
                temp=supportSet[str(i)]/supportSet[str(j)]
                if temp>=min_conf:
                    temp1=i-j
                    string=str(j)+"=>"+str(temp1)+" conf:"+str(temp)
                    result.append(string)
    return result


if __name__ == '__main__':
    itemSet=[]#频繁项集集合
    supportSet=dict()#支持度集合
    result=[]
    data_set=loadData()
    C=createC(data_set)
    data=list(map(set,data_set))
    retList,d=statisticsC_getL(data,C,minSupport=0.5)
    #print(d)
    #print(retList)
    itemSet.extend(retList)
    supportSet.update(d)
    k=2
    while (len(retList[k-2:]) > 0):
        retList = createC_byL(retList, k)
        retList, d = statisticsC_getL(data, retList, minSupport=0.5)
        print(retList)
        supportSet.update(d)
        itemSet.extend(retList)
        res=generatingRules(supportSet,retList,itemSet,0.5)
        result.extend(res)
        # print(d)
        #print(retList)
        k+=1
    #print(retList)
    #s=generatingSubset(itemSet,[{'l2', 'l1', 'l5'}])
    for i in result:
        print(i)







