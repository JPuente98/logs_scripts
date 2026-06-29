def processLog(type_error):

    levels = {"INFO":0,
             "WARNING":0,
             "ERROR":0}
    try:
        with open('aplication.log') as file:

            if type_error != "ALL": 
                print("===== "+ type_error + " =====\n")
            else: 
                print("===== LOG SUMMARY =====\n")

            for line in file:
                level = line.split()[2]
                levels[level] += 1

                if type_error == level:
                    # strip() removes blank lines between printed log entries.
                    print(line.strip())

        if type_error == "ALL":
            print("INFO: ", levels["INFO"])
            print("WARNING:", levels["WARNING"])
            print("ERROR:", levels["ERROR"])
            print("\nTotal Entries: ", sum(levels.values()))

    except FileNotFoundError:
        print("Log file not found")

def main():
    type_error = str.upper(input("Put the error type that you want to see (All, ERROR, WARNING, INFO): "))

    if type_error in ("ERROR", "WARNING", "INFO", "ALL"):
        processLog(type_error)
    else:
        print("Error the request cannot be processed.")
main()

