amount = int(input("plz enter your mortgage amount"))
int_rate = int(input("plz enter your yearly interest rate"))
term = int(input("plz enter your terms to pay the loan"))
monthly_rate = int_rate/100/12
payment = (monthly_rate/(1-(1+monthly_rate)**(-term)))*amount

print("Monthly pay/ ment for a %.2f %s year mortgage at %.2f%% interest rate is : %.2f" %(amount, (term/12),int_rate, payment))
