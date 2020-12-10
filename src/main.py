import time
from phone_bot import Phone_Bot



def main():
	wakeup_msg = "wake up you useless piece of shit"
	sleep_time = 5  # minutes

	bot = Phone_Bot()
	while (1):
		bot.make_call(wakeup_msg)
		time.sleep(sleep_time*60)
		


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass