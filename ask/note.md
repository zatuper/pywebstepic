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
