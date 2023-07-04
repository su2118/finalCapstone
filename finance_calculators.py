import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calcualte the amount you'll have to pay on a home loan \n")

cal_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() #asking user to choose investment or bond

if(cal_type=="investment"): #if the user chooses investment, the following data will be asked for input

    deposit_amount = int(input("Enter the amount of money for deposit: ")) #deposit amount input by user
    interest_rate = int(input("Enter the interest rate: ")) #interest rate input by user
    year = int(input("Enter the number years you want to plan on investing: ")) #the number of years for investing
    interest_type = input("Do you want to 'Simple' or 'Compound' interest? :").lower() #interest type 
    interest_rate = interest_rate/100 #calculating interest rate divided by 100
    if(interest_type == "simple"): #if the user chooses simple interest, the following formula will be used to calcualate the total amount
        total_amount = deposit_amount * (1 + interest_rate * year)
    else:  #if the user chooses compund, the following formula will be used to calculate the total amount
        total_amount = deposit_amount * math.pow((1 + interest_rate), year)
    print("The total amount is: ","%.2f" % total_amount) #print the total amount

else: #if the user chooses bond, the following data will be asked for input

    present_value = int(input("Enter the present value of the house: ")) #present value of the house
    monthly_interest_rate = int(input("Enter the monthly interest rate: ")) #the monthly interest rate
    months = int(input("Enter the number of months you plan to take to repay the bond: ")) #the number of months to repay the bond
    monthly_interest_rate = (monthly_interest_rate/100)/12 #calculating monthly interest rate
    repayment = (monthly_interest_rate * present_value) / (1 - (1+ monthly_interest_rate) ** (-months)) # calculating repayment
    print("The repayment is: ", "%.2f" % repayment) #printing the repayment amount 
