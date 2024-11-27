def log_dec(func):
    def wrapper(*args):
        result=func(*args)
        with open('log.txt','a')as file:
            file.write(f"Called function {func.__name__} result is {result} \n")
            return result
    return wrapper

@log_dec
def hello():
    print("Hello World")
    return "Hi"
@log_dec
def sum(a,b):
    return a+b

hello()
sum(1,3)