import json

class CredentialsManager:
    def __init__(self, filename):
        self.filename = filename
        self.credentials = []
        self.load_credentials()

    def load_credentials(self):
        try:
            with open(self.filename, 'r') as file:
                self.credentials = json.load(file)
        except FileNotFoundError:
            self.credentials = []

    def save_credentials(self):
        with open(self.filename, 'w') as file:
            json.dump(self.credentials, file, indent=4)

    def add_credentials(self, host, username, password):
        credential = {
            'host': host,
            'username': username,
            'password': password
        }
        self.credentials.append(credential)
        self.save_credentials()

    def remove_credentials(self, index):
        if index < 0 or index >= len(self.credentials):
            raise IndexError('Invalid credential index')
        del self.credentials[index]
        self.save_credentials()

    def get_credentials(self):
        return self.credentials
