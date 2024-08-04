#Socket and Communication Script
import socket
import time


#ports
networkPort = 5025
supplyIP = "169.254.152.229"

#Connector object which interfaces with the socket object
class Connector ():

    def __init__(self): 
        self.port = networkPort
        self.IP =supplyIP

        self.time = None
        self.question = input("Do you want ramping or not? \n")

        self.voltage = [] 
    
    def query(self,socket):
        with socket.socket() as socket:
            socket.connect((self.supplyIP, self.networkPort))
            socket.sendall(("*IDN?" + "\n").encode("ascii"))
            socket.sendall(("OUTP:COUP DC" + "\n").encode("ascii"))
            rec = socket.recv(1024)
            print(rec.decode("ascii"))

#Selects the choice and runs the AVR
    def algorithm (self): 
        i = 0
        if (i < 1.5):
            socket.sendall((f"VOLT:OFFS {i}\n").encode("ascii"))
            socket.sendall(("VOLT?\n").encode("ascii"))
            time.sleep(1)
            i += 0.1
                
        else: 
            socket.sendall((f"VOLT:OFFS 0 \n").encode("ascii"))
            time.sleep(1)
            i = 0
            print(i)
            
        
        return i


