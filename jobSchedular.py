"""
implement a job schedular which takes in a function f and an integer n, and calls f after n ms
"""


from time import sleep
val =1
def hello_job_schedular():
	global val
	print("schedular runned {} time".format(val))
	val+=1

def schedular(f, delayMS):
	delayS = delayMS /1000
	sleep(delayS)
	f()
	schedular(f,delayMS)
	
schedular(hello_job_schedular, 1000)