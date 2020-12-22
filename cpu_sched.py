import sys
from itertools import groupby
from operator import itemgetter

class Algo():
    def __init__(self):
        super().__init__()

    def FCFS(self, params):
        #assuming all process passed in here are already in ordered
        arrival_and_burst = params
        list_arrival_and_burst = params  #list(arrival_and_burst.items())
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

        self.wait_time[0] = 0 #update position 0 to 0 waiting time

    def PREEMPTIVE_PRIORITY(self):
        #assumption : already sorted by arrival time
        arrival_burst_priority = {"p1": [0, 8, 1], "p4": [1, 5, 3], "p3": [2, 2, 2], "p5": [3, 3, 4], "p2": [4, 6, 5]}
        self.list_arr_burst_pri = list(arrival_burst_priority.items())
        list_by_priority = {} #dictionary that will hold the sorted process by priority
        sequence = 0
        #sorting by priority using selection sort
        # algorithm
        #print(list_arrival_burst_priority[0][1][2])
        print(self.list_arr_burst_pri)
        for i in range(len(self.list_arr_burst_pri)):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            sequence += 1 #serves as key of the "by_priority" dict variable
            for j in range(i + 1, len(self.list_arr_burst_pri)):
                if self.list_arr_burst_pri[i][1][2] > self.list_arr_burst_pri[j][1][2]:
                    min_idx = j
                    list_by_priority[sequence] = self.list_arr_burst_pri[i]
                    sequence += 1
                    list_by_priority[sequence] = self.list_arr_burst_pri[min_idx]
                    remaining_burst = self.list_arr_burst_pri[i][1][1] - self.list_arr_burst_pri[min_idx][1][1]
                    self.list_arr_burst_pri[i][1][1] = remaining_burst

            list_by_priority[sequence] = self.list_arr_burst_pri[min_idx]
            self.list_arr_burst_pri[i], self.list_arr_burst_pri[min_idx] = self.list_arr_burst_pri[min_idx], self.list_arr_burst_pri[i]

        self.tat = []
        ganttchart = []
        wait_time = []
        self.arrival_time = []
        tattemp=0
        print(list_by_priority)
        list_by_priority = list(list_by_priority.items())
        #print(list_by_priority[0][1][1][1]) #burst position
        self.tat.insert(0, list_by_priority[0][1][1][1] + list_by_priority[0][1][1][0])
        self.arrival_time.insert(0, list_by_priority[0][1][1][0])
        for i in range(1, len(list_by_priority)):
            self.tat.insert(i, list_by_priority[i][1][1][1])
            self.arrival_time.insert(i, list_by_priority[i][1][1][0])

        for i in range(0, len(self.tat)):
            tattemp += self.tat[i]
            ganttchart.insert(i, tattemp)
            wait_temp = tattemp - self.arrival_time[i]
            wait_time.insert(i, wait_temp)

        '''print("tat:", self.tat)
        print("gantt chart", ganttchart)
        print("arrival :" , self.arrival_time)
        print("wait time", wait_time)
        print(self.list_arr_burst_pri)'''


