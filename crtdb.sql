
-- Create the database
CREATE DATABASE ABC;

-- Switch to the ABC database
USE ABC;

-- Create the Video table
CREATE TABLE Video (
videoCode INTEGER PRIMARY KEY,
videoLength INTEGER
);

-- Create the Model table
CREATE TABLE Model (
modelNo CHAR(10) PRIMARY KEY,
width NUMERIC(6,2),
height NUMERIC(6,2),
weight NUMERIC(6,2),
depth NUMERIC(6,2),
screenSize NUMERIC(6,2)
);

-- Create the Site table
CREATE TABLE Site (
siteCode INTEGER PRIMARY KEY,
type VARCHAR(16) CHECK (type IN ('bar', 'restaurant')),
address VARCHAR(100),
phone VARCHAR(16)
);

-- Create the DigitalDisplay table
CREATE TABLE DigitalDisplay (
serialNo CHAR(10) PRIMARY KEY,
schedulerSystem CHAR(10) CHECK (schedulerSystem IN ('Random', 'Smart', 'Virtue')),
modelNo CHAR(10),
FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

-- Create the Client table
CREATE TABLE Client (
clientId INTEGER PRIMARY KEY,
name VARCHAR(40),
phone VARCHAR(16),
address VARCHAR(100)
);

-- Create the TechnicalSupport table
CREATE TABLE TechnicalSupport (
empId INTEGER PRIMARY KEY,
name VARCHAR(40),
gender CHAR(1)
);

-- Create the Administrator table
CREATE TABLE Administrator (
empId INTEGER PRIMARY KEY,
name VARCHAR(40),
gender CHAR(1)
);

-- Create the Salesman table
CREATE TABLE Salesman (
empId INTEGER PRIMARY KEY,
name VARCHAR(40),
gender CHAR(1)
);

-- Create the AirtimePackage table
CREATE TABLE AirtimePackage (
packageId INTEGER PRIMARY KEY,
class VARCHAR(16) CHECK (class IN ('economy', 'whole day', 'golden hours')),
startDate DATE,
lastDate DATE,
frequency INTEGER,
videoCode INTEGER,
FOREIGN KEY (videoCode) REFERENCES Video (videoCode)
);

-- Create the AdmWorkHours table
CREATE TABLE AdmWorkHours (
empId INTEGER,
day DATE,
hours NUMERIC(4,2),
PRIMARY KEY (empId, day),
FOREIGN KEY (empId) REFERENCES Administrator (empId)
);

-- Create the Broadcasts table
CREATE TABLE Broadcasts (
videoCode INTEGER,
siteCode INTEGER,
PRIMARY KEY (videoCode, siteCode),
FOREIGN KEY (videoCode) REFERENCES Video (videoCode),
FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

-- Create the Administers table
CREATE TABLE Administers (
empId INTEGER,
siteCode INTEGER,
PRIMARY KEY (empId, siteCode),
FOREIGN KEY (empId) REFERENCES Administrator (empId),
FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

-- Create the Specializes table
CREATE TABLE Specializes (
empId INTEGER,
modelNo CHAR(10),
PRIMARY KEY (empId, modelNo),
FOREIGN KEY (empId) REFERENCES TechnicalSupport (empId),
FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

-- Create the Purchases table
CREATE TABLE Purchases (
clientId INTEGER,
empId INTEGER,
packageId INTEGER,
commissionRate NUMERIC(4,2),
PRIMARY KEY (clientId, empId, packageId),
FOREIGN KEY (clientId) REFERENCES Client (clientId),
FOREIGN KEY (empId) REFERENCES Salesman (empId),
FOREIGN KEY (packageId
