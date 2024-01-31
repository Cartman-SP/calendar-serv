import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import Dropdown from 'primevue/dropdown';
import InputMask from 'primevue/inputmask';
import Password from 'primevue/password';
import InputText from 'primevue/inputtext';
import Menubar from 'primevue/menubar';
import Badge from 'primevue/badge';


import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'


const app = createApp(App);
app.use(router).use(PrimeVue).mount('#app');

app.component('DropdownComponent', Dropdown);
app.component('InputMaskComponent', InputMask);
app.component('PasswordComponent', Password);
app.component('InputTextComponent', InputText);
app.component('MenubarComponent', Menubar);
app.component('BadgeComponent', Badge);