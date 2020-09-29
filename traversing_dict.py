"""
This function will traverse the all keys in a dictionary, irrespective of their location or level. and return all the keys.

"""

def my_dict(x):
   if isinstance(x,dict):
       for key,val in x.items():
           if isinstance(val,dict):
               print(key)
               my_dict(val)
           elif isinstance(val,list):
                   print(key)
                   my_dict(val)
           else:
               print(key)        
   elif isinstance(x,list):
       for i in x:
           if isinstance(i,dict):
               my_dict(i)

       
my_dict(d_or_l)
