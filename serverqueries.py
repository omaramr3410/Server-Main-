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
def getdebt(debtID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.DebtTable where debtid =" + debtID)

	cursor.execute(query)

	for (debtid,userid,initialamount1,remaining,minimumpayment,debtdescription) in cursor:
		return {'debtid':debtid, "minimumpayment":minimumpayment}

	cursor.close()

	cnx.close()
			

#get the expenses
def getexpenses(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.ExpenseTable where userid =" + userID)

	cursor.execute(query)

	for (userid,category,amount) in cursor:
		return {'userid':userid,'category':category, "amount":amount}


def addDebt(debtID,userID,InitalAmount,Remaining,MinimumPayment,DebtDescription):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.DebtTable(debtid,userid,initalamount,remaining,minimumpayment,debtdescription) 
                           VALUES 
                           (debtID,userID,InitialAmount,Remaining,MinimumPayment,debtDescription) """

	cursor.execute(insert_query)

	#records=cursor.fetchall()

	print("Successfully rcorded:")

	number_of_rows =cursor.execute("SELECT * FROM CapitolOneDB.DebtTable where userID =" + userID)

	for i in range(number_of_rows):
		print(row[i])

	for (userid,category,amount) in cursor:
		return {'userid':userid, 'category':category, "amount of expenses":amount}



#update 
#def update():











def addExpense(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.DebtTable(debtid,userid,initalamount,remaining,minimumpayment,debtdescription) 
                           VALUES 
                           (debtID,userID,InitialAmount,Remaining,MinimumPayment,debtDescription) """

	cursor.execute(insert_query)

	

print(getuser('12345'))

print(getdebt('1'))

print(getexpenses('12345')

addDebt()