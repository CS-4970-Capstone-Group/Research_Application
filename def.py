import pymysql

connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='12345678'，db='GhostRiders',charset='utf8')
effect_row = cursor.execute('''
CREATE TABLE `users` (
  `name` varchar(32) NOT NULL,
  `age` int(255) unsigned NOT NULL DEFAULT '0',
  `highblood` int(255)
  'lowblood` int(255)
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
''')
effect_row = cursor.executemany(
    'INSERT INTO `users` (`name`, `age`) VALUES (%s, %s) ON DUPLICATE KEY UPDATE age=VALUES(age)', [
        ('user1', 13,110,85),
        ('user2', 28,120,60),
    ])
    
connection.commit()