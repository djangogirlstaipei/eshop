# 安裝 Vagrant

我們準備了 vagrant box 來協助 local 練習，如果已經有 ubuntu 16.04 機器的人可以略過這部分 。

[安裝 Vagrant](https://www.vagrantup.com) 以及 [VirtualBox](https://www.virtualbox.org)

啟動 vagrant

```
vagrant up
```

執行之後會啟動一個虛擬機器，灌好 ubuntu 16.04. 如果想連進去看看可以執行

```
vagrant ssh
```


# 使用說明

先修改 fabfile.py，設定好你要的參數。參數說明如下：

```
USER = 'vagrant'    # deploy 的使用者名稱
PROJECT_DIR = '/home/{USER}/project/eshop/'.format(USER=USER)  # project 的位置
GIT_REPOSITORY = 'https://github.com/daikeren/eshop'   # git repository 的位置
DB_USER = 'django'   # 資料庫使用者
DB_PASSWORD = 'django'   # 資料庫密碼
DB_NAME = 'eshop'  # 資料庫名稱
```

接下來執行 provision 來對機器做基本的設定。

```
fab -u vagrant --port=2222 -H localhost provision
```

provision 會安裝 Linux 基本需要的套件，並且設定好 nginx, systemd, postgresql 安裝的套件
可以參考 fabfile.py 當中的 install_packages 這個 function. 設定檔則放在 config 這個目錄

可以透過 manage 這個 fabric command 來執行 manage.py 相關的指令

```
fab -u vagrant --port=2222 -H localhost manage:createsuperuser
```

當程式碼修改過，commit 進遠方的 git repository 之後，可以透過 deploy 來做 deployment

```
fab -u vagrant --port=2222 -H localhost deploy
```

最後打開 http://localhost:8080 即可看到網站