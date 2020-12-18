import sys
from itertools import groupby
from operator import itemgetter

class Algo():
    def __init__(self):
        super().__init__()

    def FCFS(self, params):
        #assuming all process passed in here are already in ordered
        arrival_and_burst = params
        list_arrival_and_burst = list(arrival_and_burst.items())
        self.tat = []
        self.tat.insert(0, list_arrival_and_burst[0][1][1] + list_arrival_and_burst[0][1][0])

        self.arrival_time = []
        self.arrival_time.insert(0, list_arrival_and_burst[0][1][0])

        for i in range(1, len(list_arrival_and_burst)):
            self.tat.insert(i, list_arrival_and_burst[i][1][1])
            self.arrival_time.insert(i,  list_arrival_and_burst[i][1][0])

        self.forgantt = []
        tattemp = 0
        self.wait_time = []
        wait_temp = 0
        tattemp = 0

        for i in range(0, len(self.tat)):
            tattemp += self.tat[i]
            self.forgantt.insert(i, tattemp)
            wait_temp = tattemp - self.arrival_time[i]
            self.wait_time.insert(i, wait_temp)

        self.wait_time[0] = 0 #update position 0 to
        # 0 waiting time

    def PREEMPTIVE_PRIORITY(self):
        #assumption : already sorted by arrival time
        arrival_burst_priority = {"p1": [1, 8, 1], "p4": [2, 5, 3], "p3": [3, 2, 2], "p5": [4, 3, 4], "p2": [6, 6, 5]}
        list_arrival_burst_priority = list(arrival_burst_priority.items())
        by_priority = {} #dictionary that will hold the sorted process by priority
        sequence = 0
        #sorting by priority using selection sort algorithm
        #print(list_arrival_burst_priority[0][1][2])
        print(list_arrival_burst_priority)
        for i in range(len(list_arrival_burst_priority)):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            sequence += 1 #serves as key of the "by_priority" dict variable
            for j in range(i + 1, len(list_arrival_burst_priority)):
                if list_arrival_burst_priority[i][1][2] > list_arrival_burst_priority[j][1][2]:
                    min_idx = j
                    by_priority[sequence] = list_arrival_burst_priority[i]
                    sequence += 1
                    by_priority[sequence] = list_arrival_burst_priority[min_idx]
                    remaining_burst = list_arrival_burst_priority[i][1][1] - list_arrival_burst_priority[min_idx][1][1]
                    list_arrival_burst_priority[i][1][1] = remaining_burst

            by_priority[sequence] = list_arrival_burst_priority[min_idx]
            list_arrival_burst_priority[i], list_arrival_burst_priority[min_idx] = list_arrival_burst_priority[min_idx], list_arrival_burst_priority[i]

        tat = []
        ganttchart = []
        wait_time = []
        arrival_time = []
        tattemp=0
        print(by_priority)
        list_by_priority = list(by_priority.items())
        #print(list_by_priority[0][1][1][1]) #burst position
        tat.insert(0, list_by_priority[0][1][1][1] + list_by_priority[0][1][1][0])
        arrival_time.insert(0, list_by_priority[0][1][1][0])
        for i in range(1, len(list_by_priority)):
            tat.insert(i, list_by_priority[i][1][1][1])
            arrival_time.insert(i, list_by_priority[i][1][1][0])

        for i in range(0, len(tat)):
            tattemp += tat[i]
            ganttchart.insert(i, tattemp)
            wait_temp = tattemp - arrival_time[i]
            wait_time.insert(i, wait_temp)

        print("tat:", tat)
        print("gantt chart", ganttchart)
        print("arrival :" , arrival_time)
        print("wait time", wait_time)
        print(list_arrival_burst_priority)

'''sched = CPU_SCHED()

print("FCFS")
arrival_and_burst = {"p1": [1, 8], "p4": [2, 5], "p3": [3, 2], "p5": [4, 3], "p2": [6, 6]}
sched.FCFS(arrival_and_burst)
print("TAT : ", sched.tat)
print("Gantt Chart : ", sched.forgantt)
print("arrival time : ", sched.arrival_time)
print("wait time : ", sched.wait_time)

print("PREEMPTIVE PRIORITY")
sched.PREEMPTIVE_PRIORITY()'''


