
def padding_zero(st,ln):
	if len(st) < ln:
		return "0"*(ln - len(st)) + st
	return st

def generator():
	# range(min , max)
	# format YYYYMMDD
	year = (2020,2020)
	month = (11,12)
	day = (00,31)
	result = ""
	for y in range(year[0],year[1]+1):
		for m in range(month[0],month[1]+1):
			m = padding_zero(str(m),2)
			for d in range(day[0],day[1]+1):
				d = padding_zero(str(d),2)
				result += str(y) + str(m) + str(d) + '\n'
	return result[:-1]

with open("./wordlist","w+") as f:
	f.write(generator())
