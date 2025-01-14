 // Función para verificar la sesión
 function checkSession() {
    fetch('/check_session/', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            if (data.session_expired) {
                window.location.href = '/logout/';  // Redirigir a logout si la sesión ha expirado
            }
        })
        .catch(error => console.error('Error al verificar la sesión:', error));
}

// Detectar clics en cualquier parte de la página
document.addEventListener('click', function() {
    checkSession();  // Comprobar sesión en cada clic
});