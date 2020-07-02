# 简化命令
git config --local alias.ci commit
git config --local alias.st status

# 格式化最近一周的提交
git config --local alias.lg7 "log --graph --pretty=format:'^[%h]^ ^[%s]^ ^[%an]^ ^[%cd]^' --date=format:'%Y-%m-%d %H:%M:%S' --since=1.weeks"

# 格式化最近一个月的提交
git config --local alias.lg30 "log --graph --pretty=format:'^[%h]^ ^[%s]^ ^[%an]^ ^[%cd]^' --date=format:'%Y-%m-%d %H:%M:%S' --since=1.months"

# 删除之前的几个提交记录 git del 1
git config --local alias.del "!f() { git reset --hard HEAD~\$1; }; f"

chmod 777 ./ci.sh

# 拉到本地后断开与远程仓库的连接
# git remote remove origin

# 重新关联到远程仓库
# git remote add origin git@github.com:xxxx


