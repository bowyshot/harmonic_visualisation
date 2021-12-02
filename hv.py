
### VARIABLES
csv_file = "/Volumes/GoogleDrive/My Drive/Piano Trainer/Piano Trainer - HV.csv" ## Location of CSV File
max_time = 10 ### Maximum Training Time in Seconds


### CODE
def hvTrg(csv_file, max_time):

    ## IMPORTS
    import csv, random, time, pyttsx3

    ## Ask for Pause Interval
    pause_interval = input("Enter your Difficulty Level")
    pause_interval = float(pause_interval)

    ##Start Time
    start_time = time.time()

    ## Turn CSV into Dictionary
    chordDict = {}
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            chordDict[row["Key"] + " " + row["Chord Type"]] = row["Frequency"]
            line_count += 1
        print(f'There are {line_count-1} Chord Types.')

    ## Turn Dictionary into List >> Randomise
    chordList = []
    for key, value in chordDict.items():
        for i in range(0,int(value)):
            chordList.append(key)

    random.shuffle(chordList)

    n = 1
    for chord in chordList:
        print(str(n) + ". " + chord)
        n+=1


    ## Speak the List
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id) # change 7 to 32 for Samantha's Voice
    engine.say("Harmonic Visualization Training Commence")
    engine.runAndWait()

    for chord in chordList:
        engine.say(chord)
        engine.runAndWait()
        time.sleep(pause_interval)

        time_now = time.time()
        elapsed_time = time_now - start_time
        if elapsed_time > max_time:
            break



    engine.say( "Training End. You may be dismissed.")
    engine.runAndWait()



## Run Program
hvTrg (csv_file, max_time)
