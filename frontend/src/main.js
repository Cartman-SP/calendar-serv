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
import axios from 'axios';
import 'primevue/resources/themes/aura-light-green/theme.css';
import 'primeicons/primeicons.css';
import store from './store';
import InputSwitch from 'primevue/inputswitch';
import Breadcrumb from 'primevue/breadcrumb';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';
import Tooltip from 'primevue/tooltip';
import Calendar from 'primevue/calendar';
// import GAuth from 'vue-google-oauth2'; // Проверьте путь к вашему плагину

// const gauthOption = {
//   clientId: '662724122488-l8brqvb93jkvm9c1tai4ce6gd8h88hrv.apps.googleusercontent.com',
//   scope: 'profile email',
//   prompt: 'select_account'
// };

store.commit('restoreRegistrationData');

const app = createApp(App).use(store);
app.config.globalProperties.$axios = axios;

app.use(router)
  //  .use(GAuth, gauthOption)
   .use(PrimeVue)
   .mount('#app');
app.component('DropdownComponent', Dropdown);
app.component('InputMaskComponent', InputMask);
app.component('PasswordComponent', Password);
app.component('InputTextComponent', InputText);
app.component('MenubarComponent', Menubar);
app.component('BadgeComponent', Badge);
app.component('InputSwitchComponent', InputSwitch);
app.component('BreadcrumbComponent', Breadcrumb);
app.component('TabViewComponent', TabView);
app.component('TabPanelComponent', TabPanel);
app.component('CalendarDisplay', Calendar);
app.directive('tooltip', Tooltip);
