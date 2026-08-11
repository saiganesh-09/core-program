'''Question 1

Write a function electricity(rate_per_unit).

-   The outer function receives the cost per unit.
-   The inner function receives the number of units consumed.
-   Print the total electricity bill.
-   Return the inner function.
def electricity(rate_per_unit):
    def inner(units):
        total=rate_per_unit*units
        print("electricity bill:",total)
    return inner
a=electricity(5)
a(100)
a(200)'''

'''Question 2

Write a function salary(bonus).

-   The outer function receives the bonus amount.
-   The inner function receives the employee’s basic salary.
-   Print the total salary after adding the bonus.
-   Return the inner function.
def salary(bonus):
    def basic_salary(salary):
        print(bonus+salary)
    return basic_salary
e1=salary(1000)
e1(10000)
------------------------------------------------------------------------'''

'''Question 3

Write a function discount(percent).
-   The outer function receives the discount percentage.
-   The inner function receives the product price.
-   Print the final price after applying the discount.
-   Return the inner function.
def discount(percent):
    def inner(price):
        discount=(price*percent)
        total=price-discount
        print("total price:",total)
    return inner
a=discount(10)
a(1500)
a(2300)'''

'''Question 4
Write a function bank_account(balance).

-   The outer function receives the initial balance.
-   The inner function receives an amount to withdraw.
-   Print the remaining balance.
-   Return the inner function.
def fun(balance):
    def inner(withdraw):
        total=balance-withdraw
        print(total)
    return inner
a=fun(10000)
a(5000)'''

'''
Question 5

Write a function movie(movie_name).

-   The outer function stores the movie name.
-   The inner function receives the person’s name.
-   Print that the person booked a ticket for the movie.
-   Return the inner function.
def movie(movie_name):
    def inner(name):
        print(f"{name} booked a ticket for the {movie_name}")
    return inner
a=movie("salaar")
a("sai")'''
'''
Question 6

Write a function multiplier(number).

-   The outer function receives one number.
-   The inner function receives another number.
-   Print their multiplication.
-   Return the inner function.
def fun(num):
    def inner(num2):
        return num*num2
    return inner
a=fun(10)
print(a(20))'''
'''
Question 7

Write a function restaurant(food_item).

-   The outer function stores the food item.
-   The inner function receives the quantity.
-   Print the order details.
-   Return the inner function.
def fun(food_item):
    def inner(quantity):
        print(f"{food_item} packed {quantity}")
    return inner
a=fun("Biryani")
a(2)'''
'''
Question 8

Write a function create_password(password).

-   The outer function stores the original password.
-   The inner function receives another password.
-   If both passwords are the same, print Access Granted; otherwise
    print Access Denied.
-   Return the inner function.
def fun(password):
    def inner(password2):
        if password==password2:
            print("Access Granted")
        else:
            print("Access Denied")
    return inner
a=fun("sai")
a("sai")'''
'''
Question 9

Write a function shopping_cart(item_name).

-   The outer function receives the item name.
-   The inner function receives:
    -   quantity
    -   price per item
-   Print the item name, quantity, and total price.
-   Return the inner function.
def fun(item):
    def inner(quantity,price):
        total=price*quantity
        print("item_name:",item)
        print("quantity:",quantity)
        print("total price:",price)
    return inner
a=fun("Choclates")
a(5,500)'''
'''Question 10

Create a function counter().

-   Inside it, initialize a variable count = 0.
-   Create an inner function that increments count by 1 every time it is
    called and prints the updated value.
-   Return the inner function.
-   Call the returned function five times.

def fun():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner
a=fun()
a()'''