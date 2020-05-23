
def getDecorator(service):
    def header():
        print("this is header")
    def footer():
        print("this is footer")
    
    def decorator():
        header()
        service()
        footer()
    
    return decorator

# @ syntax create decorator for you with the given decorator
@getDecorator
def core_service():
    print("core operations")


# follwoing two lines are manual way to create and use decorator
# new_service = getDecorator(core_service)
#new_service()

#while using pi syntax its done automatically by python itself
core_service()


#decorator with arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")



greet("Bob")

help(greet)
