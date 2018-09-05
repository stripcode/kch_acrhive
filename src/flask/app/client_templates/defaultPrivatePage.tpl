{% extends "private.tpl" %}

{% block content %}
<ul class="list-unstyled">
  <li>Адресс: {{ client.cityName }}, {{ client.streetName }}, дом №{{ client.houseNumber }}, кв.№{{ client.flatNumber }}</li>
  <li>ФИО: {{ client.fio }}</li>
  <li>л/с: {{ client.number[:-2] }}-{{ client.number[-2:] }}</li>
  <li>квартира: {{ client.flatNumber }}</li>
  <li>телефон: {{ client.telephone }}</li>
  <li>email: {{ client.email }}</li>
  <li>начисление за предыдущий расчетный период: {{ client.debt }} руб</li>
  <li>пени: {{ client.penalty }} руб</li>
  <li>дата оплаты: {{ client.payDate }}</li>
</ul>
<a href="{{ url_for('ClientPage.showEditDialog') }}" class="btn btn-default">Изменить email, телефон</a>
{% endblock %}