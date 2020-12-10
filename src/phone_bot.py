import os
from twilio.rest import Client

class Phone_Bot():
	def __init__(self):
		self.__from_number = os.environ["TWILIO_FROM_NUMBER"]
		self.__to_number = os.environ["TWILIO_TO_NUMBER"]

		self.__account_sid = os.environ["TWILIO_ACCOUNT_SID"]
		self.__auth_token = os.environ["TWILIO_AUTH_TOKEN"]
		self.__client = Client(self.__account_sid, self.__auth_token)

	def send_msg(self, msg):
		self.__client.messages.create(
			body = msg,
			from_ = self.__from_number,
			to = self.__to_number
		)

	def make_call(self, msg):
		self.__client.calls.create(
			twiml = f"<Response><Say>{msg}</Say></Response>",
			from_ = self.__from_number,
			to = self.__to_number
		)

def main():
	bot = Phone_Bot()
	bot.make_call("wake up shithead")

if __name__ == "__main__":
	main()