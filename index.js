
function background() {
    document.querySelectorAll('.hideable').forEach(el => el.classList.toggle('hidden'));
  }

function foreground() {
    document.querySelectorAll('.hideable').forEach(el => el.classList.toggle('hidden'));
  }

  document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const subject = document.getElementById("sub").value;
    const content = document.getElementById("content").value;
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    if (!subject) {
      alert("Subject is required");
      return;
    }

    if (!content) {
      alert("Message is required");
      return;
    }

    if (!name) {
      alert("Name is required");
      return;
    }

    if (!email) {
      alert("Email is required");
      return;
    }

    if (!validateEmail(email)) {
      alert("Invalid email address");
      return;
    }

    alert("Form submitted successfully");
  });



// rohith male
// 2-13-23
// ucid: rm982

