# Bible-Quote
A command line script that prints out Bible verses 

## What is this? 

I've been using the `fortune` console app combined with `lolcat` for my terminal and wanted to try something new. This is really just curling Bible verses from a public page and printing it out on the console. 

## How to install this? 

You can simply copy this locally to your system. 

Install the modules with the command `$ pip install -r requirements.txt` 

Now you can add the following to you login script, in my case, `.bash_profile`. 

`~/.scripts/biblequote | lolcat` note - lolcat is optional, but it's fun

## Improvements 

Since this is just a few lines, I really like to complete the following

* Package this for a single command deploy
* Revert the quotes by using a local SQLite database

## Important Notes

If this script doesn't running correctly as a login you need to hard-code the Python path in the script. 

This is due to the system Python might be different and this can break the script since the modules are not installed.  
