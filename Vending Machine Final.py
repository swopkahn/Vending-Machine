a = {'code': 101, 'item': 'KitKat', 'price': 5} #items, name of item, price, and number code
b = {'code': 102, 'item': 'Lays', 'price': 3.5}
c = {'code': 103, 'item': 'M&Ms', 'price': 4}
d = {'code': 104, 'item': 'Cheetos', 'price': 4}
e = {'code': 105, 'item': 'Snickers', 'price': 3.5}
f = {'code': 106, 'item': 'Beef Sandwich', 'price': 7.5}
g = {'code': 107, 'item': 'Oreo', 'price': 3.5}
h = {'code': 108, 'item': 'Veggie Sandwich', 'price': 7.5}
i = {'code': 109, 'item': 'Ritz', 'price': 3}
j = {'code': 110, 'item': 'Chicken Sandwich', 'price': 7.5}
k = {'code': 201, 'item': 'Capri-Sun', 'price': 4}
l = {'code': 202, 'item': 'Gatorade', 'price': 8}
m = {'code': 203, 'item': 'Chips Ahoy', 'price': 5}
n = {'code': 204, 'item': 'Chocolate Milk', 'price': 2}
o = {'code': 205, 'item': 'Water', 'price': 1}
p = {'code': 206, 'item': 'Red Bull', 'price': 7}
q = {'code': 207, 'item': 'Nescafe', 'price': 5}
r = {'code': 208, 'item': 'iCafe', 'price': 5}
s = {'code': 209, 'item': 'Coca Cola', 'price': 3.5}
t = {'code': 210, 'item': 'Mountain Dew', 'price': 3.5}
items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t] #list of items
money = 0

print(" ________________________ ") 
print("|  ____________________  |")
print("| | []  []  []  []  [] | |")
print("| |--------------------| |")
print("| | []  []  []  []  [] | |")
print("| |--------------------| |")
print("| | []  []  []  []  [] | |")
print("| |--------------------| |")
print("| | []  []  []  []  [] | |")
print("| |--------------------| |")
print("| |____________________| |")
print("| |  ________________  | |")
print("| | | COLLECT        | | |")
print("| | |           HERE | | |")
print("| |  ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅   | |")
print("|  ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅   |")
print("|̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ |")
print("|_|̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ |_|") #text art of vending machine

KitKat = 5 #assigning the products their prices
Lays = 3.5
MnMs = 4
Cheetos = 4
Snickers = 3.5
Beef_Sandwich = 7.5
Oreo = 3.5
Veggie_Sandwich = 7.5
Ritz = 3
Chicken_Sandwich = 7.5
Capri_Sun = 4
Gatorade = 8
Chips_Ahoy = 5
Chocolate_Milk = 2
Water = 1
Red_Bull = 7
Nescafe = 5
iCafe = 5
Coca_Cola = 3.5
Mountain_Dew = 3.5

def show(items): #defining "show(items)" to print out the items available and their code and price when the code is activated
    print('\nitems available \n')
    print("------------------------")
    for item in items:
        print(item.get('code'), item.get('item'), item.get('price'))

print("")
money = float(input("Input money: ")) #this lets the user input the amount of money they want to use
PurchaseAgain = True #this makes it so that the code is currently true on "Purchase Again"

while PurchaseAgain == True: #this starts the loop for the user when purchasing from the vending machine
    show(items) #this prints the codes inputed into the term "show(items)"
    print("------------------------")
    print("")
    Item_selection = input("Input code: ") #this allows the user to input the code of the product they want to purchase
    print("")

    if Item_selection == '101': #if item code 101 is selected, the user will go through this path
        print("Item selected = KitKat | Price = 5 ") #this code prints the item that has been selected and its price
        if money < KitKat: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= KitKat: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= KitKat #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour KitKat has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '102': #if item code 102 is selected, the user will go through this path
        print("Item selected = Lays | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Lays: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Lays: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Lays #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Lays has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '103': #if item code 103 is selected, the user will go through this path
        print("Item selected = M&Ms | Price = 4 ") #this code prints the item that has been selected and its price
        if money < MnMs: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= MnMs: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= MnMs #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour M&Ms has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '104': #if item code 104 is selected, the user will go through this path
        print("Item selected = Cheetos | Price = 4 ") #this code prints the item that has been selected and its price
        if money < Cheetos: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Cheetos: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Cheetos #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Cheetos has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '105': #if item code 105 is selected, the user will go through this path
        print("Item selected = Snickers | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Snickers: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Snickers: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Snickers #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Snickers has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '106': #if item code 106 is selected, the user will go through this path
        print("Item selected = Beef Sandwich | Price = 7.5 ") #this code prints the item that has been selected and its price
        if money < Beef_Sandwich: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Beef_Sandwich: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Beef_Sandwich #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Beef Sandwich has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '107': #if item code 107 is selected, the user will go through this path
        print("Item selected = Oreo | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Oreo: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Oreo: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Oreo #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Oreo has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '108': #if item code 108 is selected, the user will go through this path
        print("Item selected = Veggie Sandwich | Price = 7.5 ") #this code prints the item that has been selected and its price
        if money < Veggie_Sandwich: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Veggie_Sandwich: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Veggie_Sandwich #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Veggie Sandwich has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '109': #if item code 109 is selected, the user will go through this path
        print("Item selected = Ritz | Price = 3 ") #this code prints the item that has been selected and its price
        if money < Ritz: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Ritz: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Ritz #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Ritz has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '110': #if item code 110 is selected, the user will go through this path
        print("Item selected = Chicken Sandwich | Price = 7.5 ") #this code prints the item that has been selected and its price
        if money < Chicken_Sandwich: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Chicken_Sandwich: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Chicken_Sandwich #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Chicken Sandwich has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '201': #if item code 201 is selected, the user will go through this path
        print("Item selected = Capri-Sun | Price = 4 ") #this code prints the item that has been selected and its price
        if money < Capri_Sun: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Capri_Sun: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Capri_Sun #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Capri-Sun has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '202': #if item code 202 is selected, the user will go through this path
        print("Item selected = Gatorade | Price = 8 ") #this code prints the item that has been selected and its price
        if money < Gatorade: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Gatorade: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Gatorade #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Gatorade has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '203': #if item code 203 is selected, the user will go through this path
        print("Item selected = Chips Ahoy | Price = 5 ") #this code prints the item that has been selected and its price
        if money < Chips_Ahoy: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Chips_Ahoy: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Chips_Ahoy #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Chips Ahoy has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '204': #if item code 204 is selected, the user will go through this path
        print("Item selected = Chocolate Milk | Price = 2 ") #this code prints the item that has been selected and its price
        if money < Chocolate_Milk: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Chocolate_Milk: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Chocolate_Milk #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Chocolate Milk has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '205': #if item code 205 is selected, the user will go through this path
        print("Item selected = Water | Price = 1 ") #this code prints the item that has been selected and its price
        if money < Water: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Water: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Water #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Water has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '206': #if item code 206 is selected, the user will go through this path
        print("Item selected = Red Bull | Price = 7 ") #this code prints the item that has been selected and its price
        if money < Red_Bull: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Red_Bull: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Red_Bull #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Red Bull has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '207': #if item code 207 is selected, the user will go through this path
        print("Item selected = Nescafe | Price = 5 ") #this code prints the item that has been selected and its price
        if money < Nescafe: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Nescafe: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Nescafe #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Nescafe has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '208': #if item code 208 is selected, the user will go through this path
        print("Item selected = iCafe | Price = 5 ") #this code prints the item that has been selected and its price
        if money < iCafe: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= iCafe: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= iCafe #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour iCafe has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '209': #if item code 209 is selected, the user will go through this path
        print("Item selected = Coca Cola | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Coca_Cola: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Coca_Cola: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Coca_Cola #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Coca Cola has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    elif Item_selection == '210': #if item code 210 is selected, the user will go through this path
        print("Item selected = Mountain Dew | Price = 3.5 ") #this code prints the item that has been selected and its price
        if money < Mountain_Dew: #if the user's amount of money is less than the price of the product, the code will say "Insufficient Funds"
            print("Insufficient Funds")
        elif money >= Mountain_Dew: #if the user's amount of money is greater or equal to the price of the product, the code will continue
            money -= Mountain_Dew #the vending machine will take the user's money and minus it from the price of the product
            print('Change returned: ' + str(money) + "\nYour Mountain Dew has been dispensed.") #the code will print the amount of money the user has left
        #the code will inform the user that the product has been dispensed

    else: #if the code that the user inputted is not one of the product's codes, it will print "Invalid code"
        print("Invalid code")

    choice = input('Buy something else? (y/n): ') #this code gives the user the choice of if they want to purchase another item or not
    if choice == 'n': #if the user inputs "n" it goes through this path
        PurchaseAgain = False #the loop stops

        if money != 0: #if money is not equal to 0, the code goes through this path
            print(str(money) + ' money left') #this prints the amount of money the user has left
            money = 0 #this makes the amount of money return to zero
            print('Thank you for buying, come again soon!\n')
            break
        else: #if money is equal to 0, the code just prints the final message
            print('Thank you for buying, come again soon!\n')
            break
    else: #if the user inputs "y" the code loops back to "PurchaseAgain"
        continue