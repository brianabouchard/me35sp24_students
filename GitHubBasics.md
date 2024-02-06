Cloning a repository: 
This is really just a fancy way of saying copying a directory or folder locally on your device
To do this, call the following command in the working directory you want the copy to be:
 
git clone https://github.com/username/[name of folder]

For example, if I wanted a copy of my me73 repository, I would call:
	
git clone https://github.com/daryaclark/me73

This can also be done with another person’s repository
Creating a new repository from the command line:
If there is an existing folder on your device you wish to put in github, you can run 

	git init

Making updates to a repository:
Let’s say you have already initialized the repository through one of the methods above. Any time you make an edit to the files, after you’re done for the day, run the following commands:

	git add .

Notice the . at the end of this one, as this will add the entire folder you are currently working in
Next, 

git commit -m “[message about the work you did]”

This is like a loading dock for the code. Finally,

	git push

This updates the repository on the github website and “pushes” all the code 

Working with another person
It is extremely helpful to use Github to work with another person and use their code. One way of doing this is cloning a repository as mentioned above. If you want to update your version to have the changes the other person made, run

git pull
Every time you run this command, it will update your version with the most recent version of any code

How to generate personal access tokens:
Personal access tokens are used to sign in on the command line, as the password is often not accepted. 
Click on your profile, then settings then scroll to the bottom of the left hand column until developer settings; click on it
Now, in this page, click personal access tokens and tokens (classic)
Click generate new, selecting all the most left checkboxes
This will then generate a token you are able to come back to on this page, but it may be helpful to store this somewhere
When being asked to sign in on the command line, this is the password associated with your account

