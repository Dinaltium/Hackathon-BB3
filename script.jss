function login() {
  // Perform login logic (e.g., validate credentials, show/hide containers)
  const loginForm = document.getElementById('loginForm');
  const uploadContainer = document.getElementById('uploadContainer');

  if (loginForm && uploadContainer) {
    loginForm.style.display = 'none';
    uploadContainer.style.display = 'block';
  }
}

function uploadProduct() {
  // Perform product upload logic (e.g., send data to the server)
  // You may want to use AJAX or fetch API to send data to the server
  alert('Product uploaded successfully!');

  const uploadForm = document.getElementById('uploadForm');
  const uploadContainer = document.getElementById('uploadContainer');
  const bidContainer = document.getElementById('bidContainer');

  if (uploadForm && uploadContainer && bidContainer) {
    uploadForm.reset();
    uploadContainer.style.display = 'none';
    bidContainer.style.display = 'block';
  }
}
