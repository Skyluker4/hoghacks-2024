#!/usr/bin/env python3

import time, requests

def countdown_timer():
    total_time = 15 * 60  # 15 minutes in seconds
    quarter_counter = 1

    while quarter_counter < 4:
        post_request(total_time, quarter_counter)
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
def post_request(time: int, quart: int):
    url = "http://127.0.0.1:5500/api/v1/time"

    remaining_time = convert_time(time)
    body = f'{{"time": "{remaining_time}", "quarter": {quart}}}'

    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=body)

    if response.status_code == 204:
        print(f"Time sent! {remaining_time}")
    else:
        print("Error sending time")

def main():
    countdown_timer()

if __name__ == "__main__":
    main()
