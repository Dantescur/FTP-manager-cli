import ftplib
import os
from colorama import Fore

class FTPManager:
    def __init__(self):
        self.ftp = ftplib.FTP()

    def ftp_login(self, host, username, password):
        self.ftp.connect(host)
        self.ftp.login(username, password)
        print(Fore.GREEN + f"Conectado al servidor FTP: {host}")

    def ftp_logout(self):
        self.ftp.quit()
        print(Fore.GREEN + 'Sesión FTP cerrada exitosamente.')

    def list_files(self):
        data = []
        self.ftp.retrlines('LIST', data.append)
        for line in data:
            print(line)

    def download_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                self.ftp.retrbinary(f'RETR {filename}', file.write)
            print(Fore.GREEN + f"Archivo '{filename}' descargado exitosamente.")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al descargar el archivo: {e}")

    def remove_file(self, filename):
        try:
            self.ftp.delete(filename)
            print(Fore.GREEN + f"Archivo '{filename}' eliminado exitosamente.")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al eliminar el archivo: {e}")

    def upload_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.ftp.storbinary(f'STOR {filename}', file)
            print(Fore.GREEN + f"Archivo '{filename}' cargado exitosamente.")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al cargar el archivo: {e}")

    def create_directory(self, directory):
        try:
            self.ftp.mkd(directory)
            print(Fore.GREEN + f"Directorio '{directory}' creado exitosamente.")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al crear el directorio: {e}")

    def remove_directory(self, directory):
        try:
            self.ftp.rmd(directory)
            print(Fore.GREEN + f"Directorio '{directory}' eliminado exitosamente.")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al eliminar el directorio: {e}")

    def change_directory(self, directory):
        try:
            self.ftp.cwd(directory)
            print(Fore.GREEN + f"Directorio cambiado a '{directory}'")
        except ftplib.error_perm as e:
            print(Fore.RED + f"Error al cambiar al directorio: {e}")
