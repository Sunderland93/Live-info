import platform
print("""
Live info 1.0
-------------
Machine: %s 
Architecture: %s  
Processor: %s 
Node: %s  
System: %s 
Kernel: %s 
Python-build: %s 
Python-compiler: %s

""" % (
    platform.machine(),
    platform.architecture(),
    platform.processor(),
    platform.node(),
    platform.system(),
    platform.release(),
    platform.python_build(),
    platform.python_compiler(),

))
    
    









