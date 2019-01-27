-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2019 at 05:10 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id_book` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `publisher` varchar(30) NOT NULL,
  `isbn` varchar(30) NOT NULL,
  `price` int(10) NOT NULL,
  `edition` varchar(20) NOT NULL,
  `date_published` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id_book`, `name`, `publisher`, `isbn`, `price`, `edition`, `date_published`) VALUES
(1, 'Python', 'Press', 'q12345', 2000, '6th Editio', '24/06/2019'),
(2, 'Java', 'Press', 'aq123', 1500, '7th Edition', '11/11/1999'),
(3, 'PHP', 'Press', 'as12', 1000, '4th Edition', '21/12/2005'),
(5, 'MYSQL', 'Press', '123qwe', 1230, '7th Edition', '00/00/0000');

-- --------------------------------------------------------

--
-- Table structure for table `buyer`
--

CREATE TABLE `buyer` (
  `id_buyer` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `contact_number` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buyer`
--

INSERT INTO `buyer` (`id_buyer`, `name`, `email`, `contact_number`) VALUES
(1, 'Roy', 'Roy@gmail.com', '2147483647'),
(2, 'Bah Bol', 'Bol@gmail.com', '9999999999'),
(3, 'Gubin', 'Gubin@gmail.com', '909090909'),
(4, 'Shapz', 'Shapz@gmail.com', '2147483647'),
(6, 'Bada', 'bada@gmail.com', '1000000009'),
(10, 'BAla', 'bala@gmail.com', '2147483647');

-- --------------------------------------------------------

--
-- Table structure for table `ordered_books`
--

CREATE TABLE `ordered_books` (
  `id_order` int(10) NOT NULL,
  `id_seller` int(10) NOT NULL,
  `id_buyer` int(10) NOT NULL,
  `id_book` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

CREATE TABLE `seller` (
  `id_seller` int(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `contact_number` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller`
--

INSERT INTO `seller` (`id_seller`, `name`, `address`, `contact_number`) VALUES
(1, 'qwerty', 'qwerty', '12345'),
(2, 'qas', 'qas', '1234567890'),
(3, 'Pereth', 'Polo', '9999999999'),
(4, 'Mummy', 'Jaiaw', '1234567890'),
(5, 'Lam', 'Lam@gmail.com', '9876543210'),
(6, 'Lakham', 'Lakham@gmail.com', '1234565432'),
(7, 'Shaphrang', 'Sunny Hill', '2147483647'),
(8, 'Joe', 'Joe@gmail.com', '1111111111'),
(9, 'Pam', 'Pam@gmail.com', '22222222222'),
(10, 'Liza', 'Liza@gmail.com', '5555555555');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id_book`);

--
-- Indexes for table `buyer`
--
ALTER TABLE `buyer`
  ADD PRIMARY KEY (`id_buyer`);

--
-- Indexes for table `ordered_books`
--
ALTER TABLE `ordered_books`
  ADD PRIMARY KEY (`id_order`);

--
-- Indexes for table `seller`
--
ALTER TABLE `seller`
  ADD PRIMARY KEY (`id_seller`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
