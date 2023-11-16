import getpass

# Function to authenticate user
def authenticate():
    with open('user_data.txt', 'r') as f:
        lines = f.readlines()

    username = input("Enter username: ")
    password = input("Enter password: ")

    valid_credentials = False

    for line in lines:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            valid_credentials = True
            break

    if valid_credentials:
        return True
    else:
        print("Invalid login credentials.")
        return False

# Function to process employee data and write results to a file
def process_employees(num_employees):
    # Create an empty list to store employee data
    employee_records = []

    # Loop to get employee details
    for i in range(num_employees):
        name = input("Enter the name of employee " + str(i+1) + ": ")
        gross_income = float(input("Enter the gross income of employee " + str(i+1) + ": "))

        # Calculate PAYE (30% of gross income) and round to 1 decimal place
        paye = round(gross_income * 0.3, 1)

        # Calculate net income and round to 1 decimal place
        net_income = round(gross_income - paye, 1)

        # Append employee data to the list with a serial number
        employee_records.append((i+1, name, round(gross_income, 1), paye, net_income))

    # Write results to a text file in tabular format
    with open('employee_data.txt', 'w') as f:
        # Header
        f.write("{:<15} {:<20} {:<15} {:<15} {:<15}\n".format("Serial Number", "Name", "Gross Income", "PAYE", "Net Income"))
        for record in employee_records:
            f.write("{:<15} {:<20} {:<15} {:<15} {:<15}\n".format(*record))

    print("Employee data has been written to employee_data.txt.")

# Main program
def main():
    # Authenticate user
    authenticated = False
    while not authenticated:
        authenticated = authenticate()
        if not authenticated:
            retry = input("Authentication failed. Do you want to retry? (yes/no): ").lower()
            if retry != 'yes':
                print("Exiting program.")
                return

    # If authenticated, proceed to process employees
    num_employees = int(input("Enter the number of employees to process: "))
    process_employees(num_employees)

if __name__ == "__main__":
    main()
