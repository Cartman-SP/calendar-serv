import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import Dropdown from 'primevue/dropdown';

import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'


const app = createApp(App);
app.use(router).use(PrimeVue).mount('#app');
app.component('DropdownComponent', Dropdown);