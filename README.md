# 托管在GitHub上的博客

## 安装ruby(ubuntu)

用snap安装会出现问题，参见这个[github issue](https://github.com/eventmachine/eventmachine/issues/881).

```bash
# 如果通过snap安装了ruby, 需要执行以下命令卸载.
# sudo snap remove ruby
gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash -s stable --rails
```

## 安装运行环境

安装依赖
```bash
gem install bundler jekyll
jekyll new my-awesome-site
```
(不知道这里为啥还要安装)
```
cd my-awesome-site
bundle install
```

## 构建并启动

```
bundle exec jekyll serve
```