<template>
  <header>
    <!-- Navbar de Bootstrap -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-custom">
      <div class="container">
        <a class="navbar-brand" href="#">PIERCINGS KIWI</a>
        <img src="../assets/images/logo.png" alt="logo" width="12%">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item"><a class="nav-link" href="#nosotros">Quienes Somos</a></li>
            <li class="nav-item"><a class="nav-link" href="#blog">Blog</a></li>
            <li class="nav-item"><a class="nav-link" href="#pideCita">Pide Tu Cita</a></li>
            <li class="nav-item"><a class="nav-link" href="#tienda">Tienda Online</a></li>
            <li class="nav-item"><a class="nav-link" href="#about">Acerca de</a></li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <!-- Botón para abrir el modal de login -->
              <button class="btn btn-outline-light" @click="toggleLoginModal">Iniciar Sesión</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Modal de Login con Bootstrap -->
    <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="loginModalLabel">Iniciar Sesión</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="handleLogin">
              <div class="mb-3">
                <label for="username" class="form-label">Nombre de usuario:</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Contraseña:</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <div class="d-flex justify-content-between">
                <button type="button" class="btn btn-secondary" @click="handleRegister">Registrarse</button>
                <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'Header',
  setup() {
    const username = ref('')
    const password = ref('')
    let modalInstance = null

    // Inicializar el modal de Bootstrap al montar el componente
    onMounted(() => {
      const modalElement = document.getElementById('loginModal')
      modalInstance = new bootstrap.Modal(modalElement, {})
    })

    const toggleLoginModal = () => {
      modalInstance.show()
    }

    const handleLogin = () => {
      console.log('Iniciando sesión con:', username.value, password.value)
      // Aquí podrías integrar la lógica de autenticación vía API
      modalInstance.hide()
    }

    const handleRegister = () => {
      console.log('Acción de registro')
      // Aquí podrías redireccionar a una página de registro o mostrar otro modal
      modalInstance.hide()
    }

    return {
      username,
      password,
      toggleLoginModal,
      handleLogin,
      handleRegister
    }
  }
}
</script>

<style scoped>
/* Puedes agregar estilos adicionales o personalizados aquí si lo requieres */
</style>
