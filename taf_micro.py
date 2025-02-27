import json
from time import sleep
import os
import datetime



while(True) :
    
    date_time = datetime.datetime.now()
    formatted_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)
    
    sleep(15)
    
    
    found = False
    found2 = False
    
    comm_pipe =  open("request.txt", 'r') 
        
    first_param = comm_pipe.readline().strip()
    
    
    if first_param == "save":
        second_param = comm_pipe.readline().strip()
        
        
        data = json.load(comm_pipe)      
        data["backup_name"] = "backup"
        data["timestamp"] = formatted_time
    

    elif first_param == "delete":
        second_param = comm_pipe.readline().strip()
        
    comm_pipe.close()
        
    
    if first_param == "save":
        with open("tracks_effects.json", 'w') as json_file:
            
            sleep(5)
            json.dump(data, json_file, indent=4)
            
            
        with open("response.txt", 'w') as response_file:
            
            sleep(5)
            response_file.write("success\n")
            response_file.write("Track/effect groups saved successfully\n")
            response_file.write("Backup_Name=backup\n")
            sleep(5)
                
                
    elif first_param == "delete":
        try:
            
            sleep(5)
            os.remove("tracks_effects.json")
            found = True
            
        except FileNotFoundError:
            print("Error: tracks_effects.json doesn't exit.")
                
                
        except Exception as e:
                print(f"An error occurred: {e}")
            
                
        with open("response.txt", 'w') as response_file:
            
            sleep(5)
            
            if found == True:
                response_file.write("success\n")
                response_file.write("Track/effect groups deleted successfully\n")
                sleep(5)
            else:
                response_file.write("error\n")
                response_file.write("Track/effect groups could not be deleted\n")
                sleep(5)
                

    elif first_param == "restore":
        
        try:
            with open("tracks_effects.json", 'r') as json_file:
                data = json.load(json_file)
                found2 = True
            
        except FileNotFoundError:
            print("Error: tracks_effects.json doesn't exit.")
        

        json_text = json.dumps(data)
            

        with open("response.txt", 'w') as response_file:
            
            sleep(5)
            
            if found2 == True:
                response_file.write("success\n")
                response_file.write("Track/effect groups restored successfully\n")
                response_file.write(json_text + '\n')
                sleep(5)
            else:
                response_file.write("error\n")
                response_file.write("Track/effect groups could not be restored\n")
                sleep(5)
            
    
        
        
        
        
        
     
    
        
        
        
        
    
    