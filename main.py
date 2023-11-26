print("Welcome to the tip calculator!")
while(True):
    try:
        bill = float(input("What was the total bill? $"))
        people_count = int(input("How many people to split the bill? "))
        percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

        tip_bill = (bill * (1 + (percentage / 100))) / people_count

        print(f"Each person should pay: ${round(tip_bill, 2)}")
        break
    except:
        print("Enter valid numbers")
        continue