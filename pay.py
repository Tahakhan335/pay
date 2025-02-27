import datetime

# 1. Display several numbers
print("Numbers: 10, 20, 30, 40, 50")

# 2. Solve and show the summation of 64 + 32
sum1 = 64 + 32
print("Sum of 64 + 32:", sum1)

# 3. Do the same as in 2, but make it sum = x + y
x = 64
y = 32
sum2 = x + y
print("Sum of x + y:", sum2)

# 4. Print the word ‘Lucky’ inside s
s = "Lucky"
print("The word inside s:", s)

# 5. Print the day, month, year in the format “Today is 2/2/2016”
today = datetime.date.today()
formatted_date = today.strftime("Today is %-m/%-d/%Y")  # Adjust formatting based on OS
print(formatted_date)

# 6. Ask user for phone number and display it
phone_number = input("Enter your phone number: ")
print("Your phone number is:", phone_number)