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

TABLE IF EXISTS `coach`;
CREATE TABLE `coach` (
  `Emp_id` bigint NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Phone_Number` int DEFAULT NULL,
  `Sport` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Emp_id`)
);

DROP TABLE IF EXISTS `booking`;
CREATE TABLE `booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `room_id` int DEFAULT NULL,
  `booked_date` date NOT NULL,
  `booked_time` time NOT NULL,
  `student_id` bigint DEFAULT NULL,
  `time_of_booking` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uc1` (`room_id`,`booked_date`,`booked_time`),
  KEY `fk1` (`student_id`),
  CONSTRAINT `fk1` FOREIGN KEY (`student_id`) REFERENCES `student` (`roll_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk2` FOREIGN KEY (`room_id`) REFERENCES `sport` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
);
