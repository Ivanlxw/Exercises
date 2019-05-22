def calculate_payment():
    """
    Calculate the monthly payments of a fixed term mortgage over Nth terms at a given interest rate. 
    Extra: add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
    """
    interval = int(input("Select compounding interval:\n1.Monthly\n2.Weekly\n3.Daily\n"))
    #take in inputs
    r = float(input("Enter interest rate in decimals (yearly)\n"))
    mortgage = float(input("How much is the mortgage?\n"))
    period = float(input("How many years?\n"))
    #adjust for time period
    if interval == 1:
        r /= 12
        period *= 12
    elif interval == 2:
        r/=52
        period *= 52
    elif interval == 3:
        r /= 365
        period *= 365
    #working
    payment = mortgage * r / (1 - (1/(1+r))**period)

    if interval == 1:
        print("You'll need to pay $%.2f per month"% payment)
    elif interval == 2:
        print("You'll need to pay $%.2f per week" % payment)
    elif interval == 3:
        print("You'll need to pay $%.2f everyday" % payment)


def time_to_repay():
    """
    Also figure out how long it will take the user to pay back the loan.  
    """
    interval = int(input("Select compounding interval:\n1.Monthly\n2.Weekly\n3.Daily\n"))
    #take in inputs
    r = float(input("Enter interest rate in decimals (yearly)\n"))
    mortgage = float(input("How much is the mortgage?\n"))
    payment = float(input("How much are you paying per time period?\n"))
    
    if interval == 1:
        r /= 12
    elif interval == 2:
        r/=52
    elif interval == 3:
        r /= 365
    
    #working
    temp = mortgage
    period = -1
    while temp > 0:
        temp = (temp - payment) * (1+r)
        period += 1
    
    if interval == 1:
        print("You'll need to take {} months".format(period))
    elif interval == 2:
        print("You'll need to take {} weeks".format(period))
    elif interval == 3:
        print("You'll need to take {} days".format(period))

    

if __name__ == '__main__':
    while True:
        option = int(input("Choose either option 1 or 2:\n1.Calculate monthly payment of mortgage\n2.Time needed to repay loan\n"))
        if option == 1:
            calculate_payment()           
            break
        elif option == 2:
            time_to_repay()
            break            
        else:
            print("Please enter the correct number option")
