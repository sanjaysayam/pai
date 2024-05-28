def sjf(process,n):
    process.sort(key=lambda x:x[0])
    executionorder=[]
    currenttime=0
    totalwaitingtime=0
    while len(process)>0:
        availableprocess=[p for p in process if p[0]<=currenttime]
        if len(availableprocess) == 0:
            currenttime=process[0][0]
        else:
            availableprocess.sort(key=lambda x:x[1])
            shortestjob=availableprocess[0]
            currenttime+=shortestjob[1]
            totalwaitingtime+=currenttime-shortestjob[0]-shortestjob[1]
            executionorder.append(shortestjob[2])
            process.remove(shortestjob)
    averagewaitingtime=totalwaitingtime/n
    return executionorder,averagewaitingtime
process=[(0,5,'p1'),(1,3,'p2'),(3,5,'p3'),(5,2,'p4'),(6,3,'p5')]
numprocess=len(process)
executionorder,averagewaitingtime=sjf(process,numprocess)
print("execution order of processes in SJF:",executionorder)
print("average waiting time of processes in SJF:",averagewaitingtime)
