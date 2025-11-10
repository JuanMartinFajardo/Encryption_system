from random import random
def KeyCreator(seguridad,minimo,maxchar):
	key=[]
	prob=1/seguridad
	t=minimo
	while len(key)<136:
		t+=1
		if t>minimo+maxchar:
			while True:
				t+=1
				if random()<prob:
					key.append(t)
					minimo=t
					break
	return key




