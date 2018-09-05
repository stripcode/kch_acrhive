import 'bootstrap/dist/css/bootstrap.css'
import "./custom.css"
import "eonasdan-bootstrap-datetimepicker"
import "eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css"

$(document).ready(function(){
  $("input[name=beginDate]").datetimepicker({
    format: "DD.MM.YYYY",
    defaultDate: moment(),
    locale: "ru"
  });

  $("input[name=endDate]").datetimepicker({
    format: "DD.MM.YYYY",
    defaultDate: moment(),
    locale: "ru"
  })
  $("input[name=monthDate]").datetimepicker({
    format: "MM.YYYY",
    defaultDate: moment(),
    locale: "ru"
  });
});