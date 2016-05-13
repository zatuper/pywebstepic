usefull reading on django templates
https://docs.djangoproject.com/en/1.8/ref/templates/api/#the-dirs-option
sudo pip install django-mysql 
созданы две базы после миграции используется default
---mysql---
SELECT User FROM mysql.user; 
CREATE DATABASE IF NOT EXISTS `default`;
CREATE DATABASE IF NOT EXISTS `ask`;
SHOW DATABASES ;

SHOW TABLES FROM `default`;                                                                                                             
+----------------------------+                                                                                                                 
| Tables_in_default          |                                                                                                                 
+----------------------------+                                                                                                                 
| ask_answer                 |                                                                                                                 
| ask_author                 |                                                                                                                 
| ask_post                   |                                                                                                                 
| ask_question               |                                                                                                                 
| ask_tag                    |                                                                                                                 
| auth_group                 |                                                                                                                 
| auth_group_permissions     |                                                                                                                 
| auth_permission            |                                                                                                                 
| auth_user                  |                                                                                                                 
| auth_user_groups           |                                                                                                                 
| auth_user_user_permissions |                                                                                                                 
| django_admin_log           |                                                                                                                 
| django_content_type        |                                                                                                                 
| django_migrations          |                                                                                                                 
| django_session             |                                                                                                                 
+----------------------------+                                                                                                                 
15 rows in set (0.00 sec)  


как удалить все миграции и очистить базу

DELETE FROM django_migrations WHERE app='ask'
SET FOREIGN_KEY_CHECKS = 0; 
SET @tables = NULL;
SELECT GROUP_CONCAT(table_schema, '.', table_name) INTO @tables
  FROM information_schema.tables 
  WHERE table_schema = 'database_name'; -- specify DB name here.

SET @tables = CONCAT('DROP TABLE ', @tables);
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
SET FOREIGN_KEY_CHECKS = 1; 

исходный файл settings.py нужно апгредить до версии 1.9 темплейты записываются по новому
https://docs.djangoproject.com/en/dev/ref/templates/upgrading/