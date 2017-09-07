-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: easedb_server
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add service center info',7,'add_servicecenterinfo'),(20,'Can change service center info',7,'change_servicecenterinfo'),(21,'Can delete service center info',7,'delete_servicecenterinfo'),(22,'Can add vehicle models',8,'add_vehiclemodels'),(23,'Can change vehicle models',8,'change_vehiclemodels'),(24,'Can delete vehicle models',8,'delete_vehiclemodels'),(25,'Can add supported car brands',9,'add_supportedcarbrands'),(26,'Can change supported car brands',9,'change_supportedcarbrands'),(27,'Can delete supported car brands',9,'delete_supportedcarbrands'),(28,'Can add scheduled services',10,'add_scheduledservices'),(29,'Can change scheduled services',10,'change_scheduledservices'),(30,'Can delete scheduled services',10,'delete_scheduledservices'),(31,'Can add complaint code',11,'add_complaintcode'),(32,'Can change complaint code',11,'change_complaintcode'),(33,'Can delete complaint code',11,'delete_complaintcode'),(34,'Can add maintenance tips',12,'add_maintenancetips'),(35,'Can change maintenance tips',12,'change_maintenancetips'),(36,'Can delete maintenance tips',12,'delete_maintenancetips'),(37,'Can add scheduled service details',13,'add_scheduledservicedetails'),(38,'Can change scheduled service details',13,'change_scheduledservicedetails'),(39,'Can delete scheduled service details',13,'delete_scheduledservicedetails'),(40,'Can add vehicle reviews',14,'add_vehiclereviews'),(41,'Can change vehicle reviews',14,'change_vehiclereviews'),(42,'Can delete vehicle reviews',14,'delete_vehiclereviews'),(43,'Can add surveys',15,'add_surveys'),(44,'Can change surveys',15,'change_surveys'),(45,'Can delete surveys',15,'delete_surveys'),(46,'Can add vehicles',16,'add_vehicles'),(47,'Can change vehicles',16,'change_vehicles'),(48,'Can delete vehicles',16,'delete_vehicles'),(49,'Can add otp transaction info',17,'add_otptransactioninfo'),(50,'Can change otp transaction info',17,'change_otptransactioninfo'),(51,'Can delete otp transaction info',17,'delete_otptransactioninfo'),(52,'Can add customer',18,'add_customer'),(53,'Can change customer',18,'change_customer'),(54,'Can delete customer',18,'delete_customer'),(55,'Can add jc vehicle info',19,'add_jcvehicleinfo'),(56,'Can change jc vehicle info',19,'change_jcvehicleinfo'),(57,'Can delete jc vehicle info',19,'delete_jcvehicleinfo'),(58,'Can add emergency service booking',20,'add_emergencyservicebooking'),(59,'Can change emergency service booking',20,'change_emergencyservicebooking'),(60,'Can delete emergency service booking',20,'delete_emergencyservicebooking'),(61,'Can add jc recommended services',21,'add_jcrecommendedservices'),(62,'Can change jc recommended services',21,'change_jcrecommendedservices'),(63,'Can delete jc recommended services',21,'delete_jcrecommendedservices'),(64,'Can add jc invoice and labour cost',22,'add_jcinvoiceandlabourcost'),(65,'Can change jc invoice and labour cost',22,'change_jcinvoiceandlabourcost'),(66,'Can delete jc invoice and labour cost',22,'delete_jcinvoiceandlabourcost'),(67,'Can add jc stocks info',23,'add_jcstocksinfo'),(68,'Can change jc stocks info',23,'change_jcstocksinfo'),(69,'Can delete jc stocks info',23,'delete_jcstocksinfo'),(70,'Can add jc status',24,'add_jcstatus'),(71,'Can change jc status',24,'change_jcstatus'),(72,'Can delete jc status',24,'delete_jcstatus'),(73,'Can add c service booking',25,'add_cservicebooking'),(74,'Can change c service booking',25,'change_cservicebooking'),(75,'Can delete c service booking',25,'delete_cservicebooking'),(76,'Can add jc other stocks info',26,'add_jcotherstocksinfo'),(77,'Can change jc other stocks info',26,'change_jcotherstocksinfo'),(78,'Can delete jc other stocks info',26,'delete_jcotherstocksinfo'),(79,'Can add jc service details',27,'add_jcservicedetails'),(80,'Can change jc service details',27,'change_jcservicedetails'),(81,'Can delete jc service details',27,'delete_jcservicedetails'),(82,'Can add inventory',28,'add_inventory'),(83,'Can change inventory',28,'change_inventory'),(84,'Can delete inventory',28,'delete_inventory'),(85,'Can add Token',29,'add_token'),(86,'Can change Token',29,'change_token'),(87,'Can delete Token',29,'delete_token');
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
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
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
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_complaintcode`
--

DROP TABLE IF EXISTS `core_complaintcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_complaintcode` (
  `Code` varchar(10) NOT NULL,
  `Description` varchar(70) NOT NULL,
  `Aggregate` varchar(50) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_complaintcode`
--

LOCK TABLES `core_complaintcode` WRITE;
/*!40000 ALTER TABLE `core_complaintcode` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_complaintcode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_maintenancetips`
--

DROP TABLE IF EXISTS `core_maintenancetips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_maintenancetips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `text` longtext NOT NULL,
  `vehicle_type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_maintenancetips`
--

LOCK TABLES `core_maintenancetips` WRITE;
/*!40000 ALTER TABLE `core_maintenancetips` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_maintenancetips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_scheduledservicedetails`
--

DROP TABLE IF EXISTS `core_scheduledservicedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_scheduledservicedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ServiceIdentifier` varchar(100) NOT NULL,
  `ServiceInfo` varchar(1000) NOT NULL,
  `Parts` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_scheduledservicedetails`
--

LOCK TABLES `core_scheduledservicedetails` WRITE;
/*!40000 ALTER TABLE `core_scheduledservicedetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_scheduledservicedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_scheduledservices`
--

DROP TABLE IF EXISTS `core_scheduledservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_scheduledservices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Brand` varchar(200) NOT NULL,
  `Model` varchar(500) NOT NULL,
  `FuelType` varchar(20) NOT NULL,
  `MinKM` int(11) NOT NULL,
  `MaxKM` int(11) NOT NULL,
  `ServiceIdentifier` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_scheduledservices`
--

LOCK TABLES `core_scheduledservices` WRITE;
/*!40000 ALTER TABLE `core_scheduledservices` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_scheduledservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_servicecenterinfo`
--

DROP TABLE IF EXISTS `core_servicecenterinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_servicecenterinfo` (
  `ServiceCenterID` varchar(20) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `ContactNumber` varchar(50) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `BuildingNo` varchar(50) NOT NULL,
  `Street` varchar(200) NOT NULL,
  `Town` varchar(200) NOT NULL,
  `District` varchar(200) NOT NULL,
  `City` varchar(200) NOT NULL,
  `Pincode` varchar(20) NOT NULL,
  `OwnerName` varchar(100) NOT NULL,
  `Specialization` varchar(1000) NOT NULL,
  `Images` varchar(1000) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`ServiceCenterID`),
  KEY `core_servicecenterinfo_USER_id_5db674a3_fk_auth_user_id` (`USER_id`),
  CONSTRAINT `core_servicecenterinfo_USER_id_5db674a3_fk_auth_user_id` FOREIGN KEY (`USER_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_servicecenterinfo`
--

LOCK TABLES `core_servicecenterinfo` WRITE;
/*!40000 ALTER TABLE `core_servicecenterinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_servicecenterinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_supportedcarbrands`
--

DROP TABLE IF EXISTS `core_supportedcarbrands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_supportedcarbrands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Brand` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_supportedcarbrands`
--

LOCK TABLES `core_supportedcarbrands` WRITE;
/*!40000 ALTER TABLE `core_supportedcarbrands` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_supportedcarbrands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_surveys`
--

DROP TABLE IF EXISTS `core_surveys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_surveys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `survey_url` varchar(200) NOT NULL,
  `survey_availability` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `ends_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_surveys`
--

LOCK TABLES `core_surveys` WRITE;
/*!40000 ALTER TABLE `core_surveys` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_surveys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vehiclemodels`
--

DROP TABLE IF EXISTS `core_vehiclemodels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_vehiclemodels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_model_id` varchar(20) NOT NULL,
  `model_name` varchar(30) NOT NULL,
  `brand_name` varchar(30) NOT NULL,
  `vehicle_type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vehiclemodels`
--

LOCK TABLES `core_vehiclemodels` WRITE;
/*!40000 ALTER TABLE `core_vehiclemodels` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_vehiclemodels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_vehiclereviews`
--

DROP TABLE IF EXISTS `core_vehiclereviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_vehiclereviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_model_id` int(11) NOT NULL,
  `stars` int(11) NOT NULL,
  `text` int(11) NOT NULL,
  `user_count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_vehiclereviews`
--

LOCK TABLES `core_vehiclereviews` WRITE;
/*!40000 ALTER TABLE `core_vehiclereviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_vehiclereviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_customer`
--

DROP TABLE IF EXISTS `customer_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_customer` (
  `mobile` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `address` json NOT NULL,
  `vehicles` json NOT NULL,
  PRIMARY KEY (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_customer`
--

LOCK TABLES `customer_customer` WRITE;
/*!40000 ALTER TABLE `customer_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_otptransactioninfo`
--

DROP TABLE IF EXISTS `customer_otptransactioninfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_otptransactioninfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `User` varchar(200) NOT NULL,
  `TranID` varchar(50) NOT NULL,
  `OTPValue` varchar(20) NOT NULL,
  `DateTime` varchar(50) NOT NULL,
  `VerificationStatus` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_otptransactioninfo`
--

LOCK TABLES `customer_otptransactioninfo` WRITE;
/*!40000 ALTER TABLE `customer_otptransactioninfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_otptransactioninfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_vehicles`
--

DROP TABLE IF EXISTS `customer_vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_vehicles` (
  `vehicle_model_id` varchar(20) NOT NULL,
  `fuel_type` varchar(20) NOT NULL,
  `vehicle_registration_number` varchar(30) NOT NULL,
  `year` int(11) NOT NULL,
  `chassis_number` varchar(200) NOT NULL,
  `customer_id` varchar(20) NOT NULL,
  `total_kms` int(11) NOT NULL,
  PRIMARY KEY (`vehicle_registration_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_vehicles`
--

LOCK TABLES `customer_vehicles` WRITE;
/*!40000 ALTER TABLE `customer_vehicles` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_vehicles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(4,'auth','permission'),(3,'auth','user'),(29,'authtoken','token'),(5,'contenttypes','contenttype'),(11,'core','complaintcode'),(12,'core','maintenancetips'),(13,'core','scheduledservicedetails'),(10,'core','scheduledservices'),(7,'core','servicecenterinfo'),(9,'core','supportedcarbrands'),(15,'core','surveys'),(8,'core','vehiclemodels'),(14,'core','vehiclereviews'),(18,'customer','customer'),(17,'customer','otptransactioninfo'),(16,'customer','vehicles'),(28,'inventory','inventory'),(25,'jobcard','cservicebooking'),(20,'jobcard','emergencyservicebooking'),(22,'jobcard','jcinvoiceandlabourcost'),(26,'jobcard','jcotherstocksinfo'),(21,'jobcard','jcrecommendedservices'),(27,'jobcard','jcservicedetails'),(24,'jobcard','jcstatus'),(23,'jobcard','jcstocksinfo'),(19,'jobcard','jcvehicleinfo'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-09-07 19:29:47.692767'),(2,'auth','0001_initial','2017-09-07 19:29:48.568334'),(3,'admin','0001_initial','2017-09-07 19:29:48.783434'),(4,'admin','0002_logentry_remove_auto_add','2017-09-07 19:29:48.803299'),(5,'contenttypes','0002_remove_content_type_name','2017-09-07 19:29:48.947055'),(6,'auth','0002_alter_permission_name_max_length','2017-09-07 19:29:48.964002'),(7,'auth','0003_alter_user_email_max_length','2017-09-07 19:29:48.986764'),(8,'auth','0004_alter_user_username_opts','2017-09-07 19:29:49.015874'),(9,'auth','0005_alter_user_last_login_null','2017-09-07 19:29:49.085500'),(10,'auth','0006_require_contenttypes_0002','2017-09-07 19:29:49.092769'),(11,'auth','0007_alter_validators_add_error_messages','2017-09-07 19:29:49.122017'),(12,'auth','0008_alter_user_username_max_length','2017-09-07 19:29:49.179587'),(13,'authtoken','0001_initial','2017-09-07 19:29:49.311134'),(14,'authtoken','0002_auto_20160226_1747','2017-09-07 19:29:49.456561'),(15,'core','0001_initial','2017-09-07 19:29:49.912434'),(16,'customer','0001_initial','2017-09-07 19:29:50.034113'),(17,'inventory','0001_initial','2017-09-07 19:29:50.080547'),(18,'jobcard','0001_initial','2017-09-07 19:29:50.538374'),(19,'sessions','0001_initial','2017-09-07 19:29:50.609686');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_inventory`
--

DROP TABLE IF EXISTS `inventory_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inventory_inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `DealerID` varchar(30) NOT NULL,
  `Brand` varchar(200) NOT NULL,
  `Model` varchar(500) NOT NULL,
  `PartIdentifier` varchar(100) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `MinQty` varchar(10) NOT NULL,
  `AvailableQty` varchar(20) NOT NULL,
  `NDP` varchar(30) NOT NULL,
  `MRP` varchar(30) NOT NULL,
  `IsCritical` varchar(10) NOT NULL,
  `AlternatePart` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_inventory`
--

LOCK TABLES `inventory_inventory` WRITE;
/*!40000 ALTER TABLE `inventory_inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_cservicebooking`
--

DROP TABLE IF EXISTS `jobcard_cservicebooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_cservicebooking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `vehicle_model_id` int(11) NOT NULL,
  `vehicle_registration_number` varchar(20) NOT NULL,
  `service_center_id` varchar(20) NOT NULL,
  `customer_address_id` int(11) NOT NULL,
  `service_details` longtext NOT NULL,
  `feedback_stars` int(11) NOT NULL,
  `feedback_text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `job_card_id` varchar(30) NOT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_cservicebooking`
--

LOCK TABLES `jobcard_cservicebooking` WRITE;
/*!40000 ALTER TABLE `jobcard_cservicebooking` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_cservicebooking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_emergencyservicebooking`
--

DROP TABLE IF EXISTS `jobcard_emergencyservicebooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_emergencyservicebooking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `vehicle_type` varchar(50) NOT NULL,
  `customer_address_id` int(11) NOT NULL,
  `customer_latlon` varchar(100) NOT NULL,
  `service_details` longtext NOT NULL,
  `feedback_stars` int(11) NOT NULL,
  `feedback_text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `service_center_id` varchar(20) NOT NULL,
  `job_card_id` varchar(30) NOT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_emergencyservicebooking`
--

LOCK TABLES `jobcard_emergencyservicebooking` WRITE;
/*!40000 ALTER TABLE `jobcard_emergencyservicebooking` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_emergencyservicebooking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcinvoiceandlabourcost`
--

DROP TABLE IF EXISTS `jobcard_jcinvoiceandlabourcost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcinvoiceandlabourcost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  `MechanicName` varchar(30) NOT NULL,
  `InvoiceNumber` varchar(30) NOT NULL,
  `LabourCharge` varchar(30) NOT NULL,
  `PaymentMode` varchar(30) NOT NULL,
  `GeneratedTime` varchar(30) NOT NULL,
  `PartsTotalPrice` varchar(30) NOT NULL,
  `VATPercentage` varchar(30) NOT NULL,
  `TaxPercentage` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcinvoiceandlabourcost`
--

LOCK TABLES `jobcard_jcinvoiceandlabourcost` WRITE;
/*!40000 ALTER TABLE `jobcard_jcinvoiceandlabourcost` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcinvoiceandlabourcost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcotherstocksinfo`
--

DROP TABLE IF EXISTS `jobcard_jcotherstocksinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcotherstocksinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `JobCardID` varchar(30) NOT NULL,
  `OtherPartsDesc` varchar(100) NOT NULL,
  `OtherPartsCost` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcotherstocksinfo`
--

LOCK TABLES `jobcard_jcotherstocksinfo` WRITE;
/*!40000 ALTER TABLE `jobcard_jcotherstocksinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcotherstocksinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcrecommendedservices`
--

DROP TABLE IF EXISTS `jobcard_jcrecommendedservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcrecommendedservices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  `ServiceItems` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcrecommendedservices`
--

LOCK TABLES `jobcard_jcrecommendedservices` WRITE;
/*!40000 ALTER TABLE `jobcard_jcrecommendedservices` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcrecommendedservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcservicedetails`
--

DROP TABLE IF EXISTS `jobcard_jcservicedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcservicedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ServiceItem` varchar(1000) NOT NULL,
  `IsAvailed` varchar(10) NOT NULL,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcservicedetails`
--

LOCK TABLES `jobcard_jcservicedetails` WRITE;
/*!40000 ALTER TABLE `jobcard_jcservicedetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcservicedetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcstatus`
--

DROP TABLE IF EXISTS `jobcard_jcstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  `MechanicName` varchar(30) NOT NULL,
  `DeliveryTime` varchar(30) NOT NULL,
  `service_reminder_time` varchar(30) NOT NULL,
  `Status` varchar(10) NOT NULL,
  `PendingReason` varchar(100) NOT NULL,
  `CreatedTime` varchar(30) NOT NULL,
  `LastedEditedTime` varchar(30) NOT NULL,
  `CustomerComplaint` longtext NOT NULL,
  `ServiceTypeId` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcstatus`
--

LOCK TABLES `jobcard_jcstatus` WRITE;
/*!40000 ALTER TABLE `jobcard_jcstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcstocksinfo`
--

DROP TABLE IF EXISTS `jobcard_jcstocksinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcstocksinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `PartIdentifier` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `UnitPrice` varchar(30) NOT NULL,
  `Qty` varchar(30) NOT NULL,
  `TotalPrice` varchar(30) NOT NULL,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcstocksinfo`
--

LOCK TABLES `jobcard_jcstocksinfo` WRITE;
/*!40000 ALTER TABLE `jobcard_jcstocksinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcstocksinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobcard_jcvehicleinfo`
--

DROP TABLE IF EXISTS `jobcard_jcvehicleinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobcard_jcvehicleinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `VehicleNumber` varchar(20) NOT NULL,
  `Brand` varchar(200) NOT NULL,
  `Model` varchar(500) NOT NULL,
  `FuelType` varchar(20) NOT NULL,
  `ChassisNumber` varchar(200) NOT NULL,
  `CustomerName` varchar(50) NOT NULL,
  `ContactNumber` varchar(50) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `KilometersTicked` varchar(20) NOT NULL,
  `CreatedTime` varchar(30) NOT NULL,
  `JobCardID` varchar(30) NOT NULL,
  `DealerID` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobcard_jcvehicleinfo`
--

LOCK TABLES `jobcard_jcvehicleinfo` WRITE;
/*!40000 ALTER TABLE `jobcard_jcvehicleinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobcard_jcvehicleinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-08  1:00:59
