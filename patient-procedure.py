
import random


def main():

    procedure1 = Procedure('Physical Exam', "Today's Date", 'Dr. Irvine', '$250.00')
    procedure2 = Procedure('X-Ray', "Today's Date", 'Dr. Jamison', '$500.00')
    procedure3 = Procedure('Blood test', "Today's Date", 'Dr. Smith', '$200.00',  )
    
    procedures = [procedure1, procedure2, procedure3]

    patient = Patient('John', 'A.', 'Doe', '1234 West Blvd', 'Santa Monica', 'CA', '90001', 
                      '(310) 123-4567', 'Joe Biden', '(310) 987-6543', procedures)
    print()

    print(patient)
    for procedure in procedures:
        print(procedure)

    print(patient.get_recommended_procedures())


class Patient:

    def __init__(self, first_name, middle_name, last_name, 
                address, city, state, zip, phone, contact, contact_num, procedures = []):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone 
        self.__contact = contact 
        self.__contact_num = contact_num
        self.__procedures = procedures
    
    # mutators 
    def set_first_name (self, first_name):
        self.__first_name = first_name

    def set_middle_name (self, middle_name):
        self.__middle_name = middle_name

    def set_last_name (self, last_name):
        self.__last_name = last_name

    def set_address (self, address):
        self.__address = address

    def set_city (self, city):
        self.__city = city

    def set_state (self, state):
        self.__state = state

    def set_zip (self, zip):
        self.__zip = zip

    def set_phone (self, phone):
        self.__phone = phone

    def set_contact (self, contact):
        self.__contact = contact
    
    def set_contact_num (self, contact_num):
        self.__contact_num = contact_num

    def set_procedures (self, procedures):
        self.__procedures = procedures

    # accessors 
    def get_first_name (self):
        return self.__first_name

    def get_middle_name (self):
        return self.__middle_name 

    def get_last_name (self):
        return self.__last_name 

    def get_address (self):
        return self.__address 

    def get_city (self):
        return self.__city 

    def get_state (self):
        return self.__state
    
    def get_zip (self):
        return self.__zip 

    def get_phone (self):
        return self.__phone 

    def get_contact (self):
        return self.__contact 

    def get_contact_num (self):
        return self.__contact_num 

    def get_recommended_procedures (self):
        return random.choice(self.__procedures)

    def __str__(self):
        return "Name: " + self.__first_name + " " + self.__middle_name + " " + self.__last_name + \
                "\nAddress: " + self.__address + " " + self.__city + " " + self.__state + " " + self.__zip + \
                "\nNumber: " + self.__phone + \
                "\nEmergency Contact: " + self.__contact + " " + self.__contact_num

class Procedure: 

    def __init__ (self, procedure, date, practitioner, charge):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    # mutators 
    def set_procedure (self, procedure):
        self.__procedure = procedure

    def set_date (self, date):
        self.__date = date 

    def set_practitioner (self, practitioner):
        self.__practitioner = practitioner

    def set_charge (self, charge): 
        self.__charge = charge

    # accessors
    def get_procedure (self):
        return self.__procedure 

    def get_date (self):
        return self.__date 

    def get_practitioner (self):
        return self.__practitioner 

    def get_charge (self): 
        return self.__charge 

    def __str__(self):
        return "\nProcedure: " + self.__procedure + \
               "\nDate: " + self.__date + \
               "\nPractitioner: " + self.__practitioner + \
               "\nCharge: " + self.__charge

main()

