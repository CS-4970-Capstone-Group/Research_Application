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

 Date: 11/03/2020 15:50:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for BCG Data
-- ----------------------------
DROP TABLE IF EXISTS `BCG Data`;
CREATE TABLE `BCG Data` (
  `bcg_data_id` int NOT NULL AUTO_INCREMENT,
  `subject_id` int DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`bcg_data_id`) USING BTREE,
  KEY `subject_id` (`subject_id`),
  CONSTRAINT `subject_id` FOREIGN KEY (`subject_id`) REFERENCES `Subjects` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for BCG Readings
-- ----------------------------
DROP TABLE IF EXISTS `BCG Readings`;
CREATE TABLE `BCG Readings` (
  `bcg_reading_id` int NOT NULL,
  `bcg_data_id` int NOT NULL,
  PRIMARY KEY (`bcg_reading_id`) USING BTREE,
  KEY `BCG_data_id` (`bcg_data_id`),
  CONSTRAINT `BCG_data_id` FOREIGN KEY (`bcg_data_id`) REFERENCES `BCG Data` (`bcg_data_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for FCL Weights
-- ----------------------------
DROP TABLE IF EXISTS `FCL Weights`;
CREATE TABLE `FCL Weights` (
  `weight_id` int NOT NULL AUTO_INCREMENT,
  `weight_value` double(200,0) DEFAULT NULL,
  `layer_id` int DEFAULT NULL,
  PRIMARY KEY (`weight_id`) USING BTREE,
  KEY `Layer_id` (`layer_id`),
  CONSTRAINT `Layer_id` FOREIGN KEY (`layer_id`) REFERENCES `Fully Connected Layer` (`layer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Fully Connected Layer
-- ----------------------------
DROP TABLE IF EXISTS `Fully Connected Layer`;
CREATE TABLE `Fully Connected Layer` (
  `layer_id` int NOT NULL AUTO_INCREMENT,
  `number_of_weights` int DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`layer_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Kernel Weights
-- ----------------------------
DROP TABLE IF EXISTS `Kernel Weights`;
CREATE TABLE `Kernel Weights` (
  `kernel_weight_id` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `kernel_weight_value` double(255,0) DEFAULT NULL,
  `kernel_id` int DEFAULT NULL,
  PRIMARY KEY (`kernel_weight_id`) USING BTREE,
  KEY `Kernel_id` (`kernel_id`),
  CONSTRAINT `Kernel_id` FOREIGN KEY (`kernel_id`) REFERENCES `Kernels` (`kernel_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Kernels
-- ----------------------------
DROP TABLE IF EXISTS `Kernels`;
CREATE TABLE `Kernels` (
  `kernel_id` int NOT NULL AUTO_INCREMENT,
  `kernel_size` double(255,0) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`kernel_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for Performance Metrics
-- ----------------------------
DROP TABLE IF EXISTS `Performance Metrics`;
CREATE TABLE `Performance Metrics` (
  `performance_test_id` int NOT NULL AUTO_INCREMENT,
  `accuracy_level` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `data_of _test` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`performance_test_id`) USING BTREE
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
  `blood_pressure` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `hypertension` varchar(255) DEFAULT NULL,
  `ground_truth` varchar(255) DEFAULT NULL,
  `heart_failure_risk` varchar(255) DEFAULT NULL,
  `ethnicity` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
