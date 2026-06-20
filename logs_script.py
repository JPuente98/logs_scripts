def main():

    levels = {"INFO":0,
             "WARNING":0,
             "ERROR":0}
    try:
        with open('aplication.log') as file:
            for line in file:
                level = line.split()[2]
                if level in levels:
                    levels[level] += 1

        print("===== LOG SUMMARY =====\n")
        print("INFO: ", levels["INFO"])
        print("WARNING:",levels["WARNING"])
        print("ERROR:", levels["ERROR"])
        print("\nTotal Entries: ", levels["INFO"] + levels["WARNING"] + levels["ERROR"])
    except FileNotFoundError:
        print("Log file not found")

main()
