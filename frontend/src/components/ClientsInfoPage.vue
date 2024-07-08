<template>
  <div class="main">
    <div class="transition">
      <router-link to="/dashboard/clients" class="employesss-link">Клиенты</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">{{ clientData.firstname + ' ' + clientData.secondname }}</p>
    </div>

    <div class="clients_header">
      <div class="info">
        <img class="info_img" src="../../static/img/clients.png" alt="">
        <div class="info_container">
          <div class="name">
            <p class="text">Клиент</p>
            <p class="subtext">{{ clientData.firstname + ' ' + clientData.secondname }}</p>
          </div>
          <div class="status">
            <p class="text">Последний заказ(статус)</p>
            <p class="accepted" v-if="lastAppStatus === 'New'" style="background-color: #28CCF0;">Новые</p>
            <p class="accepted" v-else-if="lastAppStatus === 'Adopted'" style="background-color: #F7D37D;">Принят</p>
            <p class="accepted" v-else-if="lastAppStatus === 'Canceled'" style="background-color: #F97F7F;">Отменен</p>
            <p class="accepted" v-else-if="lastAppStatus === 'Done'" style="background-color: #00A490;">Завершен</p>
          </div>
        </div>
      </div>
      <div class="contact">
        <div class="number">
          <p class="text">Контакты</p>
          <p class="subtext">{{ clientData.phone }}</p>
        </div>
        <div class="income">
          <p class="text">Доход от клиента</p>
          <p class="subtext">NaN ₸</p>
        </div>
      </div>
      <div class="date">
        <p class="text">Дата регистрации</p>
        <p class="subtext">{{ clientData.date }}</p>
      </div>
      <div class="total">
        <p class="text">Всего записей</p>
        <p class="subtext">{{ applications.length }}</p>
      </div>
    </div>
    <div class="history">
      <div class="pages">
        <p class="history_text">История записей клиента</p>
        <div class="subnav_page"  v-show="false">
          <img src="../../static/img/arrow-left.svg" alt="<">
          <div class="list">
            <div class="number_page">
              <p class="page_text">1</p>
              <p class="page_text">2</p>
              <p class="page_text">3</p>
            </div>
          </div>
          <img src="../../static/img/arrow-right.svg" alt=">">
        </div>
      </div>
      <div class="divider"></div>
      <div class="history_nav">
        <p class="text">Сотрудник</p>
        <p class="text">Услуга</p>
        <p class="text">Дата</p>
        <p class="text">Филиал</p>
      </div>
      <div  v-if="applications.length > 0">
        <div v-for="a in applications" :key="a.id">
          <div class="clients_info">
            <p class="clients_text">{{ a.employee }}</p>
            <p class="clients_text">{{ a.usluga }}</p>
            <p class="clients_text">{{ a.data }}</p>
            <p class="clients_text">{{ a.filial }}</p>
          </div>
          <div class="clients_divider"></div>
        </div>
      </div>
      <div v-else>
        <p class="clients_text">Пока не было записей :(</p>
    
      </div>
      
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      clientData: {},
      applications: [],
      lastAppStatus: '',
    }
  },
  methods:{
    getObjectById() {
      for (let obj of this.clients) {
        if (obj.id === parseInt(this.$route.params.clientId)) {
          this.clientData = obj;
          break;
        }
      }
    },
    async fetchApplications() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/client/${this.clientData.id}/applications/`);
        const applications = response.data;

        const updatedApplications = await Promise.all(applications.map(async application => {
          const employeeResponse = await this.getEmployee(application.employee);
          const uslugaResponse = await this.getUsluga(application.usluga);
          const filialResponse = await this.getfilial(application.branch);

          return {
            ...application,
            employee: employeeResponse.data.firstname + ' ' + employeeResponse.data.secondname,
            usluga: uslugaResponse.data.name,
            filial: filialResponse.data.name
          };
        }));

        this.applications = updatedApplications;
        this.lastAppStatus = this.applications[0].status
      } catch (error) {
        console.error("There was an error fetching the applications:", error);
      }
    },
    async getEmployee(id) {
      const response = await axios.get(`http://127.0.0.1:8000/api/employee/${id}/`);
      return response;
    },
    async getUsluga(id) {
      const response = await axios.get(`http://127.0.0.1:8000/api/usluga/${id}/`);
      return response;
    },
    async getfilial(id) {
      const response = await axios.get(`http://127.0.0.1:8000/api/get_filialbyid/?variable=${id}`);
      return response;
    },
  },
  computed: {
    clients() {
      return this.$store.state.clients;
    }
  },
  async mounted() {
    this.getObjectById();
    await this.fetchApplications();
  }
}
</script>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.transition {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.employesss-link {
  font-family: 'TT Norms Medium';
  font-size: 20px;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}
.creation_text {
  color: #535C69;
  font-family: 'TT Norms Medium';
  font-size: 20px;
  line-height: 24px;
  letter-spacing: 0em;
  text-align: left;
  margin: 0;
}
.arrow-container {
  display: flex;
  align-items: center;
}

.arrow-icon {
  height: 50%;
}
.clients_header{
  display: flex;
  background: #FFFFFF;
  gap: 90px;
  width: 100%;
  border-radius: 5px;
  padding: 20px;
}
.number{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.income{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.date{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.total{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.name{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.status{
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.contact{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #AFB6C1;
}
.subtext{
  font-family: TT Norms Medium;
  font-size: 16px;
  line-height: 18.88px;
  text-align: left;
  color: #535C69;
}
p{
  margin: 0;
}
.info{
  display: flex;
  gap: 20px;
}
.info_img{
  border-radius: 10px;
  width: 100px;
  height: 100px;
}
.accepted{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14.16px;
  text-align: left;
  color: #FFFFFF;
  background: #F7D37D;
  padding: 2px 10px;
  width: fit-content;
  text-align: center;
  border-radius: 3px;
}
.info_container{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.history{
  width: 100%;
  background: #FFFFFF;
  padding: 20px;
}
.history_text{
  font-family: TT Norms Medium;
  font-size: 16px;
  font-weight: 500;
  line-height: 18.88px;
  text-align: left;
  color: #535C69;
}
.page_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: center;
  color: #B7C0C8;
  cursor: pointer;
}
.page_text:hover{
  color: #6266EA;
}
.page_text.active {
  color: #6266EA;
}
.pages{
  display: flex;
  justify-content: space-between;
}
.number_page{
  display: flex;
  gap: 10px;
}
.list{
  display: flex;
  gap: 15px;
  align-items: end;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 20px 0;
}
.history_nav{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;
  margin-bottom: 20px;
}
.clients_info{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 1fr;
}
.clients_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
}
.clients_divider{
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: auto;
  margin: 10px 0;
}
.subnav_page{
  display: flex;
  gap: 20px;
}
</style>