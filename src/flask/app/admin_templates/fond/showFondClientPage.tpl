{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / <a href="/fond/{{ client.cityName }}/">{{ client.cityName }}</a> / <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/">{{ client.streetName }}</a> /  <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/{{ client.houseNumber }}/">дом №{{ client.houseNumber }}</a> / кв.№{{ client.flatNumber }} {{ client.fio }} л/с №{{ client.number }}
</p>
<h3>Информация</h3>
<ul class="list-unstyled">
  <li>ФИО: {{ client.fio }}</li>
  <li>л/с: {{ client.number }}</li>
  <li>квартира: {{ client.flatNumber }}</li>
  <li>комната: {{ client.room }}</li>
  <li>телефон: {{ client.telephone }}</li>
  <li>email: {{ client.email }}</li>
  <li>долг: {{ client.debt }}</li>
  <li>пени: {{ client.penalty }}</li>
  <li>дата оплаты: {{ client.payDate }}</li>
</ul>
<a class="btn btn-default" href="/fond/client/{{ client.id }}/edit/" role="button">Редактировать</a>
<a class="btn btn-default {% if not client.email %} disabled {% endif %}" href="/fond/client/{{ client.id }}/generatePassword/" role="button">Сгенерировать пароль</a>
<a class="btn btn-default" href="/fond/client/{{ client.id }}/metrics/" role="button">Показания</a>
<ul class="list-unstyled">
<h3>Счетчики</h3>
{% for pu in client.pus %}
  <li> счетчик №{{ pu.order }}, {{ pu.serviceName }}{% if pu.serial %}, с/н №{{ pu.serial }}{% endif %}</li>
{% endfor %}
</ul>
{% endblock %}