
# Calculates various measures of position, also known as measures of relative standing, within a dataset of this field : 

## note : You can change this dataset

dataset = [1 ,28  , 12  , 13 , 19  , 46, 16 , 10 , 21 ,25 , 37 ,  7 ,14 , 32 ,17 , 1, 9 , 22, 12 , 5 , 15 ,24 , 3 , 30 , 43 , 35 ]  

sorting = sorted(dataset)

print("\n \t Sorted Dataset given : ")
print(sorting)
print("\n ")
print(f"The n of Dataset given : {len(sorting)}")
# print("\n ")



#--------------------------------------------

## this list can be change depends on list of "K" in Quartile, Decile or Percentile

# for example 
# QK_list = [3, 1] are the same as ( Q3 and Q1 ) 

QK_list = [3, 1]
DK_list = [1 , 5, 7, 4 , 6 , 3]
PK_list = [1 ,  50 , 20,  40 , 20 , 69 , 20 ,4 ,5]

# ----------------------------------------
 
if not QK_list == [] :
	# validation if qk has list of quartiles
	print("\n\n\t has quartile list ... \n") 

	def quartile(i) :
		answer = (i * (len(dataset) + 1)) / 10	

		print(f"the quartile of {i}  are in index position of : {answer}    \t value : {sorting[int (round(answer,0))-1]}")
		
	for x in range(len(QK_list)):
		quartile(QK_list[x])
else :
	print("\t the Quartile list was empty \n\n") 


#--------------------------------



# print(len(dataset))


 
if not DK_list == [] :
	print("\n\n\t has decile list ... \n") 

	def decile(i) :
		answer = (i * (len(dataset) + 1)) / 10	

		print(f"the decile of {i}  are in index position of : {answer}    \t value : {sorting[int (round(answer,0))-1]}")
		
	for x in range(len(DK_list)):
		decile(DK_list[x])

else :
	print("\t the decile list was empty ") 
	
#-------------------------------------



if not PK_list == [] :
	print("\n\n\t has percentile list ... \n") 

	def percentile(i) :
		answer = (i * (len(dataset) + 1)) / 100	
		print(f"the percentile of {i} are in index of : {answer}   \tvalue : {sorting[int (round(answer,0))-1]}")
		
	for x in range(len(PK_list)):
		percentile(PK_list[x])

else :
	print("\t the percentile list was empty ") 
	

# This Python code was create by Vinluen Ener
# This Python code was create by Vinluen Ener

