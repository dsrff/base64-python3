b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def prepareString(fstr):
	outstr = ''.join([format(ord(i),'b').zfill(8) for i in fstr])
	while len(outstr) % 6 != 0: outstr += '0'
	b64string = ''.join([b64chars[int(sb,2)] for sb in [outstr[i:i+6] for i in range(0,len(outstr),6)]])
	while len(b64string) % 4 != 0: b64string += '='
	return b64string
while True:
	print(prepareString(input('Enter text: ')))
