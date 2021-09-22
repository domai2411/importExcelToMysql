CREATE TABLE `quiz1` (
  `id` int(10) NOT NULL,
  `question` text,
  `A` text,
  `B` text,
  `C` text,
  `D` text,
  `linhvuc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8