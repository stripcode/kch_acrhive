{% extends "private.tpl" %}

{% block content %}
<p>
  <a href="/fond/">Города</a> / <a href="/fond/{{ client.cityName }}/">{{ client.cityName }}</a> / <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/">{{ client.streetName }}</a> /  <a href="/fond/{{ client.cityName }}/{{ client.streetName }}/{{ client.houseNumber }}/">дом №{{ client.houseNumber }}</a> / кв.№{{ client.flatNumber }} {{ client.fio }} л/с №{{ client.number }}
</p>
<div class="row">
  <div class="col-md-6">
    <form method="post">
      <div class="form-group">
        <label>Город</label>
        <input type="text" name="cityName" class="form-control" value="{{ client.cityName }}" autofocus required />
      </div>
      <div class="form-group">
        <label>Улица</label>
        <input type="text" name="streetName" class="form-control" value="{{ client.streetName }}" required />
      </div>
      <div class="form-group">
        <label>Дом</label>
        <input type="text" name="houseNumber" class="form-control" value="{{ client.houseNumber }}" required />
      </div>
      <div class="form-group">
        <label>Корпус</label>
        <input type="text" name="buildingName" class="form-control" value="{{ client.buildingName }}" />
      </div>
      <div class="form-group">
        <label>Квартира</label>
        <input type="text" name="flatNumber" class="form-control" value="{{ client.flatNumber }}" required />
      </div>
      <div class="form-group">
        <label>л/с</label>
        <input type="text" name="number" class="form-control" value="{{ client.number }}" required />
      </div>
      <div class="form-group">
        <label>ФИО</label>
        <input type="text" name="fio" class="form-control" value="{{ client.fio }}" required />
      </div>
      <div class="form-group">
        <label>Телефон</label>
        <input type="text" name="telephone" class="form-control" value="{{ client.telephone }}" />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input type="text" name="email" class="form-control" value="{{ client.email }}" />
      </div>
      <div class="form-group">
        <label>Долг</label>
        <input type="text" name="debt" class="form-control" value="{{ client.debt }}" required />
      </div>
      <div class="form-group">
        <label>Пени</label>
        <input type="text" name="penalty" class="form-control" value="{{ client.penalty }}" required />
      </div>
      <button class="btn btn-primary" type="submit">Сохранить</button>
    </form>
  </div>
</div>
{% endblock %}