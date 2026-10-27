# 1. Git vs. GitHub: Git is a local version control software that tracks changes in your files. GitHub is a cloud-based hosting platform where you store, share, and collaborate on those Git repositories.
# 2. Terminal vs. Command Line: The command line is the text-based interface where you type commands. The terminal is the actual wrapper application that executes and renders that interface.
# 3. Local vs. Remote Repository: A local repository lives directly on your computer's hard drive. A remote repository lives on a hosted server online (like GitHub).
# 4. Version Control: A system that records changes to files over time so you can track revisions, revert to previous versions, and collaborate without overwriting others' work.
# 5. Staging Area: A temporary preparation area in Git where changes are indexed and bundled before they are officially committed to history.
# 6. git add: Moves changes from your working directory into the staging area.
# 7. git commit: Permanently saves your staged snapshot into the local repository's history with a descriptive message.
# 8. git push: Uploads your local repository commits to a remote repository on GitHub.
# 9. git status: Displays the state of your working directory and staging area, showing which files are modified, staged, or untracked.
# 10. git pull: Fetches updates from a remote repository and immediately merges them into your current local branch.
# 11. pwd: Print Working Directory. Shows the exact absolute folder path you are currently in.
# 12. ls: List. Shows the files and folders contained inside your current directory.
# 13. cd: Change Directory. Moves you from your current folder into another folder.
# 14. nano: A simple, text-only code editor built directly into the command terminal.
# 15. touch: Creates a new, blank file at your current location without opening it.
# 16. mv: Move. Relocates a file/folder to a new directory, or renames a file/folder.
# 17. rm: Remove. Permanently deletes a specified file from your system.
# 18. cat: Concatenate. Displays the entire text contents of a file directly within the terminal screen.

#Questions:

#You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
#   pwd
#The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
#   ls
#Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
#   cd ../brianna , git pull
#How would you move this new homework.py to the homework/ folder in your personal repos-itory?
#   mv homework.py ../ahana/homework5
#How would you move yourself to the same repository as homework.py?
#   cd pythdondecal/brianna_repo
#You want to see the contents of homework.py in your terminal, how would you do this?
#   cat homework5.py
#Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
#   git add .
#   git commit -m "finsih hw5"
#   git push origin main
#Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
#   The error means your remote GitHub repository has updates that your local computer doesn't know about. 
#   To fix this, run:
#   git pull origin main
#What absolute path will allow you to move to Recents/?
#   cd ~/Recent

def checkDataType(val):
    return type(val).__name__

def evenOrOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

def square(num):
    return num * num
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))