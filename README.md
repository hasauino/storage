### Commands for pushing updates

- From the directory, open a terminal and run the following commands:
```bash
git add --all
```
```bash
git commit -m "commit message, a description explaining why a particular change was made"
```
```bash
git push origin [branch]
```
for example, if you want to push to the master branch:
```bash
git push origin master
```

### Useful commands

- Clone the online repository to the current directory
```bash
git clone [url]
```

- Pull changes from a branch
```bash
git pull origin [branch]
```


- To see all the changes, or to see on which branch your are
```bash
git status
```

- To change to a different (must commit all changes before switching to a different branch):
```bash
git checkout [branch] 
```

- Amendding: To edit your last commit. This way you can add more files to the stage area, or edit stagged files, or edit commit message.
```
git commit --amend -m "message"
git commit --amend --no-edit
```


### Undo

- Make HEAD point to previous commit, staging area will have the changes you did in last commit as staged files:
```
git reset --soft HEAD~
```

- Make HEAD point to previous commit, make staging area = HEAD, make directory = staging area :
```
git reset --hard HEAD~
```
- HEAD~ means parent of HEAD. HEAD points to current branch. If you have staged files in the staging area, HEAD doesnt have them. The staging area is the future state of the HEAD.

- Instead of HEAD~, you can write the ID of the commit you want to go back to. Example
```
git reset --hard 311b0105b63e09d575934679aa17a17c09fff9af
```

- To show history of commits on a branch:
```
git log
```
