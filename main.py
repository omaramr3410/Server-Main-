import sys
import mysql.connect

def main():

	#for (amount) in cursor:
	#	debt.append({'amount':amount});

	speed = 'fast'
	expense = {'rent':800,'util':300,'transp':150,'foodShop':50,'entertain':30,'misc':20}
	debt = [{'amount':1200,'percent':.05},{'amount':300,'percent':.03},{'amount':600,'percent':.04},{'amount':2000,'percent':.10}]
	priority = []
	#for index,value in enumerate(priority):

	income = 1500
	spent = 0

	for key, value in expense.items():
		spent = value+spent

	remaining = income - spent

	maxRate = 0
	sorted(debt,key=lambda debt: debt["percent"])


	for i in range(0,len(debt),1):
		print(debt[i])

	"""for (percent) in debt:
		if debt[percent] > maxRate:
			maxRate = debt[percent]
			priority.append(percent)
			debt.remove(percent)

	numDebt = len(debt)"""




	print(maxRate)
	print(*priority)




main()
