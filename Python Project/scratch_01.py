# ask = input(" check if guamagaga tong hayop nato: ").lower()

# yes = ["yes" , 'Y', "y", 'Oo', "yes" , "oo nga", "yep", "Yep"] 

# yess = [item.lower() for item in yes]
# #
# # print(yess)

# if ask in yess :
# 	print("valid")
# 	print(ask)
# else : 
# 	print("invalid")
# 	print(ask)


import numpy as np


heyt = [3 ,5 ,2 ]
weyt = [1 ,2 ,3 ]
np_heyt = np.array(heyt)
np_weyt = np.array(weyt)

tayms_heyt  = np_heyt  / weyt 

print(tayms_heyt)

# print(tayms_heyt)
# print(np_heyt)

