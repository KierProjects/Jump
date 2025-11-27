import speedtest
import datetime

st = speedtest.Speedtest()

download = st.download() / 1_000_000  # Mbps
upload = st.upload() / 1_000_000      # Mbps
ping = st.results.ping

# Timestamp with AM/PM format
now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

# Build the log line
line = f"{now}, Download: {download:.2f} Mbps, Upload: {upload:.2f} Mbps, Ping: {ping:.2f} ms\n"

# Append mode ("a") = add new line, NEVER erase old data
with open("network_log.csv", "a") as file:
    file.write(line)

print(line)
