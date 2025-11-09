def KeyCreator(seguridad,minimo,maxchar):
	from random import random
	key=[]
	prob=1/seguridad
	t=minimo
	while True:
		t+=1
		if t>minimo+maxchar:
			while True:
				t+=1
				if random()<prob:
					key.append(t)
					minimo=t
					break
		if len(key)==136:
			break
	return key




