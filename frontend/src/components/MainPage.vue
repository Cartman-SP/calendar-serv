<template>
  <div class="main">
    <ModalPage v-if="showModal" :result="modalResult" @closeModal="closeModal" />
  </div>
</template>

<script>
import ModalPage from './ModalPage.vue';
import axios from 'axios';

export default {
  components: { ModalPage },
  data() {
    return {
      showModal: false,
      modalResult: 0,
    };
  },
  mounted() {
    this.checkUserProfile();
  },
  methods: {
    async checkUserProfile() {
      try {
        const response = await axios.post('http://sked.online/api/checkprofile/' + this.$store.getters.getRegistrationData.user_id);
        console.log(response.data)
        // Проверяем результат и показываем модальное окно при необходимости
        if (response.data == 0) {
          this.showModal = true;
          this.modalResult = 0;
          console.log('окно показанно')
        } else {
          this.showModal = false;
          this.modalResult = 1;
          console.log('окно ')

        }
      } catch (error) {
        console.error('Ошибка при выполнении запроса:', error);
      }
    },
    closeModal() {
      this.showModal = false;
    },
  },
};
</script>

<style scoped>
</style>
