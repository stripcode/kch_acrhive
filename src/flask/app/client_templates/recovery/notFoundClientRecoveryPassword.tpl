{% extends "public.tpl" %}

{% block content %}
  <p>Лицевой счет не найден. Введите верный лицевой счет</p>
  <a href="{{ url_for('ClientPage.recoveryPassword') }}" class="btn btn-default">Попрробовать еще раз</a>
{% endblock %}