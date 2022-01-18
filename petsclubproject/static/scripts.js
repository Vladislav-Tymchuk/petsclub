searchBTN.onclick = function() {

  var username = document.getElementById("usernameINPUT").value;
  if (username == '') {
    document.getElementById("goToProfile").removeAttribute("href");
  }
  else {
    document.getElementById("goToProfile").removeAttribute("href");
    document.getElementById("goToProfile").setAttribute("href", `http://127.0.0.1:8000/profile/${username}/`);
  }
}