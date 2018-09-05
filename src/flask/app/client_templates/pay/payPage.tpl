{% extends "private.tpl" %}

{% block content %}
<form method="post">
  <div class="row">
   <div class="col-md-3">
    <div class="form-group">
      <input class="form-control debt" name="debt" value="{{ debt }}">
    </div>
    <button class="btn btn-primary" type="submit">Оплатить задолженость</button>
   </div>
   {% if penalty > 0 %}
   <div class="col-md-3">
    <div class="form-group">
      <input class="form-control debt" name="penalty" value="{% if penalty > 0 %}{{ penalty }}{% else %}0.00{% endif %}">
    </div>
    <button class="btn btn-primary" type="submit" name="penaltySubmit">Оплатить пени</button>
   </div>
   {% endif %}
  </div>
</form>
{% endblock %}