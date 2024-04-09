<template>
  <div class="main">
    <div class="content" v-if="uslugiLoaded && allwidgets.length > 0">
      <router-link to="/dashboard/widgets/create" class="add">
        <div class="svg-plus">
          <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
          </svg>            
        </div>
        <p>Добавить виджет</p>
      </router-link>
      <CardWidget v-for="Widget in allwidgets" :key="Widget.id" :widgetData="Widget"/>
    </div>
    <div class="widgets" v-else-if="uslugiLoaded && allwidgets.length == 0">
        <img src="../../static/img/big_flag.png" alt="" class="img_widgets">
        <p class="header">Последний рывок</p>
        <p class="subheader">Осталось только создать виджет, выбрать его оформление<br> и разместить его на сайте или в социальных сетях. После<br> чего ваши клиенты смогут записываться к вам онлайн.</p>
        <router-link to="/dashboard/widgets/create" style="text-decoration:none">
          <button class="widgets_btn"> + Добавить виджет</button>
        </router-link>
    </div>
    <div v-else style="padding-top: 200px;">
      <!-- Показываем значок загрузки -->
      <i class="pi pi-spin pi-spinner" style="font-size: 2rem;  color: #6266EA"></i>
    </div>
  </div>
  </template>

  <script>
import CardWidget from '../components/CardWidget.vue';
import axios from 'axios';
export default {
  components: { CardWidget },
    data() {
      return{
        link:'',
        allwidgets:[],
        uslugiLoaded: false
      };
    },
    methods:{
      getwidgets(){
        axios.get(`http://127.0.0.1:8000/api/get_widget/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`)
    .then(response => {
        this.allwidgets = response.data;
        this.allwidgets.reverse();
        this.uslugiLoaded = true;

    })
    .catch(error => {
        console.error('Ошибка при получении данных о пользователе:', error);
    });
      },
    },
    mounted(){
      this.getwidgets()
    }
  }
  </script>
  
  <style scoped>
  .main{
    overflow-y: scroll;
    width: 100%;
    height: 87vh;
  }
  .widgets {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
  }
  .img_widgets {
    margin-bottom: 10px;
    width: 100px;
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
  .widgets_btn{
    margin: 0 auto;
  }
  .content{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .add {
    text-decoration-line: initial;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    display: flex;
    height: 130px;
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
  svg{
    height: 40px;
    width: 40px;
  }
  p{
    margin: 0;
  }
  @media (max-width: 1061px){
    .add{
      min-height: 135px;
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
    .widgets_btn{
      margin: 0;
      width: 100%;
    }
    .button_a{
      width: 100%;
    }
  }
  </style>