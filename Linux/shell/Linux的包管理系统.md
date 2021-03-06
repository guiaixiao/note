## Linux的包管理系统

### 软件包系统工具
| 系统类型 | 低级工具 |高级工具 |
| ------ | ------   |--- |
| Debian 类  | dpkg | apt-get & aptitude |
| Red Hat 类  | rpm | yum |
---
### 在库里面查找软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get update & apt-cache search pkg_name |
| Red Hat 类  | yum search pkg_name |
---
### 安装库里面的软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get install pkg_name |
| Red Hat 类  | yum install pkg_name |
---
### 安装软件包文件中的软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | dpkg -i pkg_file.deb |
| Red Hat 类  | rpm -i pkg_file.rpm |
---
### 删除软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get remove pkg_name |
| Red Hat 类  | yum erase pkg_name |
---
### 更新库里的软件包
- 高级工具

| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get upgrade |
| Red Hat 类  | yum update |
- 低级工具

| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | dpkg -i pkg_file.deb |
| Red Hat 类  | rpm -U pkg_file.rpm |
---
### 列出已安装的软件包列表
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | dpkg --list |
| Red Hat 类  | rpm -qa |
---
### 判断软件包是否安装
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | dpkg --status pkg_name |
| Red Hat 类  | rpm -q pkg_name |
---
### 显示已安装的软件包的相关信息
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-cache show pkg_name &per aptitude show pkg_name |
| Red Hat 类  | yum info pkg_name|
---
### 查看某个具体文件由哪个安装包得到
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | dpkg --search file_name |
| Red Hat 类  | rpm -qf file_name |
---
### 在库里面查找软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get |
| Red Hat 类  | yum |
---
### 在库里面查找软件包
| 系统类型 | 命令 |
| ------ | ------ |
| Debian 类  | apt-get |
| Red Hat 类  | yum |
---