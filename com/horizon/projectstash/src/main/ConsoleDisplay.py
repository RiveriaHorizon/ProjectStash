'''
Created on 14 Jan 2018

@author: Yong Quan
'''
from colorama import init, Fore, Back, Style

class ConsoleDisplay:
    '''
    Console display formatting to look nicer for the user
    '''


    def __init__(self):
        '''
        Constructor
        '''
        init()
    
    def displayLineDivider(self):
        print("=============================================")
        
    def displayWelcomeMessage(self):
        self.displayLineDivider()
        print("||         Welcome to ProjectStash         ||")
        self.displayLineDivider()
    
    def displayExitMessage(self):
        print(Back.LIGHTWHITE_EX + Fore.MAGENTA + "Program exiting... See you!")
        print(Style.RESET_ALL)
    
    def displayDirectoryMessage(self):
        print("Please choose directory to clone to...")
        
    def displayStartMessage(self, fp):
        print(Fore.GREEN + "Starting clone to " + fp + " ...")
        print(Style.RESET_ALL)
    
    def displayEndMessage(self):
        print(Fore.LIGHTYELLOW_EX + "Cloning done, enter next project to clone or press Ctrl+Z and Return to exit")
        print(Style.RESET_ALL)
        
    def displayAuthErrorMessage(self):
        print(Fore.RED + "Invalid credentials. Please try again or press Ctrl+Z and return to exit")
        print(Style.RESET_ALL)
        