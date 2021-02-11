#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=FPyt8xOCwTZd4Irc9jIjf75zplVXcIrIzPoL0krh' ## this is our api key

## pretty print json
def main():
    """Get variables"""
    date = input('Enter date of image you would like to view as [YYY-MM-DD]: ')
    
    
    """run-time code"""
    if date == '':
        nasaapiobj = requests.get(NASAAPI + MYKEY) # call the webservice

    else:
        print(NASAAPI + 'date=' + date + MYKEY)
        nasaapiobj = requests.get(NASAAPI + 'date=' + date + '&' +  MYKEY)
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['date'])
    print(nasaread['title'])
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

