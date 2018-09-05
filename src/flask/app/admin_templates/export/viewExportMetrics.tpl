{% extends "private.tpl" %}

{% block content %}
<h2>Быстрый просмотр переданных показаний</h2>
<table class="table table-striped">
  <thead>
    <th>Месяц</th>
    <th>Время</th>
    <th>Абонент</th>
    <th>Счетчик</th>
    <th>1-ое показание</th>
    <th>2-ое показание</th>
  </thead>
  {% for metric in metrics %}
  {% set m = metric.m.split(";") %}
  <tr>
    <td>{{ months[metric.month[4:]] }} {{ metric.month[:4] }}</td>
    <td>{{ datetime.fromtimestamp(metric.time).strftime("%d.%m.%Y %H:%M") }}</td>
    <td><a href="{{ url_for('Fond.showFondClientPage', clientId = metric.id) }}" target="_blank">{{ metric.fio }} (л/с {{ metric.number }})<a></td>
    <td>
      счетчик №{{ metric.order }},  {{ serviceNames[metric.service] }} {% if metric.serial %}, с/н №{{ metric.serial }}{% endif %}
    </td>
    <td>
      {{ m[0] }}
    </td>
    <td>
      {% if metric.service == "11" %}
        {% if m[1] %}{{ m[1] }}{% endif %}
      {% endif %}
    </td>
  </tr>
  {% endfor %}
</table>
{% endblock %}