'''
Created on 2018年11月16日

@author: cy
'''
import threading, random, time

gMoney = 1000
gLock = threading.Lock()
#记录生产者生产的次数 10后就不在生产
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gTimes
        
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            print('%s 当前存入 %s 元钱，剩余 % s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            time.sleep(0.5)
            gLock.release()
        
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gTimes
        
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney > money:
                gMoney -= money
                print('%s 当前取出 %s 元钱，剩余 %s 元钱' % (threading.current_thread(), money, gMoney))
                time.sleep(0.5)
            else:
                # 如果钱不够了，有可能是已经超过了次数，这时候就判断一下
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s 当前想取 %s 元钱，剩余 %s 元钱，不足！" % (threading.current_thread(),money,gMoney))
            gLock.release()
        
def main():
    for x in range(5):
        Consumer(name='消费者线程%d'%x).start()

    for x in range(5):
        Producer(name='生产者线程%d'%x).start()

if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        