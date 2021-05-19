from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = Lock()
        self.b = Lock()
        self.b.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.f.acquire()
            printFoo()
            self.b.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.b.acquire()
            printBar()
            self.f.release()
