###在github上创建新分支
- 在github上创建仓库：
- create a new repository on the command line

- touch README.md
- git init
- git add README.md
- git commit -m "first commit"
- git remote add origin git@github.com:zhudingsuifeng/python.git
- git push -u origin master
- 一般来说，master就是默认的主分支


- 在本地新建一个分支：git branch B1
- 切换到你的新分支：git checkout B1
- 将新分支发布在github上：git push origin B1
- 在本地删除一个分支：git branch -d B1
- 在github远程端删除一个分支：git push origin :B1(分之名前的冒号代表删除)



- 直接使用git pull和git push的设置
- Git branch  --set-upstream-to =origin/master master
- git branch  --set-upstream-to =origin/ThirdParty ThirdParty
- git config --global push.default matching

###使用sublimetext搭建Python开发环境
- 前面准备，首先要安装Python和Github和sublimetext
- 在安装sublimentext后，使用ctrl+shift+P打开控制面板，安装install Package
- 安装sublimecodeintel,sublimeREPL
- 安装GitGutter插件，然后在sublime的preferences-Package Settings下的GitGutter-Settings User添加 
{
"git_binary": "git.exe目录，注意\转义字符，最后要到git.exe"
}
- 安装Anaconda（号称最强的Python IDE插件），这个插件和前面的不是很好的搭配，但是既然安装了就要彻底解决麻烦，可以参考http://www.cnblogs.com/nx520zj/p/5787393.html


###windows下使用cmd安装numpy和matplotlib出现常见问题：
- permission error:在cmd下执行需要管理员的命令时，没有管理员权限。
- 在C:\Windows\System32下找到cmd.exe文件，右键，以管理员身份运行。
- python3.5.2版本里有pip，因此只需要更新一下就可以了：Python -m pip install -U pip ,显示Requirement already up-to-date:就是说要求已经更新
- 还需要安装wheel: pip install wheel
- 安装Numpy: pip install Numpy
- 安装Matplotlib: pip install Matplotlib
![pip安装插件](images/pip安装插件.jpg)