from django.db import models

# Create your models here.
class Message_data(models.Model):
	message = models.CharField(max_length = 5000000)
 	date = models.DateTimeField()
 	reciver_id = models.IntegerField()
 	recieved = models.IntegerField()
 	sender_id = models.IntegerField()
 	def __str__(self):
 		return self.message + " << Sent by >> " + self.sender

