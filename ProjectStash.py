#! /usr/bin/env python

# Used to clone multiple repos from projects 
# that you have access to.
# Program cannot handle folder names with whitespace

__author__ = 'Cheng Yong Quan yongquan.riveria@gmail.com'

import os
import stashy
import getpass
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Style

class ConsoleDisplay:
    def initColorama(self):
        init()
        
    def getProject(self):
        return input("Project to clone:")
    
    def displayLineDivider(self):
        print("=============================================")
    
    def displayWelcomeMessage(self):
        self.displayLineDivider()
        print("||         Welcome to StashProject         ||")
        self.displayLineDivider()
        
    def displayDirectoryMessage(self):
        print("Please choose directory to clone to..")
    
    def displayStartMessage(self, fp):
        print(Fore.GREEN + "Starting clone to " + fp + " ...")
        print(Style.RESET_ALL)
        
    def displayEndMessage(self):
        print(Fore.LIGHTYELLOW_EX + "Cloning done, enter next project to clone or press Ctrl+Z and return to exit")
        print(Style.RESET_ALL)
    
class Parser:
    def getRepoName(self, url, project):
        preamble = project + '/'
        postamble = '.git'
        return url.split(preamble.lower(),1)[1].split(postamble,1)[0]        

def getCredentials():
    return input("Username:"), getpass.getpass("Password:")

def setFilePath():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

def listAllRepos(stash):
    for project in stash.projects.list():
        for url in project[""]:
            print(url["name"])

def retrieveAllRepos(stash, project, fp, parser):
    for repo in stash.projects[project].repos.list():
        for url in repo["links"]["clone"]:
            if (url["name"] == "http"):
                repoName = parser.getRepoName(url["href"], project)
                os.system("git clone %s %s/%s" % (url["href"], fp, repoName))
    
def main():     
    parser = Parser()
    
    [user, passwd] = getCredentials()
    
    stash = stashy.connect("http://stash", user, passwd)
    
    listAllRepos(stash)
    project = console.getProject()
    
    console.displayDirectoryMessage()
    fp = setFilePath()
    
    console.displayStartMessage(fp)
    retrieveAllRepos(stash, project, fp, parser)
    console.displayEndMessage()
    
    return False

if __name__ == '__main__':
    os.system('cls')      
    console = ConsoleDisplay()
    console.initColorama()
    console.displayWelcomeMessage()        
    
    while True: 
        try:
            main()

        except stashy.errors.AuthenticationException:
            print(Fore.RED + "Invalid credentials. Please try again or press Ctrl+Z and return to exit")
            print(Style.RESET_ALL)

        except (KeyboardInterrupt, EOFError) as e:
            print(Fore.MAGENTA + "Program exiting..")
            print(Style.RESET_ALL)
            exit()
