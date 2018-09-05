{% extends "private.tpl" %}

{% block content %}
<h2>Импорт ПУ</h2>
<form enctype="multipart/form-data" method="post">
  <div class="form-group">
    <input type="file" name="file" class="form-control" required>
  </div>
  <div class="form-group">
    <div class="checkbox">
      <label>
        <input type="checkbox" name="yes"> Импортировать показания
      </label>
    </div>
  </div>
  <button class="btn btn-primary" type="submit">Импортировать</button>
</form>
{% endblock %}