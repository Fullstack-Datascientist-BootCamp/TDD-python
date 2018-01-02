# 安装环境
你需要安装python3。 使用python2.7运行下面的测试会报错

你需要安装并使用pipenv，攻略在[这里](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)


# 运行单元测试

运行单元测试的方式有三种。在根目录（即TDD-python）下


搜索并运行全部测试用例（一般用于提交代码前的整体测试）
```
python3 -m unittest discover tests
```


运行某个特定的单元测试文件
```
python3 -m unittest tests.test_scorer
```

运行某个特定的单元测试模块

```
python3 -m unittest tests.test_scorer.TestScore
```



# 根据测试修改代码
现在第二个测试是错的，把代码改对，使得测试能够通过

学习保龄球计分方法会有些帮助
