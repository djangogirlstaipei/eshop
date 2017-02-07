# Deploy to heroku

在 [heroku](https://www.heroku.com) 創建帳號，並且[安裝 Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

創建 heroku APP

```
heroku create
```

設定環境變數

```
heroku config:set DJANGO_SETTINGS_MODULE=bookshop.production_settings
```

把程式碼更新至 heroku

```
git push heroku master
```

migrate 資料庫

```
heroku run python bookshop/manage.py migrate
```

創建 superuser

```
heroku run python bookshop/manage.py createsuperuser
```

打開你的網站

```
heroku open
```

之後在更新網站的時候，只要記得 `git push heroku master` 即可
