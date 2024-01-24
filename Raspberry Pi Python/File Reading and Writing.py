import time
import datetime
import tmp102

filename = "temp_log.csv"

# Create header row in new CSV file
csv = open(filename, 'w')
csv.write("Timestamp,Temperature\n")
csv.close

# Initialize communication with TMP102
tmp102.init()

# Sample temperature every second for 10 seconds
for t in range(0, 10):

    # Construct CSV entry from timestamp and temperature
    temp_c = str(round(tmp102.read_temp(), 2))
    entry = str(datetime.datetime.now())
    entry = entry + "," + temp_c + "\n"

    # Log (append) entry into file
    csv = open(filename, 'a')
    try:
        csv.write(entry)
    finally:
        csv.close()

    # Wait 1 second before sampling temperature again
    time.sleep(1)

# When all the writing has been completed, print the CSV contents
csv = open(filename, 'r')
print(csv.read())
csv.close()
