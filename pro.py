
import mysql.connector

#source: https://pynative.com/python-mysql-database-connection/

#practice source: https://pynative.com/python-database-programming-exercise-with-solution/

def get_connection():
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'LPMCenter',
                                         user='root',
                                         password='030399th_do')
    
    return connection

def close_connection(connection):
    if connection: 
        connection.close()
        
#1: Get physician info who performed certained proc
    
def Q_1(p_name):
    '''
    input proID. eg.1,2,3,4,5,6:

    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''  SELECT p.physicianID, p.Ph_name, p.Ph_position, p.ssn
                            FROM Undergoes as u, Physician as p, `Procedure` as pr
                            WHERE u.physicianID = p.physicianID AND pr.procID = u.procedureID
                                AND pr.p_name = %s ''' 
        cursor.execute(select_query,(p_name,))
        records = cursor.fetchall()
        
        print('Info for physician(s) who have performed',p_name)
        for row in records:
            print('physicianID: ',row[0])
            print('name: ',row[1])
            print('position: ',row[2])
            print('ssn: ',row[3])
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
        

#2: 

def Q_2():
    '''
    inpur appID. eg.1,2,3,4,5,6,7: 
    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''  SELECT t2.appID, t1.p_name as PatientName,
                            		t2.PhysicianName, t2.NurseName, t2.startDateTime, 
                                    t2.endDateTime, t1.primaryPhysician
                            FROM Table1 as t1, Table2 as t2
                            WHERE t1.patientID = t2.patientID
                                AND t2.PhysicianName != t1.primaryPhysician; ''' 
        cursor.execute(select_query)
        records = cursor.fetchall()
        
        print('Information of patient(s) meeting with a physician other than their primary physician with appID:')
        for row in records:
            print('PatientName: ', row[1])
            print('PhysicianName: ', row[2])
            print('NurseName: ', row[3])
            print('Start Date and Time: ', row[4])
            print('End Date and Time: ', row[5])
            print('Primary Physician: ', row[6])
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
        


#Patient info who undergone a procedure with cost higher than a certain cost:
    
def Q_3(cost):
    '''
    input a cost. eg.: 300, 400, 1500, etc.
    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT p.patientID, p.ssn, p.P_name as name,
                            		p.address, p.dob, p.phone,
                                    p.insuranceNumber, p.primaryPhysID
                        FROM Patient as p JOIN Table3 as t3 
                        ON p.patientID = t3.patientID
                        WHERE t3.cost > %s;
  ''' 
        cursor.execute(select_query,(cost,))
        records = cursor.fetchall()
        
        print('Information of patient(s) undergoing a procedure with a cost larger than $',cost)
        for row in records:
            print('Patient ID: ', row[0])
            print('ssn: ', row[1])
            print('name: ', row[2])
            print('address: ', row[3])
            print('date of birth: ', row[4])
            print('phone: ', row[5])
            print('insurance number: ', row[6])
            print('Primary Physician: ', row[7])
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
        

#4:
def Q_4(D_name):
    '''
    input department name. Eg.: Surgery, General Medicine, Psychiatry
    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT *
                            FROM Patient
                            WHERE primaryPhysID IN (SELECT physicianID
                                                    FROM Physician
                                                    WHERE physicianID IN 
                                                    (SELECT headID FROM Department
                                                     WHERE D_name = %s)); ''' 
        cursor.execute(select_query,(D_name,))
        records = cursor.fetchall()
        
        print('Patient(s)\'s information whose physician is department head of',D_name)
        for row in records:
            print('Patient ID: ', row[0])
            print('ssn: ', row[1])
            print('name: ', row[2])
            print('address: ', row[3])
            print('date of birth: ', row[4])
            print('phone: ', row[5])
            print('insurance number: ', row[6])
            print('Primary Physician: ', row[7])
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
        
#5
def Q_5(m_name):
    '''
    input the name of the medicine: eg.: Med A, Med B, etc.
    

    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT p.P_name, ph.Ph_name, pr.prescribedDate
                            FROM Prescribes as pr, Patient as p, 
                                Physician as ph, Medication as m
                            WHERE pr.physicianID = ph.physicianID
                        		AND pr.patientID = p.patientID
                                AND pr.medicationID = m.medID
                                AND m.m_name = %s; ''' 
        cursor.execute(select_query,(m_name,))
        records = cursor.fetchall()
        
        print('Information of each patient(s) who use',m_name)
        for row in records:
            print('Patient Name: ', row[0])
            print('Physician name: ', row[1])
            print('Prescription Date: ', row[2])
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
 
#6

def Q_6(date):
    ''' input a date '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT o.nurseID, n.N_name, n.N_position, 
                            		n.ssn, o.startDate, o.endDate
                        FROM Oncall as o, Nurse as n
                        WHERE o.nurseID = n.nurseID
                        AND %s BETWEEN o.startDate AND o.endDate;
     
        
                    ''' 
        cursor.execute(select_query,(date,))
        records = cursor.fetchall()
        
        print('Nurse on call on ',date)
        for row in records:
            print('nurseID: ',row[0])
            print('name: ',row[1])
            print('position: ',row[2])
            print('ssn: ',row[3])
            print('on_call_start_date: ',row[4])
            print('on_call_end_date: ',row[5])
            
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
 
   
#7


def Q_7(date):
    '''
    input a date
    '''

    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT p.P_name,s.startDate, s.endDate, r.roomID
                            FROM Stay as s, Patient as p, Room as r
                            WHERE s.patientID = p.patientID AND s.roomID = r.roomID
                                    AND r.roomType = 'Double'
                                    AND %s BETWEEN s.startDate AND s.endDate;
                    ''' 
        cursor.execute(select_query,(date,))
        records = cursor.fetchall()
        
        print('Patient Stay period ',date)
        
        for row in records:
            print('Room Type: ',row[3])
            print('Patient: ',row[0])
            print('Stay Start Date: ',row[1])
            print('Stay End Date: ',row[2])
            
            
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
  
    
 
        
#8

def Q_8(D_name):
    '''
    input department name: Surgery, General Medicine, Psychiatry

    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT t5.patientID, t5.ssn, t5.P_name as patient_name,
		t5.address as patient_address, t5.dob as patient_dob,
        t5.phone as patient_phone, t5.insuranceNumber as patient_insuranceNumber,
        t5.primaryPhysID as patient_primaryPhysID,
		t4.physicianID, t4.Ph_Name, t4.Ph_position, t4.ssn as physician_ssn, t5.appID
        FROM Table4 as t4, Table5 as t5
        WHERE t4.physicianID = t5.physicianID
        AND t4.D_name = %s; ''' 
        cursor.execute(select_query,(D_name,))
        records = cursor.fetchall()
        
        print('Information of each patient along with the detailed information of the physician with whom they have met and the appointment ID from ',D_name, 'department')
        for row in records:
            print('patientID: ',row[0])
            print('patient_ssn: ',row[1])
            print('patient_name: ',row[2])
            print('patient_address: ',row[3])
            print('patient_dob: ',row[4])
            print('patient_phone: ',row[5])
            print('patient_insuranceNumber: ',row[6])
            print('patient_primaryPhysID: ',row[7])
            print('physicianID: ',row[8])
            print('physician_name: ',row[9])
            print('physician_position: ',row[10])
            print('physician_ssn: ',row[11])
            print('appointmentID: ',row[12])
            
            
            print()
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print('Error while getting data', error)
 
def main():
    
    import sys
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '1':
        print(Q_1(args[1]))
        
    if len(args) == 1 and args[0] == '2':
        print(Q_2())
        
    if len(args) == 2 and args[0] == '3':
        print(Q_3(args[1]))
        
    if len(args) == 2 and args[0] == '4':
        print(Q_4(args[1]))
        
    if len(args) == 2 and args[0] == '5':
        print(Q_5(args[1]))
        
    if len(args) == 2 and args[0] == '6':
        print(Q_6(args[1]))
        
    if len(args) == 2 and args[0] == '7':
        print(Q_7(args[1]))
        
    if len(args) == 2 and args[0] == '8':
        print(Q_8(args[1]))
        
    
    
if __name__ == '__main__':
    
    main()
































