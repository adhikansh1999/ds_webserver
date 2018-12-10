-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 10, 2018 at 07:15 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webapp1`
--

-- --------------------------------------------------------

--
-- Table structure for table `cab_share`
--

CREATE TABLE `cab_share` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `time` time NOT NULL,
  `date` date NOT NULL,
  `src` varchar(30) NOT NULL,
  `dest` varchar(30) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cab_share`
--

INSERT INTO `cab_share` (`id`, `username`, `time`, `date`, `src`, `dest`, `timestamp`) VALUES
(5, 'as', '02:23:00', '2018-12-09', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(6, 'as', '04:00:00', '2018-12-27', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(8, 'as', '04:30:00', '2018-12-06', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(9, 'as', '02:00:00', '2018-12-27', 'IIT', 'Dominos', '2018-12-10 18:11:45'),
(10, 'as', '02:00:00', '2018-12-27', 'Hijli', 'Dominos', '2018-12-10 18:11:45'),
(11, 'as', '02:00:00', '2018-12-27', 'Kgp Jn', 'IIT', '2018-12-10 18:11:45'),
(12, 'as', '02:00:00', '2018-12-25', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(13, 'as', '02:00:00', '2018-12-01', 'Dominos', 'IIT', '2018-12-10 18:11:45'),
(14, 'as', '02:00:00', '2018-12-02', 'Dominos', 'IIT', '2018-12-10 18:11:45'),
(15, 'as', '02:00:00', '2018-12-03', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(16, 'as', '02:00:00', '2018-12-10', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45'),
(17, 'as', '04:00:00', '2018-12-31', 'Hijli', 'CCU Airport', '2018-12-10 18:11:45');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `name` varchar(256) NOT NULL,
  `item_type` varchar(256) NOT NULL,
  `item_name` varchar(256) NOT NULL,
  `price` int(11) NOT NULL,
  `phone` int(11) NOT NULL,
  `sold` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`, `item_type`, `item_name`, `price`, `phone`, `sold`, `timestamp`) VALUES
(1, 'tatti', 'furniture', 'usha', 35, 23, 0, '2018-12-10 16:44:55'),
(2, 'shit', 'book', 'jsdajdjs', 345, 32134432, 0, '2018-12-10 16:44:55'),
(3, 'bojack', 'book', 'Eleanor and Park', 0, 0, 0, '2018-12-10 16:44:55'),
(4, 'horseman', 'furniture', 'table', 450, 0, 0, '2018-12-10 16:44:55'),
(5, 'tatti', 'book', 'cold/mess', 100, 32898932, 0, '2018-12-10 16:44:55'),
(7, 'tatti', 'book', 'jsdahjh', 231, 911, 0, '2018-12-10 16:44:55'),
(9, 'tatti', 'book', 'asjdk', 312, 451, 0, '2018-12-10 16:44:55'),
(10, 'tatti', 'book', 'The Diary of Jane', 420, 69, 0, '2018-12-10 16:44:55'),
(11, 'tatti', 'furniture', '1', 2, 2147483647, 0, '2018-12-10 06:32:39');

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `username` varchar(20) NOT NULL,
  `content` varchar(50) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`username`, `content`, `timestamp`) VALUES
('shit', 'free churros', '2018-12-09 03:29:35'),
('shit', 'tattiwant to buyjsdajdjs', '2018-12-09 04:32:58'),
('horseman', 'tattiwant to buytable', '2018-12-09 04:33:03'),
('bojack', 'tattiwant to buyEleanor and Park', '2018-12-09 21:15:56'),
('horseman', 'tatti wants to buy table', '2018-12-09 21:18:06'),
('%s', 'tatti wants to buy %s', '2018-12-10 06:31:14'),
('%s', 'tatti wants to buy %s', '2018-12-10 06:31:14'),
('shit', 'tatti wants to buy jsdajdjs', '2018-12-10 06:31:16'),
('bojack', 'tatti wants to buy Eleanor and Park', '2018-12-10 06:31:17');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `userid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `emailid` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`userid`, `name`, `username`, `emailid`, `password`) VALUES
(1, 'tatti', 'tatti', 'tatti@shit.com', 'tatti'),
(2, 'adhikansh', 'adhikansh1999', 'adhikansh1999@gmail.', 'aaaa1234'),
(3, 'adhikansh', 'adhikansh1999', 'djaskdjk@gmail.com', 'mmksadkasj'),
(4, 'Bojack Horseman', 'queefburglar69', 'whatver@dawg.in', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cab_share`
--
ALTER TABLE `cab_share`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cab_share`
--
ALTER TABLE `cab_share`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
