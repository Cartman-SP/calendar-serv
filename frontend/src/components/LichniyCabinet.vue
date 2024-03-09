<template>
    <div class="cabinet">
        <div class="navigation">
            <SidebarPage/>
            <div class="lk">
                <NavbarPage/>
                <ModalPage v-if="showModal" @regdone="showModal = !showModal" :result="modalResult" @closeModal="closeModal" />
                <router-view v-else></router-view>
                <WidgetSite style="display: none;"></WidgetSite>
            </div>
        </div>
    </div>
</template>

<script>
import ModalPage from './ModalPage.vue';
import axios from 'axios';
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';
import WidgetSite from './WidgetSite.vue';  

export default {
    components: { NavbarPage, SidebarPage, ModalPage, WidgetSite},
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


<style scoped>
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
@media (max-width: 768px){
  .lk {
    padding: 0;
    border-radius: 0;
  }
}
</style>