#Project Phase 2:

#1: Get physician info who performed certained proc
SELECT p.physicianID, p.Ph_name, p.Ph_position, p.ssn
FROM Undergoes as u, Physician as p, `Procedure` as pr
WHERE u.physicianID = p.physicianID AND pr.procID = u.procedureID
	and pr.p_name = 'Proc B';

#2: 
SELECT t2.appID, t1.p_name as PatientName,
		t2.PhysicianName, t2.NurseName, t2.startDateTime, 
        t2.endDateTime, t1.primaryPhysician
FROM Table1 as t1, Table2 as t2
WHERE t1.patientID = t2.patientID;

#3: 
SELECT p.patientID, p.ssn, p.P_name as name,
		p.address, p.dob, p.phone, p.insuranceNumber,
        p.primaryPhysID, t3.cost
FROM Patient as p JOIN Table3 as t3 
	ON p.patientID = t3.patientID
WHERE t3.cost > 3000;

#4:
SELECT *
FROM Patient
WHERE primaryPhysID IN (SELECT physicianID
						FROM Physician
						WHERE physicianID IN (SELECT headID FROM Department
												));

#5: 
SELECT p.P_name, ph.Ph_name, pr.prescribedDate
FROM Prescribes as pr, Patient as p, Physician as ph, Medication as m
WHERE pr.physicianID = ph.physicianID
		AND pr.patientID = p.patientID
        AND pr.medicationID = m.medID;

#6: Nurse on call for a certain date

SELECT o.nurseID, n.N_name, n.N_position, 
		n.ssn, o.startDate, o.endDate
FROM Oncall as o, Nurse as n
WHERE o.nurseID = n.nurseID;


#7:

SELECT p.P_name,s.startDate, s.endDate, r.roomType
FROM Stay as s, Patient as p, Room as r
WHERE s.patientID = p.patientID AND s.roomID = r.roomID AND r.roomType = 'Double';

#8: input 'department' output info from of patient and physician

SELECT t5.patientID, t5.ssn, t5.P_name as patient_name,
		t5.address as patient_address, t5.dob as patient_dob,
        t5.phone as patient_phone, t5.insuranceNumber as patient_insuranceNumber,
        t5.primaryPhysID as patient_primaryPhysID,
		t4.physicianID, t4.Ph_Name, t4.Ph_position, t4.ssn as physician_ssn, t5.appID
FROM Table4 as t4, Table5 as t5
WHERE t4.physicianID = t5.physicianID
	AND t4.D_name = 'Psychiatry';













