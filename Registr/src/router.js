import { createRouter, createWebHashHistory} from "vue-router";

import HelloPage from "./components/HelloPage.vue";
import EnterPage from "./components/EnterPage.vue";
import RegPage from "./components/RegPage.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: HelloPage, alias: '/'},
        { path: '/login', component: EnterPage},
        { path: '/register', component: RegPage},
    ]
});