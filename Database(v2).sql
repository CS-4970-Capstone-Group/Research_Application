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

 Date: 27/02/2020 00:32:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for BCG
-- ----------------------------
DROP TABLE IF EXISTS `BCG`;
CREATE TABLE `BCG` (
  `BCG_id` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `BCG_signal_values` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`BCG_id`) USING BTREE,
  CONSTRAINT `BCG_id` FOREIGN KEY (`BCG_id`) REFERENCES `TRM` (`TRM_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of BCG
-- ----------------------------
BEGIN;
INSERT INTO `BCG` VALUES ('TRM10101', NULL);
INSERT INTO `BCG` VALUES ('TRM10102', NULL);
INSERT INTO `BCG` VALUES ('TRM10103', NULL);
INSERT INTO `BCG` VALUES ('TRM10104', NULL);
INSERT INTO `BCG` VALUES ('TRM10105', NULL);
INSERT INTO `BCG` VALUES ('TRM10106', NULL);
INSERT INTO `BCG` VALUES ('TRM10107', NULL);
INSERT INTO `BCG` VALUES ('TRM10108', NULL);
INSERT INTO `BCG` VALUES ('TRM10109', NULL);
INSERT INTO `BCG` VALUES ('TRM10110', NULL);
INSERT INTO `BCG` VALUES ('TRM10111', NULL);
INSERT INTO `BCG` VALUES ('TRM10112', NULL);
INSERT INTO `BCG` VALUES ('TRM10113', NULL);
COMMIT;

-- ----------------------------
-- Table structure for TRM
-- ----------------------------
DROP TABLE IF EXISTS `TRM`;
CREATE TABLE `TRM` (
  `TRM_id` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `TRM_name` text,
  `TRM_gender` varchar(255) DEFAULT NULL,
  `TRM_age` varchar(255) DEFAULT NULL,
  `TRM_height(cm)` float(255,1) DEFAULT NULL,
  `TRM_weight(Kg)` float(255,1) DEFAULT NULL,
  `TRM_BP(mmHg)` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `TRM_inpatient` varchar(255) DEFAULT NULL,
  `TRM_class` varchar(255) DEFAULT NULL,
  `w/EF(%)` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`TRM_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of TRM
-- ----------------------------
BEGIN;
INSERT INTO `TRM` VALUES ('TRM10101', 'NULL', 'Male', '62', 162.6, 70.6, '110/71', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10102', 'NULL', 'Male', '62', 162.6, 68.4, '99/65', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10103', 'NULL', 'Male', '62', 162.6, 69.0, '111/73', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10104', 'NULL', 'Male', '62', 162.6, 68.5, '113/71', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10105', 'NULL', 'Male', '62', 162.6, 68.5, '122/79', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10106', 'NULL', 'Male', '62', 162.6, 68.0, '114/78', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10107', 'NULL', 'Male', '62', 162.6, 68.5, '116/82', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10108', 'NULL', 'Male', '62', 162.6, 67.0, '112/73', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10109', 'NULL', 'Male', '62', 162.6, 67.9, '109/71', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10110', 'NULL', 'Male', '62', 162.6, 68.0, '121/77', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10111', 'NULL', 'Male', '62', 160.0, 69.1, '111/74', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10112', 'NULL', 'Male', '62', 160.0, 69.9, '111/74', 'Y', 'IV', '65');
INSERT INTO `TRM` VALUES ('TRM10113', 'NULL', 'Male', '62', 160.0, 70.4, '96/64', 'Y', 'IV', '65');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
