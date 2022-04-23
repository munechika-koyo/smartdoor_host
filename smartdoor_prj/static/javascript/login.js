// scripts of showing pwd at login form
const showPasswordToggle = document.getElementById("pwd-eye");
const password = document.getElementById("id_password");

showPasswordToggle.addEventListener("click", function () {
    if (password.type === "password") {
        password.type = "text";
        showPasswordToggle.className = "fas fa-eye show-pwd-toggle";
    }
    else {
        password.type = "password";
        showPasswordToggle.className = "fas fa-eye-slash show-pwd-toggle";
    }
}, false);
