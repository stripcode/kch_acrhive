{% extends "public.tpl" %}

{% block content %}
<div class="row">
  <div class="col-md-6">
    <h2>Востановление пароля </h2>
    <form method="post">
      <div class="form-group">
        <label>Логин (номер лицевого счета)</label>
        <input class="form-control" type="text" name="login" autofocus required />
      </div>
      <button type="submit" class="btn btn-primary">Восстановить</button>
      <a href="/" class="btn btn-default">Отмена</a>
    </form>
  </div>
</div>
{% endblock %}