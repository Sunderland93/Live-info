import platform

def info ():
    print("""
Live info 0.2
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
    
info()


def logo ():
    if platform.system()=="Linux":
        print ("""
    __    _                 
   / /   (_)___  __  ___  __
  / /   / / __ \/ / / / |/_/
 / /___/ / / / / /_/ />  <  
/_____/_/_/ /_/\__,_/_/|_|  
                            """)


    if platform.system()=="Windows":
       print("""                                         
          _       _________  
__      _(_)_ __ |___ /___ \ 
\ \ /\ / / | '_ \  |_ \ __) |
 \ V  V /| | | | |___) / __/ 
  \_/\_/ |_|_| |_|____/_____|
                             
                                          """)


    if platform.system()=="Unix":
        print("""
              _           
             (_)     
  _   _ _ __  ___  __
 | | | | '_ \| \ \/ /
 | |_| | | | | |>  < 
  \__,_|_| |_|_/_/\_\
                     
                      """)

    
    if platform.system()=="MacOs":
        print("""

    __  ___              ____      
   /  |/  /___ ______   / __ \_____
  / /|_/ / __ `/ ___/  / / / / ___/
 / /  / / /_/ / /__   / /_/ (__  ) 
/_/  /_/\__,_/\___/   \____/____/  
                                   
                                 
                   """)

logo()








    
 
    
    
    




    

    
    
    
