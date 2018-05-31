var loginDetails = document.getElementById("login-form");
loginDetails.addEventListener("submit", function(evt) {
  evt.preventDefault();
  loginFunction();
});
function login() {
  var email = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  if (email == "admin" && password == "root") {
    window.location.href = "admindash.html";
  } else {
    window.location.href = "usersdash.html";
  }
}
