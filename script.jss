function login() {
  // Perform login logic (e.g., validate credentials, show/hide containers)
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Perform your login logic here (e.g., check credentials, show/hide containers)
  if (username === 'admin' && password === 'admin') {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('uploadContainer').style.display = 'block';
  } else {
    alert('Invalid credentials. Please try again.');
  }
}

function uploadProduct() {
  // Perform product upload logic (e.g., send data to the server)
  // You may want to use AJAX or fetch API to send data to the server
  alert('Product uploaded successfully!');
  document.getElementById('uploadForm').reset();
}
