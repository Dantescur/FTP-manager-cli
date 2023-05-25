import os
from colorama import init, Fore
from credentials_manager import CredentialsManager
from ftp_manager import FTPManager

# Inicializar Colorama
init(autoreset=True)

# Nombre del archivo JSON de credenciales
CREDENTIALS_FILE = 'credentials.json'

def print_credentials(credentials):
    print(Fore.YELLOW + 'Credenciales disponibles:')
    for i, credential in enumerate(credentials):
        print(f"[{i}] Host: {credential['host']}, Username: {credential['username']}")

def select_credential():
    credentials = credentials_manager.get_credentials()
    print_credentials(credentials)

    while True:
        try:
            index = int(input('Selecciona un número de credencial para conectar: '))
            if index < 0 or index >= len(credentials):
                print(Fore.RED + 'Índice de credencial no válido. Intenta nuevamente.')
            else:
                return credentials[index]
        except ValueError:
            print(Fore.RED + 'Valor no válido. Intenta nuevamente.')

# Instanciar el administrador de credenciales
credentials_manager = CredentialsManager(CREDENTIALS_FILE)

# Instanciar el administrador de FTP
ftp_manager = FTPManager()

# Menú principal
while True:
    print(Fore.YELLOW + 'Operaciones disponibles:')
    print('1. Ver credenciales guardadas.')
    print('2. Agregar nuevas credenciales.')
    print('3. Eliminar credenciales existentes.')
    print('4. Conectar a un servidor FTP.')
    print('5. Salir.')

    try:
        option = int(input('Selecciona una opción: '))
        if option == 1:
            credentials = credentials_manager.get_credentials()
            print_credentials(credentials)
        elif option == 2:
            host = input('Ingrese el host: ')
            username = input('Ingrese el nombre de usuario: ')
            password = input('Ingrese la contraseña: ')
            credentials_manager.add_credentials(host, username, password)
            print(Fore.GREEN + 'Credenciales agregadas exitosamente.')
        elif option == 3:
            credentials = credentials_manager.get_credentials()
            print_credentials(credentials)
            index = int(input('Selecciona el número de credencial a eliminar: '))
            credentials_manager.remove_credentials(index)
            print(Fore.GREEN + 'Credencial eliminada exitosamente.')
        elif option == 4:
            credentials = credentials_manager.get_credentials()
            print_credentials(credentials)
            index = int(input('Selecciona un número de credencial para conectar: '))
            credential = credentials[index]
            ftp_manager.ftp_login(credential['host'], credential['username'], credential['password'])
            print(Fore.GREEN + f"Conectado al servidor FTP: {credential['host']}")
            while True:
                print(Fore.YELLOW + 'Operaciones disponibles:')
                print('1. Ver archivos y directorios.')
                print('2. Navegar a un directorio.')
                print('3. Descargar archivo.')
                print('4. Eliminar archivo.')
                print('5. Cargar archivo.')
                print('6. Crear directorio.')
                print('7. Eliminar directorio.')
                print('8. Cerrar sesión FTP.')

                try:
                    option_ftp = int(input('Selecciona una opción: '))
                    if option_ftp == 1:
                        ftp_manager.list_files()
                    elif option_ftp == 2:
                        directory = input('Introduce el nombre del directorio al que deseas navegar: ')
                        ftp_manager.change_directory(directory)
                    elif option_ftp == 3:
                        filename = input('Introduce el nombre del archivo que deseas descargar: ')
                        ftp_manager.download_file(filename)
                    elif option_ftp == 4:
                        filename = input('Introduce el nombre del archivo que deseas eliminar: ')
                        ftp_manager.remove_file(filename)
                    elif option_ftp == 5:
                        filename = input('Introduce el nombre del archivo que deseas cargar: ')
                        ftp_manager.upload_file(filename)
                    elif option_ftp == 6:
                        directory = input('Introduce el nombre del directorio que deseas crear: ')
                        ftp_manager.create_directory(directory)
                    elif option_ftp == 7:
                        directory = input('Introduce el nombre del directorio que deseas eliminar: ')
                        ftp_manager.remove_directory(directory)
                    elif option_ftp == 8:
                        ftp_manager.ftp_logout()
                        print(Fore.GREEN + 'Sesión FTP cerrada exitosamente.')
                        break
                    else:
                        print(Fore.RED + 'Opción no válida. Intenta nuevamente.')
                except ValueError:
                    print(Fore.RED + 'Valor no válido. Intenta nuevamente.')

        elif option == 5:
            break
        else:
            print(Fore.RED + 'Opción no válida. Intenta nuevamente.')
    except ValueError:
        print(Fore.RED + 'Valor no válido. Intenta nuevamente.')
