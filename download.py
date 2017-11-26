# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
# 引入下载模块
import os


# 获取每一个程序的主页
def getUrlToAnotherPage(html, f):
    note = 'Getting the URL of download pages of each app.'
    print note + '  Strat!'
    f.write(note + '  Strat!\n')
    pattern_url = re.compile('<a class="package-header" href="/(.*?)">', re.S)
    result_url = re.findall(pattern_url, html)
    # 循环30次因为后6个数据不是
    result = range(30)
    for i in range(30):
        result[i] = 'https://f-droid.org/' + result_url[i]
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return result


# 在主页获取APP名字
def getAppName(html, f):
    note = 'Getting the name of each app.'
    print note + '  Start!'
    f.write(note + '  Start!\n')
    pattern_name = re.compile('<h4\sclass="package-name">(.*?)</h4>', re.S)
    result_name = re.findall(pattern_name, html)
    result = range(30)
    # 循环30次因为后6个数据不是
    del result_name[0]
    for i in range(30):
        result[i] = result_name[i][4:-3]
        # 【4:-3】 是因为爬下来的name有空格
        result[i] = result[i].replace('/', ' ')
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return result


# 分析二级页面，获取app下载地址
def getUrlOfAppDownload(html, f):
    # 传入二级页面地址，返回app下载地址
    note = 'Getting the download URL of each app.'
    print note + '  Start!'
    f.write(note + '  Start!\n')
    # 匹配apk下载地址
    pattern_apk = re.compile('<p class="package-version-download">.*?<a href="(.*?)">', re.S)
    result_apk = re.findall(pattern_apk, html)
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return result_apk


# 分析二级页面，获取版本号,返回list
def  getNumOfVersion(html, f):
    # 传入二级页面地址，返回version
    note = 'Getting the version number of each app.'
    print note + '  Start!'
    f.write(note + '   Start!\n')
    # 匹配版本号
    pattern_version = re.compile('<div class="package-version-header">.*?<b>(.*?)<',
                                 re.S)
    result_version = re.findall(pattern_version, html)
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return result_version


# 分析二级页面，获取签名下载地址,返回list
def getNumOfAsc(html, f):
    # 传入二级页面地址，返回asc下载地址
    note = 'Getting the Signature of each app.'
    print note + '  Start!'
    f.write(note + '  Start!\n')
    # 匹配签名下载地址
    pattern_asc = re.compile('<p class="package-version-download".*?a href=".*?">.*?<a href="(.*?)">', re.S)
    result_asc = re.findall(pattern_asc, html)
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return result_asc


# 获取list长度,返回int，用于检测版本的数量
def getLengthOfList(list):
    return list.__len__()


# 创建文件夹
def creatFolder(folderName, f):
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(folderName)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.mkdir(folderName)
        note = "\"" + folderName + '\" folder creation successful.'
        print note
        f.write(note + '\n')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        note = "\"" + folderName + '\" folder already exists.'
        print note
        f.write(note + '\n')
        return False


# 生成主页每一页的url，共45页
def nextUrl(url, i):
    # 如果是第一页则返回原网址
    if (i == 0):
        return url
    else:
        i = i + 1
        url=url+i.__str__()+'/'
        print url
        return url



# 获取APK的github地址
def getUrlOfGithub(html, f):
    # 传入二级页面地址，返回github
    note = 'Getting the Github of each app.'
    print note + '  Start!'
    f.write(note + '  Start!\n')
    # 匹配版本号

    pattern = re.compile('<li class="package-link">.*?<a href="(.*?)">', re.S)
    result = re.findall(pattern, html)
    len = result.__len__()
    for i in range(len):
        print "result"+i.__str__()+" "+result[i]
        if 'github.com' in result[i]:
            str = cutGithub(result[i])
            break
        elif 'bitbucket.org' in result[i]:
            str = cutGithub(result[i])
            break
        elif 'gitlab' in result[i]:
            str=cutGithub(result[i])
            break
        elif 'code.google.com' in result[i]:
            str=cutGithub(result[i])
            break
        else :
            str=cutGithub(result[i])
    print note + '  Done.'
    f.write(note + '  Done!\n')
    return str
#blob/HEAD/README.asciidoc


def cutGithub(url):
    str = url
    if 'issues' in url:
        str = url[0:-7]
    if 'README.asciidoc' in url:
        str = url[0:-26]
    if 'README.md' in url:
        str = url[0:-20]
    if 'wiki' in url:
        str = url[0:-5]
    if 'releases' in url:
        str = url[0:-9]
    if '/src' in url:
        str = url[0:-4]
    if '/overview' in url:
        str = url[0:-9]
    return str

# 克隆github到本地
def clone(url):
    os.system('git clone ' + url + '.git')



def download(url, f):
    note = "The file is downloading from " + url
    print note + '  Start!'
    f.write(note + '  Start!\n')
    file_name = url.split('/')[-1]
    if os.path.exists(file_name):
        no='Download failed.This file already exists.'
        print no
        f.write(no+'\n')
    else:
        urllib.urlretrieve(url, file_name)
        print note + '  Done.'
        f.write(note + '  Done!\n')


# sgy
def whereIAm():
    note = "Now the working directory is " + os.getcwd()
    print note
    return note + "\n"


def run():
    url = 'https://f-droid.org/en/packages/'
    # 主页每一页循环一次
    # 在主页生成log
    #flie_name = 'main.log'
    #f = open(flie_name, 'w')

    for i in range(45):
        flie_name = 'page'+i.__str__()+'.log'
        f = open(flie_name, 'w')
        f_git=open('url-git'+flie_name, 'w')
        note = '\n\n*************************************************************\nPage' + (i + 1).__str__()
        print note
        f.write(note+'\n')
        # 当前页面的url，主页
        urlNow = nextUrl(url, i)
        html = urllib2.urlopen(urlNow).read()
        # 程序名字，list，长度30
        appName = getAppName(html, f)
        # 获取二级页面的地址，list，长度30
        url2 = getUrlToAnotherPage(html, f)
        # 每一页有30个app，对每个APP的页面操作
        for j in range(30):

            print '\n*************************************************************\n'
            f.write('\n*************************************************************\n')
            note = "App Num." + (i * 30 + j + 1).__str__() + '   Name:' + appName[j]
            print note + "  Start!" + '\n*************************************************************'
            f.write(note + "  Start!\n")
            # 创建每个APP所对应的文件夹
            f.write(whereIAm())
            creatFolder(appName[j], f)

            os.chdir(appName[j])
            f.write(whereIAm())
            #  url2[j]  表示当前APP网页链接
            html = urllib2.urlopen(url2[j]).read()
            versionList = getNumOfVersion(html, f)
            ascList = getNumOfAsc(html, f)
            apkList = getUrlOfAppDownload(html, f)

            github = getUrlOfGithub(html, f)
            note1= "github:\n  " + github
            f_git.write(github+'\n')
            print note1
            f.write(note1+'\n')
            clone(github)
            #单独写入git信息，方便查错
            f_git.write('page:'+i.__str__()+' Num:'+j.__str__()+' Name: '+appName[j]+github+'\n')
            download(url2[j]+'/index.html',f)

            length = getLengthOfList(versionList)
            # 下载一个App的对应文件
            for x in range(length):
                # 创建版本文件夹
                creatFolder(versionList[x], f)
                # 进入版本文件夹
                os.chdir(versionList[x])
                whereIAm()
                download(apkList[x], f)
                download(ascList[x], f)
                os.chdir('..')  # 返回上级目录，也就是app的文件夹
            os.chdir('..')  # 返回上级目录，也就是项目根目录
            print note + "  Done!\n*************************************************************\n\n"
            f.write(note + "  Done!\n*************************************************************\n\n")

        f.close()
        f_git.close()

# 主程序


run()
