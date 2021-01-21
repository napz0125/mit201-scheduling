class Process:
    def __init__(self):
        self.p_id = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.priority = 0

        self.waiting_time = 0
        self.return_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completed = False