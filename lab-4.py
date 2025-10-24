import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.name = ""
        self.phone = ""
        self.email = ""
        self.balance = ""
        self.credit_card = []
        self.debit_card = ""
    def create_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.acc_no = input("Enter Account Number: ")
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.balance = int(input("Enter Customer Balance: "))
    def debit(self, amount):
        print("Old Balance: ", self.balance)
        if self.balance < amount:
            print("Balance too low")
            did_not_work = 1
            return did_not_work
        else:
            self.balance -= amount
            print("New Balance: ", self.balance)
            did_not_work = 0
            return did_not_work
    def credit(self, amount):
        print("Old Balance: ", self.balance)
        self.balance += amount
        print("New Balance: ", self.balance)
    def display(self):
        print("Customer ID: ", self.cid)
        print("Account #: ", self.acc_no)
        print("Name: ", self.name)
        print("Phone: ", self.phone)
        print("Email: ", self.email)
        print("Balance: ", self.balance)
    def add_card(self, card, card_type):
        if card_type == "Credit":
            self.credit_card.append(card)
            print(f_card.card_no, "added to the account of ", f_customer.name, "as a credit card")
        elif card_type == "Debit":
            self.debit_card = card
            print(f_card.card_no, "added to the account of ", f_customer.name, "as a debit card")
        else:
            print("Invalid Card")

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.expiry_date = ""
        self.cvc = ""
        self.balance = ""
    def create_card(self):
        self.type = input("Enter Card Type (Credit/Debit): ")
        self.card_no = int(input("Enter Card Number: "))
        self.expiry_date = input("Enter Expiry Date: ")
        self.cvc = int(input("Enter CVC: "))
        self.balance = int(input("Enter Balance: "))
    def display(self):
        print("Card Type: ", self.type)
        print("Card Number: ", self.card_no)
        print("Expiry Date: ", self.expiry_date)
        print("CVC: ", self.cvc)
        print("Balance: ", self.balance)

def f_customer(to_find, customers_all):
    for find_c in customers_all:
        if find_c.cid == to_find:
            return find_c
    print("Customer not found")
    return None
def f_card(to_find, cards_all):
    for find_c in cards_all:
        if find_c.card_no == to_find:
            return find_c
    print("Card not found")
    return None

customer_file = open("bank_customers.dat", "rb")
all_customers = pickle.load(customer_file)
customer_file.close()
card_file = open("bank_cards.dat", "rb")
all_cards = pickle.load(card_file)
card_file.close()
while True:
    print("")
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer Funds")
    print("4. Assign Card")
    print("5. Display Customer")
    print("6. Display Card")
    print("7. Commit")
    print("0. Exit")
    op = input("Select Operation: ")
    print("")

    #Create Customer
    if op == "1":
        customer = Customer()
        customer.create_customer()
        all_customers.append(customer)

    #Create Card
    elif op == "2":
        card = Card()
        card.create_card()
        all_cards.append(card)

    #Transfer Funds
    elif op == "3":
        paying = input("Enter Account Number for the one Paying: ")
        paying_c = f_customer(paying, all_customers)
        paid = input("Enter Account Number for the one Being Paid: ")
        paid_c = f_customer(paid, all_customers)
        payment = int(input("Enter Payment Amount: "))
        failure = paying_c.debit(paid)
        if failure == 1:
            print("Payment Failed")
        else:
            paid_c.credit(payment)

    #Assign Card
    elif op == "4":
        fid = input("Enter Customer ID: ")
        f_customer = f_customer(fid, all_customers)
        fno = input("Enter Card Number: ")
        f_card = f_card(fno, all_cards)
        f_type = f_card.type
        f_customer.add_card(f_card, f_type)

    #Display Customer
    elif op == "5":
        fid = input("Enter Customer ID: ")
        f_customer = f_customer(fid, all_customers)
        f_customer.display()

    #Display Card
    elif op == "6":
        fno = input("Enter Card Number: ")
        f_card = f_card(fno, all_cards)
        f_card.display()

    #Commit
    elif op == "7":
        customer_file = open("bank_customers.dat", "wb")
        pickle.dump(all_customers, customer_file)
        customer_file.close()
        card_file = open("bank_cards.dat", "wb")
        pickle.dump(all_cards, card_file)
        card_file.close()

    #Exit
    elif op == "0":
        break

    else:

        print("Invalid Operation")
