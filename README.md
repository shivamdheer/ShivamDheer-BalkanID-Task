[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/e3nG7TEg)

<h1 align="center">Github API Data Fetching and Storing Program</h1>

## <img src="https://openclipart.org/download/307315/1538154643.svg" width="32" height="32"> About the project
This program is designed to fetch data from the Github API using OAuth authentication and store it in a Postgres database. The program will normalize and deduplicate the data before storing it in the database. Additionally, the program will retrieve an access token from Github API to access the data. The program will be able to dynamically fetch repository data along with the owner's information, both public and private repositories of a user.


## <img src="https://cdn.iconscout.com/icon/free/png-512/laptop-user-1-1179329.png" width="32" height="32"> Getting Started
To get a local copy up and running follow these simple steps.
### Prerequisites
In order to get a copy of the project you will require you to have Node.js (v14+) and the NPM package manager installed. If you don't have it, you can download the latest version of Node.js from the [official website](https://nodejs.org/en/download/) which also installs the NPM package manager by default. For Python, you will require a Python environment (like Anaconda) with Python version 3.9 and above.

### Set up the environemnt variables
Create an env file named .env and add the following credentials:
```
CLIENT_ID=3d0699fbc4ce7a45b004
CLIENT_SECRET=f30956d0f31d0b57589be2214c5e2462636216c1
DB_USERNAME=admin
DB_PASSWORD=password
```

### Installation
Open the terminal in the folder 
Create a python virtual environment
``` 
conda create --name myenv
```
Install the packages using the requirements.txt
```
conda install --yes --file requirements.txt
```
Export the python server and set up Flask configuration
```
export FLASK_APP=app
```
Run the flask server
```
flask run
```
