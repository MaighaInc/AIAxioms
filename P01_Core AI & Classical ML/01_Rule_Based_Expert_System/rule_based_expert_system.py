"""
Rule-Based Expert System
------------------------
This program simulates a simple medical diagnosis system
using human-defined rules.

Author: AI Course
"""

def diagnose_patient(temperature, cough, headache, fatigue):
    """
    Diagnoses a patient based on symptoms.

    Parameters:
    temperature (float): Body temperature in Celsius
    cough (bool): True if patient has cough
    headache (bool): True if patient has headache
    fatigue (bool): True if patient feels fatigue

    Returns:
    str: Diagnosis result
    """

    # Rule 1: Flu
    if temperature >= 38.0 and cough and headache and fatigue:
        return "Flu"

    # Rule 2: Common Cold
    elif temperature >= 37.0 and cough:
        return "Common Cold"

    # Rule 3: Healthy
    else:
        return "Healthy"


def main():
    """
    Main function to test the expert system
    """

    print("RULE-BASED MEDICAL EXPERT SYSTEM")
    print("--------------------------------")

    # Sample patient data
    patient_temperature = 38.5
    patient_cough = True
    patient_headache = True
    patient_fatigue = True

    print("Patient Symptoms:")
    print("Temperature:", patient_temperature)
    print("Cough:", patient_cough)
    print("Headache:", patient_headache)
    print("Fatigue:", patient_fatigue)

    diagnosis = diagnose_patient(
        patient_temperature,
        patient_cough,
        patient_headache,
        patient_fatigue
    )

    print("\nDiagnosis Result:", diagnosis)


if __name__ == "__main__":
    main()
