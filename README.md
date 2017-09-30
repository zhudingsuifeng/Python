## 一些在python使用过程中的基础知识
#### git问题
- git clone git@github.com:zhudingsuifeng/python.git  #克隆远程代码库到本地
- $git branch -a 查看所有分支(包括远程分支)
- master   #本地分支
- remotes/origin/master #远程分支
- git branch -d master   #删除本地分支，远程还是会显示分支
- git push origin --delete master  #删除远程分支，刷新网页，远程分支不见了
- git checkout master    #切换分支
- git merge branch1     #合并branch1到当前分支
### python
- centos7下安装python-pip
```javascript 
#yum install -y python-pip    #报错
No package python-pip available.
#yum -y install epel-release   #安装epel扩展源
#yum -y install python-pip     #只有就可以使用pip安装python的程序包了
#pip install SomePackage #Install a package from PyPI
pip show --files SomePackage #show what files were installed
pip list --outdated    #list what package are outdated
pip install --upgrade SomePackage #upgrade a package
pip uninstall SomePackage   #uninstall a package
pip search SomePackage    #search PyPI for packages
pip list    #to list installed packages
python2 -m pip list #列出在python2环境下安装的包
python2 -m pip uninstall numpy #删除python2环境下的numpy包
python2 -m pip install numpy==1.13.1    #在python2环境下安装指定版本的包
python2 -m pip install pandas #重新安装对numpy有依赖的pandas包
```
- pip list显示的结果是已经安装的软件包的版本，并不一定是真正实用的软件包的版本。
## 下面介绍一个遇到的实际问题：
- import skimage.measure as sm   #skimage是一个图像处理的包，在执行程序的时候报错
- ValueError: numpy.dtype has the wrong size, try recompiling.Expected 88, got 96.
- 执行的这段程序是我之前在虚拟机上执行过的，没有报过错。
- pip list #在虚拟机里显示numpy(1.13.1),在电脑上同样是numpy(1.13.1)
- 在python中也有个查看引用的包所使用的版本的方法。
- import numpy
- numpy.version.version #虚拟机里显示'1.13.1',电脑里显示'1.9.0',这就显示出不同了。
- numpy.__file__   #这个命令可以查看对应的文件位置。
- 其实都是电脑里面同时存在python2和python3惹的祸，两个不同版本的numpy分别安装在不同版本的python中。
```javascript
$python2
>>>import numpy
>>>numpy.version.version
'1.9.0'
>>>numpy.__file__
'/usr/lib64/python2.7/site-packages/numpy/__init__.pyc'
$python3
>>>import numpy
>>>numpy.version.version
'1.13.1'
>>>numpy.__file__
'/usr/lib64/python3.4/site-packages/numpy/__init__.py'
python2 -m pip uninstall numpy #卸载原有版本
python2 -m pip install numpy==1.13.1 #安装numpy1.13.1
python2 -m pip install pandas #重新安装对numpy有依赖的pandas包
import skimage.measure as sm   #运行成功
``` 
- 打开文件的两种方式略有不同：
```javascript
with open("../data/changefile.csv") as csvf:
	reader=csv.reader(csvf)
	print(type(reader))   #<type 'list'>
	print(len(reader))    #TypeError:object of type '_csv.reader' has no len() 
csf=open("../data/changefile.csv").readlines()
print(type(csf))       #<type 'list'>
print(len(csf))        #2918
```
