-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 07, 2021 at 02:34 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `curator`
--

-- --------------------------------------------------------

--
-- Table structure for table `ban_list`
--

DROP TABLE IF EXISTS `ban_list`;
CREATE TABLE IF NOT EXISTS `ban_list` (
  `room_key` char(12) NOT NULL,
  `user` varchar(15) NOT NULL,
  PRIMARY KEY (`room_key`),
  KEY `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ban_list`
--

INSERT INTO `ban_list` (`room_key`, `user`) VALUES
('sad345gfd4d6', '420.69.69.420');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
CREATE TABLE IF NOT EXISTS `room` (
  `room_key` char(12) NOT NULL,
  `host` varchar(15) NOT NULL,
  `room_name` varchar(64) NOT NULL,
  `log` text NOT NULL,
  `mute` tinyint(1) NOT NULL,
  `note` varchar(512) NOT NULL,
  `capacity` int UNSIGNED NOT NULL DEFAULT '32',
  `file_name` varchar(256) NOT NULL,
  `file` mediumblob NOT NULL,
  PRIMARY KEY (`room_key`),
  KEY `host_idx` (`host`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_key`, `host`, `room_name`, `log`, `mute`, `note`, `capacity`, `file_name`, `file`) VALUES
('234p985ujy3h', '420.69.69.420', 'Skeletor\'s House for cool guys', 'OMG I can\'t believed they banned meeeee!!!1!!!', 0, 'Only cool dudes allowed', 32, '', ''),
('sad345gfd4d6', '123.456.7.890', 'test room', 'TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...TESTING...', 0, '', 1, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `address` varchar(15) NOT NULL,
  `name` varchar(16) NOT NULL,
  `role` enum('std','mod','host') NOT NULL DEFAULT 'std',
  `color` char(6) NOT NULL,
  `in_room` char(12) NOT NULL,
  PRIMARY KEY (`address`,`in_room`) USING BTREE,
  UNIQUE KEY `usr_info` (`name`,`color`,`in_room`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`address`, `name`, `role`, `color`, `in_room`) VALUES
('123.456.7.890', 'tester', 'host', '343530', 'sad345gfd4d6'),
('420.69.69.420', 'Skeletor', 'std', '366163', '234p985ujy3h'),
('fake_host', 'fake_host', 'host', '', '');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ban_list`
--
ALTER TABLE `ban_list`
  ADD CONSTRAINT `banned_from` FOREIGN KEY (`room_key`) REFERENCES `room` (`room_key`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `banned_user` FOREIGN KEY (`user`) REFERENCES `user` (`address`);

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `host_id` FOREIGN KEY (`host`) REFERENCES `user` (`address`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
