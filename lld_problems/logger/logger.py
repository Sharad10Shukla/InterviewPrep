# Design a logger,ATM,Vending Machine
# Using Chain Responsibility principle

from abc import ABC, abstractmethod
class Logger(ABC):
    def __init__(self, next_logger):
        self.logger  = next_logger

    @abstractmethod
    def log(self,log_level):
        if self.logger is not None:
            self.logger.log(log_level)


class InfoLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self,log_level):
        if log_level == 'info':
            print("Info log .")
        else:
            print("not a info log .")
            super().log(log_level)


class DebugLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level):
        if log_level == 'debug':
            print("Debug log .")
        else:
            print("not a debug log .")
            super().log(log_level)

class ErrorLogger(Logger):
    def __init__(self, next_logger):
        super().__init__(next_logger)

    def log(self, log_level):
        if log_level == 'error':
            print("ERROR log .")
        else:
            print("not a error log .")
            super().log(log_level)

class LoggerHandler():
    def main(self):
        log_obj = InfoLogger(DebugLogger(ErrorLogger(None)))
        log_obj.log('error')

if __name__ == '__main__':
    LoggerHandler().main()




