-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2022 at 01:21 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `feedback`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `sno` int(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `token` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`sno`, `email`, `token`, `password`) VALUES
(1, 'shikhasingh56440@gmail.com', '2875a39d-8cc0-4762-b', 'right');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`sno`, `name`, `email`, `message`) VALUES
(15, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(16, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(17, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(18, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(19, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(20, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'checking flash'),
(38, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'course bca is not avavilable'),
(39, 'Swaran Singh', 'thakurchetasi1y4768@gmail.com', 'unknown response please train it time to time'),
(40, 'Swaran Singh', 'thakurchetasi1y4768@gmail.com', 'unknown response please train it time to time'),
(41, 'Swaran Singh', 'thakurchetasi1y4768@gmail.com', 'unknown response please train it time to time'),
(42, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'keep train'),
(43, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'keep train'),
(44, 'Deekasha Rani', 'shikhasingh56440@gmail.com', 'keep train'),
(45, 'Swaran Singh', 'thakurchetansingh1@gmail.com', 'for testing email this feedback is send');

-- --------------------------------------------------------

--
-- Table structure for table `unanswer`
--

CREATE TABLE `unanswer` (
  `sno` int(20) NOT NULL,
  `question` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `unanswer`
--

INSERT INTO `unanswer` (`sno`, `question`) VALUES
(14, 'hel'),
(15, 'joy'),
(16, 'what'),
(17, 'morning'),
(18, 'What is land pollution?'),
(19, 'Actually all for MC.'),
(20, 'At Jody of MCA.'),
(21, 'At your day of MCA.'),
(22, 'MC course.'),
(23, 'NCAA quotes.'),
(24, 'Land pollution.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `unanswer`
--
ALTER TABLE `unanswer`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `sno` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `unanswer`
--
ALTER TABLE `unanswer`
  MODIFY `sno` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
