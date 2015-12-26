from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from models import Message_data
from django.http import HttpResponseRedirect
from accounts.models import User_Account
import datetime
import itertools


def dash(request):
	try:
		_id = request.session['logid']
	except Exception, e:
		return render(request,'login.html',{'message' : 'Please Login Again to Continue'  })
	dat = Message_data.objects.all().filter(reciver_id = _id)
	acc = User_Account.objects.all().filter(id = _id)
	for h in acc:
		name = h.name
	lis = []
	id = []
	for e in dat:
		tem = e.sender_id
		data = User_Account.objects.all().filter(id = tem)
		for d in data:
			if(tem not in id):
				id.append(tem)
				lis.append({'name':d.name , 'user_id': tem  })
	print lis
	return render(request,'dash.html',{'name' : name,'dat':lis , 'link':"/message/mess?id="})

def mess(request):
	senid = request.GET.get('id','')
	try:recid = request.session['logid']
	except Exception, e:return render(request,'login.html',{'message' : 'Please Login Again to Continue'  })
	if(id == ''):return render(request,'dash.html')
	dat = Message_data.objects.all().filter(reciver_id__in = [recid,senid] , sender_id__in = [senid,recid])
	na = User_Account.objects.all().filter(id = senid);
	for e in na:name = e.name
	request.session['rid'] = senid
	return render(request,'dashm.html',{'dat' : dat ,'name':name , 'recid' : recid })

def send(request):
		message = request.POST.get('message')
		try:
			sendid = request.session['logid']
			recid = request.session['rid']
		except Exception, e:
			return render(request,'login.html',{'message' : 'Please Login Again to Continue'  })
		a = Message_data(message = message , reciver_id = recid , sender_id = sendid , date = datetime.datetime.now(), recieved = 0)
		a.save()
		return HttpResponseRedirect('/message/mess?id=' + str(recid))

def logout(request):
	request.session.flush()
	return HttpResponseRedirect('/app')

def newmes(request):
	return render(request,'newmess.html')

def create(request):
	man = request.session['logid']
	usern = request.GET.get("user")
	dat = User_Account.objects.all().filter(username = usern)
	chk = 0;
	for e in dat:
		chk = 1
		name = e.name
		recid = e.id
	if(chk == 0):
		return render(request,'newmess.html',{'message' : 'This user Does not exist in our Database'})
	request.session['rid'] = recid
	return render(request,'dashm.html',{'name':name})
