from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	try:
    	mydb = mysql.connector.connect(host="mysql49",user="super",password="mysql12345")
	except:
		print("Cannot connect to mysql...")
	mycursor = mydb.cursor()
	try:
		mycursor.execute("CREATE DATABASE mydatabase")
	except:
		print('db exists')
	mycursor.execute("USE mydatabase")
	try:
		mycursor.execute("CREATE TABLE somedata (name VARCHAR(255), id VARCHAR(255))")
	except:
		print('table exists')
	query = """INSERT INTO somedata VALUES (%s, %s) """
	if request.method=="POST":
		details=request.form
		tname=details['name']
		tid=details['id']
		indata=(tname,tid)
		mycursor.execute(query, indata)
		mycursor.execute("commit;")
	mycursor.execute("select * from somedata")
	result=mycursor.fetchall()
	pname=[]
	pid=[]
	if(result!=[]):
		for data in result:
			pname.append(data[0])
			pid.append(data[1])
	return render_template('index.html',pname=pname,pid=pid)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
