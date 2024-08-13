while True:
    try:
        value = int(input("How many coins are there? Please enter an integer value."))
    except ValueError:
        print("That is an invalid answer. Please try again")
    else:
        break

# Initialize the pennies
coins = [1] * value

# Replace every coin in the needed place with the coin to be swapped at that position
x = 0
y = 1
coin_value = [5, 10, 25]

#simulate flipping each coin by hand using the rules pennies #, flip every second penny into a nickel, every third inot a dime, and every fourth into a quarter
for integer in range(3):
    x += 1
    y += 1
    for i in range(x, value, y):
        coins[i] = coin_value[integer]

money_value_cents = sum(coins)
money_value_cents = str(money_value_cents)
print('The cents value of the coins is: ¢' + money_value_cents)

#convert cents to dollars
index_to_insert = len(money_value_cents)-2
dot_char = "."
number_as_a_list = list(money_value_cents)
number_as_a_list.insert(index_to_insert, dot_char)
money_value_dollars = ''.join(number_as_a_list)
print('The value of the coins in dollars is: $' + money_value_dollars)