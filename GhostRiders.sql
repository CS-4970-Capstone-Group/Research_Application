/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : GhostRiders

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 12/05/2020 14:42:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bcg_data
-- ----------------------------
DROP TABLE IF EXISTS `bcg_data`;
CREATE TABLE `bcg_data` (
  `bcg_data_id` int NOT NULL AUTO_INCREMENT,
  `subject_id` int DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`bcg_data_id`) USING BTREE,
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `subject_id` FOREIGN KEY (`subject_id`) REFERENCES `people` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30000 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bcg_readings
-- ----------------------------
DROP TABLE IF EXISTS `bcg_readings`;
CREATE TABLE `bcg_readings` (
  `bcg_reading_id` int NOT NULL,
  `bcg_data_id` int NOT NULL,
  PRIMARY KEY (`bcg_reading_id`) USING BTREE,
  KEY `BCG_data_id` (`bcg_data_id`),
  CONSTRAINT `BCG_data_id` FOREIGN KEY (`bcg_data_id`) REFERENCES `bcg_data` (`bcg_data_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bcg_table
-- ----------------------------
DROP TABLE IF EXISTS `bcg_table`;
CREATE TABLE `bcg_table` (
  `health_data` float DEFAULT NULL,
  `bcg_data_id` int NOT NULL AUTO_INCREMENT,
  `person_id` int DEFAULT NULL,
  PRIMARY KEY (`bcg_data_id`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `bcg_table_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `people` (`subject_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fcl_weights
-- ----------------------------
DROP TABLE IF EXISTS `fcl_weights`;
CREATE TABLE `fcl_weights` (
  `weight_id` int NOT NULL AUTO_INCREMENT,
  `weight_value` double(200,0) DEFAULT NULL,
  `layer_id` int DEFAULT NULL,
  PRIMARY KEY (`weight_id`) USING BTREE,
  KEY `Layer_id` (`layer_id`),
  CONSTRAINT `Layer_id` FOREIGN KEY (`layer_id`) REFERENCES `fully_connected_layer` (`layer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fully_connected_layer
-- ----------------------------
DROP TABLE IF EXISTS `fully_connected_layer`;
CREATE TABLE `fully_connected_layer` (
  `layer_id` int NOT NULL AUTO_INCREMENT,
  `number_of_weights` int DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`layer_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for heart_data
-- ----------------------------
DROP TABLE IF EXISTS `heart_data`;
CREATE TABLE `heart_data` (
  `heart_data_id` int NOT NULL AUTO_INCREMENT,
  `age` int DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `cp` varchar(255) DEFAULT NULL,
  `trestbps` varchar(255) DEFAULT NULL,
  `chol` varchar(255) DEFAULT NULL,
  `fbs` varchar(255) DEFAULT NULL,
  `restecg` varchar(255) DEFAULT NULL,
  `thalach` varchar(255) DEFAULT NULL,
  `exang` varchar(255) DEFAULT NULL,
  `oldpeak` varchar(255) DEFAULT NULL,
  `slope` varchar(255) DEFAULT NULL,
  `ca` varchar(255) DEFAULT NULL,
  `thal` varchar(255) DEFAULT NULL,
  `target` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`heart_data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10304 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for kernel_weights
-- ----------------------------
DROP TABLE IF EXISTS `kernel_weights`;
CREATE TABLE `kernel_weights` (
  `kernel_weight_id` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `kernel_weight_value` double(255,0) DEFAULT NULL,
  `kernel_id` int DEFAULT NULL,
  PRIMARY KEY (`kernel_weight_id`) USING BTREE,
  KEY `Kernel_id` (`kernel_id`),
  CONSTRAINT `Kernel_id` FOREIGN KEY (`kernel_id`) REFERENCES `kernels` (`kernel_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for kernels
-- ----------------------------
DROP TABLE IF EXISTS `kernels`;
CREATE TABLE `kernels` (
  `kernel_id` int NOT NULL AUTO_INCREMENT,
  `kernel_size` double(255,0) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`kernel_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for people
-- ----------------------------
DROP TABLE IF EXISTS `people`;
CREATE TABLE `people` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `blood_pressure_high` varchar(255) DEFAULT NULL,
  `blood_pressure_low` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `hypertension` varchar(255) DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  `heart_failure_risk` varchar(255) DEFAULT NULL,
  `ethnicity` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1060 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of people
-- ----------------------------
BEGIN;
INSERT INTO `people` VALUES (1036, 'James', 50, 'MALE', 180, 80, '80', '150', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1037, 'John', 49, 'MALE', 190, 90, '80', '130', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1038, 'Robert', 52, 'MALE', 190, 100, '80', '140', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1039, 'Michael', 57, 'MALE', 178, 100, '80', '140', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1040, 'William', 58, 'MALE', 185, 100, '80', '140', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1041, 'Joseph', 66, 'MALE', 179, 70, '80', '140', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1042, 'Thomas', 75, 'MALE', 177, 110, '80', '140', 'NO', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1043, 'Mattew', 68, 'MALE', 185, 68, '80', '130', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1044, 'Mark', 57, 'MALE', 190, 60, '80', '140', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1045, 'test1', 32, 'MALE', 170, 80, '80', '130', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1046, 'Test2', 66, 'MALE', 170, 80, '86', '97', 'YES', 'YES', NULL, 'Aboriginal American');
INSERT INTO `people` VALUES (1047, 'test3', 66, 'MALE', 180, 90, '80', '130', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1048, 'test4', 43, 'MALE', 2312, 324, '432', '32', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1049, 'dadad', 123, 'MALE', 3211, 231, '31', '213', 'YES', 'YES', NULL, 'Aboriginal American');
INSERT INTO `people` VALUES (1050, 'adaa', 213, 'MALE', 1231, 321, '31232', '312', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1051, 'test7', 424, 'MALE', 42, 324, '423', '423', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1052, 'test8', 432, 'MALE', 414, 432, '42', '2434', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1053, 'daqd', 3123, 'MALE', 1231, 312, '31', '132', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1054, 'bdjad', 4654, 'MALE', 645446, 4656, '54', '645', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1055, 'chdad', 3123, 'MALE', 31231, 31231, '311', '312', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1056, 'adda', 32, 'MALE', 312, 41, '432', '432', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1057, 'acd', 234, 'MALE', 14, 423, '4342', '423', 'YES', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1058, 'hocus', 312, 'MALE', 12, 312, '31', '123', 'NO', 'YES', NULL, 'African');
INSERT INTO `people` VALUES (1059, 'cscd', 423, 'MALE', 432, 423, '423', '423', 'YES', 'YES', NULL, 'African');
COMMIT;

-- ----------------------------
-- Table structure for performance_metrics
-- ----------------------------
DROP TABLE IF EXISTS `performance_metrics`;
CREATE TABLE `performance_metrics` (
  `performance_test_id` int NOT NULL AUTO_INCREMENT,
  `accuracy_level` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `data_of _test` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`performance_test_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
