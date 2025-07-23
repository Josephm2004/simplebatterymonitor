#!/usr/bin/env python3
#This is a python script for monitoring battery status
#It will print the battery percentage and status every 10 seconds
import psutil
import datetime
import time

def get_battery_info():
    """
    Retrieves and prints current battery status and percentage.
    """
    battery = psutil.sensors_battery()

    if battery is None:
        print("No battery information available on this system.")
        return

    print(f"Battery percentage: {battery.percent}%")

    if battery.power_plugged:
        print("Status: Charging")
        if battery.secsleft != psutil.POWER_TIME_UNLIMITED and battery.secsleft != psutil.POWER_TIME_UNKNOWN:
            # Convert seconds to a human-readable timedelta format
            time_left_delta = datetime.timedelta(seconds=int(battery.secsleft))
            print(f"Time until fully charged: {time_left_delta / 60} hours")
        else:
            print("Time until fully charged: Calculating/Unlimited (or not available)")
    else: 
        print("Status: Discharging")
        
    print("-" * 30) # Separator for readability in continuous output

if __name__ == "__main__":
    print("Starting battery monitoring. Press Ctrl+C to stop.")
    try:
        while True:
            get_battery_info()
            time.sleep(5) # Wait for 10 seconds before the next check
    except KeyboardInterrupt:
        print("\nBattery monitoring stopped.")