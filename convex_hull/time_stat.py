#coding=utf8

import time
from matplotlib import pyplot as plot

class TimeStat(object) :
    def __init__(self) :
        self.pnt_nums = []
        self.bruteforce_time_cost = []
        self.grahamscan_time_cost = []
        self.dc_time_cost = []
        self.start_time = 0
        self.end_time = 0

    def add_stat_pnt_num(self , pnt_num) :
        self.pnt_nums.append(pnt_num)

    def add_stat_brute_force_timecost(self , t) :
        self.bruteforce_time_cost.append(t)

    def add_stat_graham_scan_timecost(self , t) :
        self.grahamscan_time_cost.append(t)

    def add_stat_dc_timecost(self , t) :
        self.dc_time_cost.append(t)

    def start_time_stat(self) :
        self.start_time =  time.time()
        return self.start_time 

    def end_time_stat(self) :
        self.end_time = time.time()
        return self.end_time

    def get_time_cost(self) :
        return self.end_time - self.start_time

    def clear_time_stat(self) :
        self.start_time = 0 
        self.end_time = 0
        self.bruteforce_time_cost = []
        self.grahamscan_time_cost = []
        self.dc_time_cost = []
        self.pnt_nums = []

    def print_time_cost(self) :
        stat_cnt = len(self.pnt_nums)
        header_line = " ".join([ "{method_name:20}" ] + [ "| {pnt_nums_str[%d]:20}" %i for i in range(stat_cnt) ])
        formated_line = " ".join([ "{left_header:20}" ] + [ "| {time_cost[%d]:20.2f}" %i for i in range(stat_cnt) ])
        method_name = "method-name"
        pnt_nums_str = ["pnt-nums=%d" %(d) for d in self.pnt_nums ]
        print header_line.format(**locals())
        left_header = "brute-force"
        time_cost = self.bruteforce_time_cost
        print formated_line.format(**locals())

        left_header = "graham scan"
        time_cost = self.grahamscan_time_cost
        print formated_line.format(**locals())

        left_header = "divide conquer"
        time_cost = self.dc_time_cost
        print formated_line.format(**locals())

    def draw_stat(self , config={}) :
        figure_title = config.get('title' , "Time Cost Statistics in different dataset with different algorithm")
        plot.figure(figure_title)  
        plot.suptitle(figure_title , fontsize=16)

        # x-axis is the pnt-nums
        x_values = self.pnt_nums 

        # y-aixs is the time cost of different algorithm
        plot.plot(x_values , self.bruteforce_time_cost , 'mo-' , label="burte force")
        plot.plot(x_values , self.grahamscan_time_cost , 'gx-' , label="graham scan")
        plot.plot(x_values , self.dc_time_cost , 'k+-' , label="divide conquer")

        x_label = config.get('x_label' , 'Pnt Num')
        y_label = config.get('y_label' , 'Time Cost / (secondes)')
        plot.xlabel(x_label)
        plot.ylabel(y_label)
        plot.legend()
        #plot.show() # `show` is a blockint function ! we call it after all have been drawed  