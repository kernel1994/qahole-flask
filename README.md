# A web project powered by Flask

## Abstract
就不写简介了（方丈别打我啊）

## Run
- Web API (Flask project)
    on Windows CMD, in backend:
    ```
    set FLASK_APP=api
    set FLASK_ENV=development
    flask run
    ```
    Listen on `http://127.0.0.1:5000/api/*`

- Web Page (Vue project)
    on Windows CMD, in frontend:
    ```
    npm run dev
    ```
    Listen on `http://127.0.0.1:8081`

- Nginx
    <details>
      <summary>add in `conf/nginx.conf`</summary>
      ```
      upstream webpage {
          server localhost:8081;
      }

      upstream webapi {
          server localhost:5000;
      }

      server {
          listen       8080;
          server_name  localhost;

          #charset koi8-r;

          #access_log  logs/host.access.log  main;

          location / {
              proxy_pass http://webpage;

              proxy_set_header Host            $host;
              proxy_set_header X-Real-IP       $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          }

          location /api/ {
              proxy_pass http://webapi;
          }

          #error_page  404              /404.html;

          # redirect server error pages to the static page /50x.html
          #
          error_page   500 502 503 504  /50x.html;
          location = /50x.html {
              root   html;
          }
      }
      ```
    </details>

    on Windows CMD:
    ```
    start nginx
    ```
    or restart config:
    ```
    nginx -s reload
    ```

Now head over to `http://127.0.0.1:8080`

## TODO
- [x] 前后端分离
- [x] RESTful API
- [ ] 响应式样式
- [ ] 评论加载、个人页等功能
- [ ] 滚动加载
- [ ] 全局搜索
- [ ] 精选、备注
- [ ] ORM

## See Also
- Backend
    - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - [Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
    - [Flask 之旅](https://spacewander.github.io/explore-flask-zh/)
    - [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html)
- Frontend
    - [Vue](https://vuejs.org/)
