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
import axios from 'axios'
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'primeicons/primeicons.css'
import store from './store'
import InputSwitch from 'primevue/inputswitch';
import Breadcrumb from 'primevue/breadcrumb';
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';



store.commit('restoreRegistrationData');
const app = createApp(App).use(store);
app.config.globalProperties.$axios = axios
app.use(router).use(PrimeVue).mount('#app');
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