'''
Created on 2018年11月30日

@author: cy
'''
import threading, random, time

a = 10

total = times = 0
gcondition = threading.Condition()

def producer():
    global total, gcondition, times
    while True:
        gcondition.acquire()
        money = random.randint(100, 1000)
        if times > a:
            gcondition.notify_all()
            gcondition.release()
            time.sleep(0.5)
            print('produce {} times...'.format(str(a)))
            return 
        total += money
        print('当前存入 {} 元， 剩余 {} 元'.format(str(money), str(total)))
        times += 1
        gcondition.notify_all()
        gcondition.release()   
        time.sleep(0.5)         

def consumer():
    global total, gcondition, times
    while True:
        gcondition.acquire()
        money = random.randint(100, 1000)
        if times > a:
            gcondition.release()
            return 
        while total < money:
            if times > a:
                gcondition.release()
                return 
            print('准备取 {} 元， 剩余 {} 元, 余额不足'.format(str(money), str(total)))
            gcondition.wait()
        total -= money
        print('当前取出 {} 元， 剩余 {} 元'.format(str(money), str(total)))
        gcondition.release()
        time.sleep(0.5)

thread_produce = threading.Thread(target=producer)
thread_consumer = threading.Thread(target=consumer)

thread_produce.start()
thread_consumer.start()

thread_produce.join()
thread_consumer.join()

