<template>
    <div class="main">
      <div class="widgets">
        <img src="../../static/img/big_flag.png" alt="" class="img_widgets">
        <p class="header">Поздравляем с регистрацией!</p>
        <p class="subheader">Предлагаем вам перейти к созданию услуги, после чего<br>у вас появится возможность прикрепить созданные услуги<br>к вашим специалистам и добавить филиал.</p>
        <a href="#/main/widgets/settings" style="text-decoration:none"><button class="widgets_btn"> + Добавить услуги</button></a>
  
      </div>
      <div class="navigation">
        <SidebarPage/>
        <NavbarPage/>
      </div>
    </div>
  </template>
  
  <script>
  import NavbarPage from './NavbarPage.vue';
  import SidebarPage from './SidebarPage.vue';
  export default {
    components: { NavbarPage, SidebarPage },
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
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
  }
  
  .img_widgets {
    margin-bottom: 10px;
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