#!/usr/bin/env python3
import os
import requests
import thesecrets

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.hudl.com/library/11214',
    'Cookie': thesecrets.thecookies,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'
}

response = requests.get(thesecrets.theurl, headers=headers)
clips = response.text

with open('clips.json', 'w') as f:
    f.write(clips)

# Get a list of [clipsList][clips]
resp = response.json()
clips = resp["clipsList"]["clips"]

# Create newdatacsv with headers
with open('data.csv', 'w') as f:
    f.write('Game Date,Team,Play,Quarter,Yard,Down,Distance,Gain/Loss,Hash,Play Type,Result,Play Direction,Eff,Series,Offensive Strength,Field/Boundary\n')
with open('bwdata.csv', 'w') as f:
    f.write('Game Date,Team,Play,Quarter,Yard,Down,Distance,Gain/Loss,Hash,Play Type,Result,Play Direction,Eff,Series,Offensive Strength,Field/Boundary\n')


for clip in clips:
    # Get the clips breakdownData
    breakdownData = clip["breakdownData"]
    playNumber = int(breakdownData["PLAY #"])
    newdata = {}
    newdata["Game Date"] = resp["cutupCreatedOn"]
    newdata["Team"] = breakdownData["TEAM"] if "TEAM" in breakdownData else ""
    newdata["Play"] = playNumber
    newdata["Quarter"] = int(breakdownData["QTR"])
    newdata["Yard"] = int(breakdownData["YARD LN"]) if "YARD LN" in breakdownData else ""
    newdata["Down"] = int(breakdownData["DN"]) if "DN" in breakdownData else ""
    newdata["Distance"] = int(breakdownData["DIST"]) if "DIST" in breakdownData else ""
    newdata["Gain/Loss"] = int(breakdownData["GN/LS"]) if "GN/LS" in breakdownData else ""
    newdata["Hash"] = breakdownData["HASH"].capitalize() if "HASH" in breakdownData else ""
    newdata["Play Type"] = breakdownData["PLAY TYPE"].capitalize() if "PLAY TYPE" in breakdownData else ""
    newdata["Result"] = breakdownData["RESULT"].capitalize() if "RESULT" in breakdownData else ""
    newdata["Play Direction"] = breakdownData["PLAY DIR"].capitalize() if "PLAY DIR" in breakdownData else ""
    newdata["Eff"] = breakdownData["EFF"].capitalize() if "EFF" in breakdownData else ""
    newdata["Series"] = int(breakdownData["SERIES"]) if "SERIES" in breakdownData else ""
    newdata["Offensive Strength"] = breakdownData["OFF STR"].capitalize() if "OFF STR" in breakdownData else ""
    newdata["Field/Boundary"] = breakdownData["FIELD/BOUND"].capitalize() if "FIELD/BOUND" in breakdownData else ""
    newdata["Opposing Team"] = breakdownData["OPP TEAM"] if "OPP TEAM" in breakdownData else ""

    # Save newdata into a csv file
    with open('data.csv', 'a') as f:
        f.write(','.join([str(newdata[key]) for key in newdata]) + '\n')

    # If the team is Bentonville West High School, save to another csv file, bwdata.csv
    if newdata["Opposing Team"] == "Bentonville West High School" or newdata["Team"] == "Bentonville West High School":
        with open('bwdata.csv', 'a') as f:
            f.write(','.join([str(newdata[key]) for key in newdata]) + '\n')

    # Get the clip's videos [clipAngles] for each [files][0]
    '''
    clipAngles = clip['clipAngles']
    for clipAngle in clipAngles:
        name = clipAngle['angleName']
        clipAngleFiles = clipAngle['files']
        print(name + ": " + clipAngleFiles[0]['fileName'])

        # Save the videos into a folder with the play number and save the file as the angle name
        video = requests.get(clipAngleFiles[0]['fileName'])
        # Make the folder playNumber if it doesn't exist

        if not os.path.exists('videos/' + str(playNumber)):
            os.makedirs('videos/' + str(playNumber))
        with open('videos/' + str(playNumber) + '/' + name + '.mp4', 'wb') as f:
            f.write(video.content)
    '''
