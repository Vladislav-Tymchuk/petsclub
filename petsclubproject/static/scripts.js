searchBTN.onclick = function() {
  var username = document.getElementById("usernameINPUT").value;
  document.getElementById("goToProfile").removeAttribute("href");
  document.getElementById("goToProfile").setAttribute("href", `http://127.0.0.1:8000/profile/${username}/`);
}