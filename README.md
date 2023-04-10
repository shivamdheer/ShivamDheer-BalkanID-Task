[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/e3nG7TEg)

<h1 align="center">Github API Data Fetching and Storing Program</h1>

## <img src="https://openclipart.org/download/307315/1538154643.svg" width="32" height="32"> About the project
This program has been specifically developed to obtain data from the Github API utilizing OAuth authentication and subsequently storing it in a Postgres database. This program has been designed to normalize and deduplicate data before storing it in the database. Furthermore, the program will retrieve an access token from the Github API to gain access to the data. This program has the capability of dynamically fetching repository data, along with the respective owner's information, which includes both public and private repositories of a user.

The utilization of OAuth authentication ensures that secure access is maintained, and any unauthorized access to sensitive data is prevented. The program is designed to follow best practices in data normalization and deduplication to ensure that data quality is maintained at a high standard before storage. By doing so, the data remains easily retrievable and usable for analysis and other purposes.

The program has been designed with scalability in mind, allowing for a large amount of data to be stored and accessed efficiently. The dynamic nature of the program enables it to retrieve repository and owner information from Github API with minimal user input, thereby ensuring the process is seamless and efficient.

Overall, this program has been designed with a professional approach to ensure the highest level of data quality, security, and efficiency. The use of Github API and Postgres database, in conjunction with OAuth authentication, ensures that the program is reliable and secure for any user to use.

## <img src="https://cdn.iconscout.com/icon/free/png-512/laptop-user-1-1179329.png" width="32" height="32"> Getting Started
To get a local copy up and running follow these simple steps.

### Set up the postgresql database to store the data
```bash
$ psql postgres
```
Create the database and users
```bash
postgres=> CREATE DATABASE balkanid;
postgres=> \c balkanid
balkanid=> CREATE USER admin WITH PASSWORD 'password';
balkanid=> GRANT ALL PRIVILEGES ON DATABASE balkanid TO admin;
```

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
Create a python virtual environment and activate it
```bash 
conda create --name myenv
conda activate myenv
```
Install pip and then the packages using the requirements.txt
```bash
conda install pip
pip install -r requirements.txt
```
Export the python server and set up Flask configuration
```
export FLASK_APP=app
```
Run the flask server
```
flask run
```
The server the starts running at `http://127.0.0.1:5000`.

## Appendix of routes
### OAuth
- `/` - Authentication and home
- `/auth` - Initialize OAuth and login
- `/auth/callback` - Receives the callback from GitHub OAuth
- `/auth/logout` - Resets the session and logs out the user

### GitHub API (Fetch and insert/update in the database)
- `/user` - Fetch data of the authenticated user
- `/user/repos` - Fetch repositories of the authenticated user (owned, collaborated and organization)
- `/user/orgs` - Fetch organizations that the authenticated user is a part of

### Downloads
- `/download` - Download the complied CSV from the data in the database in the required format
