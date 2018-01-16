'''
Created on 14 Jan 2018

@author: Yong Quan
'''
import stashy

class StashManager:
    '''
    classdocs
    '''
    url = "http://stash"

    def __init__(self, user, passwd):
        '''
        Constructor
        '''
        self.user = user
        self.passwd = passwd
        self.stash = stashy.connect(self.url, user, passwd)
    
    def listAllProjects(self, stash):
        '''
        Method is still WIP
        '''
        for project in stash.projects.list():
            for url in project["name"]:
                print(url)
    
    def retrieveAllRepos(self, stash, project, fp, parser):
        '''
        Returns a list of urls of the repo from the provided project
        '''
        for repo in stash.projects[project].repos.list():
            for url in repo["links"]["cline"]:
                if (url["name"] == "http"):
                    self.repoList.add(parser.getRepoName(url["href"], project))
                    
    def getStash(self):
        return self.stash
    
    def getRepoList(self, stash, project, fp, parser):
        self.retrieveAllRepos(stash, project, fp, parser)
        return self.repoList