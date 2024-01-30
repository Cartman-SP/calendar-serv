import { createRouter} from "vue-router";

import HelloPage from "./components/HelloPage.vue";
import EnterPage from "./components/EnterPage.vue";

export default createRouter({
    routes: [
        { path: '/', component: HelloPage},
        { path: '/login', component: EnterPage},
    ]
});