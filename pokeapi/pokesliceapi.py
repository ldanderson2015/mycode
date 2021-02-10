#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget

def main():
    pokemon = input('choose your pokemon! : ').lower().strip()
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

    picurl = (pokeapi["sprites"]["front_default"])
    wget.download(picurl, "/home/student/")



    print("URL: " + pokeapi["sprites"]["front_default"])
    print("# of Games: " + str(len(pokeapi["game_indices"])))

    for movedict in pokeapi["moves"]:
        print(movedict["move"]["name"])

main()
