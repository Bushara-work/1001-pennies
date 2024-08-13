#ask for the amount of coins, until an integer is given
while True:
    try:
        coins = int(input("How many coins are there? Please enter an integer value."))
    except ValueError:
        print("That is an invalid answer. Please try again")
    else:
        break
#number of coin groups is how many times the group of 12 coins goes into the amount of coins we have, pattern since the coin value repeats in a pattern of 12
#pattern: penny, nickel, dime, quarter, penny, dime, penny, quarter, dime, nickel, penny, quarter
number_of_coin_groups, remaining_coin = divmod(coins, 12)

#add all the coin values in the pattern together get 119
#multiply the amount of these coin groups by the value of the group which is 119, to get the amount of cents we have from the group of 12 coins
coin_value_cents = number_of_coin_groups * 119

#sums of remaining coins calculted by hand
remaining_coins_total_value = {1:1, 2:6, 3:16, 4:41, 5:42, 6:52, 7:53, 8:78, 9:88, 10:93, 11:94}

#add the value of the remaining coins, the remainder, of our division/divmod
coin_value_cents += remaining_coins_total_value[remaining_coin]

coin_value_cents = str(coin_value_cents)
print('The cents value of the coins is: ¢' + coin_value_cents)

#insert a '.' to the 3rd last position to turn the cents value into the dollars value, in a dolars variable
index_to_insert = len(coin_value_cents)-2
dot_char = "."
number_as_a_list = list(coin_value_cents)
number_as_a_list.insert(index_to_insert, dot_char)
money_value_dollars = ''.join(number_as_a_list)
print('The value of the coins in dollars is: $' + money_value_dollars)