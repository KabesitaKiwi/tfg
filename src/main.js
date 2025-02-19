import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'
// Importa Bootstrap Bundle JS (incluye Popper.js)
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import './custom.sass'  // Tu CSS personalizado después de Bootstrap

createApp(App).mount('#app')
