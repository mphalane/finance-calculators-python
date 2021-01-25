import math

#Display user instruction 

print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment\t -to calculate the amount of interest you'll earn on interest\n")
print("bond      \t -to calculate the amount you'll have to pay on a home loan\n")

#Get user input
print("\n")
user_choice=input("Enter your choice here : ")

#Capitalize user input
user_choice=user_choice.upper()

#Check what the user choice is 
#If it is investment then ask the user to enter respective values
#   Ask the user to enter the type of investment aswell
#   If simple interest then calculate total investment amount
#       based of the this formula: A = P(1 + r * t)
#   If complex interest then calculate total investment amount
#       based of the this formula: A = P(1 + r) ^ t
#If it is bond then ask user to enenter respective values
#   calculate the monthly bond repay_amount
if user_choice=="INVESTMENT":
    print("\n")
    deposit=float(input("Enter the deposit amount in rands :"))
    interest=float(input("Enter the interest rate :"))
    years=int(input("Enter the length of the investment in years :"))
    invst_type=input("Do you want (simple) or (compound) interest:")
    invst_type=invst_type.lower()
    
    print(f'\nAmount Deposited:   \t R{round(deposit,2)}')
    print(f'Interest Rate:      \t {round(interest,1)}%')
    print(f'Investment Duration:\t {years} years')
    print(f'Investment Type:    \t {invst_type}')
    
    interest=interest/100        #converting from percentage to value
    
    if invst_type=="simple":
        #Calculate
        total_amount=deposit*(1+interest*years)
        
        #Display Total Amount
        print("\t ----------------------- \t")
        print(f'The total amount:\t R{round(total_amount,2)}')  
        print("\t ----------------------- \t")
        
    elif invst_type=="compound":
        #Calculate
        total_amount=deposit*math.pow((1+interest),years)
        
        #Display Total Amount
        print("\t ----------------------- \t")
        print(f'The total amount: \t R{round(total_amount,2)}')
        print("\t ----------------------- \t")
    else:
        print("\nYou have made an invalid choice :( ")
elif user_choice=="BOND":
    print("\n")
    market_value=float(input("Enter the present value of the house in rands: "))
    interest=float(input("Enter the interest rate: "))
    months=int(input("Enter the length of the repayments in months: "))
        
    print(f'\nMarket Value of the House:             \t R{round(market_value,2)}')
    print(f'Interest Rate:                         \t {round(interest,1)}%')
    print(f'Repayment Duration:                    \t {months} months')
    
    
    interest=(interest/100)/12      #converting from percentage to value
    
    #Calculate Repayment
    repay_amount=(interest*market_value)/(1-math.pow((1+interest),(-1*months)))
    
    #Display Repayment
    print("\t ----------------------- \t")
    print(f'The total monthly repayment amount: \t R{round(repay_amount,2)}')  
    print("\t ----------------------- \t")
else:
    print("\nYou have made an invalid choice :( ")


#Press enter to exit
esc_str=input("\nPress Enter to esc : ")