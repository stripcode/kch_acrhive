{% extends "private.tpl" %}

{% block content %}
<h2>Отправка Email по всему жилфонду</h2>
<form method="post">
  <p class="alert alert-info">
    <b>Шаблон сообщения</b>
    <br>
    Уважаемый {fio}, Вам, поступило информационное сообщение для лицевого счета №{number} из личного кабинета УЖК "Наш дом".
    <br>Вы можете войти в личный кабинет по ссылке {site}.
    <br>{message}
  </p>
  <div class="form-group">
    <textarea name="message" class="form-control" required></textarea>
  </div>
  <button class="btn btn-primary" type="submit">Отправить</button>
</form>
{% endblock %}