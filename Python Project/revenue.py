
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
            print("\n \n")
            revenue = int(input("Input Total sales or revenue : ")) 
            print("\n")
            cogs = int(input("Input cost of all goods : "))               
            gross(cogs,revenue) 
            # grok() 
            break 
        except Exception as e: 
            # print(e)
            print(f"\n {e} \n You inputted string, kindly input integers only") 
        continue 
#------------------------------------------

def gross(cogs, revenue) :
    # print(type(cogs))
    print("\n \n \n")
    print(f"Revenue \t: \t{revenue}")    
    print(f"COGS \t \t : \t{cogs} \n")
    grosss =  revenue - cogs
    print(f" The gross profit \t: \t{revenue - cogs} \n" )       
    return gross   
    
    
    
def revenue_sum(sums): 
    print("#----------------------------------------")
    revenue_sum = sum(sums)
    print(revenue_sum) 
    return revenue_sum

    # print(type(revenue_sum))
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
    
    ask_cogs = input("\n Do you have cost of all goods ? ( yes / no) : ").lower().strip()
    
    if ask_cogs in yes : 
        convert() 
    else :    

        print("\n")

        cogs_list = []
        write_cogs = input("Type list of cogs category : ").lower().strip()
        cogs_list.append(write_cogs)
        print(cogs_list) 
        print("\n")

        while not write_cogs in quit_list : 
            print("if you to quit type (q)")
            write_cogs = input("Type more : ").lower().strip()
            if not write_cogs in quit_list : 
                cogs_list.append(write_cogs)
                
            print(f"{cogs_list} \n")        

        # print(len(cogs_list))   
        
        print("\n \n")
        print(cogs_list)
        print()
        print("Define the value of of each cogs list") 
        print( " List \t \t:  \tValue") 

        cogs_values = []
        for x in range(len(cogs_list)) : 
            while True : 
                try : 
                    conglest = int(input(f"{cogs_list[x]} \t \t: \t" ))  
                    cogs_values.append(conglest)
                    break
                except : 
                    print("Invalid input, input integers only\n" )
                    continue 
            
        cogs_values_sum = sum(cogs_values)
        print("---------------------------------------")
        print(f"Total \t \t: \t{cogs_values_sum}")

        # IF BOTH YES !!! 
        

        print("\n")

        def convert_value(cogs_val) :
            # revenue = int(input("Input Total sales or revenue :")) 
            while True : 
                try : 
                    revenue = int(input("Input Total sales or revenue : ")) 
                    # cogs = int(input("Input all cost of goods : "))       
                    gross(cogs_val , revenue) 
                    # grok() 
                    break 
                except Exception as e: 
                    
                    print(f"\n {e}")
                    print("Unable to validate string, please input integers only \n ")
                continue 
                    

        convert_value(cogs_values_sum) 

    # --------------------------------------------------                        
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
    # ---------------------------------------------------
        


else : 
    print("\n \n \n I can campute it for yuo \n ") 
    ask_compute = input("Would you like to compute it ? : ")

    if ask_compute in yes : 
        revenue_list = []  
        revenue_ask = input("\n What first list in revenue  ? : ")
        revenue_list.append(revenue_ask)
        print(revenue_list)
        
        # quit_list = ['Q', 'q', 'quit', 'quits', 'Ayaw', 'enap', 'exit']
        while not revenue_ask in quit_list :             
            print("\n \n If the list is okay press : (Q) ")
            revenue_ask = input("Input other list : ").lower().strip()
            if not revenue_ask in quit_list : 
                revenue_list.append(revenue_ask)
            print("\n \n")
            print(revenue_list)
        
        print("\n \n \n")
        # print(type(len(revenue_list)))
        # print(len(revenue_list))
        print("Define the value of of each ") 
        print( "List \t \t: \tValue")
        
        valuess = []
        for x in range(len(revenue_list)) : 
            while True : 
                try : 
                    congver = int(input(f"{revenue_list[x]}\t\t: \t" ))  
                    valuess.append(congver)
                    break
                except : 
                    print("Invalid input, input integers only\n")
                    continue
            
        revenue_sum(valuess)

        # print(revenue_ask[0])
    else :
        print("Okay mamatay kang maaga")


# --------------------------------------------------------------------    

# while ask_revenue : 
#     Revenue = input('Enter Revenue :  ')   
#     try : 
        
#     except :

# # if 
# print(type(Revenue))

# Cogs = input()
