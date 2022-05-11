-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: 002_bear_robotics
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add subsidary',7,'add_subsidary'),(26,'Can change subsidary',7,'change_subsidary'),(27,'Can delete subsidary',7,'delete_subsidary'),(28,'Can view subsidary',7,'view_subsidary'),(29,'Can add ward',8,'add_ward'),(30,'Can change ward',8,'change_ward'),(31,'Can delete ward',8,'delete_ward'),(32,'Can view ward',8,'view_ward'),(33,'Can add restaurant',9,'add_restaurant'),(34,'Can change restaurant',9,'change_restaurant'),(35,'Can delete restaurant',9,'delete_restaurant'),(36,'Can view restaurant',9,'view_restaurant'),(37,'Can add neighborhood',10,'add_neighborhood'),(38,'Can change neighborhood',10,'change_neighborhood'),(39,'Can delete neighborhood',10,'delete_neighborhood'),(40,'Can view neighborhood',10,'view_neighborhood'),(41,'Can add menu',11,'add_menu'),(42,'Can change menu',11,'change_menu'),(43,'Can delete menu',11,'delete_menu'),(44,'Can view menu',11,'view_menu'),(45,'Can add payment',12,'add_payment'),(46,'Can change payment',12,'change_payment'),(47,'Can delete payment',12,'delete_payment'),(48,'Can view payment',12,'view_payment'),(49,'Can add result',13,'add_result'),(50,'Can change result',13,'change_result'),(51,'Can delete result',13,'delete_result'),(52,'Can view result',13,'view_result'),(53,'Can add result menu',14,'add_resultmenu'),(54,'Can change result menu',14,'change_resultmenu'),(55,'Can delete result menu',14,'delete_resultmenu'),(56,'Can view result menu',14,'view_resultmenu');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'restaurants','menu'),(10,'restaurants','neighborhood'),(9,'restaurants','restaurant'),(7,'restaurants','subsidary'),(8,'restaurants','ward'),(12,'results','payment'),(13,'results','result'),(14,'results','resultmenu'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-05-02 06:40:00.262089'),(2,'auth','0001_initial','2022-05-02 06:40:01.316892'),(3,'admin','0001_initial','2022-05-02 06:40:01.510968'),(4,'admin','0002_logentry_remove_auto_add','2022-05-02 06:40:01.523929'),(5,'admin','0003_logentry_add_action_flag_choices','2022-05-02 06:40:01.537893'),(6,'contenttypes','0002_remove_content_type_name','2022-05-02 06:40:01.645679'),(7,'auth','0002_alter_permission_name_max_length','2022-05-02 06:40:01.735021'),(8,'auth','0003_alter_user_email_max_length','2022-05-02 06:40:01.761949'),(9,'auth','0004_alter_user_username_opts','2022-05-02 06:40:01.774889'),(10,'auth','0005_alter_user_last_login_null','2022-05-02 06:40:01.849689'),(11,'auth','0006_require_contenttypes_0002','2022-05-02 06:40:01.857668'),(12,'auth','0007_alter_validators_add_error_messages','2022-05-02 06:40:01.871630'),(13,'auth','0008_alter_user_username_max_length','2022-05-02 06:40:01.963410'),(14,'auth','0009_alter_user_last_name_max_length','2022-05-02 06:40:02.056733'),(15,'auth','0010_alter_group_name_max_length','2022-05-02 06:40:02.076708'),(16,'auth','0011_update_proxy_permissions','2022-05-02 06:40:02.089645'),(17,'auth','0012_alter_user_first_name_max_length','2022-05-02 06:40:02.170164'),(18,'restaurants','0001_initial','2022-05-02 06:40:02.639695'),(19,'results','0001_initial','2022-05-02 06:40:02.981495'),(20,'sessions','0001_initial','2022-05-02 06:40:03.041702'),(21,'restaurants','0002_alter_menu_delete_at_alter_restaurant_delete_at_and_more','2022-05-02 08:18:28.101067'),(22,'results','0002_alter_result_delete_at_alter_resultmenu_delete_at','2022-05-02 08:18:28.256694'),(24,'results','0003_alter_result_updated_at_alter_resultmenu_updated_at','2022-05-02 09:44:08.915743'),(26,'restaurants','0003_alter_menu_created_at_alter_restaurant_created_at_and_more','2022-05-03 01:06:56.934957'),(27,'results','0003_alter_result_created_at_alter_resultmenu_created_at','2022-05-03 01:06:57.107744'),(28,'restaurants','0003_alter_menu_updated_at_alter_restaurant_updated_at_and_more','2022-05-03 02:27:03.480439'),(29,'restaurants','0004_merge_20220503_1004','2022-05-03 02:27:03.487451'),(30,'results','0004_resultmenu_quantity','2022-05-03 02:27:03.586024'),(31,'restaurants','0005_restaurant_name_restaurant_store_and_more','2022-05-04 00:32:48.739921'),(32,'restaurants','0006_alter_menu_name_alter_menu_price_and_more','2022-05-07 18:10:24.303145'),(33,'results','0005_rename_restuarants_result_menus_result_restaurant','2022-05-07 18:10:25.782240'),(34,'results','0006_alter_result_payment_delete_payment','2022-05-07 18:10:26.323804'),(35,'results','0007_result_subsidary_alter_result_restaurant','2022-05-07 18:10:26.570209'),(36,'results','0006_alter_result_payment','2022-05-07 18:10:26.584148'),(37,'results','0008_merge_20220505_1904','2022-05-07 18:10:26.590131'),(38,'results','0009_rename_total_payments_result_total_price','2022-05-07 18:10:26.631048'),(39,'results','0010_alter_result_menus_alter_result_numbers_of_party_and_more','2022-05-07 18:10:26.682883');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `delete_at` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `price` decimal(12,2) DEFAULT NULL,
  `subsidary_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menus_subsidary_id_cfe06acb_fk_subsidaries_id` (`subsidary_id`),
  CONSTRAINT `menus_subsidary_id_cfe06acb_fk_subsidaries_id` FOREIGN KEY (`subsidary_id`) REFERENCES `subsidaries` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menus`
--

LOCK TABLES `menus` WRITE;
/*!40000 ALTER TABLE `menus` DISABLE KEYS */;
/*!40000 ALTER TABLE `menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `neighborhoods`
--

DROP TABLE IF EXISTS `neighborhoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `neighborhoods` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `ward_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `neighborhoods_ward_id_ed86dcbf_fk_wards_id` (`ward_id`),
  CONSTRAINT `neighborhoods_ward_id_ed86dcbf_fk_wards_id` FOREIGN KEY (`ward_id`) REFERENCES `wards` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `neighborhoods`
--

LOCK TABLES `neighborhoods` WRITE;
/*!40000 ALTER TABLE `neighborhoods` DISABLE KEYS */;
INSERT INTO `neighborhoods` VALUES (1,'서울',3),(2,'서울',4),(3,'서울',5),(4,'경기',7);
/*!40000 ALTER TABLE `neighborhoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurants` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `delete_at` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `subsidary_id` bigint NOT NULL,
  `ward_id` bigint NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `store` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `restaurants_subsidary_id_2f94d615_fk_subsidaries_id` (`subsidary_id`),
  KEY `restaurants_ward_id_7bde2ce7_fk_wards_id` (`ward_id`),
  CONSTRAINT `restaurants_subsidary_id_2f94d615_fk_subsidaries_id` FOREIGN KEY (`subsidary_id`) REFERENCES `subsidaries` (`id`),
  CONSTRAINT `restaurants_ward_id_7bde2ce7_fk_wards_id` FOREIGN KEY (`ward_id`) REFERENCES `wards` (`id`),
  CONSTRAINT `restaurants_chk_1` CHECK ((`store` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (1,'2022-05-02 10:50:05.902354','2022-05-03 00:43:48.369421',NULL,1,1,3,'맥도날드, 서초구 신림동',1),(2,'2022-05-02 10:52:16.882945','2022-05-05 12:49:12.214212',NULL,0,1,3,'맥도날드, 서초구 서초동점',2),(3,'2022-05-02 10:52:46.518119','2022-05-02 10:52:46.518119',NULL,0,1,7,'맥도날드, 서초구 신림동',1),(4,'2022-05-02 10:53:03.541460','2022-05-02 10:53:03.541460',NULL,0,2,5,'맥도날드, 서초구 신림동',1),(6,'2022-05-02 11:04:04.776932','2022-05-02 11:04:04.776932',NULL,0,3,4,'맥도날드, 서초구 신림동',1),(7,'2022-05-02 11:04:11.774578','2022-05-02 11:04:11.774578',NULL,0,3,7,'맥도날드, 서초구 신림동',1),(8,'2022-05-02 11:20:29.742054','2022-05-02 11:20:29.742054',NULL,0,3,4,'맥도날드, 서초구 신림동',1),(20,'2022-05-05 05:38:05.638611','2022-05-05 05:38:05.638611',NULL,0,1,3,'맥도날드, 서초구 서초동점',NULL);
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result_menus`
--

DROP TABLE IF EXISTS `result_menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result_menus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `delete_at` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `discount_rate` decimal(4,3) DEFAULT NULL,
  `menu_id` bigint NOT NULL,
  `result_id` bigint NOT NULL,
  `quantity` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `result_menus_menu_id_32dd80b6_fk_menus_id` (`menu_id`),
  KEY `result_menus_result_id_8035adb5_fk_results_id` (`result_id`),
  CONSTRAINT `result_menus_menu_id_32dd80b6_fk_menus_id` FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`),
  CONSTRAINT `result_menus_result_id_8035adb5_fk_results_id` FOREIGN KEY (`result_id`) REFERENCES `results` (`id`),
  CONSTRAINT `result_menus_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result_menus`
--

LOCK TABLES `result_menus` WRITE;
/*!40000 ALTER TABLE `result_menus` DISABLE KEYS */;
/*!40000 ALTER TABLE `result_menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `delete_at` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `numbers_of_party` int unsigned DEFAULT NULL,
  `total_price` decimal(12,2) DEFAULT NULL,
  `payment` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `restaurant_id` bigint NOT NULL,
  `subsidary_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `results_restaurant_id_66e1c4e7_fk_restaurants_id` (`restaurant_id`),
  KEY `results_subsidary_id_b4e31fb3_fk_subsidaries_id` (`subsidary_id`),
  CONSTRAINT `results_restaurant_id_66e1c4e7_fk_restaurants_id` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`id`),
  CONSTRAINT `results_subsidary_id_b4e31fb3_fk_subsidaries_id` FOREIGN KEY (`subsidary_id`) REFERENCES `subsidaries` (`id`),
  CONSTRAINT `results_chk_1` CHECK ((`numbers_of_party` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (86,'2022-05-07 23:23:57.708246','2022-05-07 23:23:57.708246',NULL,0,2,20000.00,'CARD',2,1),(87,'2022-05-07 23:23:57.708246','2022-05-07 23:23:57.708246',NULL,0,2,20000.00,'CARD',2,1),(88,'2022-05-07 23:23:57.708246','2022-05-07 23:23:57.708246',NULL,0,2,30000.00,'CASH',2,1),(89,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'BITCOIN',2,1),(90,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CASH',2,1),(91,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(92,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(93,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'PHONE',2,1),(94,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'PHONE',2,1),(95,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'BITCOIN',2,1),(96,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'BITCOIN',2,1),(97,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(98,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(99,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(100,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(101,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(102,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(103,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(104,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(105,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(106,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(107,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(108,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(109,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(110,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(111,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(112,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(113,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(114,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(115,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(116,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(117,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(118,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(119,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(120,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(121,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',2,1),(122,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',2,1),(123,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',3,1),(124,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,20000.00,'CARD',3,1),(125,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,10000.00,'CARD',3,1),(126,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',3,1),(127,'2022-05-07 23:23:57.709242','2022-05-07 23:23:57.709242',NULL,0,2,30000.00,'CARD',3,1),(128,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(129,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(130,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(131,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(132,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(133,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(134,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(135,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(136,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(137,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(138,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(139,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,20000.00,'CARD',3,1),(140,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(141,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(142,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,10000.00,'CARD',3,1),(143,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(144,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(145,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(146,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(147,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(148,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,20000.00,'CARD',3,1),(149,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(150,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,10000.00,'CARD',3,1),(151,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,30000.00,'CARD',3,1),(152,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CASH',3,1),(153,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CASH',3,1),(154,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,10000.00,'CARD',3,1),(155,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(156,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,20000.00,'CARD',3,1),(157,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,3,10000.00,'CARD',3,1),(158,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(159,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(160,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,30000.00,'CARD',3,1),(161,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,10000.00,'CARD',3,1),(162,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(163,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,2,20000.00,'CARD',3,1),(164,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,4,20000.00,'CARD',3,1),(165,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.710240',NULL,0,4,10000.00,'CARD',3,1),(166,'2022-05-07 23:23:57.710240','2022-05-07 23:23:57.711238',NULL,0,2,20000.00,'CARD',3,1),(167,'2022-05-07 23:23:57.711238','2022-05-07 23:23:57.711238',NULL,0,2,30000.00,'CARD',3,1),(168,'2022-05-07 23:23:57.711238','2022-05-07 23:23:57.711238',NULL,0,3,30000.00,'CARD',3,1),(169,'2022-05-07 23:23:57.711238','2022-05-07 23:23:57.711238',NULL,0,3,10000.00,'CARD',3,1),(170,'2022-05-07 23:23:57.711238','2022-05-07 23:23:57.711238',NULL,0,2,30000.00,'CARD',3,1);
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subsidaries`
--

DROP TABLE IF EXISTS `subsidaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subsidaries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `delete_at` datetime(6) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subsidaries`
--

LOCK TABLES `subsidaries` WRITE;
/*!40000 ALTER TABLE `subsidaries` DISABLE KEYS */;
INSERT INTO `subsidaries` VALUES (1,'2022-01-01 00:00:00.000000','2022-01-01 00:00:00.000000',NULL,0,'맥도날드'),(2,'2022-01-01 00:00:00.000000','2022-01-01 00:00:00.000000',NULL,0,'버거킹'),(3,'2022-01-01 00:00:00.000000','2022-01-01 00:00:00.000000',NULL,0,'쉑쉑버거');
/*!40000 ALTER TABLE `subsidaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wards`
--

DROP TABLE IF EXISTS `wards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wards` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wards`
--

LOCK TABLES `wards` WRITE;
/*!40000 ALTER TABLE `wards` DISABLE KEYS */;
INSERT INTO `wards` VALUES (3,'서초구 서초동'),(4,'관악구 신림동'),(5,'강남구 개포동'),(7,'무슨동');
/*!40000 ALTER TABLE `wards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-11 11:33:54
