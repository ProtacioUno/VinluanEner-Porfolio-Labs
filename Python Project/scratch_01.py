ask = input(" check if guamagaga tong hayop nato: ").lower()

yes = ["yes" , 'Y', "y", 'Oo', "yes" , "oo nga", "yep", "Yep"] 

yess = [item.lower() for item in yes]
#
# print(yess)

if ask in yess :
	print("valid")
	print(ask)
else : 
	print("invalid")
	print(ask)