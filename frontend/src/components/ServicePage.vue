<template>
  <div class="main">
    <div class="content" v-if="uslugiLoaded && uslugi.length > 0">
      <router-link to="/lk/service/create" class="add">
        <div class="svg-plus">
          <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
          </svg>            
        </div>
        <p>Добавить услугу</p>
      </router-link>
      <Card v-for="(usluga, index) in uslugi" :key="index" :usluga="usluga" />
    </div>
    <div v-else-if="uslugiLoaded && uslugi.length === 0">
      <div class="service">
        <img src="static/viewapp/img/flag.svg" alt="" class="img_service">
        <p class="header">Поздравляем с регистрацией!</p>
        <p class="subheader">Предлагаем вам перейти к созданию услуги, после чего у вас появится возможность прикрепить созданные услуги к вашим специалистам и добавить филиал.</p>
        <a href="#/lk/service/create" style="text-decoration:none"><button class="service_btn"> + Добавить услуги</button></a>
      </div>
    </div>
    <div v-else style="padding-top: 200px;">
      <!-- Показываем значок загрузки -->
      <i class="pi pi-spin pi-spinner" style="font-size: 2rem;  color: #6266EA"></i>
    </div>
    <div class="overlay" v-show="false"></div>
    <FirstService v-show="false"/>
  </div>
</template>

<script>
import axios from 'axios';
import Card from '../components/CardPage.vue';
import FirstService from '../components/ModalServicePage.vue';
import { mapMutations } from 'vuex';

export default {
  components: { Card, FirstService},
  data() {
    return {
      uslugi: [], // Создаем массив для хранения объектов Usluga
      uslugiLoaded: false // Переменная состояния для отслеживания загрузки
    };
  },
  methods: {
    ...mapMutations(['setUpdateSidebar']),
      rerenderSidebar() {
        this.setUpdateSidebar();
      },
    async get_uslugi(){
      try {
        const response = await axios.get(`http://95.163.243.5/api/uslugi/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`);
        this.uslugi = response.data; // Присваиваем полученные данные массиву uslugi
        this.uslugi.reverse();
        this.uslugiLoaded = true; // Устанавливаем флаг загрузки в true sd
        this.rerenderSidebar();
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    }
  },
  async mounted() {
    // Выполняем запрос при монтировании страницы
    await this.get_uslugi();
  }
};
</script>

<style scoped>
.overlay {
    background-color: rgba(0, 0, 0, 0.6);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
.main{
  overflow-y: scroll;
  height: 87vh;
}
.service {
  height: 87vh;
  text-align: center;
  align-items: center;
  justify-content: center;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.header {
  color: #535C69;
  font-family: TT Norms Medium;
  font-size: 20px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: center;
}

.subheader {
  font-size: 16px;
  line-height: 18px;
  color: #AFB6C1;
  font-family: TT Norms Medium;
  font-weight: 500;
  letter-spacing: 0em;
  text-align: center;
  max-width: 500px;
}
.service_btn{
  margin: 0 auto;
}

.content{
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(4, 1fr);
}
.add {
  text-decoration-line: initial;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  display: flex;
  height: 100%;
  min-height: 250px;
  gap: 10px;
  color: #6266EA;
  border-style: dashed;
  border-width: 2px;
  border-color: #D9D9D9;
  transition: 0.3s ease;
  padding: 20px;
  border-radius: 5px;
}
.svg-plus{
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
  width: 1em;
  height: 1em;
}
p{
  margin: 0;
}
.add:hover{
  background: #EFEFFF;
}
@media (max-width: 1340px){
  .content{
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 900px){
  .service{
    height: 70vh;
  }
  .img_service{
    width: 60px;
    height: 60px;
  }
  .content{
    grid-template-columns: 1fr
  }
  .add{
    min-height: 135px;
  }
}

@media (max-width: 768px){
  .subheader{
    max-width: 500px;
  }
  .main{
    padding: 20px;
  }
}
@media (max-width: 398px){
  .header{
    font-size: 18px;
  }
}

</style>