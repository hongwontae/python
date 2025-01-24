import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

n1 = 0
n2 = 0

def speed_calc_decorator(func):
    def wrapper_function () :
        func()
        global n1
        n1 = time.time()
    return wrapper_function
  
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

def print_func() :
    print(n1)
    print(n2)
    print(n1-n2)


fast_function()
slow_function()
print_func()
