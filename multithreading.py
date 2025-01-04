#mulitasking : 
#multithreading : multithreading is subset of multitasking
#multitasking is called multiple process in simontariously - like a OS -(operating system is simontariously process the) is open the python,chrome,youtupe,notepad,and
##watch movie etc...    

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
# import _thread
# #import time
# def a(msg):
#     count=0
#     while count<5:
#         count+=1
#         #time.sleep(3)
#         print(msg)

# def b(msg):
#     count=0
#     while count<5:
#         count+=1
#         #time.sleep(5)
#         print(msg)
# try:
#     _thread_start_new_thread(a,("thread 1"))
#     _thread_start_new_thread(b,("thread 2"))
# except:
#     pass
#    # print("first thread is error")
# while 1:
#     pass

import threading
import time
def threads():
    n=0
    while True:
        print("First Thread is running")
        time.sleep(4)

def threds1():
  # print("The join() purpose because, join() is one function execute until not exit this function before complete that function.")
  for i in range(5):
    print(i)
    time.sleep(2)        
thr=threading.Thread(target=threads,daemon=True)

thr2=threading.Thread(target=threds1,daemon=True)
thr.start()


time.sleep(5)



print("Out of thread.....")