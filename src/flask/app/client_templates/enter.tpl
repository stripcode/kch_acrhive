<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>УЖК Наш Дом</title>
    <link href="/static/vendor.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <h2>Личный кабинет УЖК "Наш дом" </h2>
          <form action="/enter/" method="post">
            <div class="form-group">
              <label>Логин (номер лицевого счета)</label>
              <input class="form-control" type="text" name="login" autofocus required />
            </div>
            <div class="form-group">
              <label>Пароль</label>
              <input class="form-control" type="password" name="password" required />
            </div>
            <button type="submit" class="btn btn-primary">Войти</button>
            <a href="/recovery/" class="btn btn-default">Воcстановление пароля</a>
          </form>
        </div>
      </div>
    </div>
    <script type="text/javascript" src="/static/app.js"></script>
  </body>
</html>