
def decorator_prefix(prefix):
    def decorator(original_func):
        def wrapper(*args,**kwargs):
            print(prefix," : Exceuted before original function")
            result = original_func(*args,**kwargs)
            print(prefix," : Exceuted after original function")
            return result
        return wrapper
    return decorator

@decorator_prefix("LOG")
def display_info(name,age):
    print(name,age)

display_info("ajay",21)