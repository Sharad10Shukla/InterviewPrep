from abc import ABC, abstractmethod
class Actor:
    x = None
    def __init__(self, x):
        self.x = x
    def set_state(self, y):
        self.x = y

class State(ABC):

    @abstractmethod
    def perform_action1(self):
        pass
    @abstractmethod
    def perform_action2(self):
        pass
    @abstractmethod
    def perform_action2(self):
        pass

class Idle(State):
    def perform_action1(self):
        print("action 1 performed")

    def perform_action2(self):
        print("function not supported")

class Running(State):
    def perform_action1(self):
        print("function not supported")
    def perform_action2(self):
        print("action 2 performed")

if __name__ == '__main__':
    idle = Idle()
    run = Running()
    actor_obj = Actor(idle)
    actor_obj.x.perform_action1()
    actor_obj.x.perform_action2()
    actor_obj.set_state(run)
    actor_obj.x.perform_action1()
    actor_obj.x.perform_action2()


