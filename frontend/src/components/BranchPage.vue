<template>
    <div class="main">
      <div v-if=" branchLoaded && filials.length > 0" class="filials">
        <router-link to="/lk/branch/createbranch" class="add">
          <div class="svg-plus">
            <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
            </svg>            
          </div>
          <p>Добавить филиал</p>
        </router-link>
        <div v-for="filial in filials" :key="filial.id">
          <CardBranch :FilialData="filial"/>
        </div>
      </div>
      <div v-else-if="branchLoaded && filials.length==0" class="branch">
        <img src="../../static/img/filial-create.svg" alt="" class="img_branch">
        <p class="header">Здесь будет ваш филиал. Будет же?</p>
        <p class="subheader">Теперь нам осталось добавить информацию о своей компании\филиале, добавить местоположение, контакты для связи и прочее</p>
        <a class="button_a" href="#/lk/branch/createbranch" style="text-decoration:none"><button class="branch_btn"> + Добавить филиал</button></a>
      </div>
      <div v-else style="padding-top: 200px;">
      <!-- Показываем значок загрузки -->
        <i class="pi pi-spin pi-spinner" style="font-size: 2rem;  color: #6266EA"></i>
      </div>
    </div>
  </template>
  
  <script>
import CardBranch from '../components/CardBranch.vue';
import axios from 'axios';

export default {
  components: { CardBranch },
    data() {
      return{
        branchLoaded: false,
        filials: [],
      };
    },
    methods:{
      getfilials(){
        axios.get(`http://127.0.0.1:8000/api/get_branch/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`)
    .then(response => {
        this.filials = response.data;
        this.filials.reverse();
        console.log(response);
        this.branchLoaded = true;
    })
    .catch(error => {
        console.error('Ошибка при получении данных о пользователе:', error);
    });
      },
    },
    mounted() {
      this.getfilials()
    },
  }
  </script>
  
  <style scoped>
  .main{
    overflow-y: scroll;
    height: 87vh;
  }
  .filials{
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
  color: #6266EA;
  border-style: dashed;
  border-width: 2px;
  border-color: #D9D9D9;
  transition: 0.3s ease;
  padding: 20px;
  border-radius: 5px;
}

.add:hover{
  background: #EFEFFF;
}
  .branch {
    height: 87vh;
    text-align: center;
    align-items: center;
    justify-content: center;
    display: flex;
    flex-direction: column;
  }
  
  .img_branch {
    margin-bottom: 10px;
    width: 86px;
    height: 86px;
  }
  
  .header {
    color: #535C69;
    font-family: 'TT Norms Medium';
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
    margin-bottom: 20px;
    margin-top: 20px;
  }
  
  .subheader {
    font-size: 16px;
    line-height: 20px;
    color: #AFB6C1;
    font-family: TT Norms Medium;
    font-weight: 500;
    letter-spacing: 0em;
    text-align: center;
    margin: 0;
    margin-bottom: 20px;
  
  }
  .branch_btn{
    margin: 0 auto;
  }
  svg{
    width: 40px;
    height: 40px;
  }
  .subheader{
    max-width: 500px;
  }
  @media (max-width: 900px){
    .branch{
      height: 70vh;
    }
    .img_branch{
      width: 60px;
      height: 60px;
    }
  }
  @media (max-width: 768px){
    .main{
      padding: 20px;
    }
  }
  @media (max-width: 576px){
    .header{
      line-height: 25px;
    }
    .branch_btn{
      margin: 0;
      width: 100%;
    }
    .button_a{
      width: 100%;
    }
  }
  </style>