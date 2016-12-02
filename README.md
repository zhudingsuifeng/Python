***在github上创建新分支
在github上创建仓库：
create a new repository on the command line

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:zhudingsuifeng/python.git
git push -u origin master
一般来说，master就是默认的主分支


在本地新建一个分支：git branch B1
切换到你的新分支：git checkout B1
将新分支发布在github上：git push origin B1
在本地删除一个分支：git branch -d B1
在github远程端删除一个分支：git push origin :B1(分之名前的冒号代表删除)



直接使用git pull和git push的设置
Git branch  --set-upstream-to =origin/master master
git branch  --set-upstream-to =origin/ThirdParty ThirdParty
git config --global push.default matching