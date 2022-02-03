let p = document.querySelector("#pass");

let p1 = document.querySelector("#pass1");
function validatePassword() {
if (p.value != p1.value) {
    p1.setCustomValidity("Passwords Don't Match");
  } else {
    p1.setCustomValidity('');
  }
}

p.onchange = validatePassword;
p1.onkeyup = validatePassword;

