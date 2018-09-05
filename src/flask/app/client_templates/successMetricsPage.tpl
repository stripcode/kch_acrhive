{% extends "private.tpl" %}

{% block content %}
  <p class="alert alert-success">Показания успешно приняты</p>
  <a class="btn btn-default" href='{{ url_for("ClientPage.showMetricsPage") }}'>Вернуться к передаче показаний</a>
{% endblock %}