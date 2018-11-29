import csv
from domein.userManagement import get_user

def load_account_file():
    with open('data/account.csv', 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    account = [i for i in your_list[0]]
    return account


def save_account_to_file(user):
    with open('data/account.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(user)
        return 'succes'

class Account():
    def __init__(self, id, name):
        self.id = id
        self.name = name