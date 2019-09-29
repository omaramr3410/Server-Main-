import mysql.connector as sql
from flask import Flask, request, jsonify
import random
#get the user id and and user income
app= Flask(__name__)
@app.route('/user')
def getUser():
	userID=request.args.get('userid')
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.UserTable where userid =" + userID )



	cursor.execute(query)

	for (userid, income, speed) in cursor:
		return jsonify({'userid':userid, "income":income, "speed":speed})


	cursor.close()

	cnx.close()	


#print(getuser('12345'))


#get the debt
@app.route('/debts')
def getDebts():
	userID=request.args.get('userid')
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.DebtTable where userid =" + userID)

	cursor.execute(query)

	debtslist = []
	for (debtid,userid,initialamount1,remaining,minimumpayment,debtdescription) in cursor:
		debtslist.append({'debtid':debtid,  "minimumpayment":minimumpayment})

	cursor.close()

	cnx.close()
	
	return jsonify({'debts':debtslist})	

#get the expenses
@app.route('/expenses')
def getexpenses():
	userID=request.args.get('userid')
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	query = ("SELECT * FROM CapitolOneDB.ExpenseTable where userid =" + userID)

	cursor.execute(query)

	expenses=[]
	for (userid,category,amount) in cursor:
		expenses.append({'userid':userid,'category':category, "amount":amount})

	cursor.close()

	cnx.close()	
	return jsonify({'expenses':expenses})
@app.route("/debt/add")
def addDebt():
	debtID=str(random.randint(1,1000000))
	userID=request.args.get('userid')
	InitialAmount=request.args.get('initalamount')
	Remaining=request.args.get('remaining')
	MinimumPayment=request.args.get('minimumpayment')
	DebtDescription=request.args.get('debtdescription')
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.DebtTable(debtid,userid,initalamount,remaining,minimumpayment,debtdescription) 
                           VALUES 
                           (debtID,userID,InitialAmount,Remaining,MinimumPayment,debtDescription) """

	cursor.execute(insert_query)

	#records=cursor.fetchall()

	print("Successfully rcorded:")

	return ""

	cursor.close()

	cnx.close()	


def addExpense(userID,Category,Amount):
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()

	insert_query = """INSERT INTO CapitolOneDB.ExpenseTable(userid,category,amount) 
                           VALUES 
                           (userID,Category,Amount) """

	cursor.execute(insert_query)


#update 
def updateDebt():
	cnx= sql.connect(user='admin', password= 'password', host='database-capitolone.chz2sscroq0a.us-east-2.rds.amazonaws.com')

	cursor = cnx.cursor()


def generateSchedule(userID):
	expense = getexpense(userID)["category","amount"]
	debt = getdebt(userID)["remaining"] 
	income = getuser(userID)["income"] 



	#update_query = 
#print(getuser('12345'))

#print(getdebt('1'))

#print(getexpenses('12345')

#addDebt(1,12345,5000,500,12,'Test')
if __name__=="__main__":
	app.run()