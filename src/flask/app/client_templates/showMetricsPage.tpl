{% extends "private.tpl" %}

{% block content %}
<div class="row">
  <div class="col-md-7">
    <h3>Передача показаний за {{ months[month[-2:]] }} {{ month[:-2] }}</h3>
    <div class="alert alert-info">Показания текущего месяца принимаются до 25 числа включительно текущего месяца. Если вы неверно передали показания вы можете их отредактировать до указанной даты.</div>
    <form method="post">
    {% for pu in client.pus %}
      <div class="form-group">
        <label>{{ pu.serviceName }}, 1-ое показание{% if pu.serial %}, с/н №{{ pu.serial }}{% endif %}</label>
        <input type="text" name="{{ pu.id }}:m1" class="form-control metric" value="{% if pu.id in currentMetrics %}{{ currentMetrics[pu.id][0] }}{% endif %}">
        {% if pu.id in lastMetrics %}
        <span id="helpBlock" class="help-block">Предыдущее показание {{ lastMetrics[pu.id][0] }}</span>
        {% endif %}
      </div>
      {% if pu.service == "11" %}
      <div class="form-group">
        <label>{{ pu.serviceName }}, 2-ое показание{% if pu.serial %}, с/н №{{ pu.serial }}{% endif %}</label>
        <input type="text" name="{{ pu.id }}:m2" class="form-control metric" value="{% if pu.id in currentMetrics %}{{ currentMetrics[pu.id][1] }}{% endif %}">
        {% if pu.id in lastMetrics %}
        <span id="helpBlock" class="help-block">Предыдущее показание {{ lastMetrics[pu.id][1] }}</span>
        {% endif %}
      </div>
      {% endif %}
    {% endfor %}
      <button class="btn btn-primary" type="submit">Сохранить</button>
    </form>
  </div>
</div>
{% endblock %}