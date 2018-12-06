'''
Created on 2018年11月16日

@author: cy

threading.Condition类似threading.Lock，可以在修改全局数据的时候进行上锁，也可以在修改完毕后进行解锁。以下将一些常用的函数做个简单的介绍：

    acquire：上锁。
    release：解锁。
    wait：将当前线程处于等待状态，并且会释放锁。可以被其他线程使用notify和notify_all函数唤醒。被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
    notify：通知某个正在等待的线程，默认是第1个等待的线程。
    notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用。


'''
import threading, random, time

gMoney = 1000
gCondition = threading.Condition()
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        global gTimes
        
        while True:
            gCondition.acquire()
            money = random.randint(100, 1000)
            if gTimes >= 10:
                gCondition.release()
                print('当前生产者总共生产了 %s 次'%gTimes)
                return
            gMoney += money
            print('%s 当前存入 %s 元钱，剩余 % s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gCondition.notify_all()
            time.sleep(0.5)
            gCondition.release()
    
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        global gTimes
        
        while True:
            gCondition.acquire()
            money = random.randint(100, 1000)
            while gMoney < money:
                if gTimes >= 10:
                    gCondition.release()
                    return
                print('%s 准备取 %s 元钱，剩余 %s 元钱，不足！'%(threading.current_thread(),money,gMoney))
                gCondition.wait()
                print(gMoney, money)
            gMoney -= money
            print('%s 当前取出 %s 元钱，剩余 %s 元钱' % (threading.current_thread(), money, gMoney))
            time.sleep(0.5)
            gCondition.release()

def main():
    for x in range(5):
        Consumer(name='消费者线程%d'%x).start()

    for x in range(2):
        Producer(name='生产者线程%d'%x).start()

if __name__ == '__main__':
    main()
            
        
        
        
        
        
        
        
        
        
        