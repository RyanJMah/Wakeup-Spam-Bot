import time
import pause
import threading
import rpi_gpio
from datetime import datetime
from phone_bot import Phone_Bot

class Alarm_Bot(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__poll_button_thread = threading.Thread(
			target = self.poll_button_routine,
			args = (self,),
			daemon = True
		)
		self.running = True
		self.daemon = True

	def poll_button_routine(self):
		rpi_gpio.init()
		while (1):
			if not rpi_gpio.get_button_status():
				break
		self.running = False

	def alarm_mainloop(self, alarm_datetime):
		pause.until(alarm_datetime)

		wakeup_msg = "wake up you useless piece of garbage"
		sleep_time = 5  # minutes

		bot = Phone_Bot()
		while (1):
			if not self.running:
				break

			bot.make_call(wakeup_msg)
			time.sleep(sleep_time*60)

	def stop(self):
		self.running = False
		


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
