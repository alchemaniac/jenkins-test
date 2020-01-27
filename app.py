from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder="templates")

@app.route('/',methods=['GET','POST'])
def index():
	print("Connecting to database ...")
	try:
		mydb = mysql.connector.connect(host="mysql",user="root",password="mysql12345")
	except:
		print("Connection failed!")
	print("Preparing database ...")
	mycursor = mydb.cursor()
	try:
		mycursor.execute("CREATE DATABASE mydatabase")
	except:
		print('db exists')
	mycursor.execute("USE mydatabase")
	try:
		mycursor.execute("CREATE TABLE somedata (name VARCHAR(255) NOT NULL, id VARCHAR(255) NOT NULL, dob DATE NOT NULL)")
	except:
		print('table exists')
	query = """INSERT INTO somedata VALUES (%s, %s, STR_TO_DATE(%s, '%d-%m-%Y'))"""
	print("Waiting for data ...")
	if request.method=="POST":
		print("Receiving data ...")
		details=request.form
		tname=details['name']
		tid=details['id']
		tdate=details['date']
		indata=(tname, tid, tdate)
		print("Inserting data ...")
		mycursor.execute(query, indata)
		mycursor.execute("commit;")
	print("Fetching data ...")
	mycursor.execute("select * from somedata")
	result=mycursor.fetchall()
	pname=[]
	pid=[]
	pdate=[]
	if(result!=[]):
		for data in result:
			pname.append(data[0])
			pid.append(data[1])
			pdate.append(data[2])
	print("Rendering data ...")
	return render_template('index.html',pdata=zip(pname,pid,pdate))

if __name__ == "__main__":
	app.run(host="0.0.0.0")
