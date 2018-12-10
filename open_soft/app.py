from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from datetime import datetime
import pymysql
import os


app = Flask(__name__)


app.secret_key=os.urandom(23564)

#registers a function that runs before any type 
#of request is made to the compiler
@app.before_request
def before_request():
	g.user=None
	if 'user' in session:
		g.user = session['user']

@app.route('/signup')
def sign():
	 return render_template('signup.html')

connection=pymysql.connect(host='localhost', user="root", password="", db="webapp1", charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)
 
#----------------- signup -------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
   
	cursor = connection.cursor()     
	
	#user is the array that stores the data received from the form
	if request.method == 'POST':
		user = request.form
		name = user['name']
		username=user['username']
		emailid = user['emailid']
		password = user['password']

		if username:
			query = "SELECT password FROM Users WHERE username=%s"
			cur = cursor.execute(query, (username))
			if cur:
				flash('username already exists')
				return redirect(url_for('signup'))
			else:	
				try:
					query="INSERT INTO Users (name, username, emailid, password) VALUES (%s, %s, %s, %s)"
					cursor.execute(query,(name, username, emailid, password))
					connection.commit() 
				
				except:
					return render_template('alert.html')

				connection.close()    
				return redirect(url_for('login'))



@app.route('/login')
def log():
	return render_template('login.html')

#-------------------------login ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	error=None
	if request.method == 'POST':
		session.pop('user', None)
		user_input = request.form['username']
		password_input = request.form['password']
		cursor = connection.cursor() 
		cursor.execute("SELECT password FROM Users WHERE username=%s", user_input)
		myresult=cursor.fetchone()
		if myresult==None:
			error = 'Invalid username or password. Please try again!'
			
		elif myresult['password']==password_input :
			session['user']=user_input
			return redirect(url_for('feed'))
		else :
			error = 'Invalid username or password. Please try again!'
	return render_template('login.html', error = error)		

@app.route ('/')	
def homequery():
	if g.user:
		return redirect(url_for('feed'))
	return redirect(url_for('login'))	




@app.route ('/dropsession')
def dropsession():
	session.pop('user', None)


# ---------------------feed after login----------------------
@app.route('/feed', methods = ['GET','POST'])
def feed():
	if(g.user):
		cursor = connection.cursor()
		query = "SELECT * FROM `items` ORDER BY `timestamp` DESC" 
		cursor.execute(query)
		connection.commit()
		result = cursor.fetchall()

		cursor2 = connection.cursor()
		query2 = "SELECT * FROM `notifications` WHERE `username` = %s ORDER BY `timestamp` DESC " 
		cursor2.execute(query2,g.user)
		connection.commit()
		notifications = cursor2.fetchall()
		
		# search for the type of item you want to buy
		if request.method == 'POST' and request.form['btn'] =='search':
			form1 = request.form
			item_type = form1['itemtype']
			if item_type == 'cab':
				return redirect(url_for('cab'))


			query = "SELECT * FROM `items` WHERE `item_type`=%s ORDER BY `timestamp` DESC" 
			cursor.execute(query,item_type)
			connection.commit()
			result = cursor.fetchall()
			return render_template('feed.html', result = result,notifications = notifications)

		# buy a particular item and send a notification to the person who posted the ad
		elif request.method == 'POST' and request.form['btn'] !=None:

			if request.form['btn'] == 'addNew':
				return redirect(url_for('addItem'))

			cursor = connection.cursor()
			query = "UPDATE `items` SET `sold` = '1' WHERE `item_name` = %s"
			cursor.execute(query,request.form['btn'])
			connection.commit()

			cursor = connection.cursor()
			query = "SELECT * FROM `items` WHERE `item_name` = %s"
			cursor.execute(query,request.form['btn'])
			username  = cursor.fetchall()
			connection.commit()

			for iterator in username:
				cursor2 = connection.cursor()
				new_stmt = g.user + " wants to buy " + request.form['btn'] 
				query2 = "INSERT INTO `notifications` (`username`, `content`, `timestamp`) VALUES ( %s, %s, CURRENT_TIMESTAMP) " 
				cursor2.execute(query2, (iterator['name'],new_stmt) )
				connection.commit()


			return redirect(url_for('feed'))


		return render_template('feed.html',result = result,notifications = notifications)
	else:
		return redirect('/login')

# ------------------------add item to sell in the marketplace----------------
@app.route('/addItem', methods = ['GET','POST'])
def addItem():

	cursor = connection.cursor()     

	if request.method == 'POST':
		ad = request.form
		name = g.user
		item_type = ad['itemtype']
		item_name = ad['itemname']
		price = int(ad['price'])
		phone = int(ad['phone'])
		sold = 0

		query="INSERT INTO `items` (`name`, `item_type`, `item_name`, `price`, `phone`, `sold`, `timestamp`) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)"
		cursor.execute(query, (name, item_type, item_name, price, phone, sold))
		connection.commit() 
		return redirect(url_for('feed'))	

	return render_template('addItem.html')




#--------------------cab sharing--------------------------------- 
@app.route('/cab',methods =['GET','POST'])
def cab():
	if g.user:
		# search for a cab
		if request.method == 'POST' and request.form['btn'] == "search":

			cabForm = request.form
			date = cabForm['date']
			time = cabForm['time']
			src = cabForm['Source']
			dest = cabForm['Destination']

			if src==0 or dest==0 :
				error="Enter valid source or destination"
				return render_template("cab.html", error = error)
			elif src == dest :
				error="Enter valid source or destination"
				return render_template("cab.html", error = error)
			else:

				cursor = connection.cursor()
				query = "SELECT * FROM `cab_share` WHERE `date` = %s AND `src` LIKE %s AND `dest` LIKE %s" 
				cursor.execute(query, (date,src,dest))
				connection.commit()
				result = cursor.fetchall()
				compatible_cab = []
				if result:
					for i in result:
						journeytime = i['time']
						journeytime = str(journeytime)
						journeytime_time = datetime.strptime(date+ ' ' +journeytime, '%Y-%m-%d %H:%M:%S')
						time_time = datetime.strptime(date+ ' ' + time , '%Y-%m-%d %H:%M')
						timediff = abs(journeytime_time - time_time)
						if timediff.seconds <= 3600:
							compatible_cab.append(i)
					if compatible_cab:
						return render_template('cabresult.html', result=compatible_cab)

				# automatically creates a cab sharing if no compatible cab found		
				elif (not result) or (not compatible_cab): 
					
					cursor.execute("Insert INTO cab_share (username, date, time, src, dest) VALUES (%s,%s, %s, %s, %s )",(g.user, date, time, src, dest))
					cursor.connection.commit()

					cursor = connection.cursor()
					query = "SELECT * FROM `cab_share` WHERE `date` = %s AND `src` LIKE %s AND `dest` LIKE %s" 
					cursor.execute(query, (date,src,dest))
					connection.commit()
					result = cursor.fetchall()

					# displays the newly created cab sharing for you
					compatible_cab = []
					if result:
						for i in result:
							journeytime = i['time']
							journeytime = str(journeytime)
							journeytime_time = datetime.strptime(date+ ' ' +journeytime, '%Y-%m-%d %H:%M:%S')
							time_time = datetime.strptime(date+ ' ' + time , '%Y-%m-%d %H:%M')
							timediff = abs(journeytime_time - time_time)
							if timediff.seconds <= 3600:
								compatible_cab.append(i)

					# tell the user you have created a cabsharing for them and display it
					error = "There was no compatible cabs so we created 1 for you"
					return render_template('cabresult.html', result=compatible_cab, error = error)
	else:
		return redirect('/login')
	return render_template('cab.html')

# send a notfication to the person who wants to share cab with you
@app.route('/notification',methods =['GET','POST'])
def notification():
	if request.method == 'POST':
		cursor2 = connection.cursor()
		new_stmt = g.user + " wants to share cab with you "
		query2 = "INSERT INTO `notifications` (`username`, `content`, `timestamp`) VALUES ( %s, %s, CURRENT_TIMESTAMP) " 
		cursor2.execute(query2, (request.form['btn'],new_stmt) )
		connection.commit()
		return redirect(url_for('feed'))

if __name__ == "__main__":
	app.run(debug=True)

