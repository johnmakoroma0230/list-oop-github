# Patient Class
class Patient:
    def __init__(self, id, name, age, gender, diagnosis):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n***** Patient Information *****")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")


# Hospital Class
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully")

    def display_patients(self):
        print("\n********** All Patients **********")
        print(f"Hospital: {self.hospital_name}")

        # Check if there are patients
        if len(self.patients) == 0:
            print("No patient records found.")
        else:
            for patient in self.patients:
                patient.display_info()


# Patient Objects
patient1 = Patient(101, "Saidu", 23, "Male", "Poverty")
patient2 = Patient(102, "Marie", 23, "Female", "Malaria")
patient3 = Patient(103, "Sarah", 23, "Female", "Typhoid")


# Hospital Object
hospital1 = Hospital("John Clinic")


# Add patients to the hospital
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)


# Display all patients' records
hospital1.display_patients()