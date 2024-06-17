#Observer pattern defines relationship between one-to-many dependency object such that when state of one object changes other are notified.
#e.g like notfication service, subscribe service , cricbuzz, weather station

from abc import ABC, abstractmethod
class Observer(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass



class Television(Observer):
    from observer_pattern_observable import WeatherObservable

    def __init__(self,observable: WeatherObservable):
        self.observable = observable


    def update(self,msg) -> None:
        print("Television Event notified with message: {}".format(msg))

class Radio(Observer):
    from observer_pattern_observable import WeatherObservable

    def __init__(self,observable: WeatherObservable):
        self.observable = observable

    def update(self,msg) -> None:
        print("radio Event notified with message: {}".format(msg))




