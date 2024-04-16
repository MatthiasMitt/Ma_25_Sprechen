#coding: utf-8

'''Simple demo of using UIDevice to query the current battery state'''

from   objc_util import *
import speech
import time

speech.say('Guten Tag. Mein Name ist Eifon','de',0.5)

UIDevice = ObjCClass('UIDevice')
device = UIDevice.currentDevice()
battery_states = {1: 'unplugged', 2: 'charging', 3: 'full'}

device.setBatteryMonitoringEnabled_(True)
battery_percent = device.batteryLevel() * 100
state = device.batteryState()
state_str = battery_states.get(state, 'unknown')
print('Battery level: %0.1f%% (%s)' % (battery_percent, state_str))
device.setBatteryMonitoringEnabled_(False)

#t = str(time.strftime('%H Uhr %M'))
#print(t)
#speech.say(t,'de',0.5)

h = time.localtime().tm_hour
m = time.localtime().tm_min
t = '%i Uhr %i' % ( h , m )
print(t)
speech.say(t,'de',0.5)

if state == 3:
	text = 'Die Batterie ist voll geladen'
elif state == 1:
	text = 'Batteriebetrieb. Die Batterie hat noch %0.0f%% ' % battery_percent
elif state == 2:
	text = 'Die Batterie läd gerade und hat inzwischen %0.0f%% ' % battery_percent
else:
	text = 'Der Status der Batterie ist unbekannt'

speech.say(text,'de',0.5)

#speech.say('Ulla, alles Gute','de',0.5)

#speech.say('Matthias ist ein komischer Name','en',0.5)


