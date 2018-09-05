{% extends "public.tpl" %}

{% block content %}
 <p>
 На вашу почту выслан пароль
 </p>
 <a href="{{ url_for('ClientPage.showLoginForm') }}" class="btn btn-default">Авторизоваться</a>
{% endblock %}