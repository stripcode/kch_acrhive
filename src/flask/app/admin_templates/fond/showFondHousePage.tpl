{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / <a href="/fond/{{ city }}/">{{ city }}</a> / <a href="/fond/{{ city }}/{{ street }}/">{{ street }}</a> / дом №{{ house }}
</p>
<ul class="list-unstyled">
{% for client in clients %}
  <li><a href="/fond/client/{{ client.id }}/">кв.№{{ client.flatNumber }} {{ client.fio }} (л/с №{{ client.number }})</li>
{% endfor %}
</ul>
{% endblock %}