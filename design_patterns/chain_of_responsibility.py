#

from abc import ABC, abstractmethod
class loggerInterface(ABC):
    _next_handler = None
    @abstractmethod
    def set_handler(self,handler):
     pass


    @abstractmethod
    def handle(self, request:str):
        pass

class Logger(loggerInterface):
    _next_handler = None

    def set_handler(self, handler):
        self._next_handler = handler

    def handle(self, request: str):
        if self._next_handler is not None:
             self._next_handler.handle(request)


class InfoLogger(Logger):

    def handle(self, request: str):
        if request == 'info':
            print("Info log !")
        else:
            print("not a info log !")
            super().handle(request)

class DebugLogger(Logger):

    def handle(self, request: str):
        if request == 'debug':
            print("Debug log !")
        else:
            print("not a debug log !")
            super().handle(request)

class ErrorLogger(Logger):

    def handle(self, request: str):
        if request == 'error':
            print("Error log !")
        else:
            print("not a error log !")
            super().handle(request)

if __name__ == '__main__':
    info = InfoLogger()
    debug = DebugLogger()
    error = ErrorLogger()
    error.set_handler(debug)
    debug.set_handler(info)
    error.handle('info')
    error.handle('debug')