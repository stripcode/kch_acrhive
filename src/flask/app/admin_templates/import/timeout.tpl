<div class="alert alert-danger">Дождитесь сообщения об окончании загрузки.
<br>Загрузка может занять 5 - 10 минут.
<br>Страница обновится через <b id="timeout">30</b> секунд.</div>
<script>
  window.onload = function(){
    setTimeout(function(){
      window.location.reload()
    }, 30000);
    var i = 29
    setInterval(function(){
      el = document.getElementById('timeout');
      el.innerHTML = i;
      i--;
    }, 1000);
  };
</script>