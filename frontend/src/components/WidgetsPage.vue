<template>
  <div class="main">
    <CardWidget/>
    <div class="widgets">
        <img src="../../static/img/big_flag.png" alt="" class="img_widgets">
        <p class="header">Последний рывок</p>
        <p class="subheader">Осталось только создать виджет, выбрать его оформление<br> и разместить его на сайте или в социальных сетях. После<br> чего ваши клиенты смогут записываться к вам онлайн.</p>
        <router-link to="/lk/widgets/settings" style="text-decoration:none">
          <button class="widgets_btn"> + Добавить услуги</button>
        </router-link>
    </div>
  </div>
  </template>
  
  <script>
import CardWidget from '../components/CardWidget.vue';

export default {
  components: { CardWidget },
    data() {
      return{
  
      };
    }
  }
  </script>
  
  <style scoped>
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
  </style>