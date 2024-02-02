<template>
    <div style="bottom: 0%; position: absolute;">
      <div v-if="userData">
        <p><strong>Телефон:</strong> {{ userData.phone }}</p>
        <p><strong>Email:</strong> {{ userData.email }}</p>
      </div>
      <div v-else>
        <p>Данные пользователя отсутствуют.</p>
      </div>
      <button @click="logout">Выйти</button>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      userData() {
        return this.$store.getters.getRegistrationData;
      },
    },
    methods: {
      logout() {
        // Вызываем действие clearRegistrationData для очистки данных из Vuex
        this.$store.dispatch('clearRegistrationData');
        this.$router.push('/');
      },
    },
  };
  </script>
  
  <style scoped>
  /* Ваши стили здесь */
  </style>
  