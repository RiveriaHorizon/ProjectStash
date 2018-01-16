'''
Created on 14 Jan 2018

@author: Yong Quan
'''
import os
import getpass
import tkinter as tk
from tkinter import filedialog

from com.horizon.projectstash.src.main import Parser

class Utils:
    '''
    classdocs
    '''
    parser = Parser()

    def __init__(self):
        '''
        Constructor
        '''
    
    def clearTerminal(self):
        os.system('cls')
        
    def cloneProject(self, stash, fp, project):
        for repo in stash.projects[project].repos.list():
            for url in repo["links"]["clone"]:
                if (url["name"] == "http"):
                    os.system("git clone %s %s/%s" % (url["href"], fp, self.parser.getRepoName(url["href"], project)))
    
    def getProject(self):
        return input("Project to clone:")
        
    def getCredentials(self):
        self.user = input("Username:")
        self.passwd = getpass.getpass("Password:")
        
    def getUsername(self):
        return self.user
    
    def getPassword(self):
        return self.passwd
        
    def getFilePath(self):
        root = tk.Tk()
        root.withdraw()
        root.focus_force()
        return filedialog.askdirectory()
    
    def getDirectoryConfirmation(self, fp):
        confirm = input("Is " + fp + " the directory to clone into? (y/n)")
        
        '''
        Input confirmation handling
        '''
        if (confirm != ("y" | "Y" | "N" | "n")):
            confirm = input("Please enter either y or n")
        
        '''
        Readdress to boolean output
        '''
        if (confirm == 'y' | 'Y'):
            return True
        
        else:
            return False
    
    def handleConfirmation(self, confirm):
        while (confirm is False):
            '''
            Continue to query if user wants to change directory
            '''
            self.getDirectoryConfirmation(self.getFilePath())
    