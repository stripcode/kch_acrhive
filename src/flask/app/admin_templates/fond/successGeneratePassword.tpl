{% extends "private.tpl" %}

{% block content %}
<p>
  Письмо со сгенерированным паролем успешно принято к отправке.
</p>
<a href="{{ url_for('Fond.showFondClientPage', clientId = client.id) }}" class="btn btn-default">Вернутся к информации об абоненте</a>
{% endblock %}