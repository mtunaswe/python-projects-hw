"MERT TUNA | 0080363 | SECTION-04"

L = []


def songtitle_check(title,playlist):            #I have defined a auxilary function to check if song is found in
    title = title.lower()                       #playlist. If it is found function takes its index on list and return 
                                                #isfound true
    isfound = False
    
    index = 0
  
    for songs in playlist:
        if title == songs[0].lower():           #to make the function char insensitive, I used lower() function, and 
            isfound = True                      #checked if it is same with lower chars of the title. 
            index = playlist.index(songs)       
            break                               #break the loop because next might not be same with title.
        
    return index, isfound
  
    
def add_song(playlist, title, year, singer): 
    
    index, isfound = songtitle_check(title,playlist) 
    
    if isfound == True:                     #if song is found in playlist function returns a warning.
        print (f"(error in add): {title} already exists.")
            
    else:                                   #otherwise it add the song to the list.
        playlist.append([title,year,singer,False])
            

                
def remove_song(playlist, title):
    
    index, isfound = songtitle_check(title,playlist)        
    
    if isfound == False:
        print (f"(error in remove): {title} is not found")
        
    else:
        del playlist[index]             #if song is found in playlist, the function got its index removed from the list.
       
    
    
def like_song(playlist, title):
    
    index, isfound = songtitle_check(title,playlist) 
    
    if isfound == False:
        print(f"(error in like): {title} is not found")
        
    else:
        playlist[index][3] = True
        
    
    
def unlike_song(playlist, title):
    
    index, isfound = songtitle_check(title,playlist) 
    
    if isfound == False:
        print(f"(error in unlike): {title} is not found")
        
    else:
        playlist[index][3] = False
    
 
    
def display_all_songs(playlist):
    if len(playlist) == 0:              #if length of list is 0, it returns empty playlist warning.
        print("--EMPTY PLAYLIST--")
        
    else:
        print("PLAYLIST")               
        for row in playlist:            
            print(row[0], "by", row[2])
    
    
def display_all_liked_songs(playlist):
    for isanyliked in playlist:         #check if there is any liked song in playlist, and print LIKED SONGS accordingly
        if isanyliked[3] == True:       #break for loop to print only once.
            print("LIKED SONGS")
            break
        
    else:
        print("--EMPTY LIKED PLAYLIST--")
            
    for likedsong in playlist:          
        if likedsong[3] == True:
            print(likedsong[0], "by", likedsong[2])
    
    
    
def show_song(playlist, title):
    
    index, isfound = songtitle_check(title,playlist) 
    
    if isfound == True:                     #check if song is found in playlist, then check the boolean flag 
        if playlist[index][3] == True:      #if it is true which shows the song is liked. If the song is liked, then
            print(title,"+")   #print + afterwards.
        
        else:
            print(title)       #first element of the song is title, then year, then the performer.
            
        print("Released in", playlist[index][1],"\nPerformed by", playlist[index][2])
        
    else:
        print (f"(error in show): {title} is not found.")
        
    