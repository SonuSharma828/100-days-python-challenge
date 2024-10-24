import time  # Importing time module for delays to simulate processing

# List of problems and available doctors with their details
problem_doctor = [
    {
        'problem': 'cancer',
        'doctor': 'Dr.Jhon',
        'open_time': '9:00am',
        'close_time': '5:00pm',
        'fee': 500
    },
    {
        'problem': 'diabetes',
        'doctor': 'Dr.Mike',
        'open_time': '10:00am',
        'close_time': '6:00pm',
        'fee': 400
    },
    {
        'problem': 'heart disease',
        'doctor': 'Dr.Lisa',
        'open_time': '11:00am',
        'close_time': '7:00pm',
        'fee': 300
    },
    {
        'problem': 'stroke',
        'doctor': 'Dr.Kate',
        'open_time': '12:00pm',
        'close_time': '8:00pm',
        'fee': 200
    },
    {
        'problem': 'cold',
        'doctor': 'Dr.Tom',
        'open_time': '1:00pm',
        'close_time': '9:00pm',
        'fee': 100
    },
]

# List to store patient details
patient_detail = []

# Function to delete patient details based on patient ID
def delete_patient_details():
    id = input("Enter patient ID to delete: ")

    print(" Searching for patient details...")
    time.sleep(3)  # Simulating search time
    for patient in patient_detail:
        if patient['id'] == id:
            patient_detail.remove(patient)  # Removing patient data from list
            print("Patient Found!!")
            time.sleep(1)
            print("Deleting patient details...")
            time.sleep(3)
            
            print("Patient details deleted successfully.")
        else:
            print("Patient not found.")  # If ID not found

# Function to update patient details
def update_patient_details():
    id = input("Enter patient ID: ")  # Getting patient ID
    for patient in patient_detail:
        if patient['id'] == id:
            # Ask what detail the user wants to change
            change = input("What do you want to change? (name, age, problem, contact, address, gender): ")
            if change in patient:
                new_value = input("Enter new value: ")  # Get new value from the user
                patient[change] = new_value  # Update the patient's detail
                print("Patient details updated successfully.")

# Function to search for a patient's details using their ID
def search_patient_details(id):
    for patient in patient_detail:
        if patient['paitent_id'] == id:
            print("Patient details:")
            print("Name:", patient['name'])
            print("Age:", patient['age'])
            print("Gender:", patient['gender'])
            print("Problem:", patient['problem'])

# Function to add new patient details
def add_patient_details():
    print("Add patient details".center(45))  # Form to add patient details
    name = input("Enter patient name: ".center(15))
    age = int(input("Enter patient age: ".center(15)))
    gender = input("Enter patient gender: ".center(15))
    address = input("Enter patient address: ".center(15))
    contact = int(input("Enter patient contact number: ".center(15)))
    email = input("Enter patient email id: ".center(15))
    problem = input("Enter patient problem: ".center(15))

    # Find the doctor corresponding to the patient's problem
    for x in problem_doctor:
        if x['problem'] == problem:
            print("--------------------".center(15))
            print("Doctor available: ".center(20), x['doctor'])
            print("Opening time: ".center(20), x['open_time'])
            print("Closing time: ".center(20), x['close_time'])
            print("Fee: ".center(20), x['fee'])
            print("--------------------".center(15))

            # Store patient details into the patient_detail list
            patient_data = {
                'name': name,
                'age': age,
                'gender': gender,
                'address': address,
                'contact': contact,
                'email': email,
                'problem': problem,
                'paitent_id': len(patient_detail) + 1,  # Automatically assign patient ID
                'doctor': x['doctor'],
                'appointment_time': f"{x['open_time']} to {x['close_time']}",
                'fee': x['fee']
            }
            patient_detail.append(patient_data)  # Add patient to the list
            print("Patient details saved successfully!")
            print("Your patient ID is", patient_data['paitent_id'])
            break
    else:
        print("Problem not found. Please try again.")

# Function for e-registration
def e_registration():
    print("e-registration".center(45))  # Form for electronic registration
    name = input("Enter patient name: ".center(15))
    email = input("Enter patient email id: ".center(15))
    password = input("Enter patient password: ".center(15))
    con_password = input("Confirm password: ".center(15))
    if password == con_password:  # Check if passwords match
        print("Registration successful!")
        print("Your patient ID is", len(patient_detail) + 1)
    else:
        print("Passwords do not match. Please try again.")

# Function to handle appointment services
def apointment():
    print("Online appointment".center(45))
    while True:
        print("1. Add patient details ".center(15))
        print("2. Search patient details ".center(15))
        print("3. Update patient details ".center(15))
        print("4. Delete patient details ".center(15))
        print("5. Back to main menu ".center(15))
        print("--------------------".center(45))
        choice = int(input("Enter your choice: ".center(45)))  # Get user choice
        if choice == 1:
            add_patient_details()  # Add a new patient
        elif choice == 2:
            id = int(input("Enter patient id: ".center(15)))
            search_patient_details(id)  # Search for a patient by ID
        elif choice == 3:
            update_patient_details()  # Update existing patient details
        elif choice == 4:
            delete_patient_details()  # Delete patient details
        elif choice == 5:
            break  # Return to main menu

# Main function to display the hospital management menu
def main():
    while True:
        print("+ S.K Hospital + ".center(45))
        print("1. Online appointment ".center(15))
        print("2. e-registration ".center(15))
        print("3. Doctor list ".center(15))
        print("4. Medicine Available ".center(15))
        print("5. Exit ".center(15))
        print("--------------------".center(45))
        choice = int(input("Enter your choice: ".center(45)))  # Get user choice
        if choice == 1:
            apointment()  # Call appointment services
        elif choice == 2:
            e_registration()  # Call registration service
        elif choice == 3:
            print("Doctor list".center(45))  # Display list of doctors
            print("--------------------".center(45))
            for x in problem_doctor:
                print(f"Doctor name: {x['doctor']} and he is available for {x['problem']} at {x['open_time']} to {x['close_time']}")
        elif choice == 4:
            print("Medicine Available".center(45))  # Placeholder for medicine info
            print("--------------------".center(45))
            print("Coming Soon!!")
        elif choice == 5:
            print("Thank you for using our services".center(45))  # Exit message
            break

# Run the main function
main()
          
