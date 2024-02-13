<template>
  <div class="main">
    <div v-if="uslugi.length > 0">
      <Card v-for="(usluga, index) in uslugi" :key="index" :usluga="usluga" />
      <a href="#/lk/service/create" style="text-decoration:none"><button class="service_btn"> + Добавить услуги</button></a>
    </div>
    <div v-else>
      <div class="service">
        <img src="../../static/img/flag.png" alt="" class="img_service">
        <p class="header">Поздравляем с регистрацией!</p>
        <p class="subheader">Предлагаем вам перейти к созданию услуги, после чего<br>у вас появится возможность прикрепить созданные услуги<br>к вашим специалистам и добавить филиал.</p>
        <a href="#/lk/service/create" style="text-decoration:none"><button class="service_btn"> + Добавить услуги</button></a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Card from '../components/CardPage.vue';

export default {
  components: { Card },
  data() {
    return {
      uslugi: [] // Создаем массив для хранения объектов Usluga
    };
  },
  mounted() {
    // Выполняем запрос при монтировании страницы
    axios.get('http://127.0.0.1:8000/api/uslugi/')
      .then(response => {
        this.uslugi = response.data; // Присваиваем полученные данные массиву uslugi
      })
      .catch(error => {
        console.error('Error fetching uslugi:', error);
      });
  }
};
</script>

<style scoped>
.service {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 450px;
}

.header {
  color: #535C69;
  font-family: "TT Norms";
  font-size: 20px;
  font-weight: 500;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: center;
  margin-bottom: 10px;
}

.subheader {
  font-size: 16px;
  line-height: 16px;
  color: #AFB6C1;
  font-family: TT Norms;
  font-weight: 500;
  letter-spacing: 0em;
  text-align: center;

}
.service_btn{
  margin: 0 auto;
}

</style>