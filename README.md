# 托管在GitHub上的博客

## 安装ruby(ubuntu)

用snap安装会出现问题，参见这个[github issue](https://github.com/eventmachine/eventmachine/issues/881).

```bash
sudo apt install ruby2.7 ruby2.7-dev
```

也可以使用rvm安装。

## 安装运行环境

```bash
gem install bundler
cd my-awesome-site
bundle install
```

## 构建并启动

```bash
bundle exec jekyll serve
```