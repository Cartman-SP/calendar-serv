<template>
    <div class="main">
      <CardBranch/>
      <div class="branch">
        <img src="../../static/img/branch.png" alt="" class="img_branch">
        <p class="header">Здесь будет ваш филиал. Будет же?</p>
        <p class="subheader">Осталось только создать виджет, выбрать его оформление и разместить его на сайте или в социальных сетях. После чего ваши клиенты смогут записываться к вам онлайн.</p>
        <a href="#/lk/branch/createbranch" style="text-decoration:none"><button class="branch_btn"> + Добавить филиал</button></a>
      </div>
    </div>
  </template>
  
  <script>
import CardBranch from '../components/CardBranch.vue';

export default {
  components: { CardBranch },
    data() {
      return{
  
      };
    }
  }
  </script>
  
  <style scoped>
  .navigation{
    display: flex;
    background-color:#FAFAFA;
  }
  .branch {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
  }
  
  .img_branch {
    margin-bottom: 10px;
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
    line-height: 16px;
    color: #AFB6C1;
    font-family: TT Norms;
    font-weight: 500;
    letter-spacing: 0em;
    text-align: center;
    margin: 0;
    margin-bottom: 20px;
  
  }
  .branch_btn{
    margin: 0 auto;
  }
  </style>