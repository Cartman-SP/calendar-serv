import { createRouter, createWebHashHistory } from 'vue-router'
import HelloPage from '../components/HelloPage.vue'
import RegPage from '../components/RegPage.vue'
import EnterPage from '../components/EnterPage.vue'
import ResetPage from '../components/ResetPage.vue'
import ResetPasswordPage from '../components/ResetPasswordPage.vue'
import RecoveryPage from '../components/RecoveryPage.vue'
import MainPage from '../components/MainPage.vue'
import DataTestPage from '../components/DataTestPage.vue'
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
    path: '/reset',
    name: 'reset',
    component: ResetPage,
  },
  {
    path: '/resetpassword',
    name: 'resetpassword',
    component: ResetPasswordPage,
  },
  {
    path: '/recovery',
    name: 'recovery',
    component: RecoveryPage,
  },
  {
    path: '/main',
    name: 'main',
    component: MainPage,
  },
  {
    path:'/profile',
    name: 'profile',
    component: DataTestPage
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
