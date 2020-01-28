CREATE DATABASE  IF NOT EXISTS `gmm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gmm`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: gmm
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `console_game`
--

DROP TABLE IF EXISTS `console_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `console_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-cfk` (`game_id`),
  CONSTRAINT `gameid-cfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `console_game`
--

LOCK TABLES `console_game` WRITE;
/*!40000 ALTER TABLE `console_game` DISABLE KEYS */;
INSERT INTO `console_game` VALUES ('God of War',77,NULL),('Resident Evil 2',78,NULL),('Sekiro: Shadows Die Twice',80,NULL),('Smash Bros. Ultimate',79,NULL);
/*!40000 ALTER TABLE `console_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `createdgamesbymod`
--

DROP TABLE IF EXISTS `createdgamesbymod`;
/*!50001 DROP VIEW IF EXISTS `createdgamesbymod`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `createdgamesbymod` AS SELECT 
 1 AS `mod_nick`,
 1 AS `game_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `creategamesrel`
--

DROP TABLE IF EXISTS `creategamesrel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creategamesrel` (
  `mod_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `contentdetails` longtext,
  `contenttype` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`mod_id`,`game_id`),
  KEY `game_idfk` (`game_id`),
  CONSTRAINT `game_idfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `mod_idfk` FOREIGN KEY (`mod_id`) REFERENCES `moderator` (`mod_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creategamesrel`
--

LOCK TABLES `creategamesrel` WRITE;
/*!40000 ALTER TABLE `creategamesrel` DISABLE KEYS */;
INSERT INTO `creategamesrel` VALUES (6,71,'Artifact,Design','English','2020-01-07 00:05:10'),(6,73,'Action fps','English','2020-01-07 14:10:09'),(6,74,'Fps','English','2020-01-07 14:10:11'),(6,77,'Fps action','English','2020-01-07 14:10:22'),(6,78,'Action','English','2020-01-07 14:10:25'),(6,79,'Strategy','English','2020-01-07 14:10:28'),(6,80,'Fps action','English','2020-01-07 14:10:31'),(6,81,'Fps','English','2020-01-07 14:10:34'),(6,82,'Artifact','English','2020-01-07 14:10:37'),(6,83,'Strategy','English','2020-01-07 14:10:40'),(6,84,'Strategy','English','2020-01-07 14:10:45'),(6,85,'Fps','English','2020-01-07 14:10:48');
/*!40000 ALTER TABLE `creategamesrel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createmoviesrel`
--

DROP TABLE IF EXISTS `createmoviesrel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createmoviesrel` (
  `mod_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `contentdetails` longtext,
  `contenttype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`mod_id`,`movie_id`),
  KEY `movieidfk` (`movie_id`),
  CONSTRAINT `movieidfk` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `moviemodfk` FOREIGN KEY (`mod_id`) REFERENCES `moderator` (`mod_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createmoviesrel`
--

LOCK TABLES `createmoviesrel` WRITE;
/*!40000 ALTER TABLE `createmoviesrel` DISABLE KEYS */;
INSERT INTO `createmoviesrel` VALUES (6,16,'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.','English'),(6,17,'A troubled child summons the courage to help a friendly alien escape Earth and return to his home world.',' English'),(6,18,'Dorothy Gale is swept away from a farm in Kansas to a magical land of Oz in a tornado and embarks on a quest with her new friends to see the Wizard who can help her return home to Kansas and help her friends as well. ',' English'),(6,19,'Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empires world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.',' English'),(6,20,'It\'s been 15 years since the Lord of the Rings trilogy ended, but we still can\'t get enough. Let\'s look at the stars who missed out on adventures in Middle-earth. ',' English'),(6,21,'Exiled into the dangerous forest by her wicked stepmother, a princess is rescued by seven dwarf miners who make her part of their household.',' English'),(6,22,'inda Hamilton has made a career out of playing strong female protagonists, especially as Sarah Connor in The Terminator and Terminator: Dark Fate. What other roles has she played?',' English'),(6,24,'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',' English Italian Latin'),(6,25,'Jesus of Nazareth,the son of God raised by a Jewish carpenter. Based on the gospel of Luke in the New Testament',' English');
/*!40000 ALTER TABLE `createmoviesrel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createmusicrel`
--

DROP TABLE IF EXISTS `createmusicrel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createmusicrel` (
  `mod_id` int(11) NOT NULL,
  `music_id` int(11) NOT NULL,
  `contentdetails` longtext,
  `contenttype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`mod_id`,`music_id`),
  KEY `musicidfk` (`music_id`),
  CONSTRAINT `musicidfk` FOREIGN KEY (`music_id`) REFERENCES `music` (`music_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `musicmodfk` FOREIGN KEY (`mod_id`) REFERENCES `moderator` (`mod_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createmusicrel`
--

LOCK TABLES `createmusicrel` WRITE;
/*!40000 ALTER TABLE `createmusicrel` DISABLE KEYS */;
INSERT INTO `createmusicrel` VALUES (6,19,'Electronic Dance Music','English'),(6,20,'Rock Music','English'),(6,22,'Dubstep','English'),(6,23,'Rhythm and Blues','English'),(6,24,'Techno','English'),(6,25,'Country Music','English'),(6,26,'Electro','English'),(6,27,'Indie Rock','English'),(6,28,'Pop Music','English');
/*!40000 ALTER TABLE `createmusicrel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `createseriesrel`
--

DROP TABLE IF EXISTS `createseriesrel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `createseriesrel` (
  `mod_id` int(11) NOT NULL,
  `series_id` int(11) NOT NULL,
  `contentdetails` longtext,
  `contenttype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`mod_id`,`series_id`),
  KEY `seriesidfk` (`series_id`),
  CONSTRAINT `seriesidfk` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `seriesmodfk` FOREIGN KEY (`mod_id`) REFERENCES `moderator` (`mod_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `createseriesrel`
--

LOCK TABLES `createseriesrel` WRITE;
/*!40000 ALTER TABLE `createseriesrel` DISABLE KEYS */;
INSERT INTO `createseriesrel` VALUES (6,17,'The travails of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.','Action, Adventure, Sci-Fi'),(6,18,'Follows the political rivalries and romance of Queen Elizabeth II\'s reign and the events that shaped the second half of the twentieth century.','Drama, History'),(6,19,'Two children embark on a magical adventure through parallel universes.','Adventure, Drama, Family'),(6,20,'Set in an alternate history where masked vigilantes are treated as outlaws, Watchmen embraces the nostalgia of the original groundbreaking graphic novel of the same name, while attempting to break new ground of its own.',' Action, Drama, Mystery'),(6,22,'An animated series that follows the exploits of a super scientist and his not-so-bright grandson.','Animation, Adventure, Comedy'),(6,23,'Far in a dystopian future, the human race has lost the sense of sight, and society has had to find new ways to interact, build, hunt, and to survive. All of that is challenged when a set of twins is born with sight.',' Action, Drama, Sci-Fi'),(6,24,'A Philadelphia couple are in mourning after an unspeakable tragedy creates a rift in their marriage and opens the door for a mysterious force to enter their home.','Drama, Horror, Thriller '),(6,25,'Elliot, a brilliant but highly unstable young cyber-security engineer and vigilante hacker, becomes a key figure in a complex game of global dominance when he and his shadowy allies try to take down the corrupt corporation he works for.','Crime, Drama, Thriller '),(6,26,'An up-and-coming CIA analyst, Jack Ryan, is thrust into a dangerous field assignment as he uncovers a pattern in terrorist communication that launches him into the center of a dangerous gambit.','Action, Drama, Thriller');
/*!40000 ALTER TABLE `createseriesrel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `fpsgames`
--

DROP TABLE IF EXISTS `fpsgames`;
/*!50001 DROP VIEW IF EXISTS `fpsgames`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `fpsgames` AS SELECT 
 1 AS `game_name`,
 1 AS `gametype`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `game_id` int(11) NOT NULL,
  `game_name` varchar(45) NOT NULL,
  `game_firm` varchar(45) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `gametype` varchar(45) NOT NULL,
  `ratingcount` int(11) DEFAULT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (71,'Minecraft','Mojang',6.95,'pc',4),(73,'Fortnite','Epic Games',0,'pc',0),(74,'Overwatch','Blizzard',0,'pc',0),(77,'God of War','SIE Santa Monica Studio',0,'console',0),(78,'Resident Evil 2','Capcom',0,'console',0),(79,'Smash Bros. Ultimate','Nintendo',0,'console',0),(80,'Sekiro: Shadows Die Twice','FromSoftware',0,'console',0),(81,'Call of Duty: Mobile','TiMi Studios',0,'mobile',0),(82,'Crashlands','Butterscotch Shenanigans',0,'mobile',0),(83,'Evoland 1','Shiro Games',0,'mobile',0),(84,'Evoland 2','Shiro Games',8.96667,'mobile',3),(85,'PUBG:Mobile','Tencent Games',0,'mobile',0);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `afteraddgame` AFTER INSERT ON `games` FOR EACH ROW BEGIN 
IF (NEW.gametype = 'pc') THEN
INSERT INTO  pc_game SET game_id = NEW.game_id, game_name = NEW.game_name;
ELSE IF (NEW.gametype = 'mobile') THEN
INSERT INTO mobile_game SET game_id = NEW.game_id, game_name = NEW.game_name;
ELSE IF (NEW.gametype = 'console') THEN
INSERT INTO console_game SET game_id = NEW.game_id, game_name = NEW.game_name;
END IF;
END IF;
END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `general_user`
--

DROP TABLE IF EXISTS `general_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `general_user` (
  `user_id` int(11) NOT NULL,
  `user_nick` varchar(45) NOT NULL,
  `usermail` varchar(45) NOT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `usermailfk_idx` (`usermail`),
  CONSTRAINT `usermail-fk1` FOREIGN KEY (`usermail`) REFERENCES `user` (`user_mail`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `general_user`
--

LOCK TABLES `general_user` WRITE;
/*!40000 ALTER TABLE `general_user` DISABLE KEYS */;
INSERT INTO `general_user` VALUES (48,'admin','admin',2),(49,'user','user@mail.com',NULL),(50,'writer','writer',3),(51,'user2','user2',NULL),(52,'admin2nick','admin2@mail.com',5);
/*!40000 ALTER TABLE `general_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `afterroleupdate` AFTER UPDATE ON `general_user` FOR EACH ROW BEGIN 
IF (NEW.role = 2) THEN
INSERT INTO  moderator SET mod_id =  (SELECT MAX(MODID) from sequences), mod_nick = NEW.user_nick, role = NEW.role, user_idfk1 = NEW.user_id;
update sequences SET MODID=MODID+1;
  ELSE IF(NEW.role = 3) THEN 
  INSERT INTO news_writer SET writer_id = (SELECT MAX(WRITERID) from sequences), writer_nick = NEW.user_nick, role = NEW.role, user_idfk2 = NEW.user_id;
  update sequences SET WRITERID=WRITERID+1;
  END IF;
END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `mobile_game`
--

DROP TABLE IF EXISTS `mobile_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobile_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-mfk` (`game_id`),
  CONSTRAINT `gameid-mfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mobile_game`
--

LOCK TABLES `mobile_game` WRITE;
/*!40000 ALTER TABLE `mobile_game` DISABLE KEYS */;
INSERT INTO `mobile_game` VALUES ('Call of Duty: Mobile',81,NULL),('Crashlands',82,NULL),('Evoland 1',83,NULL),('Evoland 2',84,NULL),('PUBG:Mobile',85,NULL);
/*!40000 ALTER TABLE `mobile_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moderator`
--

DROP TABLE IF EXISTS `moderator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moderator` (
  `mod_id` int(11) NOT NULL,
  `mod_nick` varchar(45) NOT NULL,
  `user_idfk1` int(11) NOT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`mod_id`),
  KEY `user_idfkmod` (`user_idfk1`),
  CONSTRAINT `user_idfkmod` FOREIGN KEY (`user_idfk1`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moderator`
--

LOCK TABLES `moderator` WRITE;
/*!40000 ALTER TABLE `moderator` DISABLE KEYS */;
INSERT INTO `moderator` VALUES (6,'admin',48,2);
/*!40000 ALTER TABLE `moderator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_id` int(11) NOT NULL,
  `movie_name` varchar(45) NOT NULL,
  `movie_type` varchar(45) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `ratingcount` int(11) DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (16,'Titanic (1997)','Drama, Romance',8.75,2),(17,'E.T. the Extra-Terrestrial',' Family Sci-Fi',0,0),(18,'The Wizard of Oz','Adventure Family Fantasy Musical',0,0),(19,'Star Wars',' Action Adventure Fantasy Sci-Fi',0,0),(20,'The Lord of the Rings: The Return of the King','Adventure Drama Fantasy',0,0),(21,'Snow White and the Seven Dwarfs','Animation Family Fantasy Musical Romance',9.25,2),(22,'Terminator 2: Judgment Day','Action Sci-Fi',9,1),(24,'The Godfather','Crime Drama',0,0),(25,'Jesus','Biography Drama Family History',0,0);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music`
--

DROP TABLE IF EXISTS `music`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `music` (
  `music_id` int(11) NOT NULL,
  `music_artist` varchar(45) DEFAULT NULL,
  `music_name` varchar(45) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `ratingcount` int(11) DEFAULT NULL,
  PRIMARY KEY (`music_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music`
--

LOCK TABLES `music` WRITE;
/*!40000 ALTER TABLE `music` DISABLE KEYS */;
INSERT INTO `music` VALUES (19,'Tones And I','Dance Monkey',0,0),(20,'Maroon 5','Memories',0,0),(22,'Regard','Ride It',0,0),(23,'Dua Lipa','Don\'t Start Now',0,0),(24,'Post Malone','Circles',0,0),(25,'Lewis Capaldi','Someone You Loved',0,0),(26,'SAINt JHN','Roses (Imanbek Remix)',0,0),(27,'Billie Eilish','everything i wanted',0,0),(28,'Meduza, Becky Hill & Goodboys','Lose Control',0,0);
/*!40000 ALTER TABLE `music` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `news_id` int(11) NOT NULL,
  `writer_id` int(11) NOT NULL,
  `newsdate` datetime DEFAULT NULL,
  `text` longtext,
  `newstitle` varchar(45) NOT NULL,
  PRIMARY KEY (`news_id`),
  KEY `writerid-fk` (`writer_id`),
  CONSTRAINT `writerid-fk` FOREIGN KEY (`writer_id`) REFERENCES `news_writer` (`writer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (26,10,'2020-01-07 14:48:17','The full list of the 2019 Golden Globe film nominations is below. Marriage Story led all films with six total nominations, followed by five for The Irishman and Once Upon a Time in Hollywood and four each for Joker and The Two Popes.','Golden Globe'),(27,10,'2020-01-07 14:54:06','These games have the highest Metascores out of all titles released from 2010-19. Games must have reviews from at least 15 critics to qualify for inclusion. If a game was released on multiple platforms, we are only including the version with the most reviews in our database.','Highest Metascores Games');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_writer`
--

DROP TABLE IF EXISTS `news_writer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news_writer` (
  `writer_id` int(11) NOT NULL,
  `writer_nick` varchar(45) NOT NULL,
  `user_idfk2` int(11) NOT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`writer_id`),
  KEY `user_idfkwri` (`user_idfk2`),
  CONSTRAINT `user_idfkwri` FOREIGN KEY (`user_idfk2`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_writer`
--

LOCK TABLES `news_writer` WRITE;
/*!40000 ALTER TABLE `news_writer` DISABLE KEYS */;
INSERT INTO `news_writer` VALUES (10,'writer',50,3);
/*!40000 ALTER TABLE `news_writer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pc_game`
--

DROP TABLE IF EXISTS `pc_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pc_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-pfk` (`game_id`),
  CONSTRAINT `gameid-pfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pc_game`
--

LOCK TABLES `pc_game` WRITE;
/*!40000 ALTER TABLE `pc_game` DISABLE KEYS */;
INSERT INTO `pc_game` VALUES ('Fortnite',73,NULL),('Minecraft',71,NULL),('Overwatch',74,NULL);
/*!40000 ALTER TABLE `pc_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewgame`
--

DROP TABLE IF EXISTS `reviewgame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviewgame` (
  `reviewgame_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `commenttext` longtext,
  `givenrating` float DEFAULT NULL,
  PRIMARY KEY (`reviewgame_id`),
  KEY `reviewgame_gameid` (`game_id`),
  KEY `reviewgame_userid` (`user_id`),
  CONSTRAINT `reviewgame_gameid` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reviewgame_userid` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewgame`
--

LOCK TABLES `reviewgame` WRITE;
/*!40000 ALTER TABLE `reviewgame` DISABLE KEYS */;
INSERT INTO `reviewgame` VALUES (18,48,71,'güzel oyun',6),(19,49,71,'not good',3),(20,48,71,'very nice game	',9.8),(22,48,84,'not bad',8),(23,48,84,'not so good',9),(25,48,71,'memo',9),(26,48,84,'Nicee',9.9);
/*!40000 ALTER TABLE `reviewgame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewmovies`
--

DROP TABLE IF EXISTS `reviewmovies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviewmovies` (
  `reviewmovie_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `commenttext` longtext,
  `givenrating` float DEFAULT NULL,
  PRIMARY KEY (`reviewmovie_id`),
  KEY `reviewmovies_movieid` (`movie_id`),
  KEY `reviewmoviews_userid` (`user_id`),
  CONSTRAINT `reviewmovies_movieid` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reviewmoviews_userid` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewmovies`
--

LOCK TABLES `reviewmovies` WRITE;
/*!40000 ALTER TABLE `reviewmovies` DISABLE KEYS */;
INSERT INTO `reviewmovies` VALUES (5,48,16,'not bad',9.5),(6,48,16,'nice',8),(7,48,21,'nice movie',9),(9,48,22,'very good	',9),(11,52,21,'Very nice movie. You should watch this.',9.5);
/*!40000 ALTER TABLE `reviewmovies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewmusic`
--

DROP TABLE IF EXISTS `reviewmusic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviewmusic` (
  `reviewmusic_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `music_id` int(11) NOT NULL,
  `commenttext` longtext,
  `givenrating` float DEFAULT NULL,
  PRIMARY KEY (`reviewmusic_id`),
  KEY `reviewmusic_musicidfk` (`music_id`),
  KEY `reviewmusic_useridfk` (`user_id`),
  CONSTRAINT `reviewmusic_musicidfk` FOREIGN KEY (`music_id`) REFERENCES `music` (`music_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reviewmusic_useridfk` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewmusic`
--

LOCK TABLES `reviewmusic` WRITE;
/*!40000 ALTER TABLE `reviewmusic` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviewmusic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviewseries`
--

DROP TABLE IF EXISTS `reviewseries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviewseries` (
  `reviewseries_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `series_id` int(11) NOT NULL,
  `commenttext` longtext,
  `givenrating` float DEFAULT NULL,
  PRIMARY KEY (`reviewseries_id`),
  KEY `reviewseries_seriesid` (`series_id`),
  KEY `reviewseries_userid` (`user_id`),
  CONSTRAINT `reviewseries_seriesid` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reviewseries_userid` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviewseries`
--

LOCK TABLES `reviewseries` WRITE;
/*!40000 ALTER TABLE `reviewseries` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviewseries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequences`
--

DROP TABLE IF EXISTS `sequences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sequences` (
  `GAMEID` int(11) NOT NULL,
  `MODID` int(11) NOT NULL,
  `MOVIEID` int(11) NOT NULL,
  `SERIESID` int(11) NOT NULL,
  `USERID` int(11) NOT NULL,
  `MUSICID` int(11) NOT NULL,
  `WRITERID` int(11) NOT NULL,
  `ADMINID` int(11) NOT NULL,
  `REVIEWID` int(11) NOT NULL,
  `NEWSID` int(11) NOT NULL,
  `REVIEWGAMEID` int(11) NOT NULL,
  `REVIEWMUSICID` int(11) NOT NULL,
  `REVIEWMOVIEID` int(11) NOT NULL,
  `REVIEWSERIESID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequences`
--

LOCK TABLES `sequences` WRITE;
/*!40000 ALTER TABLE `sequences` DISABLE KEYS */;
INSERT INTO `sequences` VALUES (86,7,26,27,53,29,11,4,21,29,27,6,12,6);
/*!40000 ALTER TABLE `sequences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `series`
--

DROP TABLE IF EXISTS `series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `series` (
  `series_id` int(11) NOT NULL,
  `series_name` varchar(45) NOT NULL,
  `rating` float DEFAULT NULL,
  `ratingcount` int(11) DEFAULT NULL,
  PRIMARY KEY (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series`
--

LOCK TABLES `series` WRITE;
/*!40000 ALTER TABLE `series` DISABLE KEYS */;
INSERT INTO `series` VALUES (17,'The Mandalorian',0,0),(18,'The Crown',0,0),(19,'His Dark Materials',0,0),(20,'Watchmen',0,0),(22,'Rick and Morty',0,0),(23,'See',0,0),(24,'Servant',0,0),(25,'Mr. Robot',0,0),(26,'Jack Ryan',0,0);
/*!40000 ALTER TABLE `series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_admin`
--

DROP TABLE IF EXISTS `system_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_admin` (
  `admin_id` int(11) NOT NULL,
  `admin_nick` varchar(45) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_admin`
--

LOCK TABLES `system_admin` WRITE;
/*!40000 ALTER TABLE `system_admin` DISABLE KEYS */;
INSERT INTO `system_admin` VALUES (1,'Eren Özger'),(2,'Nehir Akbaş'),(3,'Mustafa Küçük');
/*!40000 ALTER TABLE `system_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `todaynews`
--

DROP TABLE IF EXISTS `todaynews`;
/*!50001 DROP VIEW IF EXISTS `todaynews`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `todaynews` AS SELECT 
 1 AS `news_id`,
 1 AS `writer_id`,
 1 AS `newsdate`,
 1 AS `text`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `topratedgame`
--

DROP TABLE IF EXISTS `topratedgame`;
/*!50001 DROP VIEW IF EXISTS `topratedgame`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `topratedgame` AS SELECT 
 1 AS `game_name`,
 1 AS `contentdetails`,
 1 AS `rating`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `topratedmovie`
--

DROP TABLE IF EXISTS `topratedmovie`;
/*!50001 DROP VIEW IF EXISTS `topratedmovie`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `topratedmovie` AS SELECT 
 1 AS `movie_name`,
 1 AS `contentdetails`,
 1 AS `rating`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `topratedmusic`
--

DROP TABLE IF EXISTS `topratedmusic`;
/*!50001 DROP VIEW IF EXISTS `topratedmusic`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `topratedmusic` AS SELECT 
 1 AS `music_name`,
 1 AS `contentdetails`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `totalgamesaddedtoday`
--

DROP TABLE IF EXISTS `totalgamesaddedtoday`;
/*!50001 DROP VIEW IF EXISTS `totalgamesaddedtoday`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `totalgamesaddedtoday` AS SELECT 
 1 AS `totalgame`,
 1 AS `Todaydate`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_mail` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  PRIMARY KEY (`user_mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('admin','admin','admin','0/0/0'),('admin2@mail.com','admin2','admin2','01/01/0001'),('user@mail.com','user','user','0/0/0'),('user2','user2','user2','1/1/1'),('writer','writer','writer','0/0/0');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `whoaddmusic`
--

DROP TABLE IF EXISTS `whoaddmusic`;
/*!50001 DROP VIEW IF EXISTS `whoaddmusic`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `whoaddmusic` AS SELECT 
 1 AS `mod_nick`,
 1 AS `music_artist`,
 1 AS `music_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'gmm'
--

--
-- Dumping routines for database 'gmm'
--
/*!50003 DROP PROCEDURE IF EXISTS `addgame` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addgame`(IN modeid INT,IN gamename VARCHAR(45),
IN gamefirm VARCHAR(45),IN rating1 FLOAT,IN gametype1 VARCHAR(45),
IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO games VALUES ((SELECT MAX(GAMEID) from sequences),gamename,gamefirm,rating1,gametype1,0);
	INSERT INTO creategamesrel VALUES(modeid,(SELECT MAX(GAMEID) from sequences),contentdetails1,contenttype1,CURRENT_TIMESTAMP);
    update sequences SET GAMEID=GAMEID+1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `addmovie` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addmovie`(IN modeid INT,
IN moviename VARCHAR(45),IN movietype VARCHAR(45),IN rating1 FLOAT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO movies VALUES((SELECT MAX(MOVIEID) from sequences),moviename,movietype,rating1,0);
    INSERT INTO createmoviesrel VALUES(modeid,(SELECT MAX(MOVIEID) from sequences),contentdetails1,contenttype1);
    update sequences SET MOVIEID=MOVIEID+1;    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `addmusic` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addmusic`(IN modeid INT,
IN musicartist VARCHAR(45),IN musicname VARCHAR(45),IN rating1 FLOAT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO music VALUES((SELECT MAX(MUSICID) from sequences),musicartist,musicname,rating1,0);
    INSERT INTO createmusicrel VALUES(modeid,(SELECT MAX(MUSICID) from sequences),contentdetails1,contenttype1);
    update sequences SET MUSICID=MUSICID+1; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `addnews` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addnews`(IN writerid1 INT ,IN newstitle VARCHAR(45),IN newsinfo TEXT)
BEGIN
	INSERT INTO news VALUES((SELECT MAX(NEWSID) from sequences),writerid1,CURRENT_TIMESTAMP,newsinfo,newstitle);
    update sequences SET NEWSID=NEWSID+1; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `addseries` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addseries`(IN modeid INT,
IN seriesname VARCHAR(45),IN rating1 FLOAT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO series VALUES((SELECT MAX(SERIESID) from sequences),seriesname,rating1,0);
    INSERT INTO createseriesrel VALUES(modeid,(SELECT MAX(SERIESID) from sequences),contentdetails1,contenttype1);
    update sequences SET SERIESID=SERIESID+1; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `addsystemadmin` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addsystemadmin`(IN adminnick VARCHAR(45))
BEGIN
	INSERT INTO system_admin VALUES((SELECT MAX(ADMINID) from sequences),adminnick);
    update sequences SET ADMINID=ADMINID+1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `createrole` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `createrole`(IN rolenumber INT)
BEGIN
	INSERT INTO role VALUES(rolenumber);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `deletegamefromid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deletegamefromid`(IN gameid INT)
BEGIN
DELETE FROM games WHERE game_id = gameid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `finduser` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `finduser`(IN userid INT)
BEGIN
	SELECT * FROM general_user WHERE user_id = userid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `gamereviewpro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `gamereviewpro`(IN userid INT,IN gameid INT,IN commenttext LONGTEXT,IN givenrate FLOAT)
BEGIN
	INSERT INTO reviewgame VALUES ((SELECT MAX(REVIEWGAMEID) from sequences),userid,gameid,commenttext,givenrate);
    update sequences SET REVIEWGAMEID=REVIEWGAMEID+1;
    update games SET rating = (((rating * ratingcount)+givenrate) / (ratingcount + 1 )) WHERE game_id = gameid;
    update games SET ratingcount = ratingcount+1 WHERE game_id = gameid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `giverole` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `giverole`(IN givenuser_id INT, IN givenrole INT)
BEGIN
UPDATE general_user
SET role = givenrole
WHERE user_id = givenuser_id;	
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `moviereviewpro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `moviereviewpro`(IN userid INT,IN movieid INT,IN commenttext LONGTEXT,IN givenrate FLOAT)
BEGIN
	INSERT INTO reviewmovies VALUES ((SELECT MAX(REVIEWMOVIEID) from sequences),userid,movieid,commenttext,givenrate);
    update sequences SET REVIEWMOVIEID=REVIEWMOVIEID+1;
    update movies SET rating = (((rating * ratingcount)+givenrate) / (ratingcount + 1 )) WHERE movie_id = movieid;
    update movies SET ratingcount = ratingcount+1 WHERE movie_id = movieid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `musicreviewpro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `musicreviewpro`(IN userid INT,IN musicid INT,IN commenttext LONGTEXT,IN givenrate FLOAT)
BEGIN
	INSERT INTO reviewmusic VALUES ((SELECT MAX(REVIEWMUSICID) from sequences),userid,musicid,commenttext,givenrate);
    update sequences SET REVIEWMUSICID=REVIEWMUSICID+1;
    update music SET rating = (((rating * ratingcount)+givenrate) / (ratingcount + 1 )) WHERE music_id = musicid;
    update music SET ratingcount = ratingcount+1 WHERE music_id = musicid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `searchgame` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `searchgame`(IN searchkey VARCHAR(45))
BEGIN
	SELECT g.game_name,g.game_firm,c.contentdetails,g.gametype,g.rating,m.mod_nick 
    FROM games as g , creategamesrel as c, moderator as m 
    WHERE g.game_id = c.game_id AND c.mod_id = m.mod_id AND g.game_name LIKE '%searchkey%' 
    ORDER BY g.rating DESC 
    LIMIT 10;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `seriesreviewpro` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `seriesreviewpro`(IN userid INT,IN seriesid INT,IN commenttext LONGTEXT,IN givenrate FLOAT)
BEGIN
	INSERT INTO reviewseries VALUES ((SELECT MAX(REVIEWSERIESID) from sequences),userid,seriesid,commenttext,givenrate);
    update sequences SET REVIEWSERIESID=REVIEWSERIESID+1;
    update series SET rating = (((rating * ratingcount)+givenrate) / (ratingcount + 1 )) WHERE series_id = seriesid;
    update series SET ratingcount = ratingcount+1 WHERE series_id = seriesid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `showsequences` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `showsequences`()
BEGIN
	SELECT * from sequences;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `updategames` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updategames`(IN gameid INT,IN gamename VARCHAR(45),IN gamefirm VARCHAR(45), IN rating1 FLOAT, IN gametype1 VARCHAR(45))
BEGIN
UPDATE games
SET game_name = gamename, game_firm = gamefirm, rating = rating1, gametype = gametype1
WHERE game_id = gameid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `userregister` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `userregister`(IN mail1 VARCHAR(45),IN password1 VARCHAR(45),IN username1 VARCHAR(45),IN dob VARCHAR(45),
IN usernick VARCHAR(45))
BEGIN
	INSERT INTO user VALUES(mail1,password1,username1,dob);
    INSERT INTO general_user (user_id,user_nick,usermail) VALUES((SELECT MAX(USERID) from sequences),usernick,mail1);
    UPDATE sequences SET USERID=USERID+1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `createdgamesbymod`
--

/*!50001 DROP VIEW IF EXISTS `createdgamesbymod`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `createdgamesbymod` AS select `m`.`mod_nick` AS `mod_nick`,`g1`.`game_name` AS `game_name` from ((`games` `g1` join `creategamesrel` `g2`) join `moderator` `m`) where ((`g1`.`game_id` = `g2`.`game_id`) and (`g2`.`mod_id` = `m`.`mod_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `fpsgames`
--

/*!50001 DROP VIEW IF EXISTS `fpsgames`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `fpsgames` AS select `g1`.`game_name` AS `game_name`,`g1`.`gametype` AS `gametype` from (`games` `g1` join `creategamesrel` `g2`) where ((`g1`.`game_id` = `g2`.`game_id`) and (`g2`.`contentdetails` like '%FPS%')) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `todaynews`
--

/*!50001 DROP VIEW IF EXISTS `todaynews`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `todaynews` AS select `n`.`news_id` AS `news_id`,`n`.`writer_id` AS `writer_id`,`n`.`newsdate` AS `newsdate`,`n`.`text` AS `text` from `news` `n` where (`n`.`newsdate` >= curdate()) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `topratedgame`
--

/*!50001 DROP VIEW IF EXISTS `topratedgame`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `topratedgame` AS select `g`.`game_name` AS `game_name`,`c`.`contentdetails` AS `contentdetails`,`g`.`rating` AS `rating` from (`games` `g` join `creategamesrel` `c`) where (`g`.`game_id` = `c`.`game_id`) order by `g`.`rating` desc limit 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `topratedmovie`
--

/*!50001 DROP VIEW IF EXISTS `topratedmovie`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `topratedmovie` AS select `m`.`movie_name` AS `movie_name`,`c`.`contentdetails` AS `contentdetails`,`m`.`rating` AS `rating` from (`movies` `m` join `createmoviesrel` `c`) where (`m`.`movie_id` = `c`.`movie_id`) order by `m`.`rating` desc limit 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `topratedmusic`
--

/*!50001 DROP VIEW IF EXISTS `topratedmusic`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `topratedmusic` AS select `m`.`music_name` AS `music_name`,`c`.`contentdetails` AS `contentdetails` from (`music` `m` join `createmusicrel` `c`) where (`m`.`music_id` = `c`.`music_id`) order by `m`.`rating` desc limit 1 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `totalgamesaddedtoday`
--

/*!50001 DROP VIEW IF EXISTS `totalgamesaddedtoday`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `totalgamesaddedtoday` AS select count(0) AS `totalgame`,max(`g2`.`date`) AS `Todaydate` from ((`games` `g1` join `creategamesrel` `g2`) join `moderator` `m`) where ((`g1`.`game_id` = `g2`.`game_id`) and (`g2`.`mod_id` = `m`.`mod_id`) and (`g2`.`date` >= curdate())) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `whoaddmusic`
--

/*!50001 DROP VIEW IF EXISTS `whoaddmusic`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `whoaddmusic` AS select `m2`.`mod_nick` AS `mod_nick`,`m1`.`music_artist` AS `music_artist`,`m1`.`music_name` AS `music_name` from ((`music` `m1` join `createmusicrel` `c`) join `moderator` `m2`) where ((`m1`.`music_id` = `c`.`music_id`) and (`c`.`mod_id` = `m2`.`mod_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-09 19:21:46
