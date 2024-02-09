<template>
    <div class="widgets">
        <img src="../../static/img/big_flag.png" alt="" class="img_widgets">
        <p class="header">Поздравляем с регистрацией!</p>
        <p class="subheader">Предлагаем вам перейти к созданию услуги, после чего<br>у вас появится возможность прикрепить созданные услуги<br>к вашим специалистам и добавить филиал.</p>
        <router-link to="/lk/widgets/settings">
          <button class="widgets_btn"> + Добавить услуги</button>
        </router-link>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return{
  
      };
    }
  }
  </script>
  
  <style scoped>
  .navigation{
    display: flex;
    background-color: white;
  }
  .widgets {
    text-align: center;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
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