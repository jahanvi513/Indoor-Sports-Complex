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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `student` WRITE;
INSERT INTO `student` VALUES (2210110914,'Jahanvi Singh','js850@snu.edu.in','dbmssem4',6394920978,'CSE',2026);
UNLOCK TABLES;
