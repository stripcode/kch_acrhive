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
        <div class="col-md-2">
          <ul class="nav nav-pills nav-stacked">
            <li>
              <a href="{{ url_for('ClientPage.defaultPrivatePage') }}">Главная</a>
            </li>
            <li>
              <a href="{{ url_for('ClientPage.showMetricsPage') }}">Показания</a>
            </li>
            <li>
              <a href="{{ url_for('ClientPage.showPayPage') }}">Оплата</a>
            </li>
            <li>
              <a href="{{ url_for('ClientPage.logout') }}">Выход</a>
            </li>
          </ul>
        </div>
        <div class="col-md-10">
          {% block content %}{% endblock %}
        </div>
      </div>
    </div>
    <script type="text/javascript" src="/static/app.js"></script>
  </body>
</html>