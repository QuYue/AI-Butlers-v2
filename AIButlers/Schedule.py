# -*- encoding: utf-8 -*-
'''
@Time     :   2023/02/23 11:54:50
@Author   :   QuYue
@File     :   Schedule.py
@Email    :   quyue1541@gmail.com
@Desc:    :   Schedule
'''
#%% Import Packages
# Basic
import schedule
import time
import datetime
import threading

# Modules

# Add Path
if __package__ is None:
    import os
    import sys
    os.chdir(os.path.dirname(__file__))
    sys.path.append("..")

# Self-defined
import utils

#%% Classes
class ScheduleTasker():
    def __init__(self, refresh=60*1):
        self.refresh = refresh
        self.jobs = dict()
        self.time = 0

    def run_threaded(self, job_func, *args):
        job_thread = threading.Thread(target=job_func, args=args)
        job_thread.start()
        
    def create_second_task(self, job_func, seconds=5, *args):
        job = schedule.every(seconds).seconds.do(self.run_threaded, job_func, *args)

    def create_day_task(self, job_func, clock="00:00", *args):
        job = schedule.every().day.at(clock).do(self.run_threaded, job_func, *args)
    
    def create_limited_second_task(self, job_func, seconds=5, times=1, *args):
        task_id = self.__get_task_id(times)
        job = schedule.every(seconds).seconds.do(self.run_threaded, self.__limited_job_func, task_id, job_func, *args)
        self.jobs[task_id]['job'] = job

    def create_limited_day_task(self, job_func, clock="00:00", times=1, *args):
        task_id = self.__get_task_id(times)
        job = schedule.every().day.at(clock).do(self.run_threaded, self.__limited_job_func, task_id, job_func, *args)
        self.jobs[task_id]['job'] = job

    def hello(self):
        print('hello')

    def __run__(self):
        i=0
        while True:
            # schedule
            schedule.run_pending()
            time.sleep(self.refresh)
            print(datetime.datetime.now())

    def run(self):
        self.run_threaded(self.__run__)
    
    def __count(self, task_id):
        if task_id in self.jobs:
            max_time = self.jobs[task_id]['max_time']
            self.jobs[task_id]['time']+=1
            now_time = self.jobs[task_id]['time']
            if now_time >= max_time:
                job = self.jobs[task_id]['job']
                self.jobs.pop(task_id)
                schedule.cancel_job(job)
                # print(f"Cancel Job {task_id}")

    def __limited_job_func(self, task_id, job_func, *args):
        job_func(*args)
        self.__count(task_id)

    def __get_task_id(self, times=1):
        task_id = 0
        while True:
            if task_id not in self.jobs:
                self.jobs[task_id] = {'max_time': times, 'time': 0}
                break
            else:
                task_id += 1
        return task_id

#%% Main Function
if __name__ == "__main__":
    def hello(a,b):
        print(a,b)

    tasker = ScheduleTasker(1)
    # tasker.create_day_task(hello, "16:25", 1,2)
    tasker.create_second_task(hello, 3,1,2)
    # tasker.create_limited_second_task(hello, 10, 1, 3,4)
    # tasker.create_limited_day_task(hello, "16:25", 1, 3, 4)
    tasker.run()
    print("Starting")

    




