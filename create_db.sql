
CREATE DATABASE LPMCenter;
# create tables:
#1
CREATE TABLE Physician
	(physicianID int,
    Ph_name varchar(40) NOT NULL,
    Ph_position varchar(40),
    ssn int,
    Primary key (physicianID),
    CHECK (Ph_position in ('Intern','Surgeon','Senior','Chief of Medicine', 'Resident', 'Psychiatrist')));
#2
CREATE TABLE Department
	(deptID int,
    D_name varchar(40),
    headID int,
    Primary key(deptID),
    Foreign key (headID) references Physician(physicianID) ON DELETE CASCADE,
    CHECK (D_name in('General Medicine','Surgery', 'Psychiatry')));

#3
CREATE TABLE AffiliatedWith
	(physicianID int,
    departmentID int,
    Primary key(physicianID, departmentID),
    Foreign key (physicianID) references Physician(physicianID) ON DELETE CASCADE,
    Foreign key (departmentID) references Department(deptID) ON DELETE CASCADE);
#4
CREATE TABLE `Procedure`
	(procID int,
    p_name varchar(40),
    cost real,
    Primary key (procID));
#5
CREATE TABLE Patient
	(patientID int,
    ssn int NOT NULL,
    P_name varchar(40) NOT NULL,
    address varchar(100),
    dob date,
    phone varchar(16),
    insuranceNumber int,
    primaryPhysID int,
    primary key (patientID),
    foreign key (primaryPhysID) references Physician(physicianID) ON DELETE SET NULL);
#6
CREATE TABLE Nurse
		(nurseID int,
        N_name varchar(40),
        N_position varchar(40),
        ssn int NOT NULL,
        primary key(nurseID),
        CHECK (N_position IN ('Head Nurse','Nurse')));
#7
CREATE TABLE Medication
		(medID int,
        m_name varchar(40),
        primary key (medID));
#8
CREATE TABLE Prescribes
	(physicianID int,
    patientID int,
    medicationID int,
    prescribedDate date,
    dose varchar(40),
    primary key (physicianID, patientID,medicationID, prescribedDate),
    foreign key (physicianID) references Physician(physicianID) ON DELETE CASCADE,
    foreign key (patientID) references Patient(patientID) ON DELETE CASCADE,
    foreign key (medicationID) references Medication(medID) ON DELETE CASCADE);
#9
CREATE TABLE Room
	(roomID int,
    roomType varchar(40),
    primary key (roomID),
    CHECK (roomType IN ('Single','Double')));
#10
CREATE TABLE Stay
	(stayID int,
    patientID int,
    roomID int,
    startDate date,
    endDate date,
    primary key (stayID),
    foreign key (patientID) references Patient(patientID) ON DELETE CASCADE,
    foreign key (roomID) references Room(roomID) ON DELETE SET NULL);
#11
CREATE TABLE Undergoes
	(patientID int,
    procedureID int,
    stayID int,
    procDate date,
    physicianID int,
    nurseID int,
    primary key (patientID, procedureID, stayID, procDate),
    foreign key (patientID) references Patient(patientID) ON DELETE CASCADE,
    foreign key (procedureID) references`Procedure`(procID),
    foreign key (stayID) references Stay(stayID),
    foreign key (physicianID) references Physician(physicianID) ON DELETE SET NULL,
    foreign key (nurseID) references Nurse(nurseID) ON DELETE SET NULL);
#12
CREATE TABLE Oncall
	(nurseID int,
    startDate date NOT NULL,
    endDate date,
    primary key (nurseID, startDate, endDate),
    foreign key (nurseID) references Nurse(nurseID) ON DELETE CASCADE);
#13
CREATE TABLE Appointment 
	(appID int,
    patientID int,
    nurseID int,
    physicianID int,
    startDateTime datetime NOT NULL,
    endDateTime datetime NOT NULL,
    primary key (appID),
    foreign key (patientID) references Patient(patientID) ON DELETE CASCADE,
    foreign key (nurseID) references Nurse(nurseID) ON DELETE SET NULL,
    foreign key (physicianID) references Physician(physicianID) ON DELETE SET NULL);
    
 