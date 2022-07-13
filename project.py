#source code: https://github.com/amesh-jayaweera/medium/blob/master/case9.py

from prettytable import PrettyTable

import mysql.connector
#pip install mydb
def get_connection():
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'LPMCenter',
                                         user='root',
                                         password='030399th_do')
    
    return connection

def close_connection(connection):
    if connection: 
        connection.close()

#Display in the mainMenu
def DisplayMenu():
    print('------Las Palmas Medical Center Database------')
    print('             1. View')
    print('             2. Insert New Records')
    print('             3. Delete record(s)')
    print('             4. Close')
    
def view_tables():
    print('1. Physicians Information')
    print('2. Nurse Information')
    print('3. Patient Information')
    print('4. Medication')
    print('5. Procedure')
    print('6. Room Information')
    print('7. Appointments Details')
    print('8. Oncall Details')
    print('9. Precriptions')
    print('10. Stay Details')
    print('11. Undergoes Details')
    print('12. EXIT')
    
def update_tables():
    print('1. Physicians Information')
    print('2. Nurse Information')
    print('3. Patient Information')
    print('4. Medication')
    print('5. Procedure')
    print('6. Room Information')
    print('7. Appointments')
    print('8. Oncall')
    print('9. Precriptions')
    print('10. Stay')
    print('11. Undergoes')
    print('12. EXIT')

def del_tables():
    print('1. Physicians Information')
    print('2. Nurse Information')
    print('3. Patient Information')
    print('4. Medication')
    print('5. Procedure')
    print('6. Room Information')
    print('7. Appointments')
    print('8. Oncall')
    print('9. Precriptions')
    print('10. Stay')
    print('11. Undergoes')
    print('12. EXIT')
    
def run(connection):
    DisplayMenu()
    n = int(input('Enter your option: '))
    connection = get_connection()
    if n == 1:
        view_tables()
        n1 = int(input('Enter your view option: '))
        
        if n1 == 1:
            phys_info(connection)
            exit()
        elif n1 == 2:
            nurse_info(connection)
            exit()
        elif n1 == 3:
            patient_info(connection)
            exit()
        elif n1 == 4:
            med(connection)
            exit()
        elif n1 == 5:
            proc(connection)
            exit()
        elif n1 == 6:
            room(connection)
            exit()
        elif n1 == 7:
            app_check(connection)
            exit()
        elif n1 == 8:
            nurse_oncall(connection)
            exit()
        elif n1 == 9:
            pres(connection)
            exit()
        elif n1 == 10:
            stay_check(connection)
            exit()
        elif n1 == 11:
            undergoes(connection)
            exit()
        elif n1 == 12:
            os.system('cls') #
            run(connection)
        else:
            print('Not Valid!!')
    elif n == 2:
        update_tables()
        n2 = int(input('Choose table to update: '))
        
        if n2 == 1:
            insert_into_physician_table(connection)
            exit()
        elif n2 == 2:
            insert_into_nurse_table(connection)
            exit()
        elif n2 == 3:
            insert_into_patient_table(connection)
            exit()
        elif n2 == 4:
            insert_into_medication_table(connection)
            exit()
        elif n2 == 5:
            insert_into_procedure_table(connection)
            exit()
        elif n2 == 6:
            insert_into_room_table(connection)
            exit()
        elif n2 == 7:
            insert_into_app_table(connection)
            exit()
        elif n2 == 8:
            insert_into_oncall(connection)
            exit()
        elif n2 == 9:
            insert_into_prescribes_table(connection)
            exit()
        elif n2 == 10:
            insert_into_stay_table(connection)
            exit()
        elif n2 == 11:
            insert_into_undergoes_table(connection)
            exit()
        elif n2 == 12:
            os.system('cls') #
            run(connection)
        else:
            print('Not Valid!!')
            exit()
    elif n == 3:
        del_tables()
        n3 = int(input('Choose table to delete: '))
        
        if n3 == 1:
            del_physician(connection)
            exit()
        elif n3 == 2:
            del_nurse(connection)
            exit()
        elif n3 == 3:
            del_pat(connection)
            exit()
        elif n3 == 4:
            del_med(connection)
            exit()
        elif n3 == 5:
            del_pro(connection)
            exit()
        elif n3 == 6:
            del_room(connection)
            exit()
        elif n3 == 7:
            del_app(connection)
            exit()
        elif n3 == 8:
            del_oncall(connection)
            exit()
        elif n3 == 9:
            del_prescribes(connection)
            exit()
        elif n3 == 10:
            del_stay(connection)
            exit()
        elif n3 == 11:
            del_undergoes(connection)
            exit()
        elif n3 == 12:
            os.system('cls') #
            run(connection)
    
        else:
            print('Not Valid')
            exit()
    elif n == 4:
        connection.close()
    else:
        
        os.system('cls')
        run(connection)
        

import os

def exit():
    n = int(input('Press 0 to exit '))
    if n == 0:
        os.system('cls') #
        run(connection)
    else:
        print('Invalid Option!')
        exit()
        
#VIEW MENU

def convert_table(records, field_names):
    my_table = PrettyTable()
    my_table.field_names = field_names
    for record in records:
        my_table.add_row(record)
        
    return my_table


def print_info(cursor, select_query, table_name, field_names):
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    print('----{} information----'.format(table_name))
    print('Number of records: ', len(records))
    print(convert_table(records, field_names))
        
        

def phys_info(connection):

    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Physician ''' 
    table_name = 'Physician'
    field_names = ['Physician ID','Physician Name','Physician Position','SSN']

    print_info(cursor, select_query, table_name, field_names)
  

def nurse_info(connection):

    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Nurse ''' 
    table_name = 'Nurse'
    field_names = ['Physician ID','Physician Name','Physician Position','SSN']

    print_info(cursor, select_query, table_name, field_names)
  

def patient_info(connection):
    
    cursor = connection.cursor()
    select_query = ''' SELECT p.*, ph.Ph_name
                            FROM Patient as p, Physician as ph
                            WHERE p.primaryPhysID = ph.physicianID ''' 
    table_name = 'Patient'
    field_names = ['Patient ID','ssn','Name','address','Date of Birth','Phone','Insurance Number','Primary Physician','Physician Name']

    print_info(cursor, select_query, table_name, field_names)
     
       

def app_check(connection):

   
    cursor = connection.cursor()
    select_query = ''' SELECT a.*,  p.P_name, n.N_name, ph.Ph_name
                            FROM Patient as p,
                                 Nurse as n,
                                Physician as ph,
                                Appointment as a
                           WHERE a.nurseID = n.nurseID
	                       AND p.patientID = a.patientID
                          AND a.physicianID = ph.physicianID; ''' 
    table_name = 'Appointment'
    field_names = ['Appointment ID','Patient ID',
                   'Nurse ID','Physician ID','Start Date/Time',
                   'End Date/Time','Patient Name','Nurse Name',
                   'Physician Name']

    print_info(cursor, select_query, table_name, field_names)
     
      

def nurse_oncall(connection):
    
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Oncall ''' 
    table_name = 'Nurse Oncall'
    field_names = ['Nurse ID','Start Date','End Date']

    print_info(cursor, select_query, table_name, field_names)

def stay_check(connection):
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Stay ''' 
    table_name = 'Stay'
    field_names = ['Stay ID','Patient ID','Room ID','Start Date','End Date']

    print_info(cursor, select_query, table_name, field_names)


def med(connection):
    
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Medication ''' 
    table_name = 'Medication'
    field_names = ['Medication ID','Medication Name']

    print_info(cursor, select_query, table_name, field_names)



def proc(connection):
    
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM `Procedure`
                '''  
    cursor.execute(select_query)
    records = cursor.fetchall()
    import pandas as pd
    test = pd.DataFrame(records)
    
    field_names = ['Procedure ID','Procedure Name','Cost']
    table_name = 'Procedure'
    
    print_info(cursor, select_query, table_name, field_names)
    print('Average cost: $', sum(test[2])/len(test))
    
def room(connection):
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Room ''' 
    table_name = 'Room'
    field_names = ['Room ID','Room Name']

    print_info(cursor, select_query, table_name, field_names)
   

def pres(connection):
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Prescribes ''' 
    table_name = 'Prescribes'
    field_names = ['Physician ID','Patient ID','Medication ID','Prescribed Date','Number of dose']

    print_info(cursor, select_query, table_name, field_names)


def undergoes(connection):
    cursor = connection.cursor()
    select_query = ''' SELECT * FROM Undergoes ''' 
    table_name = 'Undergoes'
    field_names = ['Patient ID','Procedure ID','Stay ID','Start Date','Physician ID','Nurse ID']

    print_info(cursor, select_query, table_name, field_names)
    


#INSERT MENU   
#OPTION: Insert data #CHECK FOR CONSTRAINTS
def insert_into_physician_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new row to physician table: ')
    #physicianID = input('Enter Physician ID: ')
    
    Ph_name = input("Physician's name: ")
    Ph_position = input('Position? (eg.: Intern, Surgeon, Senior, Chief of Medicine, Resident, Psychiatrist): ')
    ssn = int(input('enter ssn: '))
    insert_query = ''' INSERT INTO Physician (physicianID, Ph_name ,Ph_position, ssn) VALUES (%s,%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (None,Ph_name, Ph_position, ssn))
        connection.commit()
        print('---SUCCESS---')
        exit()

    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---')
        
def insert_into_nurse_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to nurse table: ')
    #nurseID = input('Enter ID: ')
    
    N_name = input("Enter full name: ")
    N_position = input('Position? (eg.: Head Nurse, Nurse): ')
    ssn = int(input('Enter ssn: '))
    
    insert_query = ''' INSERT INTO Nurse (nurseID, N_name ,N_position, ssn) VALUES (%s,%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (None, N_name, N_position, ssn))
        connection.commit()
        print('---SUCCESS---')
        exit()
    except: 
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---')  
         
def insert_into_patient_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to patient table: ')
    #patientID = int(input('ID: '))
    ssn = int(input('ssn: '))
    P_name = input('Patient Name: ')
    address = input('Address: ')
    dob = input('Date of Birth: ')
    phone = input('Phone number: ')
    insuranceNumber = int(input('Insurance Number: '))
    primaryPhysID = int(input('Primary Physician ID: '))
    
    
    
    insert_query = ''' INSERT INTO Patient (patientID, ssn ,P_name, address, dob, phone, insuranceNumber, primaryPhysID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
    try: 
        cursor.execute(insert_query, (None, ssn, P_name, address, dob,phone,insuranceNumber,primaryPhysID))
        connection.commit()
        
        print('---SUCCESS---')
        exit()
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---')  
         
def insert_into_medication_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to medication table: ')
    #medID = int(input('ID: '))
    m_name = input('Medication name: ')
   
    insert_query = ''' INSERT INTO Medication (medID,m_name) VALUES (%s,%s)'''
    try:
        cursor.execute(insert_query, (None, m_name))
        connection.commit()
        
        print('---SUCCESS---')
        exit()
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_procedure_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to procedure table: ')
    #procID = int(input('ID: '))
    p_name = input('Procedure name: ')
    cost = int(input('cost: '))
    
    insert_query = ''' INSERT INTO `Procedure` (procID, p_name,cost) VALUES (%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (None, p_name, cost))
        connection.commit()
        
        print('---SUCCESS---')
        exit()    
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_room_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to room table: ')
    roomID = int(input('ID: '))
    roomType = (input('Room Type (eg., Double, Single): '))
    
    insert_query = ''' INSERT INTO Room (roomID, roomType) VALUES (%s,%s)'''
    try:
        cursor.execute(insert_query, (roomID, roomType))
        connection.commit()
        
        print('---SUCCESS---')
        exit()    
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_app_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to appointment table: ')
    #appID = int(input('ID: '))
    patientID = int(input('Patient ID: '))
    nurseID = int(input('Nurse ID: '))
    physicianID = int(input('Physician ID: '))
    startDateTime = input('Start date and time (YYYY-MM-DD): ')
    endDateTime = input('End date and time (YYYY-MM-DD): ' )
    
    insert_query = ''' INSERT INTO Appointment (appID, patientID, nurseID, physicianID, startDateTime, endDateTime) VALUES (%s,%s,%s,%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (None, patientID,nurseID, physicianID,startDateTime, endDateTime))
        connection.commit()
        
        print('---SUCCESS---')
        exit()
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_oncall(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to oncall table: ')
    nurseID = int(input('NurseID: '))
    startDate = input('Start Date (YYYY-MM-DD): ')
    endDate = input('End Date (YYYY-MM-DD): ')
    
    insert_query = ''' INSERT INTO Oncall (nurseID, startDate, endDate) VALUES (%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (nurseID, startDate, endDate))
        connection.commit()
        
        print('---SUCCESS---')
        exit()    
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_prescribes_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to prescribes table: ')
    physicianID = int(input('Physician ID: '))
    patientID = int(input('Patient ID: '))
    medicationID = int(input('Medication ID: '))
    prescribedDate = input('Date (YYYY-MM-DD): ')
    dose = input('Number of dose per day (eg, 2/day): ')
    
    insert_query = ''' INSERT INTO Prescribes (physicianID, patientID, medicationID, prescribedDate, dose) VALUES (%s,%s,%s, %s,%s)'''
    try:
        cursor.execute(insert_query, (physicianID, patientID, medicationID, prescribedDate, dose))
        connection.commit()
        
        print('---SUCCESS---')
        exit()     
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_stay_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to stay table: ')
    #stayID = int(input('ID: '))
    patientID = int(input('Patient ID: '))
    roomID = int(input('Room ID: '))
    startDate = input('Start Date (YYYY-MM-DD): ')
    endDate = input('End Date (YYYY-MM-DD): ')
    
    insert_query = ''' INSERT INTO Stay (stayID, patientID, roomID, startDate, endDate) VALUES (%s,%s,%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (None, patientID,roomID,startDate,endDate))
        connection.commit()
        
        print('---SUCCESS---')
        exit()  
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 
        
def insert_into_undergoes_table(connection):
   
    #connection = get_connection()
    cursor = connection.cursor()
    print('Add a new record to undergoes table: ')
    patientID = int(input('Patien ID: '))
    procedureID = int(input('Procedure ID: '))
    stayID = int(input('Stay ID: '))
    procDate = input('Procedure Date (YYYY-MM-DD): ')
    physicianID = int(input('Physician ID:'))
    nurseID = int(input('Nurse ID: '))
    
    insert_query = ''' INSERT INTO Undergoes (patientID, procedureID,stayID,procDate,physicianID, nurseID) VALUES (%s,%s,%s,%s,%s,%s)'''
    try:
        cursor.execute(insert_query, (patientID, procedureID, stayID,procDate, physicianID,nurseID))
        connection.commit()
        
        print('---SUCCESS---')
        exit()   
    except:
        connection.rollback() #in case there is an error
        print('---ERROR: Please check your input---') 


#DELETE MENU
def delete_table(connection, del_query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(del_query)
        return 0
    except Exception as e:
        return -1
    
    
def del_physician(connection):
    phys_info(connection)
    user_input = int(input('Enter PhysicianID you want to remove: '))
    del_query = ''' DELETE FROM Physician WHERE physicianID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('Success')
        print('Table after deletion')
        phys_info(connection)
    else:
        print('Error')
        
def del_nurse(connection):
    nurse_info(connection)
    user_input = int(input('Enter NurseID you want to remove: '))
    del_query = ''' DELETE FROM Nurse WHERE NurseID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        nurse_info(connection)
    else:
        print('-----Error-----')
        
def del_pat(connection):
    patient_info(connection)
    user_input = input('Enter PatientID you want to remove: ')
    del_query = ''' DELETE FROM Patient WHERE patientID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        patient_info(connection)
    else:
        print('-----Error-----')
        
def del_med(connection):
    med(connection)
    user_input = int(input('Enter Medication ID you want to remove: '))
    del_query = ''' DELETE FROM Medication WHERE medID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        med(connection)
    else:
        print('-----Error-----')
        
def del_pro(connection):
    proc(connection)
    user_input = int(input('Enter Procedure ID you want to remove: '))
    del_query = ''' DELETE FROM Procedure WHERE procID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        proc(connection)
    else:
        print('-----Error-----')
        
def del_room(connection):
    room(connection)
    user_input = input('Enter Room ID you want to remove: ')
    del_query = ''' DELETE FROM Room WHERE roomID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        room(connection)
    else:
        print('-----Error-----')

def del_app(connection):
    app_check(connection)
    user_input = int(input('Enter Appointment ID you want to remove: '))
    del_query = ''' DELETE FROM Appointment WHERE appID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        app_check(connection)
    else:
        print('-----Error-----')
    
def del_oncall(connection):
    nurse_oncall(connection)
    user_input = int(input('Enter Nurse ID you want to remove: '))
    del_query = ''' DELETE FROM Oncall WHERE NurseID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        nurse_oncall(connection)
    else:
        print('-----Error-----')
        
def del_prescribes(connection):
    pres(connection)
    print('Which option do you want to remove? ')
    print('1. Physician ID')
    print('2. Patient ID')
    print('3. Medication ID')
    user_input = int(input('Your option: '))
    if user_input == 1:
        input1 = int(input('Enter Physician ID you want to remove: '))
        del_query = ''' DELETE FROM Prescribes WHERE physicianID = {} '''.format(input1)
        status = delete_table(connection, del_query)
        if status == 0:
            print('-----SUCCESS-----')
            print('Table after deletion')
            pres(connection)
        else:
            print('-----Error-----')
    elif user_input == 2:
        input1 = int(input('Enter Patient ID you want to remove: '))
        del_query = ''' DELETE FROM Prescribes WHERE patientID = {} '''.format(input1)
        status = delete_table(connection, del_query)
        if status == 0:
            print('-----SUCCESS-----')
            print('Table after deletion')
            pres(connection)
        else:
            print('-----Error-----')
    elif user_input == 3:
        input1 = int(input('Enter Medication ID you want to remove: '))
        del_query = ''' DELETE FROM Prescribes WHERE medicationID = {} '''.format(input1)
        status = delete_table(connection, del_query)
        if status == 0:
            print('-----SUCCESS-----')
            print('Table after deletion')
            pres(connection)
        else:
            print('-----Error-----')
    else:
        print('Invalid option')
        
def del_stay(connection):
    stay_check(connection)
    user_input = int(input('Enter Stay ID you want to remove: '))
    del_query = ''' DELETE FROM Stay WHERE StayID = {} '''.format(user_input)
    status = delete_table(connection, del_query)
    if status == 0:
        print('-----SUCCESS-----')
        print('Table after deletion')
        stay_check(connection)
    else:
        print('-----Error-----')
        
def del_undergoes(connection):
    undergoes(connection)
    print('Which option do you want to remove? ')
    print('1. Patient ID')
    print('2. Procedure ID')
    print('3. Physician ID')
    print('4. Nurse ID')
    
    user_input = int(input('Your option: '))
    if user_input == 1:
       input1 = int(input('Enter Patient ID you want to remove: '))
       del_query = ''' DELETE FROM Undergoes WHERE patientID = {} '''.format(input1)
       status = delete_table(connection, del_query)
       if status == 0:
           print('-----SUCCESS-----')
           print('Table after deletion')
           undergoes(connection)
       else:
           print('-----Error-----')
    if user_input == 2:
       input1 = int(input('Enter Procedure ID you want to remove: '))
       del_query = ''' DELETE FROM Undergoes WHERE procedureID = {} '''.format(input1)
       status = delete_table(connection, del_query)
       if status == 0:
           print('-----SUCCESS-----')
           print('Table after deletion')
           undergoes(connection)
       else:
           print('-----Error-----')
    
    if user_input == 3:
       input1 = int(input('Enter Physician ID you want to remove: '))
       del_query = ''' DELETE FROM Undergoes WHERE physicianID = {} '''.format(input1)
       status = delete_table(connection, del_query)
       if status == 0:
           print('-----SUCCESS-----')
           print('Table after deletion')
           undergoes(connection)
       else:
           print('-----Error-----')
    if user_input == 4:
       input1 = int(input('Enter Nurse ID you want to remove: '))
       del_query = ''' DELETE FROM Undergoes WHERE nurseID = {} '''.format(input1)
       status = delete_table(connection, del_query)
       if status == 0:
           print('-----SUCCESS-----')
           print('Table after deletion')
           undergoes(connection)
       else:
           print('-----Error-----')

 
def main(connection):
    run(connection)
    
if __name__ == '__main__':
    try:
        connection = get_connection()
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
    main(connection)


      
    
    
    
    
    
    
    
    
    
    
    
    