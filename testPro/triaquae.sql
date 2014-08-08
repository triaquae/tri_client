-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (x86_64)
--
-- Host: 10.168.0.218    Database: triaquae
-- ------------------------------------------------------
-- Server version	5.1.71

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add idc',7,'add_idc'),(20,'Can change idc',7,'change_idc'),(21,'Can delete idc',7,'delete_idc'),(22,'Can add group',8,'add_group'),(23,'Can change group',8,'change_group'),(24,'Can delete group',8,'delete_group'),(25,'Can add ip',9,'add_ip'),(26,'Can change ip',9,'change_ip'),(27,'Can delete ip',9,'delete_ip'),(28,'Can add remote user',10,'add_remoteuser'),(29,'Can change remote user',10,'change_remoteuser'),(30,'Can delete remote user',10,'delete_remoteuser'),(31,'Can add triaquae user',11,'add_triaquaeuser'),(32,'Can change triaquae user',11,'change_triaquaeuser'),(33,'Can delete triaquae user',11,'delete_triaquaeuser'),(34,'Can add auth by ip and remote user',12,'add_authbyipandremoteuser'),(35,'Can change auth by ip and remote user',12,'change_authbyipandremoteuser'),(36,'Can delete auth by ip and remote user',12,'delete_authbyipandremoteuser'),(37,'Can add server status',13,'add_serverstatus'),(38,'Can change server status',13,'change_serverstatus'),(39,'Can delete server status',13,'delete_serverstatus'),(40,'Can add ops log',14,'add_opslog'),(41,'Can change ops log',14,'change_opslog'),(42,'Can delete ops log',14,'delete_opslog'),(43,'Can add ops log temp',15,'add_opslogtemp'),(44,'Can change ops log temp',15,'change_opslogtemp'),(45,'Can delete ops log temp',15,'delete_opslogtemp'),(46,'Can add quick link',16,'add_quicklink'),(47,'Can change quick link',16,'change_quicklink'),(48,'Can delete quick link',16,'delete_quicklink'),(49,'Can add trunk_servers',17,'add_trunk_servers'),(50,'Can change trunk_servers',17,'change_trunk_servers'),(51,'Can delete trunk_servers',17,'delete_trunk_servers'),(52,'Can add templates',18,'add_templates'),(53,'Can change templates',18,'change_templates'),(54,'Can delete templates',18,'delete_templates'),(55,'Can add services',19,'add_services'),(56,'Can change services',19,'change_services'),(57,'Can delete services',19,'delete_services'),(58,'Can add items',20,'add_items'),(59,'Can change items',20,'change_items'),(60,'Can delete items',20,'delete_items'),(61,'Can add triggers',21,'add_triggers'),(62,'Can change triggers',21,'change_triggers'),(63,'Can delete triggers',21,'delete_triggers'),(64,'Can add graphs',22,'add_graphs'),(65,'Can change graphs',22,'change_graphs'),(66,'Can delete graphs',22,'delete_graphs'),(67,'Can add actions',23,'add_actions'),(68,'Can change actions',23,'change_actions'),(69,'Can delete actions',23,'delete_actions'),(70,'Can add conditions',24,'add_conditions'),(71,'Can change conditions',24,'change_conditions'),(72,'Can delete conditions',24,'delete_conditions'),(73,'Can add operations',25,'add_operations'),(74,'Can change operations',25,'change_operations'),(75,'Can delete operations',25,'delete_operations'),(76,'Can add migration history',26,'add_migrationhistory'),(77,'Can change migration history',26,'change_migrationhistory'),(78,'Can delete migration history',26,'delete_migrationhistory');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$9ZV0tFW2VP9c$uUEEXEDdb9uIlfw0pg4LHropP873tsdk/zQ1DymL/RY=','2014-07-30 07:15:26',1,'admin','','','zxbjob@126.com',1,1,'2014-06-27 09:11:04');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-06-27 09:35:21',1,20,'1','cpu_idle',1,''),(2,'2014-06-27 09:36:16',1,20,'2','cpu_system_use',1,''),(3,'2014-06-27 09:36:26',1,20,'1','cpu_idle',2,'Changed key.'),(4,'2014-06-27 09:36:49',1,20,'3','cpu_iowait',1,''),(5,'2014-06-27 09:37:09',1,20,'4','cpu_status',1,''),(6,'2014-06-27 09:37:37',1,20,'5','cpu_user_use',1,''),(7,'2014-06-27 09:38:12',1,20,'6','mem_total',1,''),(8,'2014-06-27 09:38:28',1,20,'7','mem_usage',1,''),(9,'2014-06-27 09:39:06',1,20,'8','mem_cache_size',1,''),(10,'2014-06-27 09:39:26',1,20,'9','mem_free',1,''),(11,'2014-06-27 09:40:03',1,19,'1','CPU',1,''),(12,'2014-06-27 09:40:22',1,19,'2','MEM',1,''),(13,'2014-06-27 09:41:32',1,7,'1','BJ',1,''),(14,'2014-06-27 09:41:37',1,7,'2','SJZ',1,''),(15,'2014-06-27 09:42:17',1,18,'1','Templates',1,''),(16,'2014-06-27 09:42:21',1,8,'1','BJ_SJZ',1,''),(17,'2014-06-27 09:43:04',1,18,'2','mytemplt',1,''),(18,'2014-06-27 09:43:07',1,9,'1','localhsot',1,''),(19,'2014-06-27 09:43:33',1,18,'3','Linux Templat',1,''),(20,'2014-06-27 09:43:45',1,18,'3','Linux Template',2,'Changed name.'),(21,'2014-06-27 09:44:07',1,18,'2','Local template',2,'Changed name.'),(22,'2014-06-30 00:38:07',1,18,'4','Win Templates',1,''),(23,'2014-06-30 00:38:18',1,8,'2','BJ_WIN_TEST',1,''),(24,'2014-06-30 00:39:16',1,9,'2','zxb_win32_test',1,''),(25,'2014-06-30 00:39:51',1,19,'2','MEM',2,'Changed check_interval.'),(26,'2014-06-30 00:40:40',1,18,'3','Linux Template',2,'No fields changed.'),(27,'2014-06-30 01:09:58',1,21,'1','CPU_trigger',1,''),(28,'2014-06-30 01:59:11',1,19,'1','CPU',2,'Changed trigger.'),(29,'2014-06-30 06:11:02',1,9,'1','localhost',2,'Changed display_name and template_list.'),(30,'2014-06-30 06:12:04',1,19,'1','CPU',2,'Changed plugin.'),(31,'2014-06-30 06:19:05',1,17,'1','Servers',1,''),(32,'2014-06-30 06:19:45',1,17,'2','bj_proxy',1,''),(33,'2014-06-30 06:22:53',1,9,'2','zxb_win32_test',2,'Changed belongs_to.'),(34,'2014-06-30 06:23:00',1,9,'1','localhost',2,'Changed belongs_to.'),(35,'2014-06-30 10:11:21',1,21,'2','MEM trigger',1,''),(36,'2014-06-30 10:11:31',1,19,'2','MEM',2,'Changed trigger.'),(37,'2014-07-01 01:00:25',1,10,'1','zxb',1,''),(38,'2014-07-01 01:00:49',1,11,'1','admin',1,''),(39,'2014-07-01 01:01:04',1,11,'2','admin',1,''),(40,'2014-07-08 09:46:01',1,9,'3','alex_test_server  haha',1,''),(41,'2014-07-09 01:54:21',1,17,'1','Servers',2,'Changed ip_address.'),(42,'2014-07-09 01:56:05',1,9,'3','alex_test_server  haha',2,'Changed belongs_to.'),(43,'2014-07-09 07:28:35',1,19,'2','MEM',2,'Changed check_interval.'),(44,'2014-07-10 02:38:19',1,20,'9','mem_free',2,'Changed key.'),(45,'2014-07-10 02:39:15',1,20,'9','mem_free',2,'Changed key.'),(46,'2014-07-10 03:01:07',1,20,'9','mem_free',2,'Changed key.'),(47,'2014-07-10 03:01:19',1,20,'8','mem_cache_size',2,'Changed key.'),(48,'2014-07-10 03:01:35',1,20,'7','mem_usage',2,'Changed key.'),(49,'2014-07-10 03:01:56',1,20,'6','mem_total',2,'Changed key.'),(50,'2014-07-10 03:18:05',1,19,'2','MEM',2,'Changed trigger.'),(51,'2014-07-10 06:20:13',1,21,'1','CPU_trigger',2,'Changed expression.'),(52,'2014-07-10 06:41:05',1,21,'2','MEM trigger',2,'Changed expression.'),(53,'2014-07-10 06:56:46',1,21,'1','CPU_trigger',2,'Changed expression.'),(54,'2014-07-10 06:57:08',1,21,'2','MEM trigger',2,'Changed expression.'),(55,'2014-07-10 08:16:06',1,21,'1','CPU_trigger',2,'Changed expression.'),(56,'2014-07-10 08:16:23',1,21,'2','MEM trigger',2,'Changed expression.'),(57,'2014-07-23 05:43:46',1,9,'4','163',1,''),(58,'2014-07-24 02:30:39',1,9,'4','163',2,'Changed belongs_to.'),(59,'2014-08-06 05:39:17',1,21,'1','CPU_trigger',2,'Changed expression.'),(60,'2014-08-06 05:39:30',1,21,'2','MEM trigger',2,'Changed expression.'),(61,'2014-08-06 05:43:35',1,21,'1','CPU_trigger',2,'Changed expression.'),(62,'2014-08-06 05:57:23',1,19,'2','MEM',2,'Changed trigger.'),(63,'2014-08-06 05:59:13',1,18,'4','Win Templates',2,'No fields changed.'),(64,'2014-08-06 06:02:39',1,9,'2','zxb_win32_test',2,'Changed group.'),(65,'2014-08-06 06:02:51',1,9,'1','localhost',2,'Changed group and template_list.'),(66,'2014-08-06 06:35:52',1,21,'1','CPU_trigger',2,'Changed expression.'),(67,'2014-08-06 08:17:22',1,21,'1','CPU_trigger',2,'Changed expression.'),(68,'2014-08-06 08:44:07',1,21,'2','MEM trigger',2,'Changed expression.'),(69,'2014-08-06 08:44:56',1,21,'1','CPU_trigger',2,'Changed expression.'),(70,'2014-08-06 08:46:23',1,21,'1','CPU_trigger',2,'Changed expression.'),(71,'2014-08-06 09:14:31',1,21,'1','CPU_trigger',2,'Changed expression.'),(72,'2014-08-06 09:15:01',1,21,'1','CPU_trigger',2,'Changed expression.'),(73,'2014-08-06 09:24:10',1,21,'1','CPU_trigger',2,'Changed expression.'),(74,'2014-08-06 09:26:10',1,21,'1','CPU_trigger',2,'Changed expression.'),(75,'2014-08-06 09:31:57',1,21,'1','CPU_trigger',2,'Changed expression.'),(76,'2014-08-06 09:32:46',1,21,'1','CPU_trigger',2,'Changed expression.'),(77,'2014-08-06 09:43:33',1,21,'1','CPU_trigger',2,'Changed expression.'),(78,'2014-08-06 09:44:10',1,21,'1','CPU_trigger',2,'Changed expression.'),(79,'2014-08-06 09:46:00',1,21,'1','CPU_trigger',2,'Changed expression.'),(80,'2014-08-07 10:00:15',1,9,'1','10.168.0.218',2,'Changed display_name.'),(81,'2014-08-07 10:00:21',1,9,'1','10.168.0.218',2,'Changed template_list.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'idc','triWeb','idc'),(8,'group','triWeb','group'),(9,'ip','triWeb','ip'),(10,'remote user','triWeb','remoteuser'),(11,'triaquae user','triWeb','triaquaeuser'),(12,'auth by ip and remote user','triWeb','authbyipandremoteuser'),(13,'server status','triWeb','serverstatus'),(14,'ops log','triWeb','opslog'),(15,'ops log temp','triWeb','opslogtemp'),(16,'quick link','triWeb','quicklink'),(17,'trunk_servers','triWeb','trunk_servers'),(18,'templates','triWeb','templates'),(19,'services','triWeb','services'),(20,'items','triWeb','items'),(21,'triggers','triWeb','triggers'),(22,'graphs','triWeb','graphs'),(23,'actions','triWeb','actions'),(24,'conditions','triWeb','conditions'),(25,'operations','triWeb','operations'),(26,'migration history','south','migrationhistory');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('voieknepunc2m4gk7xhvnwpef3bmrojy','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-16 07:23:34'),('2xzsrqpjgygr9kfdr5l1l3cjziygjsqy','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-11 09:31:41'),('9g4m1pth45zs2m6ncqjb8worumct8z7a','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-22 09:45:29'),('m2biuuzbhinvjdluipt2vhuve0ylm3sw','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-08-06 05:41:25'),('18gj3173bat99v5gfmljcydyhkunyt7d','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-07-22 10:23:57'),('snbcau8ri6cgeq2nih1u1bc7i8p5j8i7','NTM1ODVkMjZmMTFkOTY3NDU0NmZjYTY3MzkxMGIyMGJmY2M3ZmNjNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-08-13 07:15:26');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'triWeb','0001_initial','2014-07-10 06:23:27'),(2,'triWeb','0002_auto__chg_field_triggers_expression','2014-07-10 06:23:54');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_actions`
--

DROP TABLE IF EXISTS `triWeb_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_actions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(250) NOT NULL,
  `recovery_notice` tinyint(1) NOT NULL,
  `recovery_subject` varchar(100) NOT NULL,
  `recovery_message` varchar(250) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_actions`
--

LOCK TABLES `triWeb_actions` WRITE;
/*!40000 ALTER TABLE `triWeb_actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_actions_condition_list`
--

DROP TABLE IF EXISTS `triWeb_actions_condition_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_actions_condition_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actions_id` int(11) NOT NULL,
  `conditions_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `actions_id` (`actions_id`,`conditions_id`),
  KEY `triWeb_actions_condition_list_5cb7c89d` (`actions_id`),
  KEY `triWeb_actions_condition_list_342389ec` (`conditions_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_actions_condition_list`
--

LOCK TABLES `triWeb_actions_condition_list` WRITE;
/*!40000 ALTER TABLE `triWeb_actions_condition_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_actions_condition_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_actions_operation_list`
--

DROP TABLE IF EXISTS `triWeb_actions_operation_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_actions_operation_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actions_id` int(11) NOT NULL,
  `operations_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `actions_id` (`actions_id`,`operations_id`),
  KEY `triWeb_actions_operation_list_5cb7c89d` (`actions_id`),
  KEY `triWeb_actions_operation_list_4a6fb3e3` (`operations_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_actions_operation_list`
--

LOCK TABLES `triWeb_actions_operation_list` WRITE;
/*!40000 ALTER TABLE `triWeb_actions_operation_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_actions_operation_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_authbyipandremoteuser`
--

DROP TABLE IF EXISTS `triWeb_authbyipandremoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_authbyipandremoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(1024) NOT NULL,
  `authtype` varchar(100) NOT NULL,
  `ip_id` int(11) DEFAULT NULL,
  `remoteUser_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`remoteUser_id`),
  KEY `triWeb_authbyipandremoteuser_6259660e` (`ip_id`),
  KEY `triWeb_authbyipandremoteuser_7d22bda5` (`remoteUser_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_authbyipandremoteuser`
--

LOCK TABLES `triWeb_authbyipandremoteuser` WRITE;
/*!40000 ALTER TABLE `triWeb_authbyipandremoteuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_authbyipandremoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_conditions`
--

DROP TABLE IF EXISTS `triWeb_conditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_conditions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `condition_type` varchar(100) NOT NULL,
  `operator` varchar(30) NOT NULL,
  `value` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_conditions`
--

LOCK TABLES `triWeb_conditions` WRITE;
/*!40000 ALTER TABLE `triWeb_conditions` DISABLE KEYS */;
INSERT INTO `triWeb_conditions` VALUES (1,'io_high','80','?','0');
/*!40000 ALTER TABLE `triWeb_conditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_graphs`
--

DROP TABLE IF EXISTS `triWeb_graphs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_graphs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `graph_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_graphs`
--

LOCK TABLES `triWeb_graphs` WRITE;
/*!40000 ALTER TABLE `triWeb_graphs` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_graphs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_graphs_datasets`
--

DROP TABLE IF EXISTS `triWeb_graphs_datasets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_graphs_datasets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `graphs_id` int(11) NOT NULL,
  `items_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `graphs_id` (`graphs_id`,`items_id`),
  KEY `triWeb_graphs_datasets_23a07432` (`graphs_id`),
  KEY `triWeb_graphs_datasets_84245b2c` (`items_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_graphs_datasets`
--

LOCK TABLES `triWeb_graphs_datasets` WRITE;
/*!40000 ALTER TABLE `triWeb_graphs_datasets` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_graphs_datasets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_group`
--

DROP TABLE IF EXISTS `triWeb_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_group`
--

LOCK TABLES `triWeb_group` WRITE;
/*!40000 ALTER TABLE `triWeb_group` DISABLE KEYS */;
INSERT INTO `triWeb_group` VALUES (1,'BJ_SJZ','BJ_SJZ'),(2,'BJ_WIN','BJ_WIN_TEST');
/*!40000 ALTER TABLE `triWeb_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_group_template_list`
--

DROP TABLE IF EXISTS `triWeb_group_template_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_group_template_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `templates_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`templates_id`),
  KEY `triWeb_group_template_list_5f412f9a` (`group_id`),
  KEY `triWeb_group_template_list_82c5b592` (`templates_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_group_template_list`
--

LOCK TABLES `triWeb_group_template_list` WRITE;
/*!40000 ALTER TABLE `triWeb_group_template_list` DISABLE KEYS */;
INSERT INTO `triWeb_group_template_list` VALUES (1,1,1),(2,2,4);
/*!40000 ALTER TABLE `triWeb_group_template_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_idc`
--

DROP TABLE IF EXISTS `triWeb_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_idc`
--

LOCK TABLES `triWeb_idc` WRITE;
/*!40000 ALTER TABLE `triWeb_idc` DISABLE KEYS */;
INSERT INTO `triWeb_idc` VALUES (1,'BJ'),(2,'SJZ');
/*!40000 ALTER TABLE `triWeb_idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_ip`
--

DROP TABLE IF EXISTS `triWeb_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(50) NOT NULL,
  `display_name` varchar(50) NOT NULL,
  `ip` char(15) NOT NULL,
  `belongs_to_id` int(11) DEFAULT NULL,
  `idc_id` int(11) DEFAULT NULL,
  `port` int(11) NOT NULL,
  `os` varchar(20) NOT NULL,
  `status_monitor_on` tinyint(1) NOT NULL,
  `snmp_on` tinyint(1) NOT NULL,
  `snmp_version` varchar(10) NOT NULL,
  `snmp_community_name` varchar(50) NOT NULL,
  `snmp_security_level` varchar(50) NOT NULL,
  `snmp_auth_protocol` varchar(50) NOT NULL,
  `snmp_user` varchar(50) NOT NULL,
  `snmp_pass` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`),
  UNIQUE KEY `display_name` (`display_name`),
  UNIQUE KEY `ip` (`ip`),
  KEY `triWeb_ip_c6404542` (`belongs_to_id`),
  KEY `triWeb_ip_7f604875` (`idc_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_ip`
--

LOCK TABLES `triWeb_ip` WRITE;
/*!40000 ALTER TABLE `triWeb_ip` DISABLE KEYS */;
INSERT INTO `triWeb_ip` VALUES (1,'host218','10.168.0.218','10.168.0.218',1,1,22,'linux',1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass'),(2,'zxb_win32','zxb_win32_test','10.168.7.50',1,1,22,'linux',1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass'),(3,'alex_test_server','alex_test_server  haha','10.168.7.161',1,NULL,22,'linux',1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass'),(4,'puppet.lzb.com','163','10.168.0.163',1,1,22,'linux',1,1,'2c','public','auth','MD5','triaquae_snmp','my_pass');
/*!40000 ALTER TABLE `triWeb_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_ip_custom_services`
--

DROP TABLE IF EXISTS `triWeb_ip_custom_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_ip_custom_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_id` int(11) NOT NULL,
  `services_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`services_id`),
  KEY `triWeb_ip_custom_services_6259660e` (`ip_id`),
  KEY `triWeb_ip_custom_services_52f10e7c` (`services_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_ip_custom_services`
--

LOCK TABLES `triWeb_ip_custom_services` WRITE;
/*!40000 ALTER TABLE `triWeb_ip_custom_services` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_ip_custom_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_ip_group`
--

DROP TABLE IF EXISTS `triWeb_ip_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_ip_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`group_id`),
  KEY `triWeb_ip_group_6259660e` (`ip_id`),
  KEY `triWeb_ip_group_5f412f9a` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_ip_group`
--

LOCK TABLES `triWeb_ip_group` WRITE;
/*!40000 ALTER TABLE `triWeb_ip_group` DISABLE KEYS */;
INSERT INTO `triWeb_ip_group` VALUES (7,3,1);
/*!40000 ALTER TABLE `triWeb_ip_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_ip_template_list`
--

DROP TABLE IF EXISTS `triWeb_ip_template_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_ip_template_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_id` int(11) NOT NULL,
  `templates_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_id` (`ip_id`,`templates_id`),
  KEY `triWeb_ip_template_list_6259660e` (`ip_id`),
  KEY `triWeb_ip_template_list_82c5b592` (`templates_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_ip_template_list`
--

LOCK TABLES `triWeb_ip_template_list` WRITE;
/*!40000 ALTER TABLE `triWeb_ip_template_list` DISABLE KEYS */;
INSERT INTO `triWeb_ip_template_list` VALUES (9,3,3),(10,1,3);
/*!40000 ALTER TABLE `triWeb_ip_template_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_items`
--

DROP TABLE IF EXISTS `triWeb_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `key` varchar(100) NOT NULL,
  `data_type` varchar(50) NOT NULL,
  `unit` varchar(30) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `key` (`key`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_items`
--

LOCK TABLES `triWeb_items` WRITE;
/*!40000 ALTER TABLE `triWeb_items` DISABLE KEYS */;
INSERT INTO `triWeb_items` VALUES (1,'cpu_idle','cpu.idle','float','%',1),(2,'cpu_system_use','cpu.system','float','%',1),(3,'cpu_iowait','cpu.iowait','float','%',1),(4,'cpu_status','cpu.status','integer','%',1),(5,'cpu_user_use','cpu.use','float','%',1),(6,'mem_total','MemTotal','float','%',1),(7,'mem_usage','MemUsage','float','%',1),(8,'mem_cache_size','Cached','float','%',1),(9,'mem_free','MemFree','float','%',1);
/*!40000 ALTER TABLE `triWeb_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_operations`
--

DROP TABLE IF EXISTS `triWeb_operations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_operations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `send_via` varchar(30) NOT NULL,
  `notice_times` int(11) NOT NULL,
  `notice_interval` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_operations`
--

LOCK TABLES `triWeb_operations` WRITE;
/*!40000 ALTER TABLE `triWeb_operations` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_operations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_operations_send_to_groups`
--

DROP TABLE IF EXISTS `triWeb_operations_send_to_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_operations_send_to_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `operations_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operations_id` (`operations_id`,`group_id`),
  KEY `triWeb_operations_send_to_groups_4a6fb3e3` (`operations_id`),
  KEY `triWeb_operations_send_to_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_operations_send_to_groups`
--

LOCK TABLES `triWeb_operations_send_to_groups` WRITE;
/*!40000 ALTER TABLE `triWeb_operations_send_to_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_operations_send_to_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_operations_send_to_users`
--

DROP TABLE IF EXISTS `triWeb_operations_send_to_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_operations_send_to_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `operations_id` int(11) NOT NULL,
  `triaquaeuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operations_id` (`operations_id`,`triaquaeuser_id`),
  KEY `triWeb_operations_send_to_users_4a6fb3e3` (`operations_id`),
  KEY `triWeb_operations_send_to_users_01383dc4` (`triaquaeuser_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_operations_send_to_users`
--

LOCK TABLES `triWeb_operations_send_to_users` WRITE;
/*!40000 ALTER TABLE `triWeb_operations_send_to_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_operations_send_to_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_opslog`
--

DROP TABLE IF EXISTS `triWeb_opslog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_opslog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` datetime NOT NULL,
  `finish_date` datetime DEFAULT NULL,
  `log_type` varchar(50) NOT NULL,
  `tri_user` varchar(30) NOT NULL,
  `run_user` varchar(30) NOT NULL,
  `cmd` longtext NOT NULL,
  `total_task` int(11) NOT NULL,
  `success_num` int(11) NOT NULL,
  `failed_num` int(11) NOT NULL,
  `track_mark` int(11) NOT NULL,
  `note` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `track_mark` (`track_mark`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_opslog`
--

LOCK TABLES `triWeb_opslog` WRITE;
/*!40000 ALTER TABLE `triWeb_opslog` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_opslog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_opslogtemp`
--

DROP TABLE IF EXISTS `triWeb_opslogtemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_opslogtemp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `user` varchar(30) NOT NULL,
  `ip` char(15) NOT NULL,
  `event_type` varchar(50) NOT NULL,
  `cmd` longtext NOT NULL,
  `event_log` longtext NOT NULL,
  `result` varchar(30) NOT NULL,
  `track_mark` int(11) NOT NULL,
  `note` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_opslogtemp`
--

LOCK TABLES `triWeb_opslogtemp` WRITE;
/*!40000 ALTER TABLE `triWeb_opslogtemp` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_opslogtemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_quicklink`
--

DROP TABLE IF EXISTS `triWeb_quicklink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_quicklink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link_name` varchar(50) NOT NULL,
  `url` varchar(200) NOT NULL,
  `color` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_quicklink`
--

LOCK TABLES `triWeb_quicklink` WRITE;
/*!40000 ALTER TABLE `triWeb_quicklink` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_quicklink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_remoteuser`
--

DROP TABLE IF EXISTS `triWeb_remoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_remoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_remoteuser`
--

LOCK TABLES `triWeb_remoteuser` WRITE;
/*!40000 ALTER TABLE `triWeb_remoteuser` DISABLE KEYS */;
INSERT INTO `triWeb_remoteuser` VALUES (1,'zxb');
/*!40000 ALTER TABLE `triWeb_remoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_serverstatus`
--

DROP TABLE IF EXISTS `triWeb_serverstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_serverstatus` (
  `host` char(15) NOT NULL,
  `hostname` varchar(100) NOT NULL,
  `host_status` varchar(10) NOT NULL,
  `ping_status` varchar(100) NOT NULL,
  `last_check` varchar(100) NOT NULL,
  `host_uptime` varchar(50) NOT NULL,
  `attempt_count` int(11) NOT NULL,
  `breakdown_count` int(11) NOT NULL,
  `up_count` int(11) NOT NULL,
  `snmp_alert_count` int(11) NOT NULL,
  `availability` varchar(20) NOT NULL,
  PRIMARY KEY (`host`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_serverstatus`
--

LOCK TABLES `triWeb_serverstatus` WRITE;
/*!40000 ALTER TABLE `triWeb_serverstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_serverstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_services`
--

DROP TABLE IF EXISTS `triWeb_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `monitor_type` varchar(50) NOT NULL,
  `plugin` varchar(100) NOT NULL,
  `trigger_id` int(11) DEFAULT NULL,
  `check_interval` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `triWeb_services_9b771456` (`trigger_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_services`
--

LOCK TABLES `triWeb_services` WRITE;
/*!40000 ALTER TABLE `triWeb_services` DISABLE KEYS */;
INSERT INTO `triWeb_services` VALUES (1,'CPU','agent','plugins.cpu',1,30),(2,'MEM','agent','plugins.mem',2,15);
/*!40000 ALTER TABLE `triWeb_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_services_item_list`
--

DROP TABLE IF EXISTS `triWeb_services_item_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_services_item_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `services_id` int(11) NOT NULL,
  `items_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `services_id` (`services_id`,`items_id`),
  KEY `triWeb_services_item_list_52f10e7c` (`services_id`),
  KEY `triWeb_services_item_list_84245b2c` (`items_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_services_item_list`
--

LOCK TABLES `triWeb_services_item_list` WRITE;
/*!40000 ALTER TABLE `triWeb_services_item_list` DISABLE KEYS */;
INSERT INTO `triWeb_services_item_list` VALUES (19,1,1),(20,1,2),(21,1,3),(22,1,4),(23,1,5),(37,2,9),(36,2,8),(39,2,7),(38,2,6);
/*!40000 ALTER TABLE `triWeb_services_item_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_templates`
--

DROP TABLE IF EXISTS `triWeb_templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_templates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_templates`
--

LOCK TABLES `triWeb_templates` WRITE;
/*!40000 ALTER TABLE `triWeb_templates` DISABLE KEYS */;
INSERT INTO `triWeb_templates` VALUES (1,'Templates'),(2,'Local template'),(3,'Linux Template'),(4,'Win Templates');
/*!40000 ALTER TABLE `triWeb_templates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_templates_graph_list`
--

DROP TABLE IF EXISTS `triWeb_templates_graph_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_templates_graph_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `templates_id` int(11) NOT NULL,
  `graphs_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `templates_id` (`templates_id`,`graphs_id`),
  KEY `triWeb_templates_graph_list_82c5b592` (`templates_id`),
  KEY `triWeb_templates_graph_list_23a07432` (`graphs_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_templates_graph_list`
--

LOCK TABLES `triWeb_templates_graph_list` WRITE;
/*!40000 ALTER TABLE `triWeb_templates_graph_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_templates_graph_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_templates_service_list`
--

DROP TABLE IF EXISTS `triWeb_templates_service_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_templates_service_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `templates_id` int(11) NOT NULL,
  `services_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `templates_id` (`templates_id`,`services_id`),
  KEY `triWeb_templates_service_list_82c5b592` (`templates_id`),
  KEY `triWeb_templates_service_list_52f10e7c` (`services_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_templates_service_list`
--

LOCK TABLES `triWeb_templates_service_list` WRITE;
/*!40000 ALTER TABLE `triWeb_templates_service_list` DISABLE KEYS */;
INSERT INTO `triWeb_templates_service_list` VALUES (1,1,1),(10,2,1),(15,3,1),(16,3,2),(19,4,1),(20,4,2);
/*!40000 ALTER TABLE `triWeb_templates_service_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_triaquaeuser`
--

DROP TABLE IF EXISTS `triWeb_triaquaeuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_triaquaeuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `triWeb_triaquaeuser_6340c63c` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_triaquaeuser`
--

LOCK TABLES `triWeb_triaquaeuser` WRITE;
/*!40000 ALTER TABLE `triWeb_triaquaeuser` DISABLE KEYS */;
INSERT INTO `triWeb_triaquaeuser` VALUES (1,1,'zxbjob@126.com'),(2,1,'zxbjob@126.com');
/*!40000 ALTER TABLE `triWeb_triaquaeuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_triaquaeuser_group`
--

DROP TABLE IF EXISTS `triWeb_triaquaeuser_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_triaquaeuser_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`group_id`),
  KEY `triWeb_triaquaeuser_group_01383dc4` (`triaquaeuser_id`),
  KEY `triWeb_triaquaeuser_group_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_triaquaeuser_group`
--

LOCK TABLES `triWeb_triaquaeuser_group` WRITE;
/*!40000 ALTER TABLE `triWeb_triaquaeuser_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_triaquaeuser_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_triaquaeuser_ip`
--

DROP TABLE IF EXISTS `triWeb_triaquaeuser_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_triaquaeuser_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `ip_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`ip_id`),
  KEY `triWeb_triaquaeuser_ip_01383dc4` (`triaquaeuser_id`),
  KEY `triWeb_triaquaeuser_ip_6259660e` (`ip_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_triaquaeuser_ip`
--

LOCK TABLES `triWeb_triaquaeuser_ip` WRITE;
/*!40000 ALTER TABLE `triWeb_triaquaeuser_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `triWeb_triaquaeuser_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_triaquaeuser_remoteuser`
--

DROP TABLE IF EXISTS `triWeb_triaquaeuser_remoteuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_triaquaeuser_remoteuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `triaquaeuser_id` int(11) NOT NULL,
  `remoteuser_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `triaquaeuser_id` (`triaquaeuser_id`,`remoteuser_id`),
  KEY `triWeb_triaquaeuser_remoteuser_01383dc4` (`triaquaeuser_id`),
  KEY `triWeb_triaquaeuser_remoteuser_29e729b2` (`remoteuser_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_triaquaeuser_remoteuser`
--

LOCK TABLES `triWeb_triaquaeuser_remoteuser` WRITE;
/*!40000 ALTER TABLE `triWeb_triaquaeuser_remoteuser` DISABLE KEYS */;
INSERT INTO `triWeb_triaquaeuser_remoteuser` VALUES (1,1,1);
/*!40000 ALTER TABLE `triWeb_triaquaeuser_remoteuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_triggers`
--

DROP TABLE IF EXISTS `triWeb_triggers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_triggers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `expression` longtext NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_triggers`
--

LOCK TABLES `triWeb_triggers` WRITE;
/*!40000 ALTER TABLE `triWeb_triggers` DISABLE KEYS */;
INSERT INTO `triWeb_triggers` VALUES (1,'CPU_trigger','{\"Information\": [], \"Problem\": [{\"mintues\": 5, \"value\": \"100\", \"handler\": \"avg\", \"logic\": \"AND\", \"operator\": \"<\", \"item_key\": \"idle\"}, {\"mintues\": 5, \"value\": \"25\", \"handler\": \"avg\", \"logic\": \"AND\", \"operator\": \">\", \"item_key\": \"iowait\"}, {\"mintues\": 5, \"value\": \"80\", \"handler\": \"avg\", \"logic\": null, \"operator\": \">\", \"item_key\": \"system\"}], \"Warning\": [], \"Disaster\": [], \"Urgent\": []}','CPU_trigger'),(2,'MEM trigger','{\"Information\": [], \"Problem\": [{\"mintues\": 5, \"value\": \"15\", \"handler\": \"avg\", \"logic\": \"else\", \"operator\": \"<\", \"item_key\": \"MemFree\"}, {\"mintues\": 5, \"value\": \"85\", \"handler\": \"avg\", \"logic\": null, \"operator\": \">\", \"item_key\": \"MemUsage\"}], \"Warning\": [{\"mintues\": 5, \"value\": \"30\", \"handler\": \"avg\", \"logic\": \"||\", \"operator\": \"<\", \"item_key\": \"MemFree\"}, {\"mintues\": 5, \"value\": \"70\", \"handler\": \"avg\", \"logic\": null, \"operator\": \">\", \"item_key\": \"MemUsage\"}], \"Disaster\": [{\"mintues\": 5, \"value\": \"10\", \"handler\": \"avg\", \"logic\": \"&\", \"operator\": \"<\", \"item_key\": \"MemFree\"}, {\"mintues\": 5, \"value\": \"90\", \"handler\": \"avg\", \"logic\": null, \"operator\": \"<\", \"item_key\": \"MemUsage\"}], \"Urgent\": []}','MEM_trigger');
/*!40000 ALTER TABLE `triWeb_triggers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `triWeb_trunk_servers`
--

DROP TABLE IF EXISTS `triWeb_trunk_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `triWeb_trunk_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(150) NOT NULL,
  `ip_address` char(15) NOT NULL,
  `port` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `triWeb_trunk_servers`
--

LOCK TABLES `triWeb_trunk_servers` WRITE;
/*!40000 ALTER TABLE `triWeb_trunk_servers` DISABLE KEYS */;
INSERT INTO `triWeb_trunk_servers` VALUES (1,'Servers','Master Server','10.168.7.161',9998),(2,'bj_proxy','BJ_Proxy','10.168.7.108',9998);
/*!40000 ALTER TABLE `triWeb_trunk_servers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-08-08 13:22:18
