#Observer pattern defines relationship between one-to-many dependency object such that when state of one object changes
# other are notified.
#e.g like notfication service, subscribe service , cricbuzz, weather station

from abc import ABC, abstractmethod
from typing import List
from observer_pattern_observer import Observer
import time
class WeatherObservable(ABC):
    observer_list: List[Observer] = []
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setdata(self):
        pass

    @abstractmethod
    def getdata(self):
        pass


class Dooordarshan(WeatherObservable):
    def __init__(self):
        self.data = None

    def add(self,obj: Observer):
        self.observer_list.append(obj)

    def remove(self,obj: Observer):
        self.observer_list.remove(obj)

    def notify(self):
        for observer in self.observer_list:
            observer.update()

    def setdata(self,val):
        if val :
            self.data = val
            self.notify()
    def getdata(self):
        return self.data




def Controller():
    from observer_pattern_observer import Television, Radio
    observable = Dooordarshan()
    teleobserver = Television(observable)
    radioObserver = Radio(observable)
    observable.add(teleobserver)
    observable.add(radioObserver)
    temp = 20
    while(1):
        observable.setdata(temp)
        temp+=1
        time.sleep(10)

if __name__ == '__main__':
    Controller()



