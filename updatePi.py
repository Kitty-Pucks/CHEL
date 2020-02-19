import sh
from sh import git
import time, os, sys

def checkForUpdate(projDir):
    # Fetch most up to date version of code.
    p = git("--git-dir=" + projDir + ".git/", "--work-tree=" + projDir, "fetch", _out_bufsize=0, _tty_in=True)
    time.sleep(2)
    statusCheck = git("--git-dir=" + projDir + ".git/", "--work-tree=" + projDir, "status")

    return "Your branch is up-to-date" not in statusCheck

if __name__ == "__main__":
    checkTimeSec = 60
    gitDir = "/home/rlagent45/CHEL/"
    while True:
        if checkForUpdate(gitDir):
            resetCheck = git("--git-dir=" + gitDir + ".git/", "--work-tree=" + gitDir, "reset", "--hard", "origin/master")
                                                                                                                                                                
        time.sleep(checkTimeSec)
