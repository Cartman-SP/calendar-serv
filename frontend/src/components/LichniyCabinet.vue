<template>
    <div class="cabinet">
        <div class="overlay" v-if="showModal"></div>
        <div class="navigation">
            <SidebarPage/>
            <div class="lk">
                <NavbarPage/>
                <ModalPage v-if="showModal" :result="modalResult" @closeModal="closeModal" />
                <router-view v-else></router-view>
            </div>
        </div>
    </div>
</template>

<script>
import ModalPage from './ModalPage.vue';
import axios from 'axios';
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';  

export default {
    components: { NavbarPage, SidebarPage, ModalPage},
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
          this.$router.push('/lk/service');
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


<style>
.navigation{
    display: flex;
}

.cabinet{
    background-color: #FAFAFA;
}

.lk{
    width: 100%;
    height: 100vh;
    padding: 20px 20px 20px 0;
}

  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
  }
</style>