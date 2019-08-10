############################################################
## The Following script will get the bank information
## based on IFSC code. Each method below return a specific 
## information of the bank.
############################################################
##
##	Usage:
###			python getBankInfo.py <IFSC CODE> <REQUEST INFO>
###		Ex:
##			python getBankInfo.py HDFC0000001 ADDRESS
############################################################

import requests
import json
import sys


def getJson(ifsc):
	''' Returns the dictionary containing the information of bank ''' 
	API="https://ifsc.razorpay.com/"
	APIQ=API + ifsc

	resp=requests.get(APIQ)
	data=json.loads(json.dumps(resp.json()))
	return data

def getBranch(ifsc):
	''' Get bank's Branch information'''
	data=getJson(ifsc)
	try:
		bankbranch=data['BRANCH']
	except Exception as error:
		bankbranch = "Not Found"

	return bankbranch

def getState(ifsc):
	''' Get bank's State'''
	data=getJson(ifsc)
	try:
		bankstate=data['STATE']
	except Exception as error:
		bankstate = "Not Found"

	return bankstate

def getContact(ifsc):
	''' Get the bank's contact number '''
	data=getJson(ifsc)
	try:
		contact=data['CONTACT']
	except Exception as error:
		contact = "Not Found"

	return contact

def getCity(ifsc):
	''' Get bank's city '''
	data=getJson(ifsc)
	try:
		city=data['CITY']
	except Exception as error:
		city = "Not Found"

	return city

def getMICR(ifsc):
	''' Get bank's MICR code '''
	data=getJson(ifsc)
	try:
		micr=data['MICR']
	except Exception as error:
		micr = "Not Found"

	return micr

def getBank(ifsc):
	''' Get bank name '''
	data=getJson(ifsc)
	try:
		bank=data['BANK']
	except Exception as error:
		bank = "Not Found"

	return bank

def getIFSC(ifsc):
	''' Get bank's IFSC code '''
	data=getJson(ifsc)
	try:
		ifsc_code=data['IFSC']
	except Exception as error:
		ifsc_code = "Not Found"

	return ifsc_code

def getAddr(ifsc):
	''' Get bank's address '''
	data=getJson(ifsc)
	try:
		addr=data['ADDRESS']
	except Exception as error:
		addr = "Not Found"

	return addr

## In case the script is used in soltitude
if(__name__ == "__main__"):
	if(len(sys.argv) > 1):
		IFSC=sys.argv[1]
		REQUEST=sys.argv[2].upper()
	else:
		print("No IFSC given")
		sys.exit(1)

	if(REQUEST == "BRANCH"):
		branch=getBranch(IFSC)
		print(branch)
	elif(REQUEST == "STATE"):
		state=getState(IFSC)
		print(state)
	elif(REQUEST == "CITY"):
		city=getCity(IFSC)
		print(city)
	elif(REQUEST == "CONTACT"):
		contact=getContact(IFSC)
		print(contact)
	elif(REQUEST == "MICR"):
		micr=getMICR(IFSC)
		print(micr)
	elif(REQUEST == "ADDRESS"):
		addr=getAddr(IFSC)
		print(addr)
	elif(REQUEST == "BANK"):
		bank=getBank(IFSC)
		print(bank)
	elif(REQUEST == "IFSC"):
		ifsc_code=getIFSC(IFSC)
		print(ifsc_code)
	else:
		print("Invalid REQUEST")
