USE `gmm`;
--CREATE TABLES
DROP TABLE IF EXISTS `console_game`;
CREATE TABLE `console_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-cfk` (`game_id`),
  CONSTRAINT `gameid-cfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `creategamesrel`;
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


DROP TABLE IF EXISTS `createmoviesrel`;
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


DROP TABLE IF EXISTS `createmusicrel`;
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


DROP TABLE IF EXISTS `createseriesrel`;
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


DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `game_id` int(11) NOT NULL,
  `game_name` varchar(45) NOT NULL,
  `game_firm` varchar(45) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `gametype` varchar(45) NOT NULL,
  PRIMARY KEY (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `general_user`;
CREATE TABLE `general_user` (
  `user_id` int(11) NOT NULL,
  `user_nick` varchar(45) NOT NULL,
  `role` int(11) NOT NULL,
  `usermail` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `usermailfk_idx` (`usermail`),
  CONSTRAINT `usermail-fk1` FOREIGN KEY (`usermail`) REFERENCES `user` (`user_mail`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `mobile_game`;
CREATE TABLE `mobile_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-mfk` (`game_id`),
  CONSTRAINT `gameid-mfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `moderator`;
CREATE TABLE `moderator` (
  `mod_id` int(11) NOT NULL,
  `mod_nick` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`mod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `movie_id` int(11) NOT NULL,
  `movie_name` varchar(45) NOT NULL,
  `movie_type` varchar(45) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `music`;
CREATE TABLE `music` (
  `music_id` int(11) NOT NULL,
  `music_artist` varchar(45) DEFAULT NULL,
  `music_name` varchar(45) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`music_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `news_id` int(11) NOT NULL,
  `writer_id` int(11) NOT NULL,
  `newsdate` datetime DEFAULT NULL,
  `text` longtext,
  PRIMARY KEY (`news_id`),
  KEY `writerid-fk` (`writer_id`),
  CONSTRAINT `writerid-fk` FOREIGN KEY (`writer_id`) REFERENCES `news_writer` (`writer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `news_writer`;
CREATE TABLE `news_writer` (
  `writer_id` int(11) NOT NULL,
  `writer_nick` varchar(45) NOT NULL,
  `role` int(11) NOT NULL,
  PRIMARY KEY (`writer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `pc_game`;
CREATE TABLE `pc_game` (
  `game_name` varchar(45) NOT NULL,
  `game_id` int(11) NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`game_name`),
  KEY `gameid-pfk` (`game_id`),
  CONSTRAINT `gameid-pfk` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `role_type` int(11) NOT NULL,
  PRIMARY KEY (`role_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `sequences`;
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
  `NEWSID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `series`;
CREATE TABLE `series` (
  `series_id` int(11) NOT NULL,
  `series_name` varchar(45) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `system_admin`;
CREATE TABLE `system_admin` (
  `admin_id` int(11) NOT NULL,
  `admin_nick` varchar(45) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `takerolerel`;
CREATE TABLE `takerolerel` (
  `role_type` int(11) NOT NULL,
  `user_mail` varchar(45) NOT NULL,
  PRIMARY KEY (`role_type`,`user_mail`),
  KEY `usermailfk` (`user_mail`),
  CONSTRAINT `roletypefk` FOREIGN KEY (`role_type`) REFERENCES `role` (`role_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `usermailfk` FOREIGN KEY (`user_mail`) REFERENCES `user` (`user_mail`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_mail` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  PRIMARY KEY (`user_mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `user_review`;
CREATE TABLE `user_review` (
  `review_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_id` int(11) NOT NULL,
  `reviewdate` datetime NOT NULL,
  PRIMARY KEY (`review_id`),
  KEY `userid-fk` (`user_id`),
  CONSTRAINT `userid-fk` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `userwritesrel`;
CREATE TABLE `userwritesrel` (
  `user_id` int(11) NOT NULL,
  `review_id` int(11) NOT NULL,
  `about` varchar(45) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  PRIMARY KEY (`user_id`,`review_id`),
  KEY `reviewrelfk` (`review_id`),
  CONSTRAINT `reviewrelfk` FOREIGN KEY (`review_id`) REFERENCES `user_review` (`review_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `userwritesfk` FOREIGN KEY (`user_id`) REFERENCES `general_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DELIMITER ;;

-- PROCEDURES
CREATE DEFINER=`root`@`localhost` PROCEDURE `addgame`(IN modeid INT,IN gamename VARCHAR(45),
IN gamefirm VARCHAR(45),IN rating1 INT,IN gametype1 VARCHAR(45),
IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO games VALUES ((SELECT MAX(GAMEID) from sequences),gamename,gamefirm,rating1,gametype1);
	INSERT INTO creategamesrel VALUES(modeid,(SELECT MAX(GAMEID) from sequences),contentdetails1,contenttype1,CURRENT_TIMESTAMP);
    update sequences SET GAMEID=GAMEID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addmoderator`(IN modnick VARCHAR(45),IN role INT)
BEGIN
	INSERT INTO moderator VALUES((SELECT MAX(MODID) from sequences),modnick,role);
    update sequences SET MODID=MODID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addmovie`(IN modeid INT,
IN moviename VARCHAR(45),IN movietype VARCHAR(45),IN rating1 INT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO movies VALUES((SELECT MAX(MOVIEID) from sequences),moviename,movietype,rating1);
    INSERT INTO createmoviesrel VALUES(modeid,(SELECT MAX(MOVIEID) from sequences),contentdetails1,contenttype1);
    update sequences SET MOVIEID=MOVIEID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addmusic`(IN modeid INT,
IN musicartist VARCHAR(45),IN musicname VARCHAR(45),IN rating1 INT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO music VALUES((SELECT MAX(MUSICID) from sequences),musicartist,musicname,rating1);
    INSERT INTO createmusicrel VALUES(modeid,(SELECT MAX(MUSICID) from sequences),contentdetails1,contenttype1);
    update sequences SET MUSICID=MUSICID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addnews`(IN writerid1 INT ,IN newsinfo TEXT)
BEGIN
	INSERT INTO news VALUES((SELECT MAX(NEWSID) from sequences),writerid1,CURRENT_TIMESTAMP,newsinfo);
    update sequences SET NEWSID=NEWSID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addnewswriter`(IN writernick VARCHAR(45), IN role INT)
BEGIN
	INSERT INTO news_writer VALUES((SELECT MAX(WRITERID) from sequences),writernick,role);
    update sequences SET WRITERID=WRITERID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addseries`(IN modeid INT,
IN seriesname VARCHAR(45),IN rating1 INT, IN contentdetails1 LONGTEXT,IN contenttype1 VARCHAR(45))
BEGIN
	INSERT INTO series VALUES((SELECT MAX(SERIESID) from sequences),seriesname,rating1);
    INSERT INTO createseriesrel VALUES(modeid,(SELECT MAX(SERIESID) from sequences),contentdetails1,contenttype1);
    update sequences SET SERIESID=SERIESID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `addsystemadmin`(IN adminnick VARCHAR(45))
BEGIN
	INSERT INTO system_admin VALUES((SELECT MAX(ADMINID) from sequences),adminnick);
    update sequences SET ADMINID=ADMINID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `adduserreview`(IN userid INT,IN contentid INT,IN about1 VARCHAR(45),IN rating1 INT)
BEGIN
	INSERT INTO user_review VALUES((SELECT MAX(REVIEWID) from sequences),userid,contentid,CURRENT_TIMESTAMP);
    INSERT INTO userwritesrel VALUES(userid,(SELECT MAX(REVIEWID) from sequences),about1,rating1);
    update sequences SET REVIEWID=REVIEWID+1;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `createrole`(IN rolenumber INT)
BEGIN
	INSERT INTO role VALUES(rolenumber);
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deletegamefromid`(IN gameid INT)
BEGIN
DELETE FROM games WHERE game_id = gameid;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `showsequences`()
BEGIN
	SELECT * from sequences;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updategames`(IN gameid INT,IN gamename VARCHAR(45),IN gamefirm VARCHAR(45), IN rating1 INT, IN gametype1 VARCHAR(45))
BEGIN
UPDATE games
SET game_name = gamename, game_firm = gamefirm, rating = rating1, gametype = gametype1
WHERE game_id = gameid;
END ;;
DELIMITER ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `userregister`(IN mail1 VARCHAR(45),IN password1 VARCHAR(45),IN username1 VARCHAR(45),IN dob VARCHAR(45),
IN usernick VARCHAR(45),IN roletype INT)
BEGIN
	INSERT INTO user VALUES(mail1,password1,username1,dob);
    INSERT INTO general_user VALUES((SELECT MAX(USERID) from sequences),usernick,roletype,mail1);
    UPDATE sequences SET USERID=USERID+1;
END ;;
DELIMITER ;



-- TRIGGERS

DELIMITER ;;

INSERT INTO takerolerel VALUES (NEW.role, NEW.usermail);

END */;;
DELIMITER ;


DELIMITER ;;
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

/*
Since we used MySQL we couldnt use these triggers,but we used sequences
---------------------------------------------------
CREATE SEQUENCE game_id_seq START WITH 1;
CREATE SEQUENCE mod_id_seq START WITH 1;
CREATE SEQUENCE movie_id_seq START WITH 1;
CREATE SEQUENCE series_id_seq START WITH 1;
CREATE SEQUENCE user_id_seq START WITH 1;
CREATE SEQUENCE writer_id_seq START WITH 1;
CREATE SEQUENCE music_id_seq START WITH 1;
CREATE SEQUENCE admin_id_seq START WITH 1;
CREATE SEQUENCE review_id_seq START WITH 1



CREATE OR REPLACE TRIGGER addgame_trig
BEFORE INSERT
ON games
FOR EACH ROW
BEGIN
  SELECT game_id_seq.nextval
  INTO :NEW.game_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addmoderator_trig
BEFORE INSERT
ON moderator
FOR EACH ROW
BEGIN
  SELECT mod_id_seq.nextval
  INTO :NEW.mod_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addmovies_trig
BEFORE INSERT
ON movies
FOR EACH ROW
BEGIN
  SELECT movie_id_seq.nextval
  INTO :NEW.movie_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addseries_trig
BEFORE INSERT
ON series
FOR EACH ROW
BEGIN
  SELECT series_id_seq.nextval
  INTO :NEW.series_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER adduser_trig
BEFORE INSERT
ON general_user
FOR EACH ROW
BEGIN
  SELECT user_id_seq.nextval
  INTO :NEW.user_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addnewswriter_trig
BEFORE INSERT
ON news_writer
FOR EACH ROW
BEGIN
  SELECT writer_id_seq.nextval
  INTO :NEW.writer_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addmusic_trig
BEFORE INSERT
ON music
FOR EACH ROW
BEGIN
  SELECT music_id_seq.nextval
  INTO :NEW.music_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER addsystemadmin_trig
BEFORE INSERT
ON system_admin
FOR EACH ROW
BEGIN
  SELECT admin_id_seq.nextval
  INTO :NEW.admin_id
  FROM dual;
END;
/

CREATE OR REPLACE TRIGGER adduserreview_trig
BEFORE INSERT
ON user_review
FOR EACH ROW
BEGIN
  SELECT review_id_seq.nextval
  INTO :NEW.review_id
  FROM dual;
END;
/
*/
