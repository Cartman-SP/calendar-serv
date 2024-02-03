<template>
    <div class="main">
      <div class="create_branch">
        <div class="transition">
          <a href="#/main/personal" class="branchs-link">Филиалы</a>
          <div class="arrow-container">
            <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
          </div>
          <p class="creation_text">Создание филиала</p>
        </div>
  

  
      </div>
  
      <div class="navigation">
        <!-- Подключение других компонентов -->
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
        return {

        };
      },
     
  }   
    </script>
    
    <style scoped>
    .transition {
      display: flex;
      flex-direction: row;
      gap: 10px;
      margin-bottom: 50px;
    }
  
    .branchs-link {
      font-family: TT Norms;
      font-size: 20px;
      font-weight: 500;
      line-height: 24px;
      text-align: left;
      text-decoration: none;
      color: #AFB6C1;
    }
  
    .creation_text {
      color: #535C69;
      font-family: TT Norms;
      font-size: 20px;
      font-weight: 500;
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
  
    .navigation {
      display: flex;
      background-color: white;
    }
  
    .create_branch {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 488px;
      height: 439px;
      color: #FFFFFF;
    }
  

  </style>
    