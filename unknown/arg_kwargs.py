
def args_example(*args):
    print(f'* args type = {type(args)}')
    for arg in args:
        print(f"*args element: {arg}")
    

def kwargs_example(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"**kwargs elements\tkey = {key}\tvalue = {value}")   



if __name__ == "__main__":	
    print("*args example")
    args_example("deneme", 'aziz', 'python', 3.7 )
    print("**kwargs example")
    kwargs_example(name="Aziz", job="Developer", country="TR", hobbies="Football" )
    
    
