-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 05, 2022 at 03:03 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1doctpredb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admintb`
--

CREATE TABLE `admintb` (
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admintb`
--

INSERT INTO `admintb` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `meditb`
--

CREATE TABLE `meditb` (
  `id` bigint(20) NOT NULL auto_increment,
  `DiseaseName` varchar(250) NOT NULL,
  `MediName` varchar(250) NOT NULL,
  `Time` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Info` varchar(500) NOT NULL,
  `Image` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `meditb`
--

INSERT INTO `meditb` (`id`, `DiseaseName`, `MediName`, `Time`, `Qty`, `Price`, `Info`, `Image`) VALUES
(1, 'fever', 'dolo', 'morning', '1', '10', 'after Meals', 'g1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no 6 trichy', 'san', 'san'),
('sanNew', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no ', 'sanNew', 'sanNew'),
('mani', 'male', '33', 'ishu@gmail.com', '9486365535', 'dgh', 'mani', 'mani');
