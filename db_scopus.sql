/*
 Navicat Premium Data Transfer

 Source Server         : localhost 3306
 Source Server Type    : MySQL
 Source Server Version : 100414
 Source Host           : localhost:3306
 Source Schema         : db_scopus

 Target Server Type    : MySQL
 Target Server Version : 100414
 File Encoding         : 65001

 Date: 12/11/2021 23:14:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_scopus` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `nama` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fakultas` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `jurusan` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `createAt` datetime(0) NULL DEFAULT NULL,
  `updateAt` datetime(0) NULL DEFAULT NULL,
  `deleteAt` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_scopus`(`id_scopus`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of author
-- ----------------------------
INSERT INTO `author` VALUES ('', '57204495477', 'Angga Setiyadi', 'Teknik dan Ilmu Komputer', 'Teknik Informatika', NULL, NULL, NULL);
INSERT INTO `author` VALUES ('2', '56411885900', 'Adam Mukharil Bachtiar', 'Teknik dan Ilmu Komputer', 'Teknik Informatika', NULL, NULL, NULL);
INSERT INTO `author` VALUES ('3', '57204187129', 'Dian Dharmayanti', 'Teknik dan Ilmu Komputer', 'Teknik Informatika', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for documents
-- ----------------------------
DROP TABLE IF EXISTS `documents`;
CREATE TABLE `documents`  (
  `eid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `doi` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `tittle` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `coverDate` date NULL DEFAULT NULL,
  `volume` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `citiedCount` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `scopus_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `issn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `createAt` datetime(0) NULL DEFAULT NULL,
  `updateAt` datetime(0) NULL DEFAULT NULL,
  `deleteAt` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`eid`) USING BTREE,
  INDEX `documents_ibfk_1`(`issn`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of documents
-- ----------------------------
INSERT INTO `documents` VALUES ('2-s2.0-84909942808', '10.1109/ICoICT.2014.6914038', 'Development of requirement elicitation model for prediction of student achievement in university', 'Conference Paper', '2014-09-30', '47-52', '2', '56411885900', '9781479935819', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85054791263', '10.1088/1757-899X/407/1/012127', 'Analysis of User Interface and User Experience on Comrades Application', 'Conference Paper', '2018-09-26', '407', '3', '57204187129', '17578981', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85054825240', '10.1088/1757-899X/407/1/012081', 'Web vulnerability analysis and implementation', 'Conference Paper', '2018-09-26', '407', '6', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85054873702', '10.1088/1757-899X/407/1/012120', 'Data Visualization of Environmental Factors in Poultry Farm', 'Conference Paper', '2018-09-26', '407', '1', '57204187129', '17578981', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85054883332', '10.1088/1757-899X/407/1/012110', 'Information System Monitoring Access Log Database on Database Server', 'Conference Paper', '2018-09-26', '407', '4', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85068714972', '10.1088/1742-6596/1233/1/012049', 'Mathematical Representations Mapping of High School Students after using Multimedia Learning Modules Assisted by an Android Smartphone', 'Conference Paper', '2019-06-27', '1233', '1', '57204495477', '17426588', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85073233388', '10.1088/1757-899X/598/1/012115', 'Critical Success Factors Evaluation of the ISO 50001 Energy Management System Implementation (Case study: PT. APAC INTI CORPORA, Bawen, Semarang Indonesia)', 'Conference Paper', '2019-09-09', '598', '0', '56411885900', '17578981', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075858419', '10.1088/1757-899X/662/2/022009', 'Building English Learning Application in University Based on Web and Mobile', 'Conference Paper', '2019-11-20', '662', '0', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075863518', '10.1088/1757-899X/662/2/022126', 'Geographic Information System for Mapping New Entrepreneurs in West Java', 'Conference Paper', '2019-11-20', '662', '1', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075873406', '10.1088/1757-899X/662/2/022072', 'Designing Information System Recruitment Professional Gamers Web-Based', 'Conference Paper', '2019-11-20', '662', '1', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075881278', '10.1088/1757-899X/662/6/062017', 'Data Visualization of Plant Resistant Towards Plant Disease at PT. East-West Seed Indonesia', 'Conference Paper', '2019-11-20', '662', '0', '57204187129', '17578981', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075885518', '10.1088/1757-899X/662/2/022043', 'Quality Analysis of Mobile Web Server', 'Conference Paper', '2019-11-20', '662', '1', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075890502', '10.1088/1757-899X/662/2/022068', 'Blind scanner Server and Batch Programming Implementation in the Process of Automatically Scan Documents', 'Conference Paper', '2019-11-20', '662', '1', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075897252', '10.1088/1757-899X/662/3/032037', 'Bitcoin influence on E-commerce', 'Conference Paper', '2019-11-20', '662', '0', '56411885900', '17578981', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85075898056', '10.1088/1757-899X/662/2/022122', 'Implementation of Micro Services Architecture on Comrades Backend', 'Conference Paper', '2019-11-20', '662', '0', '56411885900', '17578981', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85077823749', '10.1088/1742-6596/1402/6/066088', 'Relationship between development and quality of video games', 'Conference Paper', '2019-12-16', '1402', '0', '56411885900', '17426588', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85091381554', '10.1088/1757-899X/879/1/012036', 'Private Cloud Development in West Java Cooperative and Entrepreneurship Education and Training Center', 'Conference Paper', '2020-08-05', '879', '1', '57204495477', '17578981', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85101642895', '0', 'Data visualization for content marketing domain in social media', 'Article', '2021-02-01', '16', '0', '57204187129', '18234690', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85101914795', '0', 'Analysis of interaction design in braille al-qur\'an learning app for visually impaired people', 'Article', '2020-10-01', '15', '0', '57204187129', '18234690', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85101917357', '0', 'Analysis of interaction design model in content marketing domain using design sprint method', 'Article', '2020-02-01', '15', '0', '57204187129', '18234690', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `documents` VALUES ('2-s2.0-85117915025', '0', 'Data visualization for education domain at Dinas Pendidikan Jawa Barat', 'Article', '2021-10-01', '16', '0', '57204187129', '18234690', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);

-- ----------------------------
-- Table structure for publisher
-- ----------------------------
DROP TABLE IF EXISTS `publisher`;
CREATE TABLE `publisher`  (
  `issn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `publication_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `aggregation_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `createAt` datetime(0) NULL DEFAULT NULL,
  `updateAt` datetime(0) NULL DEFAULT NULL,
  `deleteAt` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`issn`) USING BTREE,
  INDEX `issn`(`issn`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of publisher
-- ----------------------------
INSERT INTO `publisher` VALUES ('17426588', 'Journal of Physics: Conference Series', 'Conference Proceeding', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `publisher` VALUES ('17578981', 'IOP Conference Series: Materials Science and Engineering', 'Conference Proceeding', '2021-11-12 23:13:05', '2021-11-12 23:13:05', NULL);
INSERT INTO `publisher` VALUES ('18234690', 'Journal of Engineering Science and Technology', 'Journal', '2021-11-12 23:13:03', '2021-11-12 23:13:03', NULL);
INSERT INTO `publisher` VALUES ('9781479935819', '2014 2nd International Conference on Information and Communication Technology, ICoICT 2014', 'Conference Proceeding', '2021-11-12 23:13:00', '2021-11-12 23:13:00', NULL);

SET FOREIGN_KEY_CHECKS = 1;
