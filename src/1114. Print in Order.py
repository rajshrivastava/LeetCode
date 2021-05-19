from threading import Lock
class Foo:
    def __init__(self):
        self.l2 = Lock()
        self.l3 = Lock()
        self.l2.acquire()
        self.l3.acquire()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l2.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.l2:
            printSecond()
        
        self.l3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        with self.l3:
            printThird()
        
