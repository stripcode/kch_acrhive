{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / {{ city }}
</p>
<ul class="list-unstyled">
{% for street in streets %}
  <li><a href="/fond/{{ city }}/{{ street[0] }}/">{{ street[0] }}</li>
{% endfor %}
</ul>
{% endblock %}