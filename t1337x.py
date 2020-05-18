from bs4 import BeautifulSoup as bs
import pyperclip as pc
import requests
import re
import search


def t1337x_search(query):
    '''
    Search for torrents and return results if find anything and print no result were found and start process again
    '''

    url='https://1337x.to/search/'+query+'/1/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
    source=requests.get(url,headers=headers)

    soup=bs(source.text,'html.parser')

    if(soup.find_all('td',class_='coll-1 name')): #check if it return null or something ( case of wrong serach query)
        results=soup.find_all('td',class_='coll-1 name')
        size=soup.find_all('td',class_="coll-4 size mob-vip")
        search_result(soup,results,size) #call for getting results

    else:
        print("No results were returned. Please refine your search.")
        search.menu() #start program again



def search_result(soup,results,size):
    '''
    return search result of torrents name upto 10 and ask user for select the desired one
    '''
    links=[] #ltst for storing all url links
    i=1

    for r,s in zip(results,size):   #print serach result upto 15 torrents

        print(i,re.sub('[\W_]+', ' ', r.text[:49]),s.text.replace("B","B,seedrs-"))
        i=i+1


    for link in soup.find_all('a'):
                                        #getting link for all 15 torrents
        b=link.get('href')
        if re.match("^/torrent",b):
            links.append("https://1337x.to"+b)

    print("select a torrent")
    choice=int(input())

    ch_url=links[choice-1] #return url of desired torrent
    getTorrent(ch_url)



def getTorrent(ch_url):
    '''
    return magnet link of desired torrent which user select
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
    source=requests.get(ch_url,headers=headers)
    soup=bs(source.text,'html.parser')
    magnet=soup.find_all('a')

    #searching for magnet link

    for link in magnet:

        b=link.get('href')
        if re.match("^magnet:",b):
            magnet_link=b
            break
    print("\nHere is your magnet link for the torrent \n")
    print(magnet_link)
    pc.copy(str(magnet_link))
    print ("\nWe make your work more easy\nYour magnet link is now in your clipboard\nGo to seedr.cc or open Torrent Downloader application and paste the link your download will start.")
    print("\nThanks for using Torrent Finder \nCreated with " + "\u2764"+ " by Rishabh Sharma")
    search.menu()
