import platform
import cpuinfo
#info
def info ():
    print("""                 
Live info 0.2.2                          
-------------                              
Architecture: %s            
Processor: %s 
Node: %s  
System: %s 
Kernel: %s
CPU: %s
Python-build: %s 
Python-compiler: %s     

""" % (
    platform.machine(),
    platform.processor(),
    platform.node(),
    platform.system(),
    platform.release(),
    cpuinfo.get_cpu_info()['brand_raw'],
    platform.python_build(),
    platform.python_compiler(),

))
    
info()
#logo
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

    
    if platform.system()=="Darwin":
        print("""
______                    _       
|  _  \                  (_)      
| | | |__ _ _ ____      ___ _ __  
| | | / _` | '__\ \ /\ / / | '_ \ 
| |/ / (_| | |   \ V  V /| | | | |
|___/ \__,_|_|    \_/\_/ |_|_| |_|
                                    
                   """)

    if platform.system()=="Java":
        print("""
   ___                  
  |_  |                 
    | | __ ___   ____ _ 
    | |/ _` \ \ / / _` |
/\__/ / (_| |\ V / (_| |
\____/ \__,_| \_/ \__,_|
                        
                        """)

logo()









    
 
    
    
    




    

    
    
    
