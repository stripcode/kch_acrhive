{% extends "private.tpl" %}

{% block content %}
{% if result.ready() and result.failed() %}
  <div class="alert alert-danger">Импорт завершился ошибкой</div>
  <p>{{result.result }}</p>
  <a href="{{ url_for('Import.showMetricsImportForm') }}" class="btn btn-default">Импортировать еще раз</a>
{% elif result.ready() and not result.failed() %}
  <div class="alert alert-success">Загрузка завершена</div>
  <a href="{{ url_for('Import.showMetricsImportForm') }}" class="btn btn-default">Импортировать еще раз</a>
{% else %}
  {% include "import/timeout.tpl" %}
{% endif %}
{% endblock %}