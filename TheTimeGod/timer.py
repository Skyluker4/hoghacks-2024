#!/usr/bin/env python3

import time, requests
import time, requests
import threading

def countdown_timer():
    total_time = 15 * 60  # 15 minutes in seconds
    quarter_counter = 1
    pause = False

    def check_pause():
        nonlocal pause
        nonlocal total_time
        nonlocal quarter_counter
        while True:
            typed = input()
            if pause:
                # If q# is typed, change the quarter
                if typed[0] == "q":
                    quarter_counter = int(typed[1])
                    post_request(convert_time(total_time), quarter_counter)
                # If a time m:SS was typed, set the time to that time
                elif ":" in typed:
                    # Set the total time correctly
                    minutes, seconds = typed.split(":")
                    total_time = int(minutes) * 60 + int(seconds)
                    post_request(typed, quarter_counter)
            pause = not pause

    pause_thread = threading.Thread(target=check_pause)
    pause_thread.start()

    while quarter_counter < 4:
        if not pause:
            post_request(convert_time(total_time), quarter_counter)
            time.sleep(1)
            total_time -= 1

            if total_time == 0:
                quarter_counter += 1
                print(f"Quarter counter: {quarter_counter}")
                total_time = 15 * 60

    print("Countdown complete!")

# Convert the current time into a string formatted as MM:SS
def convert_time(time: int) -> str:
    minutes = time // 60
    seconds = time % 60

    new_seconds = str(seconds) if seconds >= 10 else f"0{seconds}"

    return f"{minutes}:{new_seconds}"

# Make a post request to a server with the current time
def post_request(time: str, quart: int):
    url = "http://127.0.0.1:5000/api/v1/time"

    body = f'{{"time": "{time}", "quarter": {quart}}}'

    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=body)

    if response.status_code == 204:
        print(f"Time sent! {time}")
    else:
        print("Error sending time")

def main():
    countdown_timer()

if __name__ == "__main__":
    main()
