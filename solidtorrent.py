from bs4 import BeautifulSoup as bs
import pyperclip as pc
import requests
import re
import search




def solidtorrent_search(query):
    '''
        search on solid torrent for long result(upto 20) and print magnet link of torrent and also copy it to clipboard
    '''

    url='https://solidtorrents.net/search?q='+query
    #print(url)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
    source=requests.get(url,headers=headers)

    soup=bs(source.text,'html.parser')

    result=soup.find_all('h3',class_='subtitle-2 text-truncate') #name of all torrents (20)

    size=soup.find_all('strong') #find size of torrent
    seeders=soup.find_all('span',class_="green--text darken-4 font-weight-bold")
    leechers=soup.find_all("span",class_="red--text darken-4 font-weight-bold")

    magnet=soup.find_all('a') #for find href links

    magnet_links=[] #list for storing magnet links

    i=1
    for r,s in zip(result,size) :
        print(i,r.text+"\nsize="+s.text+" | seeders="+sd.text.rstrip()+"| leechers="+l.text.replace("\n",""))
        i+=1

    for link in magnet:
        b=link.get('href')
        if re.match("^magnet:",b):
            magnet_links.append(b)


    print("Select a torrent")
    ch=int(input())

    print(magnet_links[ch-1])


    print("\nHere is your magnet link for the torrent \n")
    pc.copy(str(magnet_links[ch-1]))

    print ("\nWe make your work more easy\nYour magnet link is now in your clipboard\nGo to seedr.cc or open Torrent Downloader application and paste the link your download will start.")

    print("\nThanks for using Torrent Finder \nCreated with " + "\u2764"+ " by Rishabh Sharma")

    search.menu()
