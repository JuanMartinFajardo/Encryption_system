print('#WAT1#WAT2#WAT3#WAT4#WAT5#···WATCRYPTION SOFTWARE···#WAT5#WAT#WAT4#WAT3#WAT2#WAT1#')
print('		-Create a new Key(1)')
print('		-Encrypt a message(2)')
print('		-Decrypt a message(3)')
print('		-MyKeys(4)')
print('		-My saved messages(5)')
print('		-Settings(6)')
print('		-Console(7)')
print('		-Close(8)')


import shutil
from os import scandir,getcwd,chdir,getcwd
from os.path import abspath, basename
from random import choice,random,randint
from ASCII import ASCII

def ks(ruta):
		return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
CWD = getcwd()
svdm = str(CWD)+'/savedMessages/'

while True:
	
	FCT=int(input(('Select a function: ')))
	
	if FCT is 1:
		seguridad=int(input('Write the security level in %: '))
		minimo=int(input('Write the minumun number which your want to be able to see in your key: '))
		maxchar=int(input('Write  characters limit for the encrypted by this key messages: '))
		from KeyCreator import KeyCreator
		key=KeyCreator(seguridad,minimo,maxchar)
		print(key)
		name=input('How do you want to call this key? ')
		name_1=str(CWD)+'/KeyStore/'+str(name)
		f = open(str(name_1),'w')
		f.write(str(key))
		f.close()
		print('Your key has been saved correctly'+'\n'+'You can find it here: '+str(name_1))

	if FCT is 2:
		from encriptadorV4 import crypter
		ruta=str(getcwd())+'/KeyStore/'
		print('Your keys:',ks(ruta))
		name=input('Write the name of the key which you want to encrypt the message with: ')
		name_=str(ruta)+str(name)
		f = open(str(name_),'r')
		t='key='+str(f.read())
		exec(t)
		f.close()
		print('The key ('+str(name)+') has been imported from :'+'\n'+str(key))
		mensaje=input('Write your .wat message: ')
		msn=crypter(mensaje,key,ASCII)
		print(msn)
		new_msn_1=str(getcwd())+'/Agora/'
		new_msn_2=str(len(ks(new_msn_1))+1)
		new_msn=str(new_msn_1)+str(new_msn_2)+'.wat'
		f = open(str(new_msn),'w')
		f.write(str(msn))
		f.close()



	if FCT is 3:
		from WatDcrypt import decode
		keys=ks(str(CWD)+'/KeyStore/')
		messages=ks(str(CWD)+'/Agora/')
		mssgs = []
		kyss = []
		for i in keys: kyss.append(basename(i))
		for i in messages: mssgs.append(basename(i))
		print('Your keys:     ',kyss)
		print('Your messages: ',mssgs)
		name_m = input('Write the message number: ')
		namem = str(CWD)+'/Agora/'+str(name_m)+'.wat'
		m = open(str(namem),'r')
		y = 'msn='+str(m.read())
		exec(y)
		m.close()
		name_k = input('Write the key name: ')
		namek = str(CWD)+'/KeyStore/'+str(name_k)
		f = open(str(namek),'r')
		t = 'key='+str(f.read())
		exec(t)
		f.close()
		print('This process can take some minutes...')
		WatM = decode(msn,key,ASCII)
		if WatM!=False:
			print('Your .wat message is: '+'\n'+str(WatM)+'\n'+'It has been decrypted by: '+str(name_k)+'\n')
			if int(input('Press 1 if you want to save this decrypted message')) is 1:
				f = open(str(svdm)+str(input('How do you want to call the message?'))+'.txt','w')
				f.write('Encrypted message:'+'\n'+str(msn)+'\n'+'\n'+'key:'+'\n'+str(key)+'\n'+'\n'+'Decrypted message:'+'\n'+str(WatM)+'\n'+'\n')
				f.close()
				print('Your message has been saved correctly. Be careful with your security.')

	if FCT is 4:
		from os import scandir,getcwd,chdir,getcwd
		from os.path import abspath, basename
		directory = getcwd()+ str('/KeyStore/')
		keys=[]
		for i in ks(directory):
			keys.append(basename(i))
		print('Your keys:'+'\n'+str(keys))	
		

	if FCT is 5:
		SM_=[]
		if len(ks(svdm))>0:
			for i in ks(svdm):
				SM_.append(basename(i))
			print('Your saved messages:'+'\n'+str(SM_))
			t = input('Write the name of the message that you want to open(press "/" to exit) ')
			if t!='/':
				f = open(str(svdm)+str(t)+'.txt','r')
				print(f.read())
				f.close()
		else: print('You haven`t got saved messages.'+'\n')

	if FCT is 6:
		print('I`m Sorry. This function isn`t available yet :(')

	if FCT is 7:
		print("I'm sorry. This function isn't available yet :(")

	if FCT is 8:
		print('Thanks for using .wat decrypter '+'\n'+'See you soon :)')
		break

	else:
		print('Please, choose one of these options: ')
		print('		-Create a new Key(1)')
		print('		-Encrypt a message(2)')
		print('		-Decrypt a message(3)')
		print('		-MyKeys(4)')
		print('		-My saved messages(5)')
		print('		-Settings(6)')
		print('		-Console(7)')
		print('		-Close(8)')

