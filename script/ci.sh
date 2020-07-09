if [ ! -n "$1" ]; then
  echo 缺少提交内容
  exit 1
fi

if [ ! -d "./.gitNote" ]; then
  touch ./.gitNote
fi

date > ./.gitNote

git add .
git ci -m $1
