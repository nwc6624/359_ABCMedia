CREATE TABLE Video (
    videoCode INTEGER PRIMARY KEY,
    videoLength INTEGER
);

CREATE TABLE Model (
    modelNo CHAR(10) PRIMARY KEY,
    width NUMERIC(6,2),
    height NUMERIC(6,2),
    weight NUMERIC(6,2),
    depth NUMERIC(6,2),
    screenSize NUMERIC(6,2)
);

CREATE TABLE Site (
    siteCode INTEGER PRIMARY KEY,
    type VARCHAR(16) CHECK (type IN ('bar', 'restaurant')),
    address VARCHAR(100),
    phone VARCHAR(16)
);

CREATE TABLE DigitalDisplay (
    serialNo CHAR(10) PRIMARY KEY,
    schedulerSystem CHAR(10) CHECK (schedulerSystem IN ('Random', 'Smart', 'Virtue')),
    modelNo CHAR(10),
    FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

CREATE TABLE Client (
    clientId INTEGER PRIMARY KEY,
    name VARCHAR(40),
    phone VARCHAR(16),
    address VARCHAR(100)
);

CREATE TABLE TechnicalSupport (
    empId INTEGER PRIMARY KEY,
    name VARCHAR(40),
    gender CHAR(1)
);

CREATE TABLE Administrator (
    empId INTEGER PRIMARY KEY,
    name VARCHAR(40),
    gender CHAR(1)
);

CREATE TABLE Salesman (
    empId INTEGER PRIMARY KEY,
    name VARCHAR(40),
    gender CHAR(1)
);

CREATE TABLE AirtimePackage (
    packageId INTEGER PRIMARY KEY,
    class VARCHAR(16) CHECK (class IN ('Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond')),
    startDate DATE,
    lastDate DATE,
    frequency INTEGER,
    videoCode INTEGER,
    FOREIGN KEY (videoCode) REFERENCES Video (videoCode)
);

CREATE TABLE AdmWorkHours (
    empId INTEGER,
    day DATE,
    hours NUMERIC(4,2),
    PRIMARY KEY (empId, day),
    FOREIGN KEY (empId) REFERENCES Administrator (empId)
);

CREATE TABLE Broadcasts (
    videoCode INTEGER,
    siteCode INTEGER,
    PRIMARY KEY (videoCode, siteCode),
    FOREIGN KEY (videoCode) REFERENCES Video (videoCode),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

CREATE TABLE Administers (
    empId INTEGER,
    siteCode INTEGER,
    PRIMARY KEY (empId, siteCode),
    FOREIGN KEY (empId) REFERENCES Administrator (empId),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);

CREATE TABLE Specializes (
    empId INTEGER,
    modelNo CHAR(10),
    PRIMARY KEY (empId, modelNo),
    FOREIGN KEY (empId) REFERENCES TechnicalSupport (empId),
    FOREIGN KEY (modelNo) REFERENCES Model (modelNo)
);

CREATE TABLE Purchases (
    clientId INTEGER,
    empId INTEGER,
    packageId INTEGER,
    commissionRate NUMERIC(4,2),
    PRIMARY KEY (clientId, empId, packageId),
    FOREIGN KEY (clientId) REFERENCES Client (clientId),
    FOREIGN KEY (empId) REFERENCES Salesman (empId),
    FOREIGN KEY (packageId) REFERENCES AirtimePackage (packageId)
);

CREATE TABLE Locates (
    serialNo CHAR(10),
    siteCode INTEGER,
    PRIMARY KEY (serialNo, siteCode),
    FOREIGN KEY (serialNo) REFERENCES DigitalDisplay (serialNo),
    FOREIGN KEY (siteCode) REFERENCES Site (siteCode)
);