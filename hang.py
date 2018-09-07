import webbrowser
import time
import random

while True:
	sites=random.choice(['google.com','youtube.com'])
	visit="http://{}".format(sites)
	webbrowser.open(visit)
	seconds=random.randrange(5,20)
	 # Delay for random minutes
	time.sleep(seconds)
