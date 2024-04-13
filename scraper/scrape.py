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
clips = response.json()['clipsList']['clips']

for clip in clips:
	# Get the clips breakdownData
	breakdownData = clip['breakdownData']
	playNumber = int(breakdownData['PLAY #'])
	print(breakdownData)

	# Get the clip's videos [clipAngles] for each [files][0]
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
