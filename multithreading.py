#mulitasking : 
#multithreading : multithreading is subset of multitasking
#multitasking is called multiple process in simontariously - like a OS -(operating system is simontariously process the) is open the python,chrome,youtupe,notepad,and watch movie etc...    

#normal function:
##def a():
##    count=0
##    while count<5:
##        print("function A")
##        count+=1
##
##def b():
##    count=0
##    while count<5:
##        print("function B")
##        count+=1
##a()
##b()

#thread program:
# two types of thread are there available:
# 1.kernal leval thread
# 2.user leval thread

#advantages of threads:
  # 1.performence is high
  # 2.Time is saving

# multithreading program:
import _thread
#import time
def a(msg):
    count=0
    while count<5:
        count+=1
        #time.sleep(3)
        print(msg)

def b(msg):
    count=0
    while count<5:
        count+=1
        #time.sleep(5)
        print(msg)
try:
    _thread_start_new_thread(a,("thread 1"))
    _thread_start_new_thread(b,("thread 2"))
except:
    pass
   # print("first thread is error")
while 1:
    pass
