

DK_list = [3 ,4, 6]

dataset = [1 ,2 , 3 ,7 , 9] 

# print(len(dataset))

def decile(i) :
	answer = (i * (len(dataset) + 1)) / 10	
	print(f"the decile one are : {answer}")
	
for x in range(len(DK_list)):
	decile(DK_list[x])

	