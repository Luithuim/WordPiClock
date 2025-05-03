This file should only be opened in the event of total data loss.

This means you should be looking at this if the sd card becomes corrupted, unusuable, or otherwise non-functioning.

In that case follow these steps:

1) flash or image a new PiOS onto the raspberry pi 4 model B

2) Connect to wifi, using the linux method *DO NOT USE UVM'S GIVEN RASPBERRY PI METHOD*

3) Open a new terminal, and type in these 3 lines to download the packages required for the code to run:
     
     1) sudo pip3 install rpi_ws281x --break-system-packages
  
     2) sudo pip3 install adafruit-circuitpython-neopixel --break-system-packages
  
     3) sudo python3 -m pip install --force-reinstall adafruit-blinka --break-system-packages
  
     4) If you are prompted to confirm, even if it breaks any packages, confirm by pressing y

  4) Open the file directory and in the home or whatever directory you the new Administrator will have to create, and create a new .py file in the desktop section

  5) Right click on file properties or navigate to it, and make sure it opens in thonny.

  6) Copy the original file called "OneStripNeopixel.py" into it, and run it.

  7) If the code returns an error, that is not a syntax, and tells you that it is not run as 'root' or with certain 'privileges' then, close out of the thonny tab, go to the terminal, and type in 'sudo thonny', and try again

  8) To restore .sh functionality, or the ability for the clock to start as soon as being plugged in, requires a little understanding of the nano GUI, steps 9-19 will guide you through

  9) In a terminal window, cd, or change directory to whatever file directory you have the .py file in.

  10) For example, at the time of writing this, the cd is cd /home/IEEE/Desktop

  11) Next create a nano file, using the line "sudo nano launcher.sh", sudo makes the file only accessible with root privileges meaning only with the sudo command

  12) launcher.sh is generally considered to be the standard naming scheme for such a nano file, as such leave it as is, or change it if you're willing (do not complain if that breaks the rest of the code)

  13) If you are prompted to select an editor, select NANO, or what is usually option 1

  14) In the nano file scroll to the bottom, even if there is a bunch of text, ignore it, because that is functional and help data, that lets be honest, if you are here, you couldn't understand it anyways.

  15) Once there, add these four lines, which are generalized to the code at the time of writing:

      1) cd / (which takes you to root)
     
      2) cd /home/IEEE/Desktop/ (brings the directory to the folder with the file in it)
     
      3) sudo python OneStripNeopixel.py (tell the computer to run the code with root privileges {sudo} )
     
      4) cd / (takes the directory back to root)

  16) hit control and the x key together to save, or ctrl+x, and when prompted to save the file put y. Then press enter to return to the terminal

  17) Once back in the terminal type "sudo chmod 755 launcher.sh"

  18) If you encounter an error at this point which is unlikely, but possible, search it up as I do know it is possible and has been solved already

  19) If you wish to test the .sh file, you may do so by using the command "sh launcher.sh" in the terminal

  20) At this point the setup of the .sh file is complete, and the error handling and actual setup begins here, and steps 21-26 will guide you through

  21) First we need a crontab, so in the terminal type "sudo crontab -e"

  22) If you are presented with the option to choose an editor at this point, once again choose NANO or most commonly option 1

  23) Once again scroll through any text, and at the bottom add the line "@reboot sh /home/IEEE/Desktop/launcher.sh >/home/IEEE/logs/cronlog 2>&1", where you replace the /home/IEEE/Desktop/ and /home/IEEE/logs/ for wherever your .sh and logs folder is respectively

  24) save and exit with the ctrl+x combo, and remember to actually save the new buffer, by pressing y before pressing enter/return to exit to the terminal

  25) At this point, if you need to edit either files, just type in their name, with sudo before it, as you need root privileges.

  26) now type in "sudo reboot" into the terminal, and let the magic work itself out

  27) If the code does not work, check the logs using the commands "cd logs" and "cat cronlog"

  28) At this point everything should be working and if not ¯\_(ツ)_/¯
