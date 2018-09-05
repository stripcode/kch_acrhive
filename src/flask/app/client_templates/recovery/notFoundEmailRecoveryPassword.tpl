{% extends "public.tpl" %}

{% block content %}
  <p>К лицевому счету не привязан email. Пожалуйста обратитесь в управляющую компанию.</p>
  <a href="{{ url_for('ClientPage.recoveryPassword') }}" class="btn btn-default">Попрробовать еще раз</a>
{% endblock %}