from os import scandir,getcwd,getcwd,name,system
from os.path import abspath, basename
from ASCII import ASCII
import hashlib
from KeyCreator import KeyCreator
from encriptadorV4 import crypter
from WatDcrypt import dcrypter


current_script = abspath(__file__)

hasher = hashlib.sha256()

try:
	with open(current_script, 'rb') as f:
		while True:
			chunk = f.read(65536) 
			if not chunk:
				break
			hasher.update(chunk)
			
	Auto_hash = hasher.hexdigest()
	
except FileNotFoundError:
	Auto_hash = 0

def ks(ruta):
		return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]
CWD = getcwd()
svdm = str(CWD)+'/savedMessages/'



def clear_screen():
    """Clears the current screen without removing the history"""
    #Windows
    if name == 'nt':
        _ = system('cls')
    # Mac and Linux (use ANSI sequences)
    else:
        # \033[2J clears the screen
        # \033[H places the cursor to the top left corner
        print("\033[2J\033[H", end="")


def print_menu(hash_val):
    clear_screen()
    print('···ENCRYPTION SOFTWARE···')
    print('		-Create a new Key(1)')
    print('		-Encrypt a message(2)')
    print('		-Decrypt a message(3)')
    print('		-MyKeys(4)')
    print('		-My saved messages(5)')
    print('		-Settings(6)')
    print('		-Console(7)')
    print('		-Github (8)') 
    print('		-Close(9)')
    if hash_val != 0:
        print('The hash of this file is: \n' + str(hash_val))




print_menu(Auto_hash)

while True:
	
	try:
		FCT=int(input(('Select a function: ')))
	except:
		print_menu(Auto_hash)
	else:
		clear_screen()
		
		if FCT==1:
			seguridad=int(input('Write the security level in %: '))
			minimo=int(input('Write the minumun number which your want to be able to see in your key: '))
			maxchar=int(input('Write the maximum number of characters that can be encrypted with this key'))
			key=KeyCreator(seguridad,minimo,maxchar)
			print(key)
			name=input('How do you want to call this key? ')
			name_1=str(CWD)+'/KeyStore/'+str(name)
			f = open(str(name_1),'w')
			f.write(str(key))
			f.close()
			print('Your key has been saved correctly'+'\n'+'You can find it here: '+str(name_1))
			input("\nPress Enter to return to the menu...")

		elif FCT==2:
			directory = getcwd()+ str('/KeyStore/')
			keys=[]
			for i in ks(directory): keys.append(basename(i))
			print('Your keys:'+'\n'+str(keys))
			ruta=str(getcwd())+'/KeyStore/'
			name=input('Write the name of the key you want to use to encrypt the message:')
			name_=str(ruta)+str(name)
			f = open(str(name_),'r')
			t='key='+str(f.read())
			exec(t)
			f.close()
			print('The key ('+str(name)+') has been imported')
			mensaje=input('Write your message: ')
			msn=crypter(mensaje,key,ASCII)
			print(msn)
			new_msn_1=str(getcwd())+'/Agora/'
			new_msn_2=str(len(ks(new_msn_1))+1)
			new_msn=str(new_msn_1)+str(new_msn_2)+'.txt'
			f = open(str(new_msn),'w')
			f.write(str(msn))
			f.close()
			print('Your message has been saved in: '+new_msn)
			input("\nPress Enter to return to the menu...")

		elif FCT==3:
			keys=ks(str(CWD)+'/KeyStore/')
			messages=ks(str(CWD)+'/Agora/')
			mssgs = []
			kyss = []
			for i in keys: kyss.append(basename(i))
			for i in messages: mssgs.append(basename(i))
			print('Your messages: ',mssgs)
			name_m = input('Write the message number: ')
			namem = str(CWD)+'/Agora/'+str(name_m)+'.txt'
			m = open(str(namem),'r')
			y = 'msn='+str(m.read())
			exec(y)
			m.close()
			print('Your keys:     ',kyss)
			name_k = input('Write the key name: ')
			namek = str(CWD)+'/KeyStore/'+str(name_k)
			f = open(str(namek),'r')
			t = 'key='+str(f.read())
			exec(t)
			f.close()
			print('This process can take some time if the message is very long...')
			try:
				WatM = dcrypter(msn,key,ASCII)
			except:
				print('There was an error during the decrypting. Try with another key.')
			else:
				if WatM!=False:
					print('Your message is: '+'\n'+str(WatM)+'\n'+'It has been decrypted by: '+str(name_k)+'\n')
					if int(input('Press 1 if you want to save this decrypted message and 2 if not'))==1:
						f = open(str(svdm)+str(input('How do you want to call the message?'))+'.txt','w')
						f.write('Encrypted message:'+'\n'+str(msn)+'\n'+'\n'+'key:'+'\n'+str(key)+'\n'+'\n'+'Decrypted message:'+'\n'+str(WatM)+'\n'+'\n')
						f.close()
						print('Your message has been saved correctly. Be careful with your security.')
			input("\nPress Enter to return to the menu...")
			
		elif FCT==4:
			directory = getcwd()+ str('/KeyStore/')
			keys=[]
			for i in ks(directory):
				keys.append(basename(i))
			print('Your keys:'+'\n'+str(keys))
			input("\nPress Enter to return to the menu...")
			
		elif FCT==5:
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
			input("\nPress Enter to return to the menu...")

		elif FCT==6:
			print('I`m Sorry. This function isn`t available yet :(')
			input("\nPress Enter to return to the menu...")

		if FCT==7:
			print("I'm sorry. This function isn't available yet :(")
			input("\nPress Enter to return to the menu...")

		elif FCT==8:
			print("Visit my github for more: https://github.com/JuanMartinFajardo")
			input("\nPress Enter to return to the menu...")
			
		elif FCT==9:
			print('See you soon :)')
			break
		
		print_menu(Auto_hash)

