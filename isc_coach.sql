TABLE IF EXISTS `coach`;
CREATE TABLE `coach` (
  `Emp_id` bigint NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Phone_Number` int DEFAULT NULL,
  `Sport` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `coach` WRITE;

UNLOCK TABLES;
