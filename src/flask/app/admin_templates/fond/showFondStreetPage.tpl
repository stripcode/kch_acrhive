{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / <a href="/fond/{{ city }}/">{{ city }}</a> / {{ street }}
</p>
<ul class="list-unstyled">
{% for house in houses %}
  <li><a href="/fond/{{ city }}/{{ street }}/{{ house[0] }}/">дом №{{ house[0] }}</li>
{% endfor %}
</ul>
{% endblock %}