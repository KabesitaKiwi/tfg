<template>
  <header>
    <!-- Navbar con Bootstrap -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-custom">
      <div class="container">
        <a class="navbar-brand" href="#">PIERCINGS KIWI</a>
        <img src="../assets/images/logo.png" alt="logo" width="100" class="ms-2">

        <!-- Botón hamburguesa -->
        <button class="navbar-toggler" type="button" @click="toggleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" :class="{'show': isNavbarOpen}" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item"><a class="nav-link" href="#nosotros">Quienes Somos</a></li>
            <li class="nav-item"><a class="nav-link" href="#blog">Blog</a></li>
            <li class="nav-item"><a class="nav-link" href="#pideCita">Pide Tu Cita</a></li>
            <li class="nav-item"><a class="nav-link" href="#tienda">Tienda Online</a></li>
            <li class="nav-item"><a class="nav-link" href="#about">Acerca de</a></li>
          </ul>

          <!-- ✅ Si el usuario está autenticado, muestra su nombre en lugar del botón -->
          <span v-if="user" class="text-white ms-auto">Bienvenido, {{ user.nombre }}</span>
          <button v-else class="btn btn-outline-light ms-auto" @click="toggleLoginModal">Iniciar Sesión</button>
        </div>
      </div>
    </nav>

    <!-- Modal de Login con Bootstrap -->
    <div class="modal fade" :class="{'show d-block': isLoginModalOpen}" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Iniciar Sesión</h5>
            <button type="button" class="btn-close" @click="toggleLoginModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="handleLogin">
              <div class="mb-3">
                <label for="email" class="form-label">Correo electrónico:</label>
                <input type="text" class="form-control" id="email" v-model="email" required>
              </div>
              <div class="mb-3">
                <label for="password" class="form-label">Contraseña:</label>
                <input type="password" class="form-control" id="password" v-model="contraseña" required>
              </div>
              <div class="d-flex justify-content-between">
                <button type="button" class="btn btn-secondary" @click="handleRegister">Registrarse</button>
                <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
              </div>
            </form>
            <p v-if="errorMessage" class="text-danger mt-2">{{ errorMessage }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Fondo oscuro del modal -->
    <div v-if="isLoginModalOpen" class="modal-backdrop fade show" @click="toggleLoginModal"></div>
  </header>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'Header',
  setup() {
    const email = ref('');
    const contraseña = ref('');
    const isLoginModalOpen = ref(false);
    const isNavbarOpen = ref(false);
    const user = ref(null);
    const errorMessage = ref('');

    const toggleLoginModal = () => {
      isLoginModalOpen.value = !isLoginModalOpen.value;
      errorMessage.value = '';
    };

    const toggleNavbar = () => {
      isNavbarOpen.value = !isNavbarOpen.value;
    };

    const handleLogin = async () => {
      try {
        console.log("Enviando datos al backend...");

        const response = await fetch('http://127.0.0.1:8000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: email.value,
            contraseña: contraseña.value
          })
        });

        if (!response.ok) {
          throw new Error("Usuario o contraseña incorrectos");
        }

        const data = await response.json();
        console.log("Respuesta recibida:", data);

        user.value = data; // Guarda el usuario autenticado
        isLoginModalOpen.value = false; // Cierra el modal

      } catch (error) {
        console.error("Error en la petición:", error);
        errorMessage.value = error.message;
      }
    };

    const handleRegister = () => {
      console.log('Acción de registro');
      isLoginModalOpen.value = false;
    };

    return {
      email,
      contraseña,
      isLoginModalOpen,
      isNavbarOpen,
      user,
      errorMessage,
      toggleLoginModal,
      toggleNavbar,
      handleLogin,
      handleRegister
    };
  }
};
</script>

<style scoped>
/* Evita que el modal quede bloqueado en pantalla */
.modal.fade {
  display: none;
}

.modal.show {
  display: block;
  animation: fadeIn 0.3s ease-in-out;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1040;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
