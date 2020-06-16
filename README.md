The secret  and legendary web project of @CodeSopranos team. <br>
---
- The project provides an opportunity to create **dashboards** based on parsed tags on social media or social networks e.g. *Twitter*. <br>
- Dashboards contains **figures** that can describe some extracted informations from the parsed data. <br>
- There is possibility to create public or private dashboard. Public dashboards will appear in feed page.<br>

## GET STARTED:
[*setuping docker environment*](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)<br>
[*how to mount disk D in toolbox*](https://headsigned.com/posts/mounting-docker-volumes-with-docker-toolbox-for-windows/)

*!If you do not have volume **postgres_data** then run ```docker volume create postgres_data```*!

Build and up docker in dev mode:
 1. ```docker-compose build```<br>
 2. ```docker-compose up -d```<br>
 3. Then check dockerIP:8000/board/<br>

You can also to run django manage commands. <br>
For example, get into db ```docker-compose exec db psql --username=admin --dbname=admin ```

Run docker in prod mode:
 1. ```docker-compose -f docker-compose.prod.yml up -d --build```<br>
 2. Then check dockerIP:1337/board/<br>

**Team**:
- Ilya Sedunov
- Vadim Alperovich
