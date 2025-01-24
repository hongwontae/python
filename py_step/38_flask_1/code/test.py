import time;

def delay_decorator(func) :
    def wrapper_func() :
        time.sleep(2)
        func()
    return wrapper_func

@delay_decorator
def say_hello () :
    print('hello')

say_hello()
