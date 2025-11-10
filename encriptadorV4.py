from random import choice,random,randint

def crypter(mensaje,key,ASCII):
	primos, nat = range(1,max(key)), True
	simplified=[]
	for i in mensaje: 
		if i not in simplified: simplified.append(i)
	def IndexReturner(x,mensaje):
		Vect=[]
		p=0
		for k in mensaje:
			if k is x:
				Vect.append(p)
			p+=1
		return Vect
	def intervalo(x,mensaje,key,ASCII,primos):
		if ASCII.index(x)==0:
			lim_1=0
		else:
			lim_1=primos.index(key[ASCII.index(x)-1])+1
			
		lim_2=primos.index(key[ASCII.index(x)])
		intervalo=primos[lim_1:lim_2]
		return intervalo
	def posicionador(x,mensaje,primos,key,ASCII):
		v=IndexReturner(x,mensaje)
		interval=intervalo(x,mensaje,key,ASCII,primos)
		M=[]
		capa_1=[]
		for n in range(0,max(v)):
			while True:
				chosen=choice(interval)
				if chosen not in capa_1:
					capa_1.append(chosen)
					break
		M.append(capa_1)
		v.pop()
		while len(v)>0:
			capa=[]
			last=M[len(M)-1]
			for i in range(0,max(v)):
				while True:
					chosen=choice(last)
					if chosen not in capa:
						capa.append(chosen)
						break
			M.append(capa)
			capa=[]
			v.pop()
		
		end=[]
		for i in M:
			for k in i:
				end.append(k)
		for i in range(0,mensaje.count(x)):
			end.append(key[ASCII.index(x)])
		return end
	mensaje_1=[]					
	for t in simplified:
		mtrx=posicionador(t,mensaje,primos,key,ASCII)
		mensaje_1.extend(mtrx)
	srtd=sorted(mensaje_1)
	msn=[[],[]]
	for i in srtd: 
		if i not in msn[0]:
			msn[0].append(i)
	for i in msn[0]:
		exp=srtd.count(i)
		msn[1].append(exp)
	if int(input('Press 1 if you want to add some noise to the code to make it more difficult to break. Press 2 otherwise.'))!=1: return msn	
	else:
		security = int(input('Write the security you want for your message in %:'))
		ssp = max(key)
		while True:
			ssp+=1
			if random()<2/security:
				msn[0].append(ssp)
				while True:
					p_1=range(1,choice(msn[1])+(security-randint(1,security)))
					if p_1!=range(1,1): break
				msn[1].append(choice(p_1)) 
			if random()<1/pow(security,2): break
		return msn





