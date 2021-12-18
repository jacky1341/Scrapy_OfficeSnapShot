# Scrapy_OfficeSnapShot

爬取OfficeSnapShot网站的数据

1. Scrapy_OfficeSnapShot是一个爬取办公椅工程社区的脚本;

2. 主要是通过requests库爬取该社区的上面办公家具工程的名称，工程介绍，以及负责该工程的公司;

3. 可以通过修改源代码的链接，去爬区其他社区的内容

4. 该文件仍在初试阶段，即还没有封装及优化速度

5. 使用：在Pycharm或Visual studio code内打开latest_officesnap.py文件

6. office_snap.py为获取工程名称和工程介绍

7. latest_officesnap.py为获取负责该工程企业的官网链接

8. 该脚本可用于配合snovi使用抓取企业关键联系人的邮箱信息，可用于自动化抓取数据；抓取的数据由Smartreach去进行自动化发开发信；最终形成一套开发信系统

5. 后期优化：动态爬取/多线程/使用scrapy库爬区/保存到sql和mongdb数据库里面



