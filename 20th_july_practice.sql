CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50),
    City VARCHAR(50),
    AccountType VARCHAR(20)
);

INSERT INTO Users VALUES
(1, 'Aman Verma', 'Delhi', 'Premium'),
(2, 'Riya Sen', 'Mumbai', 'Regular'),
(3, 'Chandan', 'Hyderabad', 'Regular'),
(4, 'Priya Mehta', 'Bangalore', 'Premium'),
(5, 'Neha Gupta', 'Delhi', 'Regular'),
(6, 'Arjun Patel', 'Mumbai', 'Premium'),
(7, 'Sneha Roy', 'Kolkata', 'Regular'),
(8, 'Vikram Singh', 'Delhi', 'Premium');
(9, 'Karan Das', 'Delhi', 'Regular');
CREATE TABLE Restaurants(
  RestaurantID INT PRIMARY KEY,
  RestaurantName Varchar(100),
  Cuisine Varchar(50),
  Rating Decimal(2,1)

);

INSERT INTO Restaurants VALUES
(101, 'Spice Symphony', 'North Indian', 4.5),
(102, 'Pizza Express', 'Italian', 3.9),
(103, 'Dragon House', 'Chinese', 4.3),
(104, 'Burger Hub', 'Fast Food', 4.1),
(105, 'South Spice', 'South Indian', 4.6),
(106, 'Tandoori Flames', 'North Indian', 4.8),
(107, 'Pasta Palace', 'Italian', 4.4),
(108, 'Food Corner', 'Fast Food', 3.7);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    RestaurantID INT,
    BillAmount DECIMAL(10,2),
    OrderDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);

INSERT INTO Orders VALUES
(501, 1, 101, 1200.00, '2026-07-15'),
(502, 2, 102, 450.00, '2026-07-16'),
(503,3,101,2500.00,'2026-07-17'),
(504,5,101,1800.00,'2026-07-17'),
(505,8,106,3200.00,'2026-07-18'),
(506,1,106,1500.00,'2026-07-18'),
(507,4,103,900.00,'2026-07-19'),
(508,6,104,650.00,'2026-07-19'),
(509,7,105,1100.00,'2026-07-20'),
(510,3,107,700.00,'2026-07-20'),
(511,2,102,500.00,'2026-07-21'),
(512,5,106,2700.00,'2026-07-21'),
(513,8,101,900.00,'2026-07-22'),
(514,4,108,350.00,'2026-07-22'),
(515,1,105,1300.00,'2026-07-23'),
(516,6,104,800.00,'2026-07-23'),
(517,7,103,1400.00,'2026-07-24'),
(518,3,101,1000.00,'2026-07-24');

CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY,
    OrderID INT,
    DeliveryStatus VARCHAR(20),
    DeliveryTimeMinutes INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
INSERT INTO Deliveries VALUES
(901, 501, 'Delivered', 25),
(902, 502, 'Delivered', 42),
(903,503,'Delivered',30),
(904,504,'Cancelled',45),
(905,505,'Delivered',22),
(906,506,'Delivered',27),
(907,507,'Delivered',38),
(908,508,'Cancelled',50),
(909,509,'Delivered',29),
(910,510,'Delivered',34),
(911,511,'Delivered',40),
(912,512,'Delivered',26),
(913,513,'In-Transit',0),
(914,514,'Cancelled',55),
(915,515,'Delivered',24),
(916,516,'Delivered',37),
(917,517,'Delivered',31),
(918,518,'Delivered',33);


-- Question 1
-- ● Problem Statement: Write a query to display the UserName of the customer, the
-- RestaurantName they ordered from, and the BillAmount for all orders.
-- ● Tables to Use: Users, Restaurants, Orders



SELECT u.UserName,
       r.RestaurantName,
       o.BillAmount
FROM Orders o
INNER JOIN Users u
ON o.UserID = u.UserID
INNER JOIN Restaurants r
ON o.RestaurantID = r.RestaurantID;


-- Question 2
-- ● Problem Statement: Fetch a unique list of all restaurant names that have
-- successfully had orders cooked and assigned to a delivery tracking record (even
-- if the delivery was later cancelled).
-- ● Tables to Use: Restaurants, Orders

SELECT DISTINCT r.RestaurantName
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Deliveries d
ON o.OrderID = d.OrderID;

-- Question 3
-- ● Problem Statement: Display all OrderID logs along with their corresponding
-- user names where the order took more than 35 minutes to deliver.
-- ● Tables to Use: Users, Orders, Deliveries

SELECT o.OrderID,
       u.UserName
FROM Orders o
JOIN Users u
ON o.UserID = u.UserID
JOIN Deliveries d
ON o.OrderID = d.OrderID
WHERE d.DeliveryTimeMinutes > 35;

-- Question 4
-- ● Problem Statement: Find the total money spent (BillAmount) on food delivery
-- orders by each individual UserName. Display the user's name and their total
-- spend amount.
-- ● Tables to Use: Users, Orders

SELECT u.UserName,
       SUM(o.BillAmount) AS TotalSpent
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
GROUP BY u.UserName;

-- Problem Statement 5: The business intelligence team needs to see a
-- comprehensive dispatch chart. Write a query to list every user name registered
-- on the system along with the total number of orders they have placed. If a user
-- has placed 0 orders, their name must still appear in the list with an order count of
-- 0.
-- ● Tables to Use: Users, Orders

SELECT u.UserName,
       COUNT(o.OrderID) AS TotalOrders
FROM Users u
LEFT JOIN Orders o
ON u.UserID = o.UserID
GROUP BY u.UserName;


-- Question 6
-- ● Problem Statement: Write a query to find the names of restaurants that have
-- generated a total cumulative revenue (sum of BillAmount) greater than ₹5,000
-- from users who live specifically in the city of 'Delhi'.
-- ● Tables to Use: Users, Restaurants, Orders

SELECT r.RestaurantName,
       SUM(o.BillAmount) AS TotalRevenue
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Users u
ON o.UserID = u.UserID
WHERE u.City = 'Delhi'
GROUP BY r.RestaurantName
HAVING SUM(o.BillAmount) > 5000;

-- Question 7
-- ● Problem Statement: Identify structural system inefficiencies. Write a query to
-- find the names of all restaurants that have suffered from 'Cancelled' orders, along
-- with the total count of cancelled orders each restaurant faced.
-- ● Tables to Use: Restaurants, Orders, Deliveries

SELECT r.RestaurantName,
       SUM(o.BillAmount) AS TotalRevenue
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Users u
ON o.UserID = u.UserID
WHERE u.City = 'Delhi'
GROUP BY r.RestaurantName
HAVING SUM(o.BillAmount) > 5000;

-- Question 8
-- ● Problem Statement: Write a query to find the UserName and Email/City profiles
-- of users who have spent more money on a single order than the average order
-- value computed across the entire platform.
-- ● Tables to Use: Users, Orders

SELECT u.UserName,
       u.City
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
WHERE o.BillAmount >
(
    SELECT AVG(BillAmount)
    FROM Orders
);

-- Question 9
-- ● Problem Statement: Generate a platform-wide operational efficiency audit
-- report. Write a query to calculate the average delivery time
-- (DeliveryTimeMinutes) for each distinct Cuisine category offered on the
-- platform, but only include cuisines where the restaurant's average rating is strictly
-- above 4.0.
-- ● Tables to Use: Restaurants, Orders, Deliveries

SELECT r.Cuisine,
       AVG(d.DeliveryTimeMinutes) AS AvgDeliveryTime
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Deliveries d
ON o.OrderID = d.OrderID
WHERE r.Rating > 4.0
GROUP BY r.Cuisine;

-- Problem Statement 10 : Write a query to rank restaurants within each unique
-- Cuisine category based on the total number of orders they have received
-- (highest orders ranked 1st). The output should show the Cuisine, Restaurant
-- Name, Order Count, and their Rank.
-- ● Tables to Use: Restaurants, Orders

SELECT
    r.Cuisine,
    r.RestaurantName,
    COUNT(o.OrderID) AS OrderCount,
    RANK() OVER (
        PARTITION BY r.Cuisine
        ORDER BY COUNT(o.OrderID) DESC
    ) AS RestaurantRank
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
GROUP BY
    r.Cuisine,
    r.RestaurantName;
