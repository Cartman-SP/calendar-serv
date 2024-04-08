import { createRouter, createWebHistory } from 'vue-router'
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
import ProjectPage from '../components/ProjectPage.vue';
import ProjectEditPage from '../components/ProjectEditPage.vue';
import ProjectGatesPage from '../components/ProjectGatesPage.vue';
import CreateProject from '../components/CreateProject.vue';
import AccessesPage from '../components/AccessesPage.vue';
import LockedPage from '../components/LockedPage.vue';
import WidgetCreatePage from '../components/WidgetCreatePage.vue';
import store from '../store';
import WidgetSite from '@/components/WidgetSite.vue';
import NProgress from 'nprogress'; // Импортируйте nprogress
import 'nprogress/nprogress.css'; // Импортируйте стили nprogress

const routes = [
 {
   path: '/',
   name: 'hello',
   component: HelloPage,
   meta: { title: 'Sked.Online - Hello' },
 },
 {
   path: '/login',
   name: 'login',  
   component: EnterPage,
   meta: { title: 'Sked.Online - Login' },
 },
 {
   path: '/register',
   name: 'register',
   component: RegPage,
   meta: { title: 'Sked.Online - Register' },
 },
 {
   path: '/reset',
   name: 'reset',
   component: ResetPage,
   meta: { title: 'Sked.Online - Reset' },
 },
 {
   path: '/resetpassword',
   name: 'resetpassword',
   component: ResetPasswordPage,
   meta: { title: 'Sked.Online - Reset password' },
 },
 {
   path: '/recovery',
   name: 'recovery',
   component: RecoveryPage,
   meta: { title: 'Sked.Online - Recovery' },
 },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: LichniyCabinet,
    meta: { requiresAuth: true },
    children: [
      {
        path: '/dashboard/widgets',
        name: 'widgets',
        component: WidgetsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Widgets' },
      },
      {
        path: '/dashboard/widgets/settings',
        name: 'widgetsSettings',
        component: WidgetsSettingsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Widgets settings' },
      },
      {
        path: '/dashboard/main',
        name: 'main',
        component: MainPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Main' }
      },
      {
        path:'/dashboard/service',
        name: 'service',
        component: ServicePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Service' }
      },
      {
        path:'/dashboard/service/create',
        name: 'create',
        component: CreatePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Create service' }
      },
      {
        path: '/dashboard/personal',
        name: 'personal',
        component: PersonalPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Personal' }
      },
      {
        path: '/dashboard/branch',
        name: 'branch',
        component: BranchPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Branch' }
      },
      {
        path: '/dashboard/personal/employees',
        name: 'employees',
        component: EmployeesPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Create personal' }
      },
      {
        path: '/dashboard/settings',
        name: 'settings',
        component: SettingsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Settings' }
      },
      {
        path: '/dashboard/branch/createbranch',
        name: 'createbranch',
        component: CreateBranchPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Create branch' }
      },
      {
        path: '/dashboard/project',
        name: 'project',
        component: ProjectPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Projects' }
      },
      {
        path: '/dashboard/project/edit',
        name: 'edit',
        component: ProjectEditPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Edit project' }
      },
      {
        path: '/dashboard/project/gates',
        name: 'gate',
        component: ProjectGatesPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Gates' }
      },
      {
        path: '/dashboard/project/new',
        name: 'new',
        component: CreateProject,
        meta: { requiresAuth: true, title: 'Sked.Online - New project' }
      },
      {
        path: '/dashboard/project/accesses',
        name: 'accesses',
        component: AccessesPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Accesses' }
      },
      {
        path: '/dashboard/locked',
        name: 'locked',
        component: LockedPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Locked' }
      },
      {
        path: '/dashboard/widgets/create',
        name: 'widget_create',
        component: WidgetCreatePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Create widget ' }
      }
    ]
  },
  {
    // Маршрут для виджета
    path: '/widget/:username/:widgetname',
    name: 'widget',
    component: WidgetSite,
    props: route => ({
      username: route.params.username,
      widgetname: route.params.widgetname
    })
  },
  {
    // Новый маршрут для перенаправления, если пользователь уже авторизован
    path: '/redirect-if-authenticated',
    redirect: to => {
      // Проверяем, авторизован ли пользователь
      if (store.getters.getRegistrationData.user_id) {
        // Если авторизован, перенаправляем на страницу /dashboard
        return '/dashboard';
      } else {
        // В противном случае, возвращаем изначальный путь
        return to.path;
      }
    },
  },
]
const router = createRouter({
  history: createWebHistory(),
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
      next('/dashboard');
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


router.beforeEach((to) => {
  document.title = to.meta?.title ?? 'Sked.Online'
})

router.beforeEach((to, from, next) => {
  // Запуск индикатора прогресса
  NProgress.start();
  NProgress.configure({ easing: 'ease', speed: 400 });
  NProgress.configure({ showSpinner: false });
  setTimeout(() => {
    next(); // Переход к следующему роуту после задержки
  }, 300);
});

router.afterEach(() => {
  // Завершение индикатора прогресса
  NProgress.done();
});

export default router
