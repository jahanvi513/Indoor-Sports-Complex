CREATE DATABASE ISC;
USE ISC;

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `roll_no` bigint NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `Phone_No` bigint DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Year` int DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
);

DROP TABLE IF EXISTS `sport`;
CREATE TABLE `sport` (
  `id` int NOT NULL,
  `Type` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

