from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	mydb = mysql.connector.connect(host="mysql",user="root",password="mysql12345")
	mycursor = mydb.cursor()
	try:
		mycursor.execute("CREATE DATABASE mydatabase")
	except:
		print('db exists')
	mycursor.execute("USE mydatabase")
	try:
		mycursor.execute("CREATE TABLE somedata (name VARCHAR(255) NOT NULL, id VARCHAR(255) NOT NULL,  dob VARCHAR(255) NOT NULL)")
	except:
		print('table exists')
	query = """INSERT INTO somedata VALUES (%s, %s, %s)"""
	try:
		if request.method=="POST":
			details=request.form
			tname=details['name']
			tid=details['id']
			tdate=details['date']
			indata=(tname, tid, tdate)
			mycursor.execute(query, indata)
			mycursor.execute("commit;")
	except:
		print("data insertion failure!")
	mycursor.execute("select * from somedata")
	result=mycursor.fetchall()
	#pdata=""
	pname=[]
	pid=[]
	pdate=[]
	if(result!=[]):
		for data in result:
			pname.append(data[0])
			pid.append(data[1])
			pdate.append(data[2])
	return render_template('index.html',pdata=zip(pname,pid,pdate))

if __name__ == "__main__":
	app.run(host="0.0.0.0")
