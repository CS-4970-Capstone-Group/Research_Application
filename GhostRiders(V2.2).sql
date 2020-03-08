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

 Date: 08/03/2020 16:30:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for BCG Data
-- ----------------------------
DROP TABLE IF EXISTS `BCG Data`;
CREATE TABLE `BCG Data` (
  `BCG_data_id` int NOT NULL AUTO_INCREMENT,
  `subject_id` int DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`BCG_data_id`),
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `subject_id` FOREIGN KEY (`subject_id`) REFERENCES `Subjects` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for BCG Readings
-- ----------------------------
DROP TABLE IF EXISTS `BCG Readings`;
CREATE TABLE `BCG Readings` (
  `BCG_reading_id` int NOT NULL,
  `BCG_data_id` int NOT NULL,
  PRIMARY KEY (`BCG_reading_id`),
  KEY `BCG_data_id` (`BCG_data_id`),
  CONSTRAINT `BCG_data_id` FOREIGN KEY (`BCG_data_id`) REFERENCES `BCG Data` (`BCG_data_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for FCL Weights
-- ----------------------------
DROP TABLE IF EXISTS `FCL Weights`;
CREATE TABLE `FCL Weights` (
  `Weight_id` int NOT NULL AUTO_INCREMENT,
  `Weight_value` double(200,0) DEFAULT NULL,
  `Layer_id` int DEFAULT NULL,
  PRIMARY KEY (`Weight_id`),
  KEY `Layer_id` (`Layer_id`),
  CONSTRAINT `Layer_id` FOREIGN KEY (`Layer_id`) REFERENCES `Fully Connected Layer` (`Layer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Fully Connected Layer
-- ----------------------------
DROP TABLE IF EXISTS `Fully Connected Layer`;
CREATE TABLE `Fully Connected Layer` (
  `Layer_id` int NOT NULL AUTO_INCREMENT,
  `Number_of_weights` int DEFAULT NULL,
  `Last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`Layer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Kernel Weights
-- ----------------------------
DROP TABLE IF EXISTS `Kernel Weights`;
CREATE TABLE `Kernel Weights` (
  `Kernel_weight_id` varchar(200) NOT NULL,
  `Kernel_weight_value` double(255,0) DEFAULT NULL,
  `Kernel_id` int DEFAULT NULL,
  PRIMARY KEY (`Kernel_weight_id`),
  KEY `Kernel_id` (`Kernel_id`),
  CONSTRAINT `Kernel_id` FOREIGN KEY (`Kernel_id`) REFERENCES `Kernels` (`Kernel_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Kernels
-- ----------------------------
DROP TABLE IF EXISTS `Kernels`;
CREATE TABLE `Kernels` (
  `Kernel_id` int NOT NULL AUTO_INCREMENT,
  `Kernel_size` double(255,0) DEFAULT NULL,
  `Last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`Kernel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Performance Metrics
-- ----------------------------
DROP TABLE IF EXISTS `Performance Metrics`;
CREATE TABLE `Performance Metrics` (
  `Performance_test_id` int NOT NULL AUTO_INCREMENT,
  `Accuracy_level` varchar(255) DEFAULT NULL,
  `Data_of _test` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Performance_test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Subjects
-- ----------------------------
DROP TABLE IF EXISTS `Subjects`;
CREATE TABLE `Subjects` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `age` int DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `height(cm)` double(200,0) DEFAULT NULL,
  `weight(Kg)` double(200,0) DEFAULT NULL,
  `blood pressure` varchar(255) DEFAULT NULL,
  `hypertension` varchar(255) DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  `heart_failure_risk` varchar(255) DEFAULT NULL,
  `ethnicity` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
