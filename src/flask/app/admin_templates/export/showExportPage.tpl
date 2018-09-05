{% extends "private.tpl" %}

{% block content %}
<h2>Экспорт показаний</h2>
<form method="post">
  <div class="row">
    <div class="form-group col-md-2">
      <input type="text" name="monthDate" class="form-control">
    </div>
  </div>
  <br>
  <button class="btn btn-primary" type="submit" name="view">Быстрый просмотр</button>
  <button class="btn btn-success" type="submit">Выгрузить в файл</button>
</form>
{% endblock %}