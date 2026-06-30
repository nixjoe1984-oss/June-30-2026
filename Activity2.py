class employee:
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making an object...")
    obj=employee()
    print("create_obj function ending...")
    return obj

print("Calling create_obj function")
obj=create_obj()
print("Program ends.")