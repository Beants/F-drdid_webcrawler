# python_webcrawler1
预期目标： 完成爬取网站f-droid.org数据的工作，并进行数据分析
## 现在已经实现的功能（爬虫部分）
* 爬取app的名称，并建立相应文件
* 爬取app介绍页网址，并下载相应文件，保存在app文件夹内
* 爬取app的版本信息，并分别建立文件夹
* 爬取app的apk和asc文件下载地址，并保存在app文件夹内
* 爬取app的源码地址（已支持github、gitlab、bitbucket，其余尚未清楚），并保存该地址到log中，同时使用git clong到app对应文件夹




### [INSTALL：配置、编译和安装该项目的说明信息](https://github.com/Beants/F-drdid_webcrawler/blob/master/INSTALL.md)

#### 运行
在终端中键入如下命令：

```
python webcrawler.py
```

#### 注意
* 文件目录结构
  * **文件总目录** -> **log文件**（一种是保存所有信息，另一种是保存git信息）和 **文件夹**（ 以APP名字命名，有多个）
  * **文件夹**（以APP名字命名）->   **源码文件**（clone生成的）与  **文件夹**（以版本号命名）
  * **文件夹**（以版本号命名）-> **apk文件** 和 **签名文件**

### [CREDITS：](https://github.com/Beants/F-drdid_webcrawler/blob/master/CREDITS.md)

#### 贡献者
* Name:Andersen Mail:beantsxu@gmail.com
* Name:Greta    Mail:854467335@qq.com


### [NEWS：](https://github.com/Beants/F-drdid_webcrawler/blob/master/NEWS.md)

#### 10-11月完成如下工作：

* 建立文件夹，在文件夹中切换
* 获取主页的url并翻页
* 获取主页html，并分析出app介绍页的url
* 获取app的名字 id 包名
* 获取app的版本号
* 获取每一个app版本的apk文件，签名文件，并保存到对应文件夹
* 获取Github的克隆地址并克隆到对应文件夹

### [HISTORY：](https://github.com/Beants/F-drdid_webcrawler/blob/master/HISTORY.md)

#### 历史发展演变记录
* 10-11月份：完成项目的初级编写工作，完成如下功能：
    * 建立文件夹，在文件夹中切换
		* 获取主页的url并翻页
		* 获取主页html，并分析出app介绍页的url
		* 获取app的名字 id 包名
		* 获取app的版本号
		* 获取每一个app版本的apk文件，签名文件，并保存到对应文件夹
		* 获取Github的克隆地址并克隆到对应文件夹
* 接下来需要完善的工作：
		* 完善源代码的克隆
		* 优化下载速度
		* 采用多线程

### [COPYING：](https://github.com/Beants/F-drdid_webcrawler/blob/master/COPYING.md)
```
GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc.
```

### [LICENS：](https://github.com/Beants/F-drdid_webcrawler/blob/master/LICENSE.md)

* 详见文档

#### [MANIFEST：](https://github.com/Beants/F-drdid_webcrawler/blob/master/MANIFEST)

* 文件列表详见文件

### [FAQ：](https://github.com/Beants/F-drdid_webcrawler/blob/master/FAQ.md)

1. 问： 程序怎么运行？
答： 查看Install.md文件

2. 问： 程序生成的文件目录结构是怎样的？
答： 查看Install.md文件

3. 问：怎么提交Bug？
答： 给贡献者发送邮件
