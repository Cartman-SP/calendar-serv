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
import RequestsPage from '../components/RequestsPage.vue';
import ClientsPage from '../components/ClientsPage.vue';
import ServiceEdit from '../components/ServiceEdit.vue';
import EmployeesEdit from '../components/EmployeesEdit.vue';
import BranchEdit from '../components/BranchEdit.vue';
import TariffPage from '../components/TariffPage.vue';
///import NotFoundPage from '../components/NotFoundPage.vue';
import CalendarPage from '../components/CalendarPage.vue';
import ClientsEditPage from '../components/ClientsEditPage.vue';
import ClientsCreatePage from '../components/ClientsCreatePage.vue';
import ClientsInfoPage from '../components/ClientsInfoPage.vue';
import HomePage from '../components/HomePage.vue';
import store from '../store';
import WidgetSite from '@/components/WidgetSite.vue';
import NProgress from 'nprogress'; // Импортируйте nprogress
import 'nprogress/nprogress.css'; // Импортируйте стили nprogress
import TestPage from '@/components/TestPage.vue'
const routes = [
  {
    path: "/:catchAll(.*)",
    name: 'NotFound',
    component: TestPage,
    meta: { title: 'Sked.Online - Not Found' },
  },
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
        meta: { requiresAuth: true, title: 'Sked.Online - Виджеты' },
      },
      {
        path: '/dashboard/widgets/settings/:widgetId',
        name: 'widgetsSettings',
        component: WidgetsSettingsPage,
        props: route => ({
          widgetId: route.params.widgetId,
        }),
        meta: { requiresAuth: true, title: 'Sked.Online - Настройка виджета' },
      },
      {
        path: '/dashboard/main',
        name: 'main',
        component: MainPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Главная' }
      },
      {
        path:'/dashboard/service',
        name: 'service',
        component: ServicePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Услуги' }
      },
      {
        path:'/dashboard/service/create',
        name: 'create',
        component: CreatePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Создание новой услуги' }
      },
      {
        path: '/dashboard/personal',
        name: 'personal',
        component: PersonalPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Сотрудники' }
      },
      {
        path: '/dashboard/branch',
        name: 'branch',
        component: BranchPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Филиалы' }
      },
      {
        path: '/dashboard/personal/employees',
        name: 'employees',
        component: EmployeesPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Создание нового сотрудника' }
      },
      {
        path: '/dashboard/settings',
        name: 'settings',
        component: SettingsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Настройки профиля' }
      },
      {
        path: '/dashboard/branch/createbranch',
        name: 'createbranch',
        component: CreateBranchPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Создание нового филиала' }
      },
      {
        path: '/dashboard/project',
        name: 'project',
        component: ProjectPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Мои проекты' }
      },
      {
        path: '/dashboard/project/edit',
        name: 'edits',
        component: ProjectEditPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Редиктирование проекта' }
      },
      {
        path: '/dashboard/project/gates/:project',
        name: 'gate',
        component: ProjectGatesPage,
        props: route => ({
          project: route.params.project,
        }),
        meta: { requiresAuth: true, title: 'Sked.Online - Доступы' }
      },
      {
        path: '/dashboard/project/new',
        name: 'new',
        component: CreateProject,
        meta: { requiresAuth: true, title: 'Sked.Online - Новый проект' }
      },
      {
        path: '/dashboard/project/accesses',
        name: 'accesses',
        component: AccessesPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Доступы' }
      },
      {
        path: '/dashboard/locked',
        name: 'locked',
        component: LockedPage,
        meta: { requiresAuth: true, title: 'Sked.Online - В этот раздел доступ закрыт' }
      },
      {
        path: '/dashboard/widgets/create',
        name: 'widget_create',
        component: WidgetCreatePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Создание виджета' }
      },
      {
        path: '/dashboard/requests',
        name: 'requests',
        component: RequestsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Заявки' }
      },
      {
        path: '/dashboard/clients',
        name: 'clients',
        component: ClientsPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Клиенты' }
      },
      {
        path: '/dashboard/calendar',
        name: 'calendar',
        component: CalendarPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Календарь' }
      },
      {
        path: '/dashboard/home',
        name: 'home',
        component: HomePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Главная' }
      },
      {
        path: '/dashboard/clients/:clientId/edit',
        props: route => ({
          clientId: route.params.clientId,
        }),
        name: 'edit',
        component: ClientsEditPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Редактирование' }
      },
      {
        path: '/dashboard/clients/create',
        name: 'createe',
        component: ClientsCreatePage,
        meta: { requiresAuth: true, title: 'Sked.Online - Создание клиента' }
      },
      {
        path: '/dashboard/tariff',
        name: 'tariff',
        component: TariffPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Тарифы' }
      },
      {
        path: '/dashboard/clients/:clientId/info',
        props: route => ({
          clientId: route.params.clientId,
        }),
        name: 'info',
        component: ClientsInfoPage,
        meta: { requiresAuth: true, title: 'Sked.Online - Информация о клиенте' }
      },
      {
        path: '/dashboard/service/:serviceToEditId/edit',
        props: route => ({
          serviceToEditId: route.params.serviceToEditId,
        }),
        name: 'ServiceEdit',
        component: ServiceEdit,
        meta: { requiresAuth: true, title: 'Sked.Online - Редактирование услуги' }
      },
      {
        path: '/dashboard/personal/:employeeToEditId/edit',
        props: route => ({
          employeeToEditId: route.params.employeeToEditId,
        }),
        name: 'EmployeesEdit',
        component: EmployeesEdit,
        meta: { requiresAuth: true, title: 'Sked.Online - Редактирование сотрудника' }
      },
      {
        path: '/dashboard/branch/:branchToEditId/edit',
        props: route => ({
          branchToEditId: route.params.branchToEditId,
        }),
        name: 'BranchEdit',
        component: BranchEdit,
        meta: { requiresAuth: true, title: 'Sked.Online - Редактирование филиала' }
      },
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
  }, 300)
});

router.afterEach(() => {
  // Завершение индикатора прогресса
  NProgress.done();
});

export default router
