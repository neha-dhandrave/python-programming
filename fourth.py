from datetime import datetime
import pytz

# Define the timezone (IST - Indian Standard Time)
timezone = pytz.timezone('Asia/Kolkata')

# Get current date and time in that timezone
current_time = datetime.now(timezone)

# Format the date and time as: Day Mon DD HH:MM:SS TZ YYYY
formatted_time = current_time.strftime('%a %b %d %H:%M:%S %Z %Y')

# Print the formatted date
print(formatted_time)