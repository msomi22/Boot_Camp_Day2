# Sending SMS using AfricasTalkingGateway SMS- API
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
class SendSMS(object):
	"""
	Attributes:
	username: The API username required for sending SMS
	apikey: A key required for sending SMS
	recipients: The recipients mobile numbers , ie 0718953974
    message: The message to send
	"""
	def __init__(self,username='',apikey='',recipients='',message=''):
		self.username = username
		self.apikey = apikey
		self.recipients = recipients
		self.message = message
    # The method thet is called to send the SMS
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

if __name__ == '__main__':
	# Prompt the user to enter the required credentials 
	username = raw_input("Enter Your API username: ")
	apikey   = raw_input("Enter Your API Key: ")
	recepients  = raw_input("Enter Your Recepient, separate with comma for multiple Recepients: ")
	message = raw_input("Type Your Message: ")

	# Instantiate the sendSMS class
	send = SendSMS(username,apikey,recepients,message)
	#Invoke the send sms function 
	send.sendNow() 
