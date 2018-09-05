{% extends "private.tpl" %}

{% block content %}
<ul class="list-unstyled">
{% for city in cities %}
  <li><a href="/fond/{{ city[0] }}/">{{ city[0] }}</li>
{% endfor %}
</ul>
{% endblock %}