# python_webcrawler1
预期目标： 完成爬取网站f-droid.org数据的工作，并进行数据分析
## 现在已经实现的功能（爬虫部分）
* 爬取app的名称，并建立相应文件
* 爬取app介绍页网址，并下载相应文件，保存在app文件夹内
* 爬取app的版本信息，并分别建立文件夹
* 爬取app的apk和asc文件下载地址，并保存在app文件夹内
* 爬取app的源码地址（已支持github、gitlab、bitbucket，其余尚未清楚），并保存该地址到log中，同时使用git clong到app对应文件夹

## 将要实现的功能（数据分析功能）
* 训练分类器->什么对分类的影响比较大
* 统计代码特征->说明文本
* 尚待添加

## 现在已知的Bug
* 源码地址尚未完善
* 在Windows平台下中文乱码
* code.google.com无法访问，导致第28个应用源码无法下载，
* 位置原因，第38、40个应用github地址不正确，附上官网：https://dulleh.github.io/akhyou/