###################################################
### Test cases for getBankInfo script
### Usage: pytest -q test_getBankInfo.py
###			or
###		   python -m pytest test_getBankInfo.py
###################################################
import getBankInfo
import pytest

def test_getBranch():
	ret=getBankInfo.getBranch('HDFC0000077')
	assert ret == "BANGALORE - IT PARK"

def test_getState():
	ret=getBankInfo.getState('HDFC0000077')
	assert ret == "KARNATAKA"
	
def test_getContact():
	ret=getBankInfo.getContact('HDFC0000077')
	assert ret == "9945863333"

def test_getCity():
	ret=getBankInfo.getCity('HDFC0000077')
	assert ret == "BANGALORE URBAN"
	
def test_getMICR():
	ret=getBankInfo.getMICR('HDFC0000077')
	assert ret == "560240006"
	
def test_getBank():
	ret=getBankInfo.getBank('HDFC0000077')
	assert ret == "HDFC Bank"
	
def test_getIFSC():
	ret=getBankInfo.getIFSC('HDFC0000077')
	assert ret == "HDFC0000077"
	
def test_getAddr():
	ret=getBankInfo.getAddr('HDFC0000077')
	assert ret == "G-O1 DISCOVERER BLDGI.T. PARK,WHITEFIELD ROADBANGALOREKARNATAKA560066"

def test_wrong_ifsc():
	ret=getBankInfo.getIFSC('HDFC11111')
	assert ret == "Not Found"