{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / <a href="/fond/{{ client.cityName }}/">{{ client.cityName }}</a> / <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/">{{ client.streetName }}</a> /  <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/{{ client.houseNumber }}/">дом №{{ client.houseNumber }}</a> / кв.№{{ client.flatNumber }} {{ client.fio }} л/с №{{ client.number }}
</p>

<table class="table">

{% for metric in metrics %}
  <tr>
    <td>{{ metric.month[4:] }}.{{ metric.month[:4] }}</td>
    <td>{{ datetime.fromtimestamp(metric.time).strftime("%d.%m.%Y %H:%M") }}</td>
    <td>
      счетчик №{{ metric.pu.order }},  {{ metric.pu.serviceName }} {% if metric.pu.serial %}, с/н №{{ metric.pu.serial }}{% endif %}
    </td>
    <td>
      {{ metric.m[0] }}
    </td>
    <td>
      {% if metric.m[1] %}{{ metric.m[1] }}{% endif %}
    </td>
  </tr>
{% endfor %}
</table>
{% endblock %}