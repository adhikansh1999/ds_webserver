from flask import Flask, render_template, request, redirect, url_for, flash, g, session
from requester_module import send_request
from datetime import datetime
import pymysql
import os


app = Flask(__name__)

# format

# response = send_request(msg)


app.secret_key=os.urandom(23564)

#registers a function that runs before any type 
#of request is made to the compiler
@app.before_request
def before_request():
	# print("before_request")
	g.pop('user',None)
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
		acc_type = user['acc_type']

		print("the acc type is " , acc_type)

		if(acc_type == "buyer"):
			if username:

				# query = "SELECT password FROM buyers WHERE username=%s"
				# cur = cursor.execute(query, (username))
				query = {"type":"read", "method":"login_buyer", "username":username}
				cur = send_request(query)

				if cur['password'] != None:
					flash('username already exists')
					return redirect(url_for('signup'))
				else:	
					try:
						# query="INSERT INTO buyers (name, username, emailid, password) VALUES (%s, %s, %s, %s)"
						# cursor.execute(query,(name, username, emailid, password))
						# connection.commit() 
						query = {"type":"write", "method":"signup_buyer", "emailid":emailid, "password":password, "name":name, "username":username}
						buyer_signup_ack = send_request(query)
						print(buyer_signup_ack)
					except:
						return render_template('alert.html')

					# connection.close()    
					return redirect(url_for('login'))
		elif(acc_type == "seller"):
			if username:
				# query = "SELECT password FROM sellers WHERE username=%s"
				# cur = cursor.execute(query, (username))
				query = {"type":"read", "method":"login_seller", "username":username}
				cur = send_request(query)
				if cur['password']!= None:
					flash('username already exists')
					return redirect(url_for('signup'))
				else:	
					try:

						# query="INSERT INTO sellers (name, username, emailid, password) VALUES (%s, %s, %s, %s)"
						# cursor.execute(query,(name, username, emailid, password))
						# connection.commit() 
						query = {"type":"write", "method":"signup_seller", "emailid":emailid, "password":password, "name":name, "username":username}
						seller_signup_ack = send_request(query)
						print(seller_signup_ack)	

					except:
						return render_template('alert.html')

					# connection.close()    
					return redirect(url_for('login'))



@app.route('/login')
def log():
	print("log")
	return render_template('login.html')

#-------------------------login ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
	print("login")
	error=None
	if request.method == 'POST':
		session.pop('user', None)
		user_input = request.form['username']
		password_input = request.form['password']
		acc_type = request.form['acc_type']
		
		# mysql query here 
		# cursor = connection.cursor()
		if(acc_type == 'buyer'): 
			# cursor.execute("SELECT password FROM buyers WHERE username=%s", user_input)
			query = {"type":"read", "method":"login_buyer", "username":user_input}
		if(acc_type == 'seller'): 
			# cursor.execute("SELECT password FROM sellers WHERE username=%s", user_input)
			query = {"type":"read", "method":"login_seller", "username":user_input}
		myresult = send_request(query)	
		


		if myresult["password"] == None:
			error = 'Invalid username or password. Please try again!'
				
		if myresult != None and  myresult["password"]==password_input:
			session['user']=user_input
			session['acc_type']=acc_type
			print("acc type is ", session['acc_type'])
			return redirect(url_for('feed'))
		
		else:
			error = 'Invalid username or password. Please try again!'
	return render_template('login.html', error = error)		

@app.route ('/')	
def homequery():
	if ('user' in g):
		return redirect(url_for('feed'))
	return redirect(url_for('log'))	


@app.route ('/dropsession')
def dropsession():
	print("dropsession")
	if 'user' in session:

		g.pop('user',None)  
		session.pop('user',None)  
	print("/dropsession")
	return redirect(url_for('log'))

#----------------display items in cart-----------------------
@app.route('/cart', methods=['GET', 'POST'])
def cart():
	if('user' in g):
		#print("-------",g.userid)

		# cursor = connection.cursor()
		# query = "SELECT * FROM carts WHERE `username`=%s"
		# cursor.execute(query,g. user)
		# data = cursor.fetchall()
		
		query = {"type":"read", "method":"view_cart", "username":g.user}
		data = send_request(query)

		print("-----------------------------------------------------",data)		

		if len(data["product_id"]) == 0:
			error = 'cart is empty!'

		if request.method == 'POST':
			form_obj = request.form
			#print(form_obj)
			if 'remove' in form_obj:
				cid = form_obj['remove']
				# cursor = connection.cursor()
				# query = "DELETE FROM carts WHERE `id`=%s"
				# cursor.execute(query,cid)		
				# connection.commit()
				
				query = {"type":"write", "method":"update_quantity", "product_id":cid, "new_quantity":0, "username":g.user}
				delete_cart_ack = send_request(query)
				flash('item removed from cart!!')
				return(redirect(url_for('cart')))

			else:

				cid = form_obj['buy']
				
				query = {"type":"write", "method":"checkout", "product_id":cid, "username":g.user}

				ret = send_request(query)
				print("buy response" , ret)	
				if(ret["error"] == ""):
					flash('item succesfully bought!!')
					return redirect(url_for('cart'))
				else:
					flash('sorry, Item out of stock')
					return redirect(url_for('cart'))
				
				# ret = {"ack":True, "error":""}
				# cursor = connection.cursor()
				# query = "SELECT * FROM `products` WHERE `id` = %s"
				# cursor.execute(query,cid)
				# results_itr  = cursor.fetchall()
				# connection.commit()





				############################################## update the notifications db
				# for iterator in results_itr:
				# 	cursor2 = connection.cursor()
				# 	new_stmt = g.user + " wants to buy " + iterator['product_name'] + "with id = " + str(iterator['id'])
				# 	query2 = "INSERT INTO `notifications` (`username`, `content`, `timestamp`) VALUES ( %s, %s, CURRENT_TIMESTAMP) " 
				# 	cursor2.execute(query2, (iterator['username'],new_stmt) )
				# 	connection.commit()
			

		return render_template('cart.html', data=data)
		
	else:
		return redirect('/login')



# ---------------------feed after login----------------------
@app.route('/feed', methods = ['GET','POST'])
def feed():
	if('user' in g):
		# print("the user is " , g.user)
		
		# cursor = connection.cursor()
		# query = "SELECT * FROM `products` ORDER BY `timestamp` DESC" 
		# cursor.execute(query)
		# connection.commit()
		# result = cursor.fetchall()

		query = {"type":"read", "method":"view_all_products"}
		result = send_request(query)

		print("------------------------------------------------------",result)
		print("all quantities used are ",result['quantity'])

		####################################### NOTIFICATIONS
		# cursor2 = connection.cursor()
		# query2 = "SELECT * FROM `notifications` WHERE `username` = %s ORDER BY `timestamp` DESC " 
		# cursor2.execute(query2,g.user)
		# connection.commit()
		notifications ={}


		# search for the type of item you want to buy
		if request.method == 'POST' and request.form['btn'] =='search':
			form1 = request.form
			product_type = form1['product_type']

			# query = "SELECT * FROM `products` WHERE `product_type`=%s ORDER BY `timestamp` DESC" 
			# cursor.execute(query,product_type)
			# connection.commit()
			# result = cursor.fetchall()
			
			query = {"type":"read", "method":"filter_products","product_type":product_type}
			result = send_request(query)


			return render_template('feed.html', result = result,notifications = notifications)


		# add to cart an item and send a notification to the seller of the product
		elif request.method == 'POST' and request.form['btn'] !=None:

			if request.form['btn'] == 'addNew':
				return redirect(url_for('addItem'))

			cursor = connection.cursor()

			# neeed to add this to the cart
			username = g.user
			product_id = request.form['btn']
			print('product id to be bought is', product_id)
			quantity = 1

			# query = "INSERT INTO `carts` (`username`,`product_id`, `quantity`) VALUES ( %s, %s, %s) "
			# cursor.execute(query,(username,product_id,quantity))
			# connection.commit()

			query = {"type":"write", "method":"add_to_cart", "product_id":product_id, "username":username, "quantity":quantity}
			add_to_cart_ack = send_request(query)
			print(add_to_cart_ack)



			# the notification table
			# cursor = connection.cursor()
			# query = "SELECT * FROM `products` WHERE `id` = %s"
			# cursor.execute(query,request.form['btn'])
			# results_itr  = cursor.fetchall()
			# connection.commit()

			# for iterator in results_itr:
			# 	cursor2 = connection.cursor()
			# 	new_stmt = g.user + " wants to buy " + iterator['product_name'] + "with id = " + str(iterator['id'])
			# 	query2 = "INSERT INTO `notifications` (`username`, `content`, `timestamp`) VALUES ( %s, %s, CURRENT_TIMESTAMP) " 
			# 	cursor2.execute(query2, (iterator['username'],new_stmt) )
			# 	connection.commit()

			flash('product added to cart!!')
			return redirect(url_for('feed'))


		return render_template('feed.html',result = result,notifications = notifications)
	else:
		return redirect(url_for('login'))

# ------------------------add item to sell in the marketplace----------------
@app.route('/addItem', methods = ['GET','POST'])
def addItem():

	cursor = connection.cursor()     

	if request.method == 'POST':
		ad = request.form
		username = g.user
		product_type = ad['product_type']
		product_name = ad['product_name']
		price = int(ad['price'])
		quantity = int(ad['quantity'])

		# query="INSERT INTO `products` (`username`, `product_type`, `product_name`, `price`, `quantity`, `timestamp`) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP)"
		# cursor.execute(query, (username, product_type, product_name, price, quantity))
		# connection.commit() 


		
		query = {"type":"write", "method":"add_product", "username":username, "product_type":product_type, "product_name":product_name, "price":price, "quantity":quantity}
		add_item_ack = send_request(query)		

		print(add_item_ack)
		return redirect(url_for('feed'))	

	return render_template('addItem.html')


if __name__ == "__main__":
	app.run(debug=True)

