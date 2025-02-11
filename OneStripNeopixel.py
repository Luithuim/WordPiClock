#include all neccessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 55, brightness=1)

#Also create an arbitary count variable
x=0

#display hour
disphour = 0

#Focusing on a particular strip, use the command Fill to make it all a single colour
#based on decimal code R, G, B. Number can be anything from 255 - 0. Use a RGB Colour
#Code Chart Website to quickly identify a desired fill colour.
#pixels1.fill((0, 220, 0))

#Below demonstrates how to individual address a colour to a LED Node, in this case
#LED Node 10 and colour Blue was selected
'''pixels1[14] = (0, 20, 255)'''

#loop for clock
while (x<1):
    
    #getting time from local pi clock time (updates with internet so has a deviation of .22 seconds on average) this is a structure
    current = time.localtime()
    #formating time so readable as display time
    formatc = time.strftime("%H:%M:%S", time.localtime())
    
    #hour variable from time package is equal to current hour from local time structure
    hour = current.tm_hour
    #same for minutes
    mim = current.tm_min
    #varible to make clock work on hr interval instead of military time
    disphour = hour
    
    print(formatc)
    pixels1[30] = (0, 20, 255)
    pixels1[31] = (0, 20, 255)
    time.sleep(1)
    #led printout decision
    if hour > 12:
        disphour -= 12
        '''
        pixels1[0] = (0, 0, 0)
        pixels1[1] = (0, 0, 0)
        pixels1[2] = (0, 0, 0)
        pixels1[3] = (0, 0, 0)
        pixels1[4] = (0, 0, 0)
        pixels1[5] = (0, 0, 0)
        pixels1[6] = (0, 0, 0)
        pixels1[7] = (0, 0, 0)
        pixels1[8] = (0, 0, 0)
        pixels1[9] = (0, 0, 0)
        pixels1[10] = (0, 0, 0)
        pixels1[11] = (0, 0, 0)
        pixels1[12] = (0, 0, 0)
        pixels1[13] = (0, 0, 0)
        pixels1[14] = (0, 0, 0)
        pixels1[15] = (0, 0, 0)
        pixels1[16] = (0, 0, 0)
        pixels1[17] = (0, 0, 0)
        pixels1[18] = (0, 0, 0)
        pixels1[19] = (0, 0, 0)
        pixels1[20] = (0, 0, 0)
        pixels1[21] = (0, 0, 0)
        pixels1[22] = (0, 0, 0)
        pixels1[23] = (0, 0, 0)
        pixels1[24] = (0, 0, 0)
        pixels1[25] = (0, 0, 0)
        pixels1[26] = (0, 0, 0)
        pixels1[27] = (0, 0, 0)
        pixels1[28] = (0, 0, 0)
        pixels1[29] = (0, 0, 0)
        '''
        

        if disphour == 0:
            if mim < 3:
                #displays 'it is twelve oclock'
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
               
                pixels1[19] = (0, 20, 255)
                     
                pixels1[20] = (0, 20, 255)
              
                pixels1[27] = (0, 20, 255)
              
                pixels1[28] = (0, 20, 255)
                       
            elif mim >= 3 and mim < 8:
                #displays it is five past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
 
            elif mim >= 8 and mim < 13:
                #displays it is ten past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
        
            elif mim >= 13 and mim < 18:
                #displays it is a quarter past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
            
            elif mim >= 18 and mim < 23:
                #displays it is twenty past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
          
            elif mim >= 23 and mim < 28:
                #displays it is twenty five past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
        
            elif mim >= 28 and mim < 33:
                #displays it is half past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
           
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[19] = (0, 0, 0)

                pixels1[20] = (0, 0, 0)

                
            elif mim >= 38 and mim < 43:
                #displays it is twenty to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

                
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
            
            elif mim >= 48 and mim < 53:
                #displays it is ten to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 53 and mim < 58:
                #displays it is five to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                     
            elif mim >= 58:
                #displays it is one oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                       
                pixels1[27] = (0, 20, 255)

                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
  
        elif disphour == 1:
            if mim < 3:
                #displays it is one oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
            
                pixels1[27] = (0, 20, 255)

                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
                
            elif mim >= 8 and mim < 13:
                #displays it is ten past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
            elif mim >= 13 and mim < 18:
                #displays it is a quarter past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                  
            elif mim >= 18 and mim < 23:
                #displays it is twenty past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 23 and mim < 28:
                #displays it is twenty five past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
              
            elif mim >= 28 and mim < 33:
                #displays it is half past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
                 
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[12] = (0, 0, 0)
                   
            elif mim >= 38 and mim < 43:
                #displays it is twenty to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                    
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
               
            elif mim >= 48 and mim < 53:
                #displays it is ten to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
                 
            elif mim >= 53 and mim < 58:
                #displays it is a five to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                  
            elif mim >= 58:
                #displays it is two oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                               
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
        
        elif disphour == 2:
            if mim < 3:            
                #displays it is two oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                       
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
        
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[13] = (0, 0, 0)
         
            elif mim >= 38 and mim < 43:
                #displays it is twenty to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                               
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
            
            elif mim >= 48 and mim < 53:
                #displays it is ten to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 53 and mim < 58:
                #displays it is five to three
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
            
            elif mim >= 58:
                #displays it is three oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
         
        elif disphour == 3:
            if mim < 3:            
                #displays it is three oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
          

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
         
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
         

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[16] = (0, 0, 0)
                
                pixels1[17] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
    
            elif mim >= 53 and mim < 58:
                #displays it is five to four
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[14] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is four oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
     
        elif disphour == 4:
            if mim < 3:            
                #displays it is four oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                      
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[9] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[15] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[14] = (0, 0, 0)

         
            elif mim >= 38 and mim < 43:
                #displays it is twenty to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

          
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

         
            elif mim >= 48 and mim < 53:
                #displays it is ten to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
                               
            elif mim >= 53 and mim < 58:
                #displays it is five to five
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[15] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is five oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
       
        elif disphour == 5:
            if mim < 3:            
                #displays it is five oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
   
            elif mim >= 3 and mim < 8:
                #displays it is five past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
        
                pixels1[15] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[18] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[15] = (0, 0, 0)

        
            elif mim >= 38 and mim < 43:
                #displays it is twenty to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to six
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[18] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is six oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
     
        elif disphour == 6:
            if mim < 3:            
                #displays it is six oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
      
            elif mim >= 3 and mim < 8:
                #displays it is five past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                    
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                    
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[18] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to seven
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is seven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
   
        elif disphour == 7:
            if mim < 3:            
                #displays it is seven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
     
            elif mim >= 3 and mim < 8:
                #displays it is five past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
        
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)


            elif mim >= 23 and mim < 28:
                #displays it is twenty five past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[21] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[22] = (0, 0, 0)
                
                pixels1[23] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to eight
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[21] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is eight oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
      
        elif disphour == 8:
            if mim < 3:            
                #displays it is eight oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)

            elif mim >= 3 and mim < 8:
                #displays it is five past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  

           
            elif mim >= 28 and mim < 33:
                #displays it is half past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[24] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[21] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to nine
                pixels1[0] = (0, 20, 255)
                
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to nine
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[24] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is nine oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
           
        elif disphour == 9:
            if mim < 3:            
                #displays it is nine oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)

            elif mim >= 3 and mim < 8:
                #displays it is five past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 18 and mim < 23:
                #displays it is twenty past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)


            elif mim >= 23 and mim < 28:
                #displays it is twenty five past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  

           
            elif mim >= 28 and mim < 33:
                #displays it is half past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[24] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 53 and mim < 58:
                #displays it is five to ten
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[29] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is ten oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
               
                pixels1[29] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
                
        elif disphour == 10:
            if mim < 3:            
                #displays it is ten oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                
                pixels1[29] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                 
            elif mim >= 3 and mim < 8:
                #displays it is five past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 

         
            elif mim >= 8 and mim < 13:
                #displays it is ten past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                    
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)    
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[29] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to eleven
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is eleven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
 
        elif disphour == 11:
            if mim < 3:            
                #displays it is eleven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
     
            elif mim >= 3 and mim < 8:
                #displays it is five past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[25] = (0, 0, 0)
                
                pixels1[26] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to twelve
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is twelve oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)

    elif hour < 12:
        """**
        *12am
        */"""
        
        if disphour == 0:
            if mim < 3:
                #displays 'it is twelve oclock'
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
               
                pixels1[19] = (0, 20, 255)
                     
                pixels1[20] = (0, 20, 255)
              
                pixels1[27] = (0, 20, 255)
              
                pixels1[28] = (0, 20, 255)
                       
            elif mim >= 3 and mim < 8:
                #displays it is five past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
 
            elif mim >= 8 and mim < 13:
                #displays it is ten past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
        
            elif mim >= 13 and mim < 18:
                #displays it is a quarter past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
            
            elif mim >= 18 and mim < 23:
                #displays it is twenty past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
          
            elif mim >= 23 and mim < 28:
                #displays it is twenty five past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
        
            elif mim >= 28 and mim < 33:
                #displays it is half past twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
           
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[19] = (0, 0, 0)

                pixels1[20] = (0, 0, 0)

                
            elif mim >= 38 and mim < 43:
                #displays it is twenty to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

                
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
            
            elif mim >= 48 and mim < 53:
                #displays it is ten to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 53 and mim < 58:
                #displays it is five to one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                     
            elif mim >= 58:
                #displays it is one oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                       
                pixels1[27] = (0, 20, 255)

                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
  
        elif disphour == 1:
            if mim < 3:
                #displays it is one oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
            
                pixels1[27] = (0, 20, 255)

                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
                
            elif mim >= 8 and mim < 13:
                #displays it is ten past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
            elif mim >= 13 and mim < 18:
                #displays it is a quarter past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                  
            elif mim >= 18 and mim < 23:
                #displays it is twenty past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 23 and mim < 28:
                #displays it is twenty five past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
              
            elif mim >= 28 and mim < 33:
                #displays it is half past one
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
                 
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[12] = (0, 0, 0)
                   
            elif mim >= 38 and mim < 43:
                #displays it is twenty to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                    
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)
                
                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
               
            elif mim >= 48 and mim < 53:
                #displays it is ten to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
                 
            elif mim >= 53 and mim < 58:
                #displays it is a five to two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
                  
            elif mim >= 58:
                #displays it is two oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                               
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
        
        elif disphour == 2:
            if mim < 3:            
                #displays it is two oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
                       
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[13] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
        
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[13] = (0, 0, 0)
         
            elif mim >= 38 and mim < 43:
                #displays it is twenty to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                               
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
            
            elif mim >= 48 and mim < 53:
                #displays it is ten to three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  

                pixels1[17] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
            
            elif mim >= 53 and mim < 58:
                #displays it is five to three
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
            
            elif mim >= 58:
                #displays it is three oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
         
        elif disphour == 3:
            if mim < 3:            
                #displays it is three oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[12] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
          

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
         
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
         

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past two
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past three
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[16] = (0, 20, 255)  
              
                pixels1[17] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[16] = (0, 0, 0)
                
                pixels1[17] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
    
            elif mim >= 53 and mim < 58:
                #displays it is five to four
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[14] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is four oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255) 
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
     
        elif disphour == 4:
            if mim < 3:            
                #displays it is four oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                      
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
         
            elif mim >= 3 and mim < 8:
                #displays it is five past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
           
            elif mim >= 28 and mim < 33:
                #displays it is half past four
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[9] = (0, 20, 255)
                
                pixels1[11] = (0, 20, 255)
            
                pixels1[14] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[15] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[14] = (0, 0, 0)

         
            elif mim >= 38 and mim < 43:
                #displays it is twenty to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

          
            elif mim >= 43 and mim < 48:
                #displays it is a quarter to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

         
            elif mim >= 48 and mim < 53:
                #displays it is ten to five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
                               
            elif mim >= 53 and mim < 58:
                #displays it is five to five
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[15] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is five oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
       
        elif disphour == 5:
            if mim < 3:            
                #displays it is five oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
   
            elif mim >= 3 and mim < 8:
                #displays it is five past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
        
                pixels1[15] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past five
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[15] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[18] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[15] = (0, 0, 0)

        
            elif mim >= 38 and mim < 43:
                #displays it is twenty to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to six
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[18] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is six oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
     
        elif disphour == 6:
            if mim < 3:            
                #displays it is six oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
      
            elif mim >= 3 and mim < 8:
                #displays it is five past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                    
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past six
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[18] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                    
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[18] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to seven
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is seven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
   
        elif disphour == 7:
            if mim < 3:            
                #displays it is seven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
     
            elif mim >= 3 and mim < 8:
                #displays it is five past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
        
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)


            elif mim >= 23 and mim < 28:
                #displays it is twenty five past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past seven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[22] = (0, 20, 255)

                pixels1[23] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[21] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[22] = (0, 0, 0)
                
                pixels1[23] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to eight
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[21] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is eight oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
      
        elif disphour == 8:
            if mim < 3:            
                #displays it is eight oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)

            elif mim >= 3 and mim < 8:
                #displays it is five past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)  

           
            elif mim >= 28 and mim < 33:
                #displays it is half past eight
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[21] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[24] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[21] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to nine
                pixels1[0] = (0, 20, 255)
                
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to nine
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[24] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is nine oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
           
        elif disphour == 9:
            if mim < 3:            
                #displays it is nine oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)

            elif mim >= 3 and mim < 8:
                #displays it is five past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 18 and mim < 23:
                #displays it is twenty past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)


            elif mim >= 23 and mim < 28:
                #displays it is twenty five past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)  

           
            elif mim >= 28 and mim < 33:
                #displays it is half past nine
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[24] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[24] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 53 and mim < 58:
                #displays it is five to ten
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[29] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is ten oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
               
                pixels1[29] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
                
        elif disphour == 10:
            if mim < 3:            
                #displays it is ten oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                
                pixels1[29] = (0, 20, 255)
           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                 
            elif mim >= 3 and mim < 8:
                #displays it is five past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 

         
            elif mim >= 8 and mim < 13:
                #displays it is ten past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                    
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[29] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past ten
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)    
                
                pixels1[29] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[29] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to eleven
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is eleven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
 
        elif disphour == 11:
            if mim < 3:            
                #displays it is eleven oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
     
            elif mim >= 3 and mim < 8:
                #displays it is five past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[27] = (0, 0, 0)
              
                pixels1[28] = (0, 0, 0) 
            
            elif mim >= 8 and mim < 13:
                #displays it is ten past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 13 and mim < 18:
                #displays it is a quarter past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)
 
            elif mim >= 18 and mim < 23:
                #displays it is twenty past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)

            elif mim >= 23 and mim < 28:
                #displays it is twenty five past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)  
           
            elif mim >= 28 and mim < 33:
                #displays it is half past eleven
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[11] = (0, 20, 255)
                
                pixels1[9] = (0, 20, 255)
            
                pixels1[25] = (0, 20, 255)

                pixels1[26] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)
    
            elif mim >= 33 and mim < 38:
                #displays it is twenty five to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)

                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
                
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[9] = (0, 0, 0)
                
                pixels1[11] = (0, 0, 0)
                
                pixels1[25] = (0, 0, 0)
                
                pixels1[26] = (0, 0, 0)

            elif mim >= 38 and mim < 43:
                #displays it is twenty to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)

                pixels1[6] = (0, 20, 255)
                
                pixels1[7] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 43 and mim < 48:
                #displays it is a quarter to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[2] = (0, 20, 255)

                pixels1[4] = (0, 20, 255)
                
                pixels1[5] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[6] = (0, 0, 0)
                
                pixels1[7] = (0, 0, 0)
                
                pixels1[8] = (0, 0, 0)

            elif mim >= 48 and mim < 53:
                #displays it is ten to twelve
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
                
                pixels1[3] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[2] = (0, 0, 0)
                
                pixels1[4] = (0, 0, 0)
                
                pixels1[5] = (0, 0, 0)
  
            elif mim >= 53 and mim < 58:
                #displays it is five to twelve
                pixels1[0] = (0, 20, 255)
              
                pixels1[1] = (0, 20, 255)
                
                pixels1[8] = (0, 20, 255)
                
                pixels1[10] = (0, 20, 255)
              
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)
                
                pixels1[3] = (0, 0, 0)

            elif mim >= 58:
                #displays it is twelve oclock
                pixels1[0] = (0, 20, 255)
            
                pixels1[1] = (0, 20, 255)
            
                pixels1[19] = (0, 20, 255)

                pixels1[20] = (0, 20, 255)  
	      	           
                pixels1[27] = (0, 20, 255)
                  
                pixels1[28] = (0, 20, 255)
                
                pixels1[8] = (0, 0, 0)
                
                pixels1[10] = (0, 0, 0)
        
        
'''
pix 0 = 'it'
pix 1 = 'is'
pix 2 = 'a'
pix 3 = 'ten'
pix 4 = 'ter' of quarter
pix 5 = 'quar' of quarter
pix 6 = 'twen' of twenty
pix 7 = 'ty' of twenty
pix 8 = 'five'
pix 9 = 'past'
pix 10 = 'to'
pix 11 = 'half'
pix 12 = 'one'
pix 13 = 'two'
pix 14 = 'four'
pix 15 = 'five'
pix 16 = 'thr' of three
pix 17 = 'ee' of three
pix 18 = 'six'
pix 19 = 'twe' of twelve
pix 20 = 'lve' if twelve
pix 21 = 'eight'
pix 22 = 'sev' of seven
pix 23 = 'en' of seven
pix 24 = 'nine'
pix 25 = 'elev' of eleven
pix 26 = 'en' of eleven
pix 27 = 'ock' of o'clock
pix 28 = 'ocl' of o'clock
pix 29 = 'ten' 
pix 30 (which does not exist) = 'IEEE'
pix 31 (to be added via led or other/DNE) = 'UVM' 
'''

#Sleep for three seconds, You should now have all LEDs showing light with the first node
#Showing a different colour
time.sleep(4)

#Little Light slider script, it will produce a nice loading bar effect all the way up
#and then all the way back
#This was created using a While Loop taking advantage of that arbitary variable to determine
#which LED Node we will taget/index with a different colour

#Below will loop until variabe x has value 35
"""while x<35:
    
    pixels1[x] = (255, 0, 0)
    pixels1[x-5] = (255, 0, 100)
    pixels1[x-10] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    #Add a small time pause which will translate to 'smoothly' changing colour
    time.sleep(0.05)

#below section is the same process as above loop just in reverse
while x>-15:
    pixels1[x] = (255, 0, 0)
    pixels1[x+5] = (255, 0, 100)
    pixels1[x+10] = (0, 255, 0)
    x=x-1
    time.sleep(0.05)

#Add a brief time delay to appreciate what has happened    
time.sleep(4)

#Complete the script by returning all the LED to off
pixels1.fill((0, 0, 0))

"""