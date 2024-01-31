import { createRouter, createWebHashHistory } from 'vue-router'
import HelloPage from '../components/HelloPage.vue'
import RegPage from '../components/RegPage.vue'
import EnterPage from '../components/EnterPage.vue'
import YandexVerify from '../components/YandexVerifide.vue'
const routes = [
  {
    path: '/',
    name: 'hello',
    component: HelloPage
  },
  {
    path: '/login',
    name: 'login',
    component: EnterPage,
  },
  {
    path: '/register',
    name: 'register',
    component: RegPage,
  },
  {
    path: '/yaverify',
    name: 'yaverify',
    component: YandexVerify,
    props: route => ({ query: route.query })
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
