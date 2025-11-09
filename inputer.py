def inputer(stopper):
	toE=''
	while True:
		a = input('!:')
		if a==stopper: break
		else:
			toE+=str(a)
			toE+='\n'
	return toE
toE = inputer('Stop')
print(toE)
			
			