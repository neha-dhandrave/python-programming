# Import necessary modules
import datetime
import pytz

# Define IST timezone
india_timezone = pytz.timezone('Asia/Kolkata')

# Get current date and time in IST
now = datetime.datetime.now(india_timezone)

# Format date string like "Sun May 29 02:26:23 IST 2017"
formatted_date = now.strftime("%a %b %d %H:%M:%S IST %Y")

# Print the formatted date
print(formatted_date)

