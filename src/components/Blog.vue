<template>
  <section id="blog" class="my-5">
    <div class="container">
      <h2 class="text-center mb-4">Bienvenid@ a mi tienda</h2>
      
      <!-- OFERTAS PARA NUEVOS CLIENTES -->
      <div class="card">
        <div class="card-body">
          <h3 class="card-title text-center">OFERTAS PARA NUEVOS CLIENTES</h3>
          <!-- Contenedor con fila de Bootstrap -->
          <div class="row align-items-center mt-4">
            <!-- Columna de texto -->
            <div class="col-md-6">
              <p>
                ¡Espero que te encanten nuestras joyas y aprendas algo nuevo en cada visita! <br>
                Aprovecha nuestra promoción 2x1 en joyas. Disfruta de descuentos exclusivos y una calidad inigualable en nuestros productos. ¡No dejes pasar esta oportunidad! <br>
                ¡Da igual cuanodo leas esto!
              </p>
            </div>
            <!-- Columna de imagen -->
            <div class="col-md-6 text-center">
              <img src="../assets/images/2x1.png" alt="Oferta 2x1 en joyas" class="img-fluid rounded w-100">
            </div>
          </div>
        </div>
      </div>
      <br>
      <br>
      
      <!-- CARRUSEL: LOS MÁS VENDIDOS -->
      <div class="card">
        <div class="card-body">
          <h3 class="card-title text-center">Los más vendidos</h3>
          <div id="carrusel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
            <!-- Indicadores -->
            <div class="carousel-indicators">
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="1" aria-label="Slide 2"></button>
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="2" aria-label="Slide 3"></button>
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="3" aria-label="Slide 4"></button>
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="4" aria-label="Slide 5"></button>
              <button type="button" data-bs-target="#carrusel" data-bs-slide-to="5" aria-label="Slide 6"></button>
            </div>
            <!-- Imágenes del Carrusel -->
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img src="../assets/images/esposa.png" class="d-block" alt="Imagen 1">
              </div>
              <div class="carousel-item">
                <img src="../assets/images/corazonEspinos.png" class="d-block w-35" alt="Imagen 2">
              </div>
              <div class="carousel-item">
                <img src="../assets/images/pato.png" class="d-block w-35" alt="Imagen 3">
              </div>
              <div class="carousel-item">
                <img src="../assets/images/arosConCorazon.png" class="d-block w-35" alt="Imagen 4">
              </div>
              <div class="carousel-item">
                <img src="../assets/images/hojas.png" class="d-block w-35" alt="Imagen 5">
              </div>
              <div class="carousel-item">
                <img src="../assets/images/pendulo.png" class="d-block w-35" alt="Imagen 6">
              </div>
            </div>
            <!-- Controles de Navegación -->
            <button class="carousel-control-prev" type="button" data-bs-target="#carrusel" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Anterior</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carrusel" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Siguiente</span>
            </button>
          </div>
        </div>
      </div>
      <br>
      <br>
      
      <!-- SECCIÓN DE COMENTARIOS -->
      <div class="card">
        <div class="card-body">
          <h3 class="card-title text-center">Comentarios</h3>
          <!-- Lista de Comentarios -->
          <ul class="list-group mb-3">
            <li v-for="comment in comments" :key="comment.id" class="list-group-item d-flex justify-content-between align-items-start">
              <div>
                <strong>{{ comment.username }}</strong>: {{ comment.text }}
              </div>
              <small class="text-muted">{{ comment.created_at }}</small>
            </li>
          </ul>
          <!-- Formulario para agregar un nuevo comentario -->
          <form @submit.prevent="submitComment">
            <div class="mb-3">
              <label for="usernameComment" class="form-label">Nombre</label>
              <input type="text" id="usernameComment" class="form-control" v-model="newComment.username" required>
            </div>
            <div class="mb-3">
              <label for="commentText" class="form-label">Comentario</label>
              <textarea id="commentText" class="form-control" v-model="newComment.text" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Enviar Comentario</button>
          </form>
        </div>
      </div>
      <br>
      <br>
      
      <!-- SECCIÓN PARA PREGUNTAS (Pregúntanos) -->
      <div class="card">
        <div class="card-body">
          <h3 class="card-title text-center">Pregúntanos</h3>
          <form @submit.prevent="submitQuestion">
            <!-- Fila para Nombre y Asunto -->
            <div class="row">
              <div class="col-md-6 mb-3">
                <label for="questionName" class="form-label">Nombre</label>
                <input type="text" id="questionName" class="form-control" v-model="newQuestion.name" required>
              </div>
              <div class="col-md-6 mb-3">
                <label for="questionSubject" class="form-label">Asunto</label>
                <input type="text" id="questionSubject" class="form-control" v-model="newQuestion.subject" required>
              </div>
            </div>
            <!-- Fila para Email -->
            <div class="row justify-content-center">
              <div class="col-md-6 mb-3 text-center">
                <label for="questionEmail" class="form-label">Email</label>
                <input type="text" id="questionEmail" class="form-control mx-auto" v-model="newQuestion.email" required>
              </div>
            </div>
            <!-- Campo de Mensaje -->
            <div class="mb-3">
              <label for="questionMessage" class="form-label">Mensaje</label>
              <textarea id="questionMessage" class="form-control" v-model="newQuestion.message" rows="3" required></textarea>
            </div>
            <!-- Mensajes de error y éxito para preguntas -->
            <div v-if="questionEmailError" class="alert alert-danger">
              {{ questionEmailError }}
            </div>
            <div v-if="questionSuccessMessage" class="alert alert-success">
              {{ questionSuccessMessage }}
            </div>
            <!-- Botón de enviar -->
            <div class="d-grid">
              <button type="submit" class="btn btn-primary">Enviar pregunta</button>
            </div>
          </form>
        </div>
      </div>
      
    </div>
  </section>
</template>

<script>
export default {
  name: 'Blog',
  data() {
    return {
      comments: [],
      newComment: {
        username: "",
        text: ""
      },
      // Datos para el formulario de preguntas
      newQuestion: {
        name: '',
        subject: '',
        email: '',
        message: ''
      },
      emailError: "",         // Para manejar errores del formulario de comentarios (si es necesario)
      successMessage: "",     // Para mostrar mensaje de éxito en comentarios
      questionEmailError: "", // Para manejar errores del formulario de preguntas
      questionSuccessMessage: "" // Para mostrar mensaje de éxito en preguntas
    };
  },
  methods: {
    fetchComments() {
      fetch('/api/comments')
        .then(response => response.json())
        .then(data => {
          this.comments = data;
        })
        .catch(error => console.error('Error fetching comments:', error));
    },
    validateEmail(email) {
      const gmailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;
      return gmailRegex.test(email);
    },
    submitComment() {
      // Simula una respuesta exitosa creando un comentario con un ID único y fecha actual
      const newCommentResponse = {
        id: Date.now(),
        username: this.newComment.username,
        text: this.newComment.text,
        created_at: new Date().toLocaleString()
      };
      // Agrega el comentario simulado a la lista
      this.comments.push(newCommentResponse);
      // Limpia el formulario
      this.newComment.username = "";
      this.newComment.text = "";
    },
    // Método para enviar preguntas
    submitQuestion() {
      // Resetea mensajes previos para el formulario de preguntas
      this.questionEmailError = "";
      this.questionSuccessMessage = "";
      
      // Validar que el email sea de @gmail.com en el formulario de preguntas
      if (!this.validateEmail(this.newQuestion.email)) {
        this.questionEmailError = "El correo debe ser @gmail.com";
        setTimeout(() => {
          this.questionEmailError = "";
        }, 3000);
        return;
      }
      
      // Simula una respuesta exitosa con un ID único y fecha actual
      const newQuestionResponse = {
        id: Date.now(),
        name: this.newQuestion.name,
        subject: this.newQuestion.subject,
        email: this.newQuestion.email,
        message: this.newQuestion.message,
        created_at: new Date().toLocaleString()
      };
      
      // Simulación: mostramos un mensaje de éxito
      this.questionSuccessMessage = "Pregunta enviada con éxito";
      
      // Limpia el formulario de preguntas
      this.newQuestion.name = "";
      this.newQuestion.subject = "";
      this.newQuestion.email = "";
      this.newQuestion.message = "";
      
      // Oculta el mensaje de éxito después de 3 segundos
      setTimeout(() => {
        this.questionSuccessMessage = "";
      }, 3000);
    }
  },
  mounted() {
    this.fetchComments();
  }
};
</script>

<style scoped>
/* Puedes agregar estilos adicionales si lo necesitas */
</style>
