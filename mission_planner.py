while True:
        print("Welcome to Bayraktar Mission Planner")
        print("Choose Mission type: \n 0. Exit program \n 1. Reconnaissance \n 2. Surveillance \n 3. Strike \n 4. Maritime Patrol \n")

        mission_type = int(input("Enter Choice: "))


        #JY add extra drone descriptions, and format output better - luqman
        if mission_type == 0:  # Terminate Program
             print("Program Terminated.")
             break
        if mission_type == 1:  # Mini UAV
            print("\n----------------------------------------")
            print("Recommended Drone for: Reconnaissance")
            print("----------------------------------------")
            print("Name      : Bayraktar Mini UAV")
            print("Endurance : 60 - 120 minutes")
            print("Purpose   : Short-range day/night reconnaissance & surveillance")
            print("Payload   : Lightweight sensors/camera")
            print("----------------------------------------\n")
            break
        elif mission_type == 2: # TB2
            print("\n----------------------------------------")
            print("Recommended Drone for: Surveillance")
            print("----------------------------------------")
            print("Name      : Bayraktar TB2")
            print("Endurance : 27 hours")
            print("Purpose   : Intelligence, surveillance, reconnaissance (ISR); sometimes armed")
            print("Payload   : Cameras, EO/IR sensors")
            print("----------------------------------------\n")
            break
        elif mission_type == 3: # Akıncı
            print("\n----------------------------------------")
            print("Recommended Drone for: Strike")
            print("----------------------------------------")
            print("Name      : Bayraktar Akıncı")
            print("Endurance : 25 hours")
            print("Purpose   : Air-to-ground and air-to-air attack missions")
            print("Payload   : Precision munitions, advanced sensors")
            print("----------------------------------------\n")
            break
        elif mission_type == 4: # Kızılelma
            print("\n----------------------------------------")
            print("Recommended Drone for: Maritime Patrol")
            print("----------------------------------------")
            print("Name      : Bayraktar Kızılelma")
            print("Endurance : 5–6 hours")
            print("Purpose   : Over-water surveillance & naval support")
            print("Payload   : Anti-ship/anti-submarine scouting equipment")
            print("----------------------------------------\n")
            break
        else: 
            print("Invalid option, try again...")
            continue