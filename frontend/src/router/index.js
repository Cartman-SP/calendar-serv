import { createRouter, createWebHashHistory } from 'vue-router'
import HelloPage from '../components/HelloPage.vue'
import RegPage from '../components/RegPage.vue'
import EnterPage from '../components/EnterPage.vue'
const routes = [
  {
    path: '/',
    name: 'hello',
    component: HelloPage
  },
  {
    path: '/login',
    name: 'login',
    component: RegPage,
  },
  {
    path: '/register',
    name: 'register',
    component: EnterPage,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
