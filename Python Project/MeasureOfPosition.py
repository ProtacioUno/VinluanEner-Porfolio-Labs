



dataset = [1 ,28  , 12  , 13 , 19  , 46, 16 , 10 , 21 ,25 , 37 ,  7 ,14 , 32 ,17 , 1, 9 , 22, 12 , 5 , 15 ,24 , 3 , 30 , 43 , 35 ]  

sorting = sorted(dataset)

print(sorting)
print("\n ")

print(len(sorting))

print("\n \n ")



DK_list = [1 , 5, 7, 4 , 6 , 3]


# print(len(dataset))
 
if not DK_list == [] :
	print("it meron \n\n") 

	def decile(i) :
		answer = (i * (len(dataset) + 1)) / 10	

		print(f"the decile of {i}  are in index of : {answer}    \t value : {sorting[int (round(answer,0))-1]}")
		
	for x in range(len(DK_list)):
		decile(DK_list[x])

else :
	print("the decile list was empty ") 
	

PK_list = [1 ,  50 , 20,  40 , 20 , 69 , 20 ]


if not PK_list == [] :
	print("it meron \n\n") 

	def percentile(i) :
		answer = (i * (len(dataset) + 1)) / 100	
		print(f"the percentile of {i} are in index of : {answer}       \tvalue : {sorting[int (round(answer,0))-1]}")
		
	for x in range(len(PK_list)):
		percentile(PK_list[x])

else :
	print("the percentile list was empty ") 
	