import mysql.connector as sql

#get the user id and and user income
def getuser(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.UserTable where userid =" + userID )



	cursor.execute(query)

	for (userid, income, speed) in cursor:
		return {'userid':userid, "income":income, "speed":speed}


	cursor.close()

	cnx.close()	


#print(getuser('12345'))


#get the debt
def getdebt(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.DebtTable where userid =" + userID)

	cursor.execute(query)

	debtslist = []
	for (debtid,userid,initialamount1,remaining,minimumpayment,debtdescription) in cursor:
		debtslist.append({'debtid':debtid,'userid':userid,'initalamount':initalamount, 'remaining': remaining,"minimumpayment":minimumpayment,"debtdescription":debtdescription})

	cursor.close()

	cnx.close()
	
	return debtslist	

#get the expenses
def getexpenses(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.ExpenseTable where userid =" + userID)

	cursor.execute(query)

	expenselist = []
	for (userid,category,amount) in cursor:
		expenselist.append({'userid':userid,'category':category, "amount":amount})

	cursor.close()

	cnx.close()	

	return expenselist


def addDebt(debtID,userID,initalamount,Remaining,MinimumPayment,DebtDescription):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.DebtTable(debtid,userid,initalamount,remaining,minimumpayment,debtdescription) 
                           VALUES 
                           (debtID,userID,initalamount,Remaining,MinimumPayment,DebtDescription) """

	cursor.execute(insert_query)

	#records=cursor.fetchall()

	print("Successfully rcorded:")

	cursor.execute("SELECT * FROM CapitolOneDB.DebtTable where userID =" + str(userID))

	rows = cursor.fetchall()

	#print("rows:"+str(rows))

	for row in rows:
		print(row)

	for (userid,category,amount) in cursor:
		return {'userid':userid, 'category':category, "amount of expenses":amount}

	cursor.close()

	cnx.close()	


def addExpense(userID,Category,Amount):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.ExpenseTable(userid,category,amount) 
                           VALUES 
                           (userID,Category,Amount) """

	cursor.execute(insert_query)

"""
#update 
def updateDebt():
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()
"""

def generateSchedule(userID):
	expense = getexpense(userID)["category","amount"]
	debt = getdebt(userID)["remaining"] 
	income = getuser(userID)["income"] 





	#update_query = 
print(getuser('12345'))

print(getdebt('1'))

print(getexpenses('12345'))

addDebt(1,12345,50000,5000,10,'check')