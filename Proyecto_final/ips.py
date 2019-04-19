from math import floor

def checkSegment(seg):
    if (int(seg) < 256) and (int(seg)>=0) and (seg[0] != '0'):
        return True
    else:
        return False

def checkIP(ip):
	segments = ip.split('.')
	for segment in segments:
		if not checkSegment(segment):
			return False
	return True


def combinations(ips):

	validIP = []

	l = len(ips)

	for i in range (3,0,-1):				#First byte
		for j in range (i+3,i,-1):			#Second byte
			for k in range (j+3,j,-1):		#Third byte
				ip = ips[0:i]+'.'+ips[i:j]+'.'+ips[j:k]+'.'+ips[k:l]
				if checkIP(ip):
					validIP.append(ip)

	return validIP


print(combinations("25525511135"))

