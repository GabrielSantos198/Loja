// Open/Close DropDown
window.document.getElementById('chk').checked = false
function dropdown(){
  var chk = window.document.getElementById('chk')
  if(chk.checked){
    window.document.getElementsByClassName('dropdown')[0].style.height = '0px'
  }else{
    window.document.getElementsByClassName('dropdown')[0].style.height = '500px'
  }
}

