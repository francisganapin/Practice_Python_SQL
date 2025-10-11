balance = 5000
withdraw = int(input("Enter amonth to withdraw: "))

if withdraw <= balance:
    balance -= withdraw
    print("Withdraw successful. New Banalance")
else:
    print("Insufficient fund")