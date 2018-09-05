{% extends "private.tpl" %}

{% block content %}
<form method="post">
<p>
  Вы действительно хотите сгененрироват пароль и отправить его на почту пользователю?
</p>
<button class="btn btn-primary" type="submit">Сгенерировать</button>
</form>
{% endblock %}