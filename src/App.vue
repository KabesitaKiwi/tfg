<template>
  <div id="app">
    <Header />
    <main class="container my-4">
      <Blog />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue"; // Asegúrate de que existe este archivo
import Blog from "./components/Blog.vue"; // Importa el componente Blog.vue correctamente
import Footer from "./components/Footer.vue"; // Asegúrate de que este archivo existe

export default {
  name: "App",
  components: {
    Header,
    Blog,
    Footer,
  },
};
</script>

<style>
/* Estilos globales opcionales */
</style>
