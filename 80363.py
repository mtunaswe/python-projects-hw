"MERT TUNA | 0080363 | SECTION-04"

#I defined 3 functions for tasks. 
#first read the user-chosen text file and return dict and list,
#second print the most eastern, western, northern, southern cities using list created in first function,
#the last one writing a new user-chosen text file using info in dict created iin first function.

def cities_read_func(fname):
    
    list_of_cities = []                                                 #create a new list.
    
    infile = open(fname, "r")
    
    for line in infile:                                                 #read, split and append every line to a new list. 
        list_of_cities.append(line.split())
        
    infile.close()
    
    dictionary_of_majors = {}                                           #create a new dict. 
    
    for i in range(len(list_of_cities)):
        if list_of_cities[i][0] == list_of_cities[i][3]:                
            
            city_number = 0                                             
            population = 0
                        
            for j in range(len(list_of_cities)):
                if list_of_cities[j][3] == list_of_cities[i][0]:
                    city_number += 1                                    
                    
                    if list_of_cities[j][4] != "-1":
                        population += int(list_of_cities[j][4])
                        
            dictionary_of_majors[list_of_cities[i][0]] = city_number, population
            
        
    return dictionary_of_majors,list_of_cities                          #return dict and list to use in auxilary functions.


def nort_east_west_south(fname):
    dict_cities, list_of_cities = cities_read_func(fname)
    
    latitudes = []                                                      #created lists for latitudes and longitudes
    
    longitudes = []
    
    for k in range(len(list_of_cities)):                    
        latitudes.append(float(list_of_cities[k][1]))                   #appending latitudes and longitudes of cities to created lists. 
        
        longitudes.append(float(list_of_cities[k][2]))
        
    for m in range(len(list_of_cities)):
        if float(list_of_cities[m][1]) == max(latitudes):               #because in text, we have no info about the location of the country
            northern = list_of_cities[m][0]                             #to equador and greenwich, I take maximum latitudes and longitudes,
                                                                        #as most northern and eastern cities, respectively.
        elif float(list_of_cities[m][1]) == min(latitudes):
            southern = list_of_cities[m][0]
            
        elif float(list_of_cities[m][2]) == max(longitudes):
            eastern = list_of_cities[m][0]
            
        elif float(list_of_cities[m][2]) == min(longitudes):
            western = list_of_cities[m][0]
    
    print(f"Most eastern city: {eastern}\nMost western city: {western}\nMost northern city: {northern}\nMost southern city: {southern}")

       
def output_cities(fname, fnameoutput):
    dict_cities, list_of_cities = cities_read_func(fname)
    
    outfile = open(fnameoutput,"w")
    
    for keys,values in dict_cities.items():
        outfile.write(keys + " " + str(values[0]) + " " + str(values[1]) + "\n")
        
    print("Cities are saved")
    
    outfile.close()
    

def main():
    fname = input("Enter an input filename: ")
    
    nort_east_west_south(fname)

    output_fname = input("Enter an output filename: ")
    
    output_cities(fname, output_fname)
    
main()
                
    

        
    
        
        
        