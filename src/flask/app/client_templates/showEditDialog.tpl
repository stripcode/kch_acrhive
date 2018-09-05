{% extends "private.tpl" %}

{% block content %}
<div class="row">
  <div class="col-md-6">
    <form method="post">
      <div class="form-group">
        <label>Телефон</label>
        <input type="text" name="telephone" class="form-control" value="{{ client.telephone }}" autofocus />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input type="text" name="email" class="form-control" value="{{ client.email }}" />
      </div>
      <button class="btn btn-primary" type="submit">Сохранить</button>
      <a class="btn btn-default" href="{{ url_for('ClientPage.defaultPrivatePage') }}" type="button">Отмена</a>
    </form>
  </div>
</div>
{% endblock %}