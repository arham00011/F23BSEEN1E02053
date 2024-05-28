class LeaveBalanceCalculator:
    def __init__(self, total_leave_allowed):
        self.total_leave_allowed = total_leave_allowed

    def calculate_leave_balance(self, leave_taken):
        leave_balance = self.total_leave_allowed - leave_taken
        return leave_balance

# Ask the user for the total leave allowed
total_leave_allowed = int(input("Enter the total number of leave days allowed: "))

# Ask the user for the leave taken
leave_taken = int(input("Enter the number of leave days already taken: "))

# Create an instance of LeaveBalanceCalculator
leave_calculator = LeaveBalanceCalculator(total_leave_allowed)

# Calculate the leave balance
balance = leave_calculator.calculate_leave_balance(leave_taken)

# Print the leave balance
print("Your leave balance is:", balance)