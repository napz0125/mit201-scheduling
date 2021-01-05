import sys
from itertools import groupby
from operator import itemgetter
import process

class Algo():
    def __init__(self):
        super().__init__()

    def FCFS(self, params):
        #All processed in here are already in ordered by arrival time
        process_by_AT = params

        self.tat = []
        self.tat.insert(0, process_by_AT[0].arrival_time + process_by_AT[0].burst_time)
        self.trueSequence = []
        self.arrival_time = []
        self.arrival_time.insert(0, process_by_AT[0].arrival_time)

        for i in range(1, len(process_by_AT)):
            self.tat.insert(i, process_by_AT[i].burst_time)
            self.arrival_time.insert(i,  process_by_AT[i].arrival_time)

        for i in range(len(process_by_AT)):
            self.trueSequence.append(process_by_AT[i].p_id)
            self.trueSequence.append(process_by_AT[i].p_id)

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

        print("tat %s, true sequence : %s" %(self.tat, self.trueSequence))

    def PREEMPTIVE_PRIORITY(self, params):

        processes = params
        gantt = []  # (,())

        # initialize
        total_waiting_time = 0
        total_turnaround_time = 0
        total_response_time = 0
        total_return_time = 0

        self.tat = []
        self.trueSequence = []
        self.arrival_time = []

        n = len(processes)

        # sort by arrival_time
        proc = sorted(processes, key=lambda proc: proc.arrival_time)

        response = []
        prev, st, ct = 0, 0, 0

        for i in range(n):
            response.append(False)

        def findWaitingTime(processes, n):

            rt = [0] * n

            # Copy the burst time into rt[]
            for i in range(n):
                rt[i] = processes[i].burst_time

            complete = 0
            t = 0
            short = 0

            ct = 1  # to count the time the process ran continously
            st = 0  # start time of that process
            # Process until all processes gets
            # completed
            while (complete != n):
                minp = 999999999
                # Find process with highest priority
                # time among the processes that
                # arrives till the current time`
                prev = short

                for j in range(n):
                    if ((processes[j].arrival_time <= t) and
                            (processes[j].priority < minp) and rt[j] > 0):
                        minp = processes[j].priority
                        short = j

                # if a process is preempted
                prev_id = ""
                if prev != short:

                    gantt_l = len(gantt)

                    if gantt_l > 0:
                        prev_id = gantt[gantt_l - 1][0]

                    if prev_id != processes[prev].p_id:
                        gantt.append(
                            (processes[prev].p_id, st, ct, processes[prev].turnaround_time, "preempted"))  # napsa
                    ct = 1
                    st = t
                else:
                    ct += 1

                # to calculate responce time || process ran for first time
                if (response[short] == False):
                    response[short] = True
                    processes[short].response_time = t - \
                                                     processes[short].arrival_time

                # Reduce remaining time by one
                rt[short] -= 1

                # If a process gets completely
                # executed
                if (rt[short] <= 0):
                    # Increment complete
                    complete += 1
                    prev_id = ""
                    if prev == short:
                        gantt_l = len(gantt)

                        if gantt_l > 0:
                            prev_id = gantt[gantt_l - 1][0]

                        if prev_id != processes[prev].p_id:
                            gantt.append((processes[prev].p_id, st, ct, processes[prev].turnaround_time, "completed"))  # napsa

                    # Find finish time of current
                    # process
                    fint = t + 1

                    # Calculate waiting time
                    processes[short].waiting_time = (
                            fint - processes[short].arrival_time - processes[short].burst_time)

                # Increment time
                t += 1

        def findTurnAroundTime(processes, n):
            processes[0].waiting_time = 0
            for i in range(n):
                processes[i].turnaround_time = processes[i].burst_time + \
                                               processes[i].waiting_time

        # setting initial values

        findWaitingTime(proc, n)
        # gantt.append((processes[prev].p_id, (st, ct)))

        findTurnAroundTime(proc, n)

        for i in range(0, n):
            proc[i].return_time = proc[i].arrival_time + proc[i].turnaround_time

        # calculate for next processes
        for i in range(1, len(proc)):
            # update total
            total_response_time += proc[i].response_time
            total_waiting_time += proc[i].waiting_time
            total_turnaround_time += proc[i].turnaround_time
            total_return_time += proc[i].burst_time

            # print(proc[i].arrival_time, proc[i].p_id, proc[i].priority, proc[i].burst_time)

        print(gantt)

        for i in range(len(gantt)):
            self.tat.append(gantt[i][2])
            self.trueSequence.append(gantt[i][0])
            self.arrival_time.append(gantt[i][1])

        print("tat", self.tat)
        print("true seq ", self.trueSequence)
