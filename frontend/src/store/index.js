// store/index.js

import { createStore } from 'vuex';
import createPersistedState from "vuex-persistedstate";

export default createStore({
  plugins: [createPersistedState()],
  state: {
    registrationData: {
      user_id: null,
      email: null,
      phone: null,
    },
    activeProjectId: null,
    isActive: false,

    updateSidebar: false,

    clients: {},
  },
  mutations: {
    addClients(state, data){
      state.clients = data;
    },

    setUpdateSidebar(state) {
      state.updateSidebar = !state.updateSidebar;
    },

    setActiveProject(state, projectId) {
      state.activeProjectId = projectId;
      state.isActive = true;
    },
    deactivateProject(state) {
      state.activeProjectId = null;
      state.isActive = false;
    },

    setRegistrationData(state, { user_id, email, phone }) {
      state.registrationData.user_id = user_id;
      state.registrationData.email = email;
      state.registrationData.phone = phone; 
  
      localStorage.setItem('registrationData', JSON.stringify(state.registrationData));
    },
    clearRegistrationData(state) {
      state.registrationData.user_id = null;
      state.registrationData.email = null;
      state.registrationData.phone = null;

      // Очищаем данные в localStorage
      localStorage.removeItem('registrationData');
    },
    // Добавляем мутацию для восстановления состояния из localStorage
    restoreRegistrationData(state) {
      const savedData = localStorage.getItem('registrationData');
      if (savedData) {
        const parsedData = JSON.parse(savedData);
        state.registrationData.user_id = parsedData.user_id;
        state.registrationData.email = parsedData.email;
        state.registrationData.phone = parsedData.phone;
      }
    },
  },
  actions: {
    saveRegistrationData({ commit }, responseData) {
      const user_id = responseData.user_id || null;
      const email = responseData.email || null;
      const phone = responseData.phone || null;

      commit('setRegistrationData', { user_id, email, phone });
    },
    clearRegistrationData({ commit }) {
      commit('clearRegistrationData');
    },
  },
  getters: {
    getRegistrationData(state) {
      return state.registrationData;
    },
  },
});
