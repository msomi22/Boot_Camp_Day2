# Sending SMS using SMS- API
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
class SendSMS(object):
	def __init__(self,username='',apikey='',recipients='',message=''):
		self.username = username
		self.apikey = apikey
		self.recipients = recipients
		self.message = message

	def sendNow(self):
		gateway = AfricasTalkingGateway(self.username, self.apikey)
		try:
			results = gateway.sendMessage(self.recipients, self.message)
			for recipient in results:
				print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                            recipient['status'],
                                                            recipient['messageId'],
                                                            recipient['cost'])
			
			
		except AfricasTalkingGatewayException, e:
			print 'Encountered an error while sending the SMS: %s' % str(e)
		


username = raw_input("Enter Your API username: ")
apikey   = raw_input("Enter Your API Key: ")
recepients  = raw_input("Enter Your Recepient, separate with comma for multiple Recepients: ")
message = raw_input("Type Your Message: ")

send = SendSMS(username,apikey,recepients,message)
send.sendNow() 
