#!/usr/bin/env python3

import requests ## 3rd party URL lookup

def moon_lengths(missdistance):
    return (float(missdistance)/238900)

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=' + input('Enter a start date: ')  ## start date for data
    enddate = '&end_date=' + input('Enter an end date: ') ## create a mechanism to utilize enddate
    mykey = '&api_key=FPyt8xOCwTZd4Irc9jIjf75zplVXcIrIzPoL0krh' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()
    
    print(f"Currently tracking {neojson['element_count']} objects.")

    hazard_count = 0
    closest_distance = 93000000
    closest_name = 'Sol'
    for date in neojson['near_earth_objects'].keys():
        for dictionary in neojson['near_earth_objects'][date]:
            #print(moon_lengths(dictionary['close_approach_data'][0]['miss_distance']['miles']))
            if float(dictionary['close_approach_data'][0]['miss_distance']['miles']) < closest_distance:
                closest_distance = float(dictionary['close_approach_data'][0]['miss_distance']['miles'])
                closest_name = dictionary['name']
            if dictionary['is_potentially_hazardous_asteroid'] == True:
                hazard_count += 1
                print("potenially hazarddous object: " + dictionary['name'])
                print(f"     {dictionary['name']} is " + str(moon_lengths(dictionary['close_approach_data'][0]['miss_distance']['miles'])) + " lunar distances away.")

    print(f"There are currently {hazard_count} potentially hazardous objects being tracked.")
    print(f"The closest object in date range is {closest_name} at {closest_distance} miles away")

    #print(neojson)

## call main
main()

