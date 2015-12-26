from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from models import User_Account
from django.http import HttpResponseRedirect
import random
import datetime
import smtplib
import time 

def index(request):
	return render(request, 'main_page.html')
def login(request):
	return render(request, 'login.html')
def signup(request):
	return render(request, 'signup.html' )
def loginprocess(request):
	mail =  request.POST.get("username","")
	password = request.POST.get("password","")
	if(len(mail) == 0 or len(password) == 0):
		return render(request,'login.html',{'message' : 'Invalid Username/Password'  })
	user_data = User_Account.objects.all().filter(mail = mail)
	got = True
	for e in user_data:
		got = False
	if(got):
		return render(request,'login.html',{'message' : 'Email id Does Not Exist Please Signup '})
	_id = 0
	_ver = 0
	for e in user_data:
		_ver = e.verified
		_id = e.id
		if(e.password != password):
			return render(request,'login.html',{'message' : 'Password/Emailid entered is wrong please Try again' })
	print _ver
	if(_ver == 0):
		return render(request,'verified.html', {'id' : _id} )
	request.session['logid'] = _id  
	return HttpResponseRedirect('/message/dash')
def signupprocess(request):
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	name = request.GET.get('name','')
	phone = request.GET.get('phonenumber','')
	vericode = '000000'
	verified = '0'	
	mail = request.GET.get('email','')
	dict = {'username' : username , 'name' : name , 'phonenumber' : phone,'email' : mail, 'message' : 'Error'}
	if(username == '' or username.__len__() >= 100 or username.__len__() <= 7 ):
		dict['message'] = "Enter a valid username"
		return render(request,'signup.html',dict)
	elif(password == '' or  password.__len__() >= 100 or password.__len__() <= 7):
		dict['message'] = "Enter a valid password"
		return render(request,'signup.html',dict)
	elif(name == ''):
		dict['message'] = "Enter a valid name"
		return render(request,'signup.html',dict)
	elif(mail == '' or mail.rfind('@') == -1):
		dict['message'] = "Enter a valid Email-Address"
		return render(request,'signup.html',dict)
	try:
		phone = int(phone)
	except Exception, e:
		dict['message'] = "Enter a valid phone number"
		return render(request,'signup.html',dict)
	data = User_Account.objects.all();vals = 0
	email_check = User_Account.objects.all().filter(mail = mail)
	for y in email_check :
		dict['message'] = "This Email-Address is already in use . Please try again with another Email "
		return render(request,'signup.html',dict)
	for e in data :vals+=1
	new_user_id = vals +  1
	sender  = 'vichuhari100@gmail.com'
	reciever = mail 
	vericode = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
	message = """
			Hello {},  
				This is a Verification Message
				Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password
			         
			      	 username : {} 

					 password : {}  These are the first three letters of the password for verification
					
				The verification code is  {}

					Thank You for using CC messaging :) 
					
					CC Messaging Support

					 DO not Reply To this message 
				""".format(name,username,password[:3],vericode)
	try:
   		server = smtplib.SMTP('mail.smtp2go.com',2525)
		server.login('vichuhari100@gmail.com','24720480')
		server.sendmail(sender, reciever, message)
		server.quit()
	except Exception, e:
		print e
   		dict['message'] = "Invalid Email Address or Try again Later" 
		return render(request,'signup.html',dict)
	response = HttpResponse( 'blah' ) 
	response.set_cookie( 'user_id', new_user_id )
	User_data = {'username':username,'email':mail,'password':password,'user_id':new_user_id,'name':name,'phone_no':phone,'vericode':vericode,'verified':0}
	p = User_Account(username=username,mail = mail,password=password,user_id=new_user_id,name=name,phone_no=phone,vericode=vericode,verified=0)
	p.save()
	return render(request, 'login.html')

def verified(request):
	id = request.GET.get('id')
	vericode = request.GET.get('veri')
	dat = User_Account.objects.all().filter(id = id)
	for e in dat:
		print e.vericode
		print vericode
		if(str(e.vericode) == str(vericode)):
			User_Account.objects.filter(id = id).update(verified = 1)
			return HttpResponseRedirect('/app')
	return render(request,'verified.html',{'id' : id})