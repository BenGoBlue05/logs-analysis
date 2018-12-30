# Logs analysis
This repo is for the Udacity Full-stack Nanodegree project Logs Analysis. It is a reporting tool for a fictional newspaper site that uses information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, data about the authors of the articles, and server logs for the site. 


## Set up
1. Install VirtualBox https://www.virtualbox.org/wiki/Downloads
2. Install Vagrant https://www.vagrantup.com/
3. Clone repo https://github.com/udacity/fullstack-nanodegree-vm
4. cd into vagrant folder and clone this repo
5. Unzip newsdata.zip. Its contents contain newdata.sql.
6. Run `vagrant up` and then `vagrant ssh`
7. `cd logs-analysis `
7. Type command `psql -d news -f newsdata.sql` into terminal to load the data.
8. Run `python newsdata.py`
