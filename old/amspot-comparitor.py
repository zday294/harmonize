#This script searches a Spotify playlist and an Apple Music playlist and finds the songs that are in one or the other but not both

from secrets import spotify_client_id, spotify_client_secret, spotify_username

import sys
from enum import Enum
import json

#here's a question, do i import based on user needs
#probably not, since it looks like im just doing apple music and spotify 

import applemusicpy #docs at https://apple-music-python.readthedocs.io/en/latest/

import spotipy #docs at https://spotipy.readthedocs.io/en/2.18.0/
from spotipy.oauth2 import SpotifyOAuth


class Library(Enum):
	APPLE = 1
	SPOTIFY = 2

class Song:
	def __init__(self, _name, _artist, _album, _library):
		self.name = _name
		self.artist = _artist
		self.album = _album
		self.libaray = _library

	def __eq__(self, obj)  -> bool:
		neq = self.name == obj.name
		areq = self.artist == obj.artist
		aleq = self.album == obj.album
		
		return neq and areq and aleq

	def __ne__(self, obj) -> bool:
		return not self == obj
	
	def __str__(self):
		return f"{self.name},{self.artist},{self.album},{self.library}"
	
	def __repr__(self):
		return str(self)



def getSpotifyPlaylistID(name:str, sp) -> str:
	jsonResponse = sp.current_user_playlists()

	# with open("playlists.json", "w") as pjson:
	# 	pjson.write(str(jsonResponse))

	pID = ""

	for playlist in jsonResponse["items"]:
		if playlist["name"] == name:
			# print(f"Found {name}")
			pID = playlist["id"]

	return pID


# Returns none on failure
def getSpotifySongs(playlistname: str) -> list:
	#grab playlist from spotify	

	scope = "playlist-read-private"
	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=spotify_client_id, client_secret=spotify_client_secret, redirect_uri="http://localhost:8888/callback/", open_browser=True))
	print("spotify connected")

	playlistID = getSpotifyPlaylistID(playlistname, sp)
	#we have the id, now we need everything in that playlist

	playlistItemsResponse = sp.playlist_items(playlist_id=playlistID)


	# print(str(playlistItems))
	# with open("songs.json", "w") as jj:
	# 	jj.write(str(playlistItems))

	songs = []

	for song in playlistItemsResponse["items"]:
		track = song["track"]
		name = track["name"]
		artist = track["artists"][0]["name"]
		album = track["album"]["name"]

		songs.append(Song(name, artist, album, "Spotify"))


	print(songs)

	return songs #list of spotify songs

# Returns none on failure
def getAppleMusicSongs(playlistname: str) -> list:
	#grab playlist from apple music
	#need to turn playlistname into a playlist id
	#use search from api
	
	#search through json to find playlist name and id

	#use either playlist or playlist_relationship from apple music api

	return None #list of apple music songs

def getNonIntersection(list1, list2) -> list:
	#this basically is the union minus the intersection
	union = list(set(list1) | set(list2)) #union - https://www.geeksforgeeks.org/python-union-two-lists/
	intersect = list(set(list1).intersection(set(list2)))
	fin = union - intersect
	return fin


def main():
	#maybe also have the script detect similar songs on different albums?
	#also truncate long names unless requested by user not to do so

	#get playlist names
	spname = input("Spotify playlist: ")
	ampname = input("Apple Music playlist (Press enter for same name): ") #would be better if i could put in as cmd line args
	if ampname == "":
		ampname = spname

	print(f"Searching for playlist {spname} on Spotify")
	spsongs = getSpotifySongs(spname)
	if spsongs == None:
		print(f"Error finding {spname} on Spotify. Make sure you spelled it correctly")
		exit()
	print("Success")
	
	print(f"Searching for playlist {ampname} on Apple Music")
	ampsongs = getAppleMusicSongs(ampname)
	if ampsongs == None:
		print(f"Error finding {ampname} on Apple Music. Make sure you spelled it correctly")
		exit()
	print("Success")

	#get intersection of the sets, python has an intersection method, dont know if it works with lists
	nonintersect = getNonIntersection(spsongs, ampsongs)

	inApple, inSpotify = splitList(nonintersect)

	listingString = "In Spotify playlist only\nTitle\tArtist\tAlbum\n" # fill in here, maybe a function? or a loop?
	for song in inSpotify:
		listingString += str(song) + "\n"

	listingString += "In Apple Music playlist only\nTitle\tArtist\tAlbum\n"
	for song in inApple:
		listingString += str(song) + "\n"	

	print(listingString)
	
	#should ask whether to update playlists to include disparate songs
	#then print report of songs that failed to sync
	

if __name__ == "__main__":
	main()
