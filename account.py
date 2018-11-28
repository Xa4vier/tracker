import csv

def save_account(account):
    with open('data/account.csv', 'w') as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(account)