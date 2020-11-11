# django-ipam

#### 介绍
Django admin 实现的IP地址管理工具

#### Installation for development
添加国内镜像源，修改setup.cfg，在最后添加如下配置：
```text
[easy_install]
index_url = https://mirrors.aliyun.com/pypi/simple/
```

Install django-ipam for development using following commands:
```bash
git clone https://github.com/xujunfei/django-ipam.git
cd django-ipam
python setup.py develop
pip install -r requirements-test.txt
```
##### 关于`python setup.py develop`命令
1. 按照requirements.txt文件安装依赖包
2. 添加sys.path，具体是在site-packages文件夹下生成了\.pth文件
3. 之后可以用命令`python setup.py develop -u`删除包

Launch the development sever:
```bash
cd tests/
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```


