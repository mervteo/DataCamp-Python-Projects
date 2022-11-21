def main():
    while True:
        try:
            print("\nWelcome to Covid-19 Vaccination Record Management System.")
            print("============================ Menu ================================")
            print(
                " 1.New Patient Registration\n 2.Vaccine Administration\n 3.Search Patient Record and Vaccination "
                "Status\n "
                "4.Statistical Information on Patients Vaccinated")
            print("==================================================================")
            choice = int(input("Enter your choice (1-4), 5 to end program: "))

            if choice == 1:
                registration()
            elif choice == 2:
                administration()
            elif choice == 3:
                search_patient()
            elif choice == 4:
                statistics()
            elif choice == 5:
                break
            else:
                print("Invalid input.Please try again.")
                main()
            return
        except ValueError:
            continue


def registration():
    # Vaccination Centre Input
    while True:
        try:
            vc_centre = input("\nPlease enter your vaccination centre(VC1 or VC2): ")
            if vc_centre in ["VC1", "VC2"]:
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Name Input
    while True:
        try:
            name = input("Please enter your name: ")
            if all(x.isalpha() or x.isspace() for x in name):  # isalpha= only character no number
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Convert Name to UPPERCASE
    while True:
        try:
            if name.isupper():
                break
            else:
                name = name.upper()
        except ValueError:
            continue

    # Phone Number Input
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if type(phone_number) == int:
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Age Input
    while True:
        age = int(input("Please enter your age: "))

        if type(age) == int and 12 <= age < 18:
            print(75 * "_")
            print("| Vaccine Code | Dosage Required | Interval Between Doses |   Age Group   |")
            print("|      AF      |        2        |   2 weeks(or 14 days)  |  12 and above |")
            print("|      DM      |        2        |   4 weeks(or 28 days)  |  12 and above |")
            print("|      CZ      |        2        |   3 weeks(or 21 days)  |    12 - 45    |")
            print(75 * "-")
            break
        elif type(age) == int and 18 <= age <= 45:
            print(75 * "_")
            print("| Vaccine Code | Dosage Required | Interval Between Doses |   Age Group   |")
            print("|      AF      |        2        |   2 weeks(or 14 days)  |  12 and above |")
            print("|      BV      |        2        |   3 weeks(or 21 days)  |  18 and above |")
            print("|      CZ      |        2        |   3 weeks(or 21 days)  |    12 - 45    |")
            print("|      DM      |        2        |   4 weeks(or 28 days)  |  12 and above |")
            print("|      EC      |        1        |           -            |  18 and above |")
            print(75 * "-")
            break
        elif type(age) == int and 46 <= age <= 100:
            print(75 * "_")
            print("| Vaccine Code | Dosage Required | Interval Between Doses |   Age Group   |")
            print("|      AF      |        2        |   2 weeks(or 14 days)  |  12 and above |")
            print("|      BV      |        2        |   3 weeks(or 21 days)  |  18 and above |")
            print("|      DM      |        2        |   4 weeks(or 28 days)  |  12 and above |")
            print("|      EC      |        1        |           -            |  18 and above |")
            print(75 * "-")
            break
        else:
            print("No eligible vaccines.Back to main menu....")
            main()

    # Vaccine Selected
    while True:
        try:
            vaccine_selected = input("Please enter your preferred vaccine code: ")
            if 12 <= age <= 18 and vaccine_selected in ["AF", "DM", "CZ"]:
                break
            elif 19 <= age <= 45 and vaccine_selected in ["AF", "DM", "BV", "EC", "CZ"]:
                break
            elif 46 <= age <= 100 and vaccine_selected in ["AF", "DM", "BV", "EC"]:
                break
            else:
                print("Invalid vaccine code. Please try again.")
        except ValueError:
            continue
    print("You have successfully registered for " + vaccine_selected + " vaccine.")

    # Generate Unique ID (Eg: MG0001)
    with open("patients.txt", mode='r') as file:
        number_of_patient = 0
        for i in file.readlines():  # "i" indicates that there's a record inside patient text file
            number_of_patient += 1  # add 1 for each patient
        id_count = str(number_of_patient).zfill(4)  # 0000 to 0001...
        patient_name = name[0] + name[1]
        patient_id = patient_name + id_count
        print("Your patient ID is: " + patient_id)

    # open 2 list and lastly append all info from list to txt file
    patient_info = []
    vaccination_info = []

    # Append all info into patients_info
    patient_info.append(patient_id)
    patient_info.append(vc_centre)
    patient_info.append(name)
    patient_info.append(age)
    patient_info.append(phone_number)
    patient_info.append(vaccine_selected)

    # # Append all info into vaccination_info list
    vaccination_info.append(patient_id)
    vaccination_info.append(name)
    vaccination_info.append(vc_centre)
    vaccination_info.append(vaccine_selected)
    vaccination_info.append("New Patient")  # "New Patient" as role for new register patient

    # patient_info list to patients.txt
    with open("patients.txt", mode='a') as file:
        for info in patient_info:
            file.write("%s; " % info)  # %s = write all string from list
        file.write("\n")  # New info to next line

    # vaccination_info list to vaccination.txt
    with open("vaccination.txt", mode='a') as file:
        for info in vaccination_info:
            file.write("%s; " % info)
        file.write("\n")

    main()


def administration():
    # Check ID (is string/ is 6 string/ is upper)
    while True:
        try:
            patient_id = input("Enter your patient ID: ")
            if type(patient_id) == str and len(patient_id) == 6 and patient_id.isupper():
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Dose
    while True:
        try:
            dose = input("Enter your dose (D1 or D2): ")
            if dose in ["D1", "D2"]:
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Check Dose Status
    with open("vaccination.txt", mode='r') as check:
        temp_list = []  # open a temp_list(Updated info to here and rewrite to vaccination.txt)
        found = 0
        for each_data in check:  # loop check(readline)
            info = each_data.split("; ")  # insert every data from txt to info and need to split for each string
            existing_id = info[0]
            if patient_id == existing_id:
                found = 1
                vaccine_selected = info[3]
                status = info[4]

                # check variable
                if status == "New Patient":
                    if vaccine_selected == "AF" and dose == "D1":
                        print("You have completed your first dose. Second dose will be two weeks later.")
                        info[4] = "Completed 1 dose"

                    elif vaccine_selected == "BV" and dose == "D1":
                        print("You have completed your first dose. Second dose will be three weeks later.")
                        info[4] = "Completed 1 dose"

                    elif vaccine_selected == "DM" and dose == "D1":
                        print("You have completed your first dose. Second dose will be four weeks later.")
                        info[4] = "Completed 1 dose"

                    elif vaccine_selected == "EC" and dose == "D1":
                        print("You have completed your vaccination. No second dose required for EC vaccination.")
                        info[4] = "Completed Vaccination"

                    elif vaccine_selected == "CZ" and dose == "D1":
                        print("You have completed your first dose. Second dose will be three weeks later.")
                        info[4] = "Completed 1 dose"

                    elif dose == "D2":
                        print("Please take your first dose before second dose.")

                elif status == "Completed 1 dose":
                    if vaccine_selected == "EC" and dose == "D1":
                        print("You completed your vaccination. No second dose required for EC vaccination.")

                    elif dose == "D1":
                        print("You have already completed dose 1.Please select for second dose.")

                    elif dose == "D2":
                        print("You have completed two doses. Thank you.")
                        info[4] = "Completed Vaccination"

                elif status == "Completed Vaccination":
                    if dose == "D1":
                        print("You have completed your vaccination.")

                    elif dose == "D2":
                        print("You have completed your vaccination.")

                    # status=[New Patient, Completed 1 dose, Completed Vaccination]

            for i in info:
                temp_list.append(i)  # Write info to temp_list (Updated status)

                # To make sure contain 5 data in info , split data with ";" if less than 5
                if i != info[5]:
                    temp_list.append("; ")

        # Rewrite vaccination.txt with temp_list
        with open("vaccination.txt", mode='w') as new:
            for w in temp_list:
                new.write(w)

        # No ID Found
        if found == 0:
            print("Invalid patient ID.Please register first.")
            main()
    main()


def search_patient():
    # Same as Administration
    # Check ID (is string/ is 6 string/ is upper)
    while True:
        try:
            patient_id = input("Enter your patient ID: ")
            if type(patient_id) == str and len(patient_id) == 6 and patient_id.isupper():
                break
            else:
                print("Invalid Input.")
        except ValueError:
            continue

    # Check Status
    with open("vaccination.txt", mode='r') as check_status:
        for each_data in check_status.readlines():  # loop check(readline)
            info = each_data.split("; ")
            # same with part 2(insert every data from txt to info and need to split for each string)
            existing_id = info[0]
            if patient_id == existing_id:
                name = info[1]
                vc_centre = info[2]
                vaccine_selected = info[3]
                status = info[4]
                print("__________________________________________________")
                print(
                    "Patient ID: " + patient_id + "\nPatient Name: " + name + "\nVaccination Centre: " + vc_centre +
                    "\nVaccine Selected: " + vaccine_selected + "\nStatus of Vaccination: " + status)
                print("__________________________________________________")
                break
        else:
            print("Invalid patient ID.No record found.")

            # No ID Found

    main()


def statistics():
    count_vc1 = 0
    count_vc2 = 0
    count_complete_vc1 = 0
    count_dose2_vc1 = 0
    count_complete_vc2 = 0
    count_dose2_vc2 = 0

    with open("vaccination.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "VC1" in line:
                count_vc1 += 1
            if "VC2" in line:
                count_vc2 += 1
            if "VC1" in line and "Completed 1 dose" in line:
                count_dose2_vc1 += 1
            if "VC1" in line and "Completed Vaccination" in line:
                count_complete_vc1 += 1
            if "VC2" in line and "Completed 1 dose" in line:
                count_dose2_vc2 += 1
            if "VC2" in line and "Completed Vaccination" in line:
                count_complete_vc2 += 1

        print("___________________________________________________________")
        print("Total number of patients registered at VC1: ", count_vc1)
        print("Total number of patients registered at VC2: ", count_vc2)
        print('Total number of patients waiting for dose 2 in VC1:', count_dose2_vc1)
        print('Total number of patients completed vaccination in VC1:', count_complete_vc1)
        print('Total number of patients waiting for dose 2 in VC2:', count_dose2_vc2)
        print('Total number of patients completed vaccination in VC2:', count_complete_vc2)
        print("___________________________________________________________")
    main()


main()  # call to main menu for starting
