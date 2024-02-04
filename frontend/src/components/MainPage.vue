<template>
  <div class="main">
    <router-view></router-view>
    <div class="navigation">
      <SidebarPage />
      <NavbarPage />
    </div>
    <ModalPage v-if="showModal" :result="modalResult" @closeModal="closeModal" />
  </div>
</template>

<script>
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';
import ModalPage from './ModalPage.vue';
import axios from 'axios';

export default {
  components: { NavbarPage, SidebarPage, ModalPage },
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
        const response = await axios.post('http://127.0.0.1:8000/api/checkprofile/' + this.$store.getters.getRegistrationData.user_id);
        
        // Проверяем результат и показываем модальное окно при необходимости
        if (response.data.result === 0) {
          this.showModal = true;
          this.modalResult = 0;
          console.log('окно показанно')
        } else {
          this.modalResult = 1;
          this.$router.push('/main/service');
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
.navigation {
  display: flex;
  background-color:#FAFAFA;
}
</style>
