// Open/Close DropDown
var header = window.document.getElementsByTagName('header')[0]
if(header){
  window.document.getElementById('chk').checked = false
  function dropdown(){
    var chk = window.document.getElementById('chk')
    if(chk.checked){
      window.document.getElementsByClassName('dropdown')[0].style.height = '0px'
    }else{
      window.document.getElementsByClassName('dropdown')[0].style.height = '450px'
    }
  }
}

// Dark Theme
function DarkTheme(){
  localStorage.theme = 'dark'
  // Icon
  window.document.getElementsByClassName('bi')[2].classList.remove('bi-moon-stars-fill')
  window.document.getElementsByClassName('bi')[2].classList.add('bi-brightness-high')
  window.document.getElementsByClassName('bi')[13].classList.remove('bi-moon-stars-fill')
  window.document.getElementsByClassName('bi')[13].classList.add('bi-brightness-high')

  window.document.body.classList.add('dark')
}


// Light Theme
function DefaultTheme(){
  localStorage.theme = 'default'
  // Icon
  window.document.getElementsByClassName('bi')[2].classList.remove('bi-brightness-high')
  window.document.getElementsByClassName('bi')[2].classList.add('bi-moon-stars-fill')
  window.document.getElementsByClassName('bi')[13].classList.remove('bi-brightness-high')
  window.document.getElementsByClassName('bi')[13].classList.add('bi-moon-stars-fill')

  window.document.body.classList.remove('dark')
}


function theme(){
  var ThemeChk = window.document.getElementById('ThemeChk')
  if(ThemeChk.checked){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}


if(localStorage.theme){
  if(localStorage.theme == "dark"){
    DarkTheme()
  }else{
    DefaultTheme()
  }
}

