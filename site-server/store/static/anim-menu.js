document.getElementById("svg-menu-1").addEventListener("click", moveMenu);
document.getElementById("svg-menu-2").addEventListener("click", moveMenu);
document.getElementById("svg-menu-3").addEventListener("click", moveMenu);


document.addEventListener("click", function(event) {
  if (event.target.id !== "svg-menu-1" && event.target.id !== "svg-menu-2" && event.target.id !== "svg-menu-3") {
    moveMenu()
    resetMenu();
    showAdditionalElements();
  }
})

function moveMenu() {
  document.getElementById("svg-menu-1").classList.add("clicked");
  document.getElementById("svg-menu-2").classList.add("clicked");
  document.getElementById("svg-menu-3").classList.add("clicked");
}

function resetMenu() {
  document.getElementById("svg-menu-1").classList.remove("clicked");
  document.getElementById("svg-menu-2").classList.remove("clicked");
  document.getElementById("svg-menu-3").classList.remove("clicked");
}


function Flash(){
  document.getElementById("Flash_Button").submit();
  }