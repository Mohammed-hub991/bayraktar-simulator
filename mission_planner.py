print("Welcome to Bayraktar Mission Planner")
print("Choose Mission type: \n 1. Reconnaissance \n 2. Surveillance \n 3. Strike \n 4. Maritime Patrol \n")

mission_type = int(input("Enter Choice: "))


#JY add extra drone descriptions, and format output better - luqman
if mission_type == 1:  # Mini UAV
    print("Recommended Drone For Reconnaissance Missions\n\
          Recommended Drone: Bayraktar Mini UAV\n\
          Endurance: 60 - 120 minutes\n\
          Purpose: Short range day and night aerial reconnaissance and surveillance applications\n")
elif mission_type == 2: # TB2
    print("Recommended Drone For Surveillance Missions\n\
          Recommended Drone: Bayraktar TB2\n\
          Endurance: 27 hours\n\
          Purpose: Intelligence, surveillance, reconnaissance (ISR), sometimes armed attack missions\n")
elif mission_type == 3: # Akıncı
    print("Recommended Drone For Strike Missions\n\
        Recommended Drone: Bayraktar Akıncı\n\
        Endurance: 25 hours\n\
        Purpose: Air-to-ground and air-to-air attack missions by carrying various munitions\n")
elif mission_type == 4: # Kızılelma
    print("Recommended Drone For Maritime Patrol Missions\n\
        Recommended Drone: Bayraktar Kızılelma\n\
        Endurance: 5-6 hours\n\
        Purpose: Over-water surveillance, ship escort, anti-surface/anti-submarine scouting and targeting support for naval task groups.\n")
else: # error handling
    placeholder = 0  #just placeholder (remove this when do error handling) - luqman