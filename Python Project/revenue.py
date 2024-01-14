
# def  cogs_def(revenue) : 
#     print("Your total" + revenue)
#     cogs = input("input cogs") 
#     gross_def(revenue, cogs)

# def gross_def(revenue, cogs) :
#     print(revenue) 
     
    # return revenue - cogs  


# INTRODUCTION 
# INTRODUCTION 

print("\n \t This mini project of This project explores the exciting possibilities that arise when Python is harnessed to address fundamental business problems")
print("\n \n") 

# print()

# FIRST VALIDATION 
# FIRST VALIDATION 
ask_revenue = input('Do you have Total Sales or Revenue ? \n ( yes / no )  : ').lower()



#------------------------------------------

# Second validation 
# Second validation 
def convert (): 
    while True : 
        try : 
            revenue = int(input("Input Total sales or revenue :")) 
            cogs = int(input("Input all cost of goods : "))               
            gross(cogs,revenue) 
            # grok() 
            break 
        except Exception as e: 
            print(e)
            print("something namo wronasdg change something")
        continue 
#------------------------------------------

def gross(cogs, revunue) :
    # print(type(cogs))
    print("-------------------------------------------- \n")
    
    print("The gross profit :") 
    print(f"Reveunue : {revunue} ,  cogs : {cogs} ")
    print(revunue - cogs)   
    
    
    
def revenue_sum(sums): 
    print("#----------------------------------------")
    revenue_sum = sum(sums)

    print(revenue_sum) 
    # print(type(revenue_sum))
    return revenue_sum
    # culated_rev(revenue_sum)

# def cogs_sum(sums):
#     print("#-----------------------")
#     revenue_sum 
# nonloc
# def culated_rev(revenue_sum) : 
    
    # print("it works")

    # print("gumana kaba")

#---------------------------------------------

quit_list = ['Q', 'q', 'quit', 'quits', 'Ayaw', 'enap', 'exit'] 
quit_list = [item.lower() for item in quit_list] 

yes = ["yes" , 'Y', "y", 'Oo', "yes" , "oo nga", "yep", "Yep"] 
yes = [item.lower() for item in yes]


if ask_revenue in yes :
    
    ask_cogs = input("\n Do you have cost of all goods ? ").lower().strip()
    
    if ask_cogs in yes : 
        convert() 
    else :    

        print("\n")

        cogs_list = []
        write_cogs = input("Type list of cogs category : ").lower().strip()
        cogs_list.append(write_cogs)
        print(cogs_list)
        while not write_cogs in quit_list : 
            print("if you to quit type (q)")
            write_cogs = input("Type more : ").lower().strip()
            if not write_cogs in quit_list : 
                cogs_list.append(write_cogs)
                
            print(cogs_list)        

        print("#---------------------------")
        print(cogs_list)
        print(len(cogs_list))   
        print("Define the value of of each cogs list") 
        print( " List : Value") 

        cogs_values = []
        for x in range(len(cogs_list)) : 
            while True : 
                try : 
                    conglest = int(input(f"{cogs_list[x]} : " ))  
                    cogs_values.append(conglest)
                    break
                except : 
                    print("You inputed string")
                    continue 
            
        cogs_values_sum = sum(cogs_values)
        print(cogs_values_sum)

        # IF BOTH YES !!! 
        
        def convert_value(cogs_val) :
            print("#----------------------")
            # revenue = int(input("Input Total sales or revenue :")) 
            while True : 
                try : 
                    revenue = int(input("Input Total sales or revenue : ")) 
                    # cogs = int(input("Input all cost of goods : "))       
                    gross(cogs_val , revenue) 
                    # grok() 
                    break 
                except Exception as e: 
                    print(e)
                    print("something namo wronasdg change something")
                continue 
                    


        convert_value(cogs_values_sum) 
            
            

        
    
        
    # while True : 
    #     try : 
    #         revenue = int(input("Input Total sales :")) 
    #         cogs = int(input("Input all cost of goods : "))  
    #         break 
    #     except Exception as e: 
    #         print(e)
    #         print("something namo wronasdg change something")
    #     continue 
    # total_sales = inaput("Input total sales")
    # cogs_def(total_sales) 
else : 
    print("I can campute it for yuo") 
    ask_compute = input("Would you like to compute it ? : ")
    if ask_compute in yes : 
        revenue_list = []  
        revenue_ask = input("What first list in revenue  ? : ")
        revenue_list.append(revenue_ask)
        print(revenue_list)
        
        # quit_list = ['Q', 'q', 'quit', 'quits', 'Ayaw', 'enap', 'exit']
        while not revenue_ask in quit_list :             
            print("If the list is okay press : (Q) ")
            revenue_ask = input("Input other list : ")
            if not revenue_ask in quit_list : 
                revenue_list.append(revenue_ask)
            print("#-----------------------------")
            print(revenue_list)
        
        print("#----------------------")
        print(type(len(revenue_list)))
        print(len(revenue_list))
        print("Define the value of of each ") 
        print( " List : Value")
        
        valuess = []
        for x in range(len(revenue_list)) : 
            while True : 
                try : 
                    congver = int(input(f"{revenue_list[x]} : " ))  
                    valuess.append(congver)
                    break
                except : 
                    print("You inputed string")
                    continue
            
        revenue_sum(valuess)

        # print(revenue_ask[0])
    else :
        print("Okay mamatay kang maaga")




    

# while ask_revenue : 
#     Revenue = input('Enter Revenue :  ')   
#     try : 
        
#     except :

# # if 
# print(type(Revenue))

# Cogs = input()
