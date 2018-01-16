'''
Created on 14 Jan 2018

@author: Yong Quan
'''

class Parser:
    '''
    Parser class to parse objects
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def getRepoName(self, url, project):
        preamble = project + '/'
        postamble = '.git'
        return url.split(preamble.lower(), 1)[1].split(postamble, 1)[0]
    