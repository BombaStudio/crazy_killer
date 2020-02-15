import subprocess

print("mac changer started")

def mac(eth, macc):
	subprogress.call(["ifconfig",eth,"down"])
	subprogress.call(["ifconfig",eth,"hw","ether",macc])
	subprogress.call(["ifconfig",eth,"up"])
