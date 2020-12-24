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
        self.trueSequence = []
        self.arrival_time = []
        self.arrival_time.insert(0, list_arrival_and_burst[0][1][0])
        self.trueSequence.append(1)

        for i in range(1, len(list_arrival_and_burst)):
            self.tat.insert(i, list_arrival_and_burst[i][1][1])
            self.arrival_time.insert(i,  list_arrival_and_burst[i][1][0])
            self.trueSequence.append(i+1)


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
        arrival_burst_priority = {"p1": [0, 4, 1], "p4": [1, 8, 3], "p3": [2, 2, 2], "p5": [3, 4, 4], "p2": [4, 6, 5]}
        print(arrival_burst_priority)
        list_arr_burst_pri = list(arrival_burst_priority.items())

        self.list_by_priority = [] #dictionary that will hold the sorted process by priority
        sequence = 0
        temp_i_burst = 0
        temp_j_burst = 0

        #sorting by priority using selection sort algorithm
        for i in range(len(list_arr_burst_pri)):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(list_arr_burst_pri)):
                if list_arr_burst_pri[i][1][2] > list_arr_burst_pri[j][1][2]:
                    min_idx = j
                    temp_j_burst = list_arr_burst_pri[j][1][1]
                    self.list_by_priority.append([list_arr_burst_pri[i][0],list_arr_burst_pri[i][1][0],temp_j_burst,list_arr_burst_pri[i][1][2]])

            self.list_by_priority.append([list_arr_burst_pri[min_idx][0],
                                          list_arr_burst_pri[min_idx][1][0],list_arr_burst_pri[min_idx][1][1],
                                          list_arr_burst_pri[min_idx][1][2]])
            list_arr_burst_pri[i], list_arr_burst_pri[min_idx] = list_arr_burst_pri[min_idx], list_arr_burst_pri[i]

        self.tat = []
        ganttchart = []
        self.wait_time = []
        self.arrival_time = []
        tattemp=0
        self.trueSequence = []

        for i in range(len(self.list_by_priority)):
            for j in range(i+1, len(self.list_by_priority)):
                if self.list_by_priority[i][0] == self.list_by_priority[j][0]:
                    remaining_burst = self.list_by_priority[j][2] - self.list_by_priority[i][2]
                    self.list_by_priority[j][2] = remaining_burst
            self.trueSequence.append(self.list_by_priority[i][0][1])

        self.tat.insert(0, self.list_by_priority[0][1] + self.list_by_priority[0][2])
        self.arrival_time.insert(0, self.list_by_priority[0][1])
        for i in range(1, len(self.list_by_priority)):
            self.tat.insert(i, self.list_by_priority[i][2])
            self.arrival_time.insert(i, self.list_by_priority[i][1])

        for i in range(0, len(self.tat)):
            tattemp += self.tat[i]
            ganttchart.insert(i, tattemp)
            wait_temp = tattemp - self.arrival_time[i]
            self.wait_time.insert(i, wait_temp)

        print(self.list_by_priority)
        print(self.trueSequence)