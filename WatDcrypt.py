def dcrypter(msn,key,ASCII):
	mensaje=[]
	length=0
	for i in msn[0]:
		if i in key:
			length+=msn[1][msn[0].index(i)]
	for p in range(0,length):
		mensaje.append(0)

	for i in key: 
		if i in msn[0]:
			if key.index(i) is 0:
				lim_1=0
			else:
				lim_1=key[key.index(i)-1]+1 
			lim_2=i
			interval=range(lim_1,lim_2)
			mtrx=[] 
			for k in range(0, msn[1][msn[0].index(i)]+1):     
				M=[]
				for t in interval:
					if t in msn[0]:
						if msn[1][msn[0].index(t)]>=k:
							M.append(t)
				mtrx.append(M)
			for k in mtrx:
				mensaje[len(k)]=ASCII[key.index(i)]
	if 0 not in mensaje:
		mensaje_final=''		
		for i in mensaje:
			mensaje_final+=str(i)
		return mensaje_final
	else:
		return False



