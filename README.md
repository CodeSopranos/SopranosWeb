# SopranosWeb
The secret  and legendary web project of @CodeSopranos team
## GET STARTED:
[*setuping docker environment*](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)<br>
[*how to mount disk D in toolbox*](https://headsigned.com/posts/mounting-docker-volumes-with-docker-toolbox-for-windows/)

*!If you do not have volume **postgres_data** then run ```docker volume create postgres_database```*!

Build and up docker in dev mode:
 1. ```docker-compose build```<br>
 2. ```docker-compose up -d```<br>
 3. Then check dockerIP:8000/board/<br>

You can also to run django manage commands. <br>
For example, get into db ```docker-compose exec db psql --username=admin --dbname=admin ```

Run docker in prod mode:
 1. ```docker-compose -f docker-compose.prod.yml up -d --build```<br>
 2. Then check dockerIP:1337/board/<br>


**Критерии**<br>
```
Что должно быть в проектах:
1. База данных, мастер-детальные отношения +
2. Генерация страниц по шаблону +
3. Пользовательский контент (POST-формы с валидацией) +
4. Аутентификация пользователей, сессии (тема следующей лекции) +
5. Работа приложения под управлением внешнего веб-сервера (nginx/apache/..., тоже будет в лекциях)
6. Админка как минимум для тех частей приложения, 
   которые не доступны для изменения через общий пользовательский интерфейс

Идеи на доп. баллы (для тех, кто хочет 9-10):
1. Логика клиентского уровня (JS, ajax/json и т.п.)
2. Интеграция с внешними веб-сервисами
3. Аутентификация через google/FB/twitter/etc.
4. Мобильный клиент
5. Дизайн страниц
``` 
