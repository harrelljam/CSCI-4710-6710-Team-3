Folder for assignment 7


How to run:


postgres:

sudo -u postgres psql
create database tempdb;
create user tmp with encrypted password 'tmp';
grant all privileges on database tempdb to tmp;
\c tempdb
GRANT ALL PRIVILEGES ON sequence ulist_usernumber_seq TO tmp;

CREATE TABLE ulist (
usernumber serial PRIMARY KEY,
userid varchar(20),
firstName varchar(20),
lastName varchar(20),
pwd varchar(20));

CREATE TABLE history (
UserId VARCHAR (20),
Function VARCHAR2 (30),
CurrentDate DATE DEFAULT GETDATE(),
 PRIMARY KEY (UserId)
);



python:


cd IdeaProjects/CSCI-4710-6710-Team-3/Assn7

mkvirtualenv -p python2.7 dev

virtualenv dev && source dev/bin/activate

pip install -r requirements.txt

python main.py
