-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2021 at 07:12 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `buyers`
--

CREATE TABLE `buyers` (
  `userid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `emailid` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buyers`
--

INSERT INTO `buyers` (`userid`, `name`, `username`, `emailid`, `password`) VALUES
(2, 'adhikansh', 'adhikansh1999', 'adhikansh1999@gmail.', 'aaaa1234'),
(5, '1', '1', 'a@b.c', '12'),
(6, 'andy', 'andy', 'andy@a.b', 'andy');

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
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
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
-- Table structure for table `carts`
--

CREATE TABLE `carts` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `carts`
--

INSERT INTO `carts` (`id`, `username`, `product_id`, `quantity`) VALUES
(1, 'andy', 12, 1),
(2, 'andy', 10, 1),
(3, 'andy', 12, 1),
(4, 'andy', 12, 1),
(5, 'andy', 12, 1),
(6, 'andy', 12, 1),
(7, 'andy', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `username` varchar(20) NOT NULL,
  `content` varchar(50) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `username` varchar(256) NOT NULL,
  `product_type` varchar(256) NOT NULL,
  `product_name` varchar(256) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `username`, `product_type`, `product_name`, `price`, `quantity`, `timestamp`) VALUES
(1, 'adhikansh1999', 'furniture', 'usha', 35, 23, '2021-04-16 05:10:53'),
(3, 'bojack', 'book', 'Eleanor and Park', 0, 0, '2018-12-10 16:44:55'),
(4, 'horseman', 'furniture', 'table', 450, 0, '2018-12-10 16:44:55'),
(5, 'adhikansh1999', 'book', 'cold/mess', 100, 32898932, '2021-04-16 05:10:53'),
(7, 'adhikansh1999', 'book', 'jsdahjh', 231, 911, '2021-04-16 05:10:53'),
(9, 'adhikansh1999', 'book', 'asjdk', 312, 451, '2021-04-16 05:10:53'),
(10, 'adhikansh1999', 'book', 'The Diary of Jane', 420, 69, '2021-04-16 05:10:53'),
(11, 'adhikansh1999', 'furniture', '1', 2, 2147483647, '2021-04-16 05:10:53'),
(12, 'andy', 'furniture', 'iphone', 12, 5, '2021-04-16 04:24:12');

-- --------------------------------------------------------

--
-- Table structure for table `sellers`
--

CREATE TABLE `sellers` (
  `userid` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sellers`
--

INSERT INTO `sellers` (`userid`, `username`, `password`, `name`, `emailid`) VALUES
(1, 'andy', 'andy', 'andy', 'a@b.c'),
(2, 'sanket', 'sanket', 'sanket', 'ad@b.c');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buyers`
--
ALTER TABLE `buyers`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `cab_share`
--
ALTER TABLE `cab_share`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `carts`
--
ALTER TABLE `carts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sellers`
--
ALTER TABLE `sellers`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buyers`
--
ALTER TABLE `buyers`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `cab_share`
--
ALTER TABLE `cab_share`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `carts`
--
ALTER TABLE `carts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `sellers`
--
ALTER TABLE `sellers`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
