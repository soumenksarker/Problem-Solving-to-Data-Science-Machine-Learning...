from Queue import Queue
import random

class car_wash:
    def __init__(self,wpm):
        self.wash_rate = wpm
        self.current_wash = None
        self.time_remaining = 0
    def tick(self):
        if self.current_wash != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_wash = None
    def busy(self):
        if self.current_wash != None:
            return True
        else:
            return False
    def startNext(self, new_wash):
        self.current_wash = new_wash
        self.time_remaining = new_wash.get_wash()*60 / self.wash_rate
        
class Wash:
    def __init__(self, time):
        self.timestamp = time
        self.washes = random.randrange(1,2)
    def get_stamp(self):
        return self.timestamp
    def get_wash(self):
        return self.washes
    def wait_time(self, current_time):
        return current_time - self.timestamp
    
    
        
def simulation(num_seconds, wash_per_minute):
    Car_wash = car_wash(wash_per_minute)
    wash_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if new_car_wash():
            wash = Wash(current_second)
            wash_queue.enqueue(wash)
        if (not Car_wash.busy() and (not wash_queue.is_empty())):
            next_wash = wash_queue.dequeue()
            waiting_times.append(next_wash.wait_time(current_second))
            Car_wash.startNext(next_wash)
            
        Car_wash.tick()
        
    average_wait = (sum(waiting_times)/len(waiting_times))/60
    print("Average_wait %6.2f minutes and %3d wash remainig"%(average_wait,wash_queue.size()))
def new_car_wash():
    num = random.randrange(1,217)
    if num == 216:
        return True
    else:
        return False
for i in range(10):
    simulation(43200,4/10)
