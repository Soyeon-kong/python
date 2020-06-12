class Car:
    company = ''
    size = ''
    def __init__(self, company, size):
        self.company = company
        self.size = size
    def __str__(self):
        return '차종은 '+self.company +', 크기는 '+self.size
    def fast(self):
        print('빠르다')
    def straight(self):
        print('직진하다')
        
class Truck:
    speed = 0
    color = ''

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    def __str__(self):
        return '속도는 '+str(self.speed)+', 색깔은 '+self.color
    
    def run(self):
        print('달리다')
    def stop(self):
        print('멈추다')

if __name__ == '__main__':
    car = Car('BMW','중형')
    print(car)
    car.fast()
    car.straight()

    truck = Truck(70,'파란색')
    print(truck)
    truck.run()
    truck.stop()