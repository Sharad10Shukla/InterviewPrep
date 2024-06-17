#Observer pattern defines relationship between one-to-many dependency object such that when state of one object changes
# other are notified.
#e.g like notfication service, subscribe service , cricbuzz, weather station

from abc import ABC, abstractmethod
from observer_pattern_observer import Observer
class WeatherObservable(ABC):
    observer_list = []
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


class Dooordarshan(WeatherObservable):
    def __init__(self):
        pass

    def add(self,obj: Observer):
        self.observer_list.append(obj)

    def remove(self,obj: Observer):
        self.observer_list.remove(obj)

    def notify(self,msg):
        for observer in self.observer_list:
            observer.update(msg)

    def setdata(self,msg):
        if msg :
            self.notify(msg)



def Controller():
    from observer_pattern_observer import Television, Radio
    observable = Dooordarshan()
    teleobserver = Television(observable)
    radioObserver = Radio(observable)
    observable.add(teleobserver)
    observable.add(radioObserver)
    observable.setdata("Overcast weather conditons")

if __name__ == '__main__':
    Controller()



