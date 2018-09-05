{% extends "private.tpl" %}

{% block content %}
<h2>Импорт лицевых счетов и задолжености</h2>
<form enctype="multipart/form-data" method="post">
  <div class="form-group">
    <input type="file" name="file" class="form-control" required>
  </div>
  <br>
  <button class="btn btn-primary" type="submit">Импортировать</button>
</form>
{% endblock %}