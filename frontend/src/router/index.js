import { createRouter, createWebHashHistory } from 'vue-router'
import HelloPage from '../components/HelloPage.vue'
import RegPage from '../components/RegPage.vue'
import EnterPage from '../components/EnterPage.vue'
import ResetPage from '../components/ResetPage.vue'
import ResetPasswordPage from '../components/ResetPasswordPage.vue'
import RecoveryPage from '../components/RecoveryPage.vue'
import MainPage from '../components/MainPage.vue'
import ServicePage from '../components/ServicePage.vue'
import CreatePage from '../components/CreatePage.vue'
import PersonalPage from '../components/PersonalPage.vue'
import BranchPage from '../components/BranchPage.vue'
import WidgetsPage from '../components/WidgetsPage.vue'
import EmployeesPage from '../components/EmployeesPage.vue'
import SettingsPage from '../components/SettingsPage.vue'
import CreateBranchPage from '../components/CreateBranchPage.vue'
import WidgetsSettingsPage from '../components/WidgetsSettingsPage.vue'
import LichniyCabinet from '../components/LichniyCabinet.vue'
import store from '../store';

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
    path: '/lk',
    name: 'lk',
    component: LichniyCabinet,
    meta: { requiresAuth: true },
    children: [
      {
        path: '/lk/widgets',
        name: 'widgets',
        component: WidgetsPage,
        meta: { requiresAuth: true },
      },
      {
        path: '/lk/widgets/settings',
        name: 'widgetsSettings',
        component: WidgetsSettingsPage,
        meta: { requiresAuth: true },
      },
      {
        path: '/lk/main',
        name: 'main',
        component: MainPage,
        meta: { requiresAuth: true }
      },
      {
        path:'/lk/service',
        name: 'service',
        component: ServicePage,
        meta: { requiresAuth: true }
      },
      {
        path:'/lk/service/create',
        name: 'create',
        component: CreatePage,
        meta: { requiresAuth: true }
      },
      {
        path: '/lk/personal',
        name: 'personal',
        component: PersonalPage,
        meta: { requiresAuth: true }
      },
      {
        path: '/lk/branch',
        name: 'branch',
        component: BranchPage,
        meta: { requiresAuth: true }
      },
      {
        path: '/lk/personal/employees',
        name: 'employees',
        component: EmployeesPage,
        meta: { requiresAuth: true }
      },
      {
        path: '/lk/settings',
        name: 'settings',
        component: SettingsPage,
        meta: { requiresAuth: true }
      },
      {
        path: '/lk/branch/createbranch',
        name: 'createbranch',
        component: CreateBranchPage,
        meta: { requiresAuth: true }
      },
      
    ]
  },
  {
    // Новый маршрут для перенаправления, если пользователь уже авторизован
    path: '/redirect-if-authenticated',
    redirect: to => {
      // Проверяем, авторизован ли пользователь
      if (store.getters.getRegistrationData.user_id) {
        // Если авторизован, перенаправляем на страницу /lk
        return '/lk';
      } else {
        // В противном случае, возвращаем изначальный путь
        return to.path;
      }
    },
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  await store.commit('restoreRegistrationData'); // Добавляем await, чтобы убедиться, что данные восстановлены

  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Если маршрут требует авторизации
    if (!store.getters.getRegistrationData.user_id) {
      // Если пользователь не авторизован, перенаправляем на страницу входа
      next('/');
    } else {
      // Если пользователь авторизован, разрешаем доступ
      next();
    }
  } else if (['hello', 'login', 'register', 'reset', 'resetpassword', 'recovery'].includes(to.name)) {
    // Если маршрут - страница hello, login, register, reset, resetpassword, recovery,
    // и пользователь авторизован, перенаправляем на /main
    if (store.getters.getRegistrationData.user_id) {
      next('/main');
    } else {
      // Если пользователь не авторизован, разрешаем доступ
      next();
    }
  } else {
    // Если маршрут не требует авторизации и не является страницей hello, login, register, reset, resetpassword, recovery,
    // разрешаем доступ
    next();
  }
});






export default router
