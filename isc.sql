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

CREATE PROCEDURE `insert_new_student`(in p_roll bigint, in p_name varchar(255), in p_email varchar(255), in p_password varchar(255), in p_phone bigint, in p_dept varchar(50), in p_year int)
begin
insert into student (roll_no, name, email, password, Phone_no, Department, Year) values (p_roll, p_name, p_email, p_password, p_phone, p_dept, p_year);
end

CREATE PROCEDURE `delete_student`(in p_id bigint)
begin
delete from student where roll_no = p_id;
end

CREATE PROCEDURE `search_room`(in p_type varchar(255), in p_booked_date date, in p_booked_time time)
begin
select * from sport where id not in(select room_id from booking where booked_date = p_booked_type and booked_time  = p_booked_time and status != 'Denied') and type = p_type;
end

CREATE PROCEDURE `update_student_password`(in p_id bigint, in p_password varchar(50))
begin update student
set password = p_password where roll_no = p_id;
end

CREATE PROCEDURE `view_booking`(in p_id bigint)
begin
select * from booking where student_id = p_id;
end

CREATE TABLE `supervisor` (
  `id` bigint NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`supervisor_id`)
);

ALTER TABLE `booking`
ADD COLUMN `status` ENUM('Pending', 'Accepted', 'Denied') DEFAULT 'Pending';

CREATE PROCEDURE `manage_booking_request`(in p_booking_id bigint, in p_status ENUM('Accepted', 'Denied'))
begin
    update booking
    set status = p_status
    where id = p_booking_id;
end;
