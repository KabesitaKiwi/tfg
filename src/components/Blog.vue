<template>
  <section id="blog" class="my-5">
    <div class="container">
      <h2 class="text-center mb-4">Bienvenid@ a mi tienda</h2>
      <div class="card">
        <div class="card-body">
          <h3 class="card-title text-center">OFERTAS PARA NUEVOS CLIENTES</h3>
          <div class="row align-items-center mt-4">
            <div class="col-md-6">
              <p>
                ¡Espero que te encanten nuestras joyas y aprendas algo nuevo en cada visita! <br />
                Aprovecha nuestra promoción 2x1 en joyas. Disfruta de descuentos exclusivos y una calidad inigualable en nuestros productos. ¡No dejes pasar esta oportunidad! <br />
                ¡Da igual cuando leas esto!
              </p>
            </div>
            <div class="col-md-6 text-center">
              <img src="../assets/images/2x1.png" alt="Oferta 2x1 en joyas" class="img-fluid rounded w-100" />
            </div>
          </div>
        </div>
      </div>

      <!-- Sección de Usuarios -->
      <div class="card mt-4">
        <div class="card-body">
          <h3 class="card-title text-center">Usuarios Registrados</h3>
          <ul v-if="usuarios.length">
            <li v-for="usuario in usuarios" :key="usuario.id">
              {{ usuario.nombre }}
            </li>
          </ul>
          <p v-else>Cargando usuarios...</p>
        </div>
      </div>

      <!-- Sección de Comentarios -->
      <div class="card mt-4">
        <div class="card-body">
          <h3 class="card-title text-center">Comentarios</h3>
          <ul class="list-group mb-3">
            <li v-for="comment in comments" :key="comment.id" class="list-group-item d-flex justify-content-between align-items-start">
              <div>
                <strong>{{ comment.username }}</strong>: {{ comment.text }}
              </div>
              <small class="text-muted">{{ comment.created_at }}</small>
            </li>
          </ul>
          <form @submit.prevent="submitComment">
            <div class="mb-3">
              <label for="username" class="form-label">Nombre</label>
              <input type="text" id="username" class="form-control" v-model="newComment.username" required />
            </div>
            <div class="mb-3">
              <label for="text" class="form-label">Comentario</label>
              <textarea id="text" class="form-control" v-model="newComment.text" rows="3" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Enviar Comentario</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "Blog",
  setup() {
    const usuarios = ref([]);
    const comments = ref([]);
    const newComment = ref({
      username: "",
      text: ""
    });

    // Obtener usuarios de la API
    const fetchUsuarios = async () => {
  try {
      const res = await fetch("http://127.0.0.1:8000/usuarios"); // URL del backend FastAPI
      const data = await res.json();
      usuarios.value = data.usuarios; // Accede al array dentro del objeto JSON
    } catch (error) {
      console.error("Error al obtener usuarios:", error);
    }
  };

    // Obtener comentarios de la API (si la API existe)
    const fetchComments = async () => {
      try {
        const res = await fetch("/api/comments"); // Asegúrate de que esta API está definida en FastAPI
        comments.value = await res.json();
      } catch (error) {
        console.error("Error al obtener comentarios:", error);
      }
    };

    // Simular agregar un comentario
    const submitComment = () => {
      if (!newComment.value.username || !newComment.value.text) return;

      const newCommentResponse = {
        id: Date.now(),
        username: newComment.value.username,
        text: newComment.value.text,
        created_at: new Date().toLocaleString()
      };

      comments.value.push(newCommentResponse);

      newComment.value.username = "";
      newComment.value.text = "";
    };

    // Ejecutar funciones al cargar la página
    onMounted(() => {
      fetchUsuarios();
      fetchComments();
    });

    return { usuarios, comments, newComment, submitComment };
  }
};
</script>

<style scoped>
/* Estilos personalizados */
</style>
