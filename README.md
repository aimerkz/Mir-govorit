# Тестовое задание для Mir govorit

Для запуска необходим Docker:


```bash
$ git clone https://github.com/aimerkz/mir-govorit.git
$ cd mir-govorit
$ cp env.example .env
$ docker-compose up -d
```
Документация к API: [Mir-govorit API](http://127.0.0.1:8001/api/docs/)

Админка: [Админка](http://127.0.0.1:8001/admin/)
```
Логин: admin
Пароль: admin
```
[show_recipes_without_product с параметром product_id](http://127.0.0.1:8001/show_recipes_without_product/1/)
