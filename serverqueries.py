import mysql.connector as sql


def getuser(userID):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.UserTable where userid =" + userID )



	cursor.execute(query)

	for (userid, income, speed) in cursor:
		return {'userid':userid, "income":income}



print(getuser('12345'))




import mysql.connector as sql


def addDebt(debtid,userid,initalamount, ):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("INSERT INTO CapitolOneDB.DebtTable (debtid,userid,inital amount, remaining, minimum payment,debtdescription) \n VALUES (" +udebtID+"+d)")



	cursor.execute(query)

	for (userid, income, speed) in cursor:
		return {'userid':userid, "income":income}



print(getuser('12345'))
