# The week 2 problem set, involving first figuring out the remaining balance after 12 months
# given an initial balance, annual interest rate, and monthly payment; then, finding the minimum
# payment required to pay off a balance in 12 months given an initial balance and annual interest
# rate in multiples of $10; then, finding the exact required minimum payment rate, with them
# specifying to use bisection search. I had already used bisection in my previous answer, so 
# easy enough!

def minMonCredCard (balance,annualInterestRate,monthlyPaymentRate):
	'''
	takes balance as float, annualInterestRate and monthlyPaymentRate
	as decimal float
	returns remaining balance after 12 months
	'''
	months=0
	while months < 12:
		if balance == 0:
			return 0
		else:
			months += 1
			balance = balance - balance * monthlyPaymentRate
			balance = balance + balance * (annualInterestRate / 12)
	return round(balance,2)

def fixedPayCredCard (balance,annualInterestRate):
	'''
	takes balance as float, annualInterestRate as decimal float
	returns lowest monthly payment for 12 month payoff
	rounded to nearest higher $10 increment
	'''
	monthInt=annualInterestRate/12
	# this is based off of an equation I found on the internet; works, but felt like cheating
	# monthPay=(balance*monthInt*(monthInt+1)**12)/((monthInt+1)**12-1)
	# return round((monthPay),-1)
	maxMonthPay=(balance+annualInterestRate*balance)/12
	minMonthPay=0
	monthPay=maxMonthPay/2
	startBal=balance
	x=0
	while balance > 0 or abs(balance) > 1:
		if balance > 0:
			minMonthPay = monthPay
			monthPay = minMonthPay + (maxMonthPay - minMonthPay) / 2
		elif balance < 0:
			maxMonthPay = monthPay
			monthPay = minMonthPay + (maxMonthPay - minMonthPay) / 2
		elif balance == 0:
			return monthPay
		x+=1
		balance=startBal
		months=0
		while months < 12:
			months += 1
			balance = balance - monthPay
			balance = balance + balance * (annualInterestRate / 12)
	#adding +5 to monthPay to ensure that it rounds UP to the nearest 10 rather than down
	return int(round((monthPay+5),-1))

def fixedPayCredCardExact (balance,annualInterestRate):
	'''
	takes balance as float, annualInterestRate as decimal float
	returns lowest monthly payment for 12 month payoff
	'''
	monthInt=annualInterestRate/12
	maxMonthPay=(balance+annualInterestRate*balance)/12
	minMonthPay=0
	monthPay=maxMonthPay/2
	startBal=balance
	x=0
	while balance > 0 or abs(balance) > .01:
		if balance > 0:
			minMonthPay = monthPay
			monthPay = minMonthPay + (maxMonthPay - minMonthPay) / 2
		elif balance < 0:
			maxMonthPay = monthPay
			monthPay = minMonthPay + (maxMonthPay - minMonthPay) / 2
		elif balance == 0:
			return monthPay
		x+=1
		balance=startBal
		months=0
		while months < 12:
			months += 1
			balance = balance - monthPay
			balance = balance + balance * (annualInterestRate / 12)
	return round(monthPay,2)

# print ("Remaining balance:",minMonCredCard (balance,annualInterestRate,monthlyPaymentRate))
# print ("Lowest Payment:",fixedPayCredCard(balance,annualInterestRate))
print ("Lowest Payment:",fixedPayCredCardExact(balance,annualInterestRate))