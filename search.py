import t1337x
import solidtorrent


def menu():
    '''
        Menu of commands for the user
    '''

    print()
    print("1. s - Search for torrent(through 1337x site)\n2. l - Want Long results , Search for torrent(through solid torrent)\n3.  q or Q- for exit from the program\n")
    choice=input()

    if(choice=='s'):
        query=input("Search for torrents.. ").replace(" ",'+')
        t1337x.t1337x_search(query)

    elif(choice=='q' or choice=='Q'):
        exit()

    elif(choice=='l'):
        query=input("Search for torrents.. ").replace(" ",'%20')
        solidtorrent.solidtorrent_search(query)

    else:
        print("It look like you did not read the command right or press something else by mistake.\n Don't worry try again no one is judging ")
        menu()


def main():
    '''
        The main() funtion
    '''
    print()
    print("------------------------------Torrent Finder------------------------------")
    print("    CLI agent for searching Torrent and find magnet link    ")

    menu() #calling menu


if __name__ == '__main__':
    main()
