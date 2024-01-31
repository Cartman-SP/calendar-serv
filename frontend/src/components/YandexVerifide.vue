<template>
    <div>
      <h1>Yandex Verify</h1>
      <div>
        <p>Access Token: {{ $route.query.access_token }}</p>
        <p>Token Type: {{ $route.query.token_type }}</p>
        <p>Expires In: {{ $route.query.expires_in }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    mounted() {
      // Вывод данных в консоль при загрузке компонента
      console.log('Access Token:', this.$route.query.access_token);
      console.log('Token Type:', this.$route.query.token_type);
      console.log('Expires In:', this.$route.query.expires_in);
    }
  };
  </script>
  
  
  <style>
  /* Добавьте стили, если необходимо */
  </style>
  