#!/usr/bin/env python3
import os
import requests
import thesecrets
import re

# Create newdatacsv with headers
# Create newdatacsv with headers
with open("data.tsv", "w") as f:
    f.write(
        "Game Date	Team	Play	Quarter	Yard	Down	Distance	Gain/Loss	Hash	Play Type	Result	Play Direction	Eff	Series	Offensive Strength	Field/Boundary	Opposing Team	Offensive Formation	Offensive Play	Defensive Front	Defensive Coverage	Defensive Play\n"
    )
with open("bwdata.tsv", "w") as f:
    f.write(
        "Game Date	Team	Play	Quarter	Yard	Down	Distance	Gain/Loss	Hash	Play Type	Result	Play Direction	Eff	Series	Offensive Strength	Field/Boundary	Opposing Team	Offensive Formation	Offensive Play	Defensive Front	Defensive Coverage	Defensive Play\n"
    )

# Define the payload for the POST request
payload = {
    "teamId": "11214",
    "categoryIds": [
        "66314897",
        "63284394",
        "63285004",
        "52105401",
        "111744760",
        "111744761",
        "111744762",
        "111744784",
        "111744785",
        "111744786",
        "112560602",
        "112560603",
        "112560604",
        "112560634",
        "112560635",
        "112560636",
        "112560682",
        "112560683",
        "112560684",
        "112560715",
        "112560716",
        "112560717",
        "112560755",
        "112560756",
        "112560757",
        "112560783",
        "112560784",
        "112560785",
        "112561709",
        "112561710",
        "112561711",
        "112561712",
        "113079617",
        "113079618",
        "113079619",
        "113079620",
        "113079621",
        "115181131",
        "115181132",
        "115181133",
        "115181151",
        "115181152",
        "115181153",
        "112560917",
        "112560918",
        "112560919",
        "112563267",
        "112563268",
        "112563269",
        "112563331",
        "112563332",
        "112563333",
        "112563347",
        "112563348",
        "112563349",
        "112563372",
        "112563373",
        "112563374",
        "112563407",
        "112563408",
        "112563409",
        "112563529",
        "112563530",
        "112563531",
        "112563581",
        "112563582",
        "112563583",
        "112563910",
        "112563911",
        "112563912",
        "112563947",
        "112563948",
        "112563949",
        "112563621",
        "112563622",
        "112563623",
        "111744704",
        "111744705",
        "111744706",
        "99334328",
        "99334329",
        "99334330",
        "99334331",
        "99334332",
        "99334333",
        "99334334",
        "99334335",
        "99334336",
        "99334337",
        "99334338",
        "101695188",
        "101695364",
        "101695365",
        "102046045",
        "103953916",
        "103953917",
        "103953918",
        "103953919",
        "103953920",
        "103953921"
    ]
}

# Send the POST request
response = requests.post(
    "https://www.hudl.com/Library/ExpandSeasonCategories",
    json=payload,
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.hudl.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://www.hudl.com/library/11214",
        "Cookie": thesecrets.thecookies,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    },
)

# print(response.json())

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.hudl.com/library/11214",
    "Cookie": thesecrets.thecookies,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
}

# Save response json to file
with open('response.json', 'w') as f:
    f.write(str(response.json()))

count = 0

for o in response.json():
    count = count + 1
    print(count)
    name_of_playlist = re.search(r'<span class="category-name">(.*?)</span>', o["html"]).group(1)

    if 'practice' in name_of_playlist.lower():
        continue

    theid = ''
    match = re.search(r'cutup_(\d+)', str(o["html"]))
    print(str(match))
    if match:
        theid = match.group(1)
    else:
        continue

    print(name_of_playlist + ": " + theid)

    response = requests.get(thesecrets.theurl.replace('theid', theid), headers=headers)

    # Get a list of [clipsList][clips]
    resp = response.json()
    clips = resp["clipsList"]["clips"]

    for clip in clips:
        # Get the clips breakdownData
        breakdownData = clip["breakdownData"]
        playNumber = int(breakdownData["PLAY #"])
        newdata = {}
        newdata["Game Date"] = resp["cutupCreatedOn"]
        newdata["Team"] = breakdownData["TEAM"] if "TEAM" in breakdownData else ""
        newdata["Play"] = playNumber
        newdata["Quarter"] = int(breakdownData["QTR"]) if "QTR" in breakdownData else ""
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
        newdata["Offensive Formation"] = breakdownData["OFF FORM"] if "OFF FORM" in breakdownData else ""
        newdata["Offensive Play"] = breakdownData["OFF PLAY"] if "OFF PLAY" in breakdownData else ""
        newdata["Defensive Front"] = breakdownData["DEF FRONT"] if "DEF FRONT" in breakdownData else ""
        newdata["Defensive Coverage"] = breakdownData["DEF COV"] if "DEF COV" in breakdownData else ""
        newdata["Defensive Play"] = breakdownData["DEF PLAY"] if "DEF PLAY" in breakdownData else ""

        if newdata["Play Type"] == "" or newdata["Down"] == "" or newdata["Distance"] == "":
            continue

        # Save newdata into a csv file
        with open('data.tsv', 'a') as f:
            f.write('\t'.join([str(newdata[key]) for key in newdata]) + '\n')

        # If the team is Bentonville West High School, save to another csv file, bwdata.csv
        if newdata["Opposing Team"] == "Bentonville West High School" or newdata["Team"] == "Bentonville West High School":
            with open('bwdata.tsv', 'a') as f:
                f.write('\t'.join([str(newdata[key]) for key in newdata]) + '\n')

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
