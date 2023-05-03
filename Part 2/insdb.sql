INSERT INTO Video (videoCode, videoLength)
VALUES
  (1, 120),
  (2, 90),
  (3, 180),
  (4, 60),
  (5, 240);

INSERT INTO Model (modelNo, width, height, weight, depth, screenSize)
VALUES
  ('M001', 20.5, 15.7, 5.3, 7.2, 15.6),
  ('M002', 18.3, 12.9, 3.9, 5.6, 13.3),
  ('M003', 23.1, 16.9, 6.8, 9.4, 17.3),
  ('M004', 17.2, 11.5, 3.1, 4.5, 12.1),
  ('M005', 21.7, 14.6, 5.1, 6.9, 14.0);

INSERT INTO Site (siteCode, type, address, phone)
VALUES
  (111, 'bar', '123 Main St', '5551234'),
  (112, 'bar', '456 Oak Ave', '5555678'),
  (113, 'restaurant', '789 Pine Rd', '5559012'),
  (114, 'restaurant', '111 Elm St', '5553456'),
  (115, 'bar', '222 Maple Ave', '5557890');

INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo)
VALUES 
('1234567890', 'Random', 'M000000001'),
('0987654321', 'Smart', 'M000000002'),
('ABCDEF1234', 'Smart', 'M000000003'),
('CBA9876543', 'Random', 'M000000004'),
('XYZ1234567', 'Virtue', 'M000000005');

INSERT INTO Client (clientId, name, phone, address)
VALUES
  (1, 'John Smith', '555-1234', '123 Main St'),
  (2, 'Jane Doe', '555-5678', '456 Oak Ave'),
  (3, 'Bob Johnson', '555-9012', '789 Pine Rd'),
  (4, 'Samantha Brown', '555-3456', '111 Elm St'),
  (5, 'Mike Davis', '555-7890', '222 Maple Ave');

INSERT INTO TechnicalSupport (empId, name, gender)
VALUES
  (1001, 'Sarah Lee', 'F'),
  (2001, 'Alex Wong', 'M'),
  (3001, 'Mark Johnson', 'M'),
  (4001, 'Emily Chen', 'F'),
  (5001, 'David Kim', 'M');

INSERT INTO Administrator (empId, name, gender)
VALUES
  (6001, 'James Smith', 'M'),
  (7001, 'Karen Lee', 'F'),
  (8001, 'Tom Wilson', 'M'),
  (9001, 'Amy Nguyen', 'F'),
  (10001, 'William Chen', 'M');

INSERT INTO Salesman (empId, name, gender) VALUES
(11001, 'John Lee', 'M'),
(12001, 'Sarah Kim', 'F'),
(13001, 'David Nguyen', 'M'),
(14001, 'Karen Park', 'F'),
(15001, 'Jason Lee', 'M');

INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode)
VALUES 
(001, 'Bronze', '2023-03-06', '2023-03-31', 2, 1),
(002, 'Silver', '2023-03-06', '2023-04-06', 3, 2),
(003, 'Gold', '2023-03-06', '2023-05-06', 4, 3),
(004, 'Platinum', '2023-03-06', '2023-06-06', 5, 4),
(005, 'Diamond', '2023-03-06', '2023-07-06', 6, 5);


INSERT INTO AdmWorkHours (empId, day, hours)
VALUES 
(6001, '2023-03-01', 8),
(7001, '2023-03-02', 9),
(8001, '2023-03-03', 7.5),
(9001, '2023-03-04', 8),
(10001, '2023-03-05', 6.5);

INSERT INTO Broadcasts (videoCode, siteCode)
VALUES 
(1, 111),
(2, 112),
(3, 113),
(4, 114),
(5, 115);

INSERT INTO Administers (empId, siteCode)
VALUES 
(6001, 1),
(7001, 2),
(8001, 3),
(9001, 4),
(1001, 5);

INSERT INTO Specializes (empId, modelNo)
VALUES 
(1001, 'M000000001'),
(2001, 'M000000002'),
(3001, 'M000000003'),
(4001, 'M000000004'),
(5001, 'M000000005');

INSERT INTO Purchases (clientId, empId, packageId, commissionRate)
VALUES 
(11, 401, 1, 0.05),
(12, 402, 2, 0.06),
(13, 403, 3, 0.07),
(14, 404, 4, 0.08),
(15, 405, 5, 0.09);