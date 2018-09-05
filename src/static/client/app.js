import 'bootstrap/dist/css/bootstrap.css'
import "./custom.css"

$(document).ready(function(){
  var loginInputMask = new Inputmask({mask: "9{3,10}-99"});
  loginInputMask.mask($("input[name=login]"))

  var loginInputMask = new Inputmask({mask: "9{1,10}.99", placeholder: "0"});
  loginInputMask.mask($("input.metric"))

  var debtInputMask = new Inputmask({mask: "9{1,10}.99", placeholder: "0"});
  debtInputMask.mask($("input.debt"))
});