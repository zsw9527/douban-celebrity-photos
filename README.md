# 如何使用

## 首先用pip安装bs4和requests
> pip install bs4

> pip install requests

## 安装完库后，打开命令行进入douban_catcher.py所在目录，执行以下命令，命令行第一个参数就是想要下载的明星相册url，比如下面这个例子中的https://movie.douban.com/celebrity/1044702/photos/

> python douban_catcher.py https://movie.douban.com/celebrity/1044702/photos/

> 相册url地址格式是这样的: https://movie.douban.com/celebrity/XXX/photos/

## 打开D盘目录，照片会下载到"celebrity" 这个目录下，这个例子是基于windows平台，使用者可自己在代码中修改要保存的路径
