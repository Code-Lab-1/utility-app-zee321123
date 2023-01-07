print("")
print ("---WELCOME TO DRINKS AND SNACKS CORNER---")
print("")
#SELECT YOUR LANGUAGE
print("LANGUAGE= ENGLISH/ARABIC")
LANGUAGE = {
    '1':'english',
    '2':'arabic'
}
print("")
Language_code=input('PLEASE SELECT YOUR LANGUAGE : ')
if Language_code== 'ENGLISH':
    print("---YOU HAVE SELECTED ENGLISH---")
elif Language_code=='ARABIC':
    print("---YOU HAVE SELECTED ARABIC---")


#CREATING MENU AND ARRANGING ITEMS IN MENU

print (":--------------MENU----------------:")
print ("| 1) WATER = 90 AED                |")
print ("| 2) pepsi = 50 AED                |")
print ("| 3) COLD COFFEE = 100 AED         |")
print ("| 4) CAPPUCCINO = 150 AED          |")
print ("| 5) TEA = 20 AED                  |")
print ("| 6) ORANGE JUICE = 60 AED         |")
print ("| 7) mixed fruit juice = 180 AED   |")
print ("| 8) LAYS CHIPS = 20 AED           |")
print ("| 9) CHEETOS CHIPS = 40 AED        |")
print ("| 10) PRINGLES CHIPS = 70 AED      |")
print ("| 11) POTATO CHIPS = 25 AED        |")   
print ("| 12) TOMATO CHIPS = 35 AED        |")      
print (":----------------------------------:")

print("---stocks available-----------------")
print("(1)water quantity 10 pcs")
print("(2)PEPSI quantity 8 pcs")
print("(3)COLD_COFFEE quantity 6 pcs")
print("(4)CAPPUCCINO quantity 9 pcs")
print("(5)TEA quantity 15 pcs")
print("(6)ORANGE_JUICE quantity 4 pcs")
print("(7)MIXED_FRUIT_JUICE quantity 2 pcs")
print("(8)LAYS_CHIPS quantity 3 pcs")
print("(9)CHEETOS_CHIPS quantity 5 pcs")
print("(10)PRINGLES_CHIPS quantity 20 pcs")
print("(11)POTATO_CHIPS quantity 16 pcs")
print("(12)TOMATO_CHIPS quantity 32 pcs")
print("------------------------------------")
print()



print ("PLEASE SELECT YOUR ITEM BY ENTERING THE PRODUCT CODE!")
print ("")

#ARRANGING ITEMS ACCORDING TO CODE

WATER = 90
PEPSI = 50
COLD_COFFEE = 100
CAPPUCCINO = 150
TEA = 20
ORANGE_JUICE = 60
MIXED_FRUIT_JUICE = 180
LAYS_CHIPS = 20
CHEETOS_CHIPS = 40
PRINGLES_CHIPS = 70
POTATO_CHIPS = 25
TOMATO_CHIPS = 35

#THE PRODUCT CODE WILL BE USED TO SELECT AN ITEM


drink_choice = int(input("PLEASE ENTER THE PRODUCT CODE : "))

#CODE FOR MANAGING MONEY

money = int(input("PLEASE INSERT CASH OR CREDIT CARD : "))

if drink_choice == 1:
    if money >= WATER:
        print ("YOU SELECTED WATER")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - WATER
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---WATER = 90 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = WATER - money
        print (money)
        
if drink_choice == 2:
    if money >= PEPSI:
        print ("YOU SELECTED PEPSI")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - PEPSI
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---PEPSI = 50 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = PEPSI - money
        print (money)


if drink_choice == 3:
    if money >= COLD_COFFEE:
        print ("YOU SELECTED COLD_COFFEE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - COLD_COFFEE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---COLD_COFFEE = 100 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = COLD_COFFEE - money
        print (money)

if drink_choice == 4:
    if money >= CAPPUCCINO:
        print ("YOU SELECTED CAPPUCCINO")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - CAPPUCCINO
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---CAPPUCCINO = 150 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = CAPPUCCINO - money
        print (money)

if drink_choice == 5:
    if money >= TEA:
        print ("YOU SELECTED  TEA")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")

        money = money - TEA
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---TEA = 20 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = TEA - money
        print (money)

if drink_choice == 6:
    if money >= ORANGE_JUICE:
        print ("YOU SELECTED ORANGE_JUICE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - ORANGE_JUICE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT---")
        print ("---ORANGE_JUICE = 60 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = ORANGE_JUICE - money
        print (money)
    
if drink_choice == 7:
    if money >= MIXED_FRUIT_JUICE:
        print ("YOU SELECTED MIXED_FRUIT_JUICE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - MIXED_FRUIT_JUICE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------------")
        print ("---MIXED_FRUIT_JUICE = 180 AED")
        print ("---THANKYOU VISIT AGAIN---------")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = MIXED_FRUIT_JUICE - money
        print (money)

if drink_choice == 8:
    if money >= LAYS_CHIPS:
        print ("YOU SELECTED  LAYS CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - LAYS_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---LAYS_CHIPS = 20 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = LAYS_CHIPS - money
        print (money)

if drink_choice == 9:
    if money >= CHEETOS_CHIPS:
        print ("YOU SELECTED CHEETOS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - CHEETOS_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---CHEETOS = 40 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = CHEETOS_CHIPS - money
        print (money)

if drink_choice == 10:
    if money >= PRINGLES_CHIPS:
        print ("YOU SELECTED PRINGLES_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - PRINGLES_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---PRINGLES_CHIPS = 70 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = PRINGLES_CHIPS - money
        print (money)

if drink_choice == 11:
    if money >= POTATO_CHIPS:
        print ("YOU SELECTED POTATO_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - POTATO_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---POTATO_CHIPS = 25 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = POTATO_CHIPS - money
        print (money)

if drink_choice == 12:
    if money >= TOMATO_CHIPS:
        print ("YOU SELECTED TOMATO_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - TOMATO_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---TOMATO_CHIPS = 35 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = TOMATO_CHIPS - money
        print (money)
print("")
user_input = input("would you like to buy something else?(yes/no): ").lower()
if user_input == "yes":print("please follow the steps again")

elif user_input == "no":print("have a great day hope to see you again")
                    
else:
                    print("Invalid command")
                    choice = 1

drink_choice = int(input("PLEASE ENTER THE PRODUCT CODE : "))
money = int(input("PLEASE INSERT CASH OR CREDIT CARD : "))

if drink_choice == 1:
    if money >= WATER:
        print ("YOU SELECTED WATER")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - WATER
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---WATER = 90 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = WATER - money
        print (money)

if drink_choice == 2:
    if money >= PEPSI:
        print ("YOU SELECTED PEPSI")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - PEPSI
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---PEPSI = 50 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = PEPSI - money
        print (money)


if drink_choice == 3:
    if money >= COLD_COFFEE:
        print ("YOU SELECTED COLD_COFFEE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - COLD_COFFEE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---COLD_COFFEE = 100 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = COLD_COFFEE - money
        print (money)

if drink_choice == 4:
    if money >= CAPPUCCINO:
        print ("YOU SELECTED CAPPUCCINO")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - CAPPUCCINO
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---CAPPUCCINO = 150 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = CAPPUCCINO - money
        print (money)

if drink_choice == 5:
    if money >= TEA:
        print ("YOU SELECTED  TEA")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")

        money = money - TEA
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---TEA = 20 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = TEA - money
        print (money)

if drink_choice == 6:
    if money >= ORANGE_JUICE:
        print ("YOU SELECTED ORANGE_JUICE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - ORANGE_JUICE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT---")
        print ("---ORANGE_JUICE = 60 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = ORANGE_JUICE - money
        print (money)
    
if drink_choice == 7:
    if money >= MIXED_FRUIT_JUICE:
        print ("YOU SELECTED MIXED_FRUIT_JUICE")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - MIXED_FRUIT_JUICE
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------------")
        print ("---MIXED_FRUIT_JUICE = 180 AED")
        print ("---THANKYOU VISIT AGAIN---------")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = MIXED_FRUIT_JUICE - money
        print (money)

if drink_choice == 8:
    if money >= LAYS_CHIPS:
        print ("YOU SELECTED  LAYS CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - LAYS_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---LAYS_CHIPS = 20 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = LAYS_CHIPS - money
        print (money)

if drink_choice == 9:
    if money >= CHEETOS_CHIPS:
        print ("YOU SELECTED CHEETOS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - CHEETOS_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---CHEETOS = 40 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = CHEETOS_CHIPS - money
        print (money)

if drink_choice == 10:
    if money >= PRINGLES_CHIPS:
        print ("YOU SELECTED PRINGLES_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - PRINGLES_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---PRINGLES_CHIPS = 70 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = PRINGLES_CHIPS - money
        print (money)

if drink_choice == 11:
    if money >= POTATO_CHIPS:
        print ("YOU SELECTED POTATO_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - POTATO_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---POTATO_CHIPS = 25 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = POTATO_CHIPS - money
        print (money)

if drink_choice == 12:
    if money >= TOMATO_CHIPS:
        print ("YOU SELECTED TOMATO_CHIPS")
        print ("THANK YOU FOR YOUR PURCHASE")
        print ("YOUR ORDER HAS BEEN DISPENSED")
        money = money - TOMATO_CHIPS
        print ("YOUR CHANGE IS", money)
        print ("PLEASE TAKE YOUR RECEIPT")
        print ("---RECEIPT----------------")
        print ("---TOMATO_CHIPS = 35 AED")
        print ("---THANKYOU VISIT AGAIN---")
    else:
        print ("YOUR AMOUNT IS INSUFFICIENT TRY AGAIN")
        money = TOMATO_CHIPS - money
        print (money)