'''
Created on 14 Jan 2018

@author: Yong Quan
'''
from stashy.errors import AuthenticationException as AuthError

from com.horizon.projectstash.src.main import ConsoleDisplay
from com.horizon.projectstash.src.main import Utils
from com.horizon.projectstash.src.main import StashManager

class ProjectStashMain:
    '''
    Program to run once, if successful, exit, else, throw
    the necessary exceptions
    '''
    programStatus = 'running'
    
    def __init__(self):
        '''
        Constructor
        '''
        self.utils = Utils()
        self.console = ConsoleDisplay()
    
    def execute(self):        
        '''
        Collect user credentials
        ''' 
        self.utils.getCredentials()
        self.sm = StashManager(self.utils.getUsername(), self.utils.getPassword())
        self.stash = self.sm.getStash()
    
        '''
        Obtain a list of projects for the user to select
        '''
        # self.sm.listAllProjects(self.stash)
        self.project = self.utils.getProject()
    
        '''
        Obtain file path the user wants to save
        '''
        self.console.displayDirectoryMessage()
        self.fp = self.utils.getFilePath()
        self.confirmation = self.utils.getDirectoryConfirmation()
        self.utils.handleConfirmation(self.confirmation)
        
        '''
        Retrieve the list of repos
        '''    
        self.console.displayStartMessage(self.fp)
        self.utils.cloneProject(self.stash, self.fp, self.project)
        self.console.displayEndMessage()

if __name__ == '__main__':
    projectStash = ProjectStashMain()
    
    while projectStash.programStatus == 'running':
        try:
            '''
            Show welcome message to user
            '''
            projectStash.console.displayWelcomeMessage()
            
            projectStash.execute()
        
        except AuthError:
            projectStash.console.displayAuthErrorMessage()
            projectStash.execute()
            
        except (KeyboardInterrupt, EOFError) as e:
            projectStash.console.displayExitMessage()
            exit()
            
            