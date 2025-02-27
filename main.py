import json
from time import sleep
import sys



def main():
    
    
    
    groups =  {
 "groups": [
 {
 "group_id": 1,
 "group_name": "Drums",
 "items": ["Kick", "Snare", "Hi-Hat"]
 },
 {
 "group_id": 2,
 "group_name": "Synths",
 "items": ["Lead", "Pad", "Bass"]
 }
 ]
    }
    
    
    json_string = json.dumps(groups)
    
    while (True):
        
        
        operation = input("Enter 1 to save groups, 2 to delete groups, or 3 to restore groups, or 4 to exit ")
        
        if operation == '1':
            
            with open('request.txt', 'w') as comm_pipe1:
                sleep(10)
                comm_pipe1.write("save\n")
                comm_pipe1.write("tracks_effects.json\n")
                json.dump(groups, comm_pipe1, indent=4)
                
                
                
            sleep(38)
            with open('response.txt', 'r') as comm_pipe2:
                response = comm_pipe2.read()
                print(response)
            
                
                
        elif operation == '2':
            
            with open('request.txt', 'w') as comm_pipe1:
                sleep(10)
                comm_pipe1.write("delete\n")
                comm_pipe1.write("backup\n")
                
                
            sleep(37)
            with open('response.txt', 'r') as comm_pipe2:
                response = comm_pipe2.read()
                print(response)
                
                    
        elif operation == '3':
            
            with open('request.txt', 'w') as comm_pipe1:
                sleep(10)
                comm_pipe1.write("restore\n")
                
                
            sleep(37)
            with open('response.txt', 'r') as comm_pipe2:
                response = comm_pipe2.read()
                print(response)
            
                
        elif operation =='4':
            sys.exit()
            


if __name__ == "__main__":
    
    main()
    
    