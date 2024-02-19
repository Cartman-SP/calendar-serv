<template>
    <div class="service_card">
      <div class="card-container">
        <div class="main_container">
          <div class="card_img">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 1C1.89543 1 1 1.89543 1 3V16C1 17.1046 1.89543 18 3 18H17C18.1046 18 19 17.1046 19 16V5C19 3.89543 18.1046 3 17 3H8C8 1.89543 7.10457 1 6 1H3Z" fill="white"/>
            </svg> 
          </div>
          <div class="main_text">
            <p class="main_header">Барбершоп на Сатпаева</p>
            <p class="main_subheader">ID 124568</p>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">24</p>
            <p class="text-subheader">Количество услуг</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">6</p>
              <p class="text-subheader">Количество филиалов</p>
            </div>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">12</p>
            <p class="text-subheader">Сотрудников</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">Владелец</p>
              <p class="text-subheader">Ваша роль</p>
            </div>
          </div>
        </div>  
        <div class="bottom">
          <p class="text-subheader">Последнее изменение: 17.07.23 в 17:44</p>
          <div class="bottom_btns">
            <router-link to="/lk/project/edit"> 
              <button class="functions">Редактировать</button>
            </router-link>
            <router-link to="/lk/project/gates" style="width:65%">
              <button class="functions">Доступы</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showDropdown: false,
        showModal: false,
      };
    },
  
    methods: {
      toggleDropdown() {
        this.showDropdown = !this.showDropdown;
      },
      toggleModal() { // добавлено
        this.showModal = !this.showModal;
      },
    }
  };
  </script>
  
  
  <style scoped>
    .text-header{
      font-family: TT Norms;
      font-size: 16px;
      font-weight: bold;
      line-height: 18px;
      letter-spacing: 0em;
      color: #535C69;
      margin: 0;
      text-align: left;
    }
    .text-subheader{
      font-family: TT Norms;
      font-size: 10px;
      font-weight: bold;
      line-height: 12px;
      letter-spacing: 0em;
      color: #AFB6C1;
      margin: 0;
      text-align: left;
    }
    .service_card{
      width: 20vw;
      height: auto;
      background-color: #FFF;
      border-radius: 5px;
    }
    .card-container{
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    p{
      margin: 0;
    }
    .cards{
      display: flex;
      gap: 10px;
      width: 100%;
    }
    .text-container{
      width: 50%;
    }
    img{
      border-radius: 5px;
    }
    .card_img{
      display: flex;
      align-items: center;
      justify-content: center;
      height: 32px;
      width: 32px;
      border-radius: 30px;
      background: #F97F7F;
    }
    .main_container{
      display: flex;
      gap: 10px;
    }
    .main_header{
      font-family: TT Norms;
      font-size: 14px;
      font-weight: bold;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: left;
      color: #535C69;
    }
    .main_subheader{
      font-family: TT Norms;
      font-size: 12px;
      font-weight: bold;
      line-height: 14px;
      letter-spacing: 0.03em;
      text-align: left;
      color: #AFB6C1;
    }
    .bottom{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .bottom_btns{
      display: flex;
      justify-content: space-between;
      gap: 20px;
    }
    .functions{
      border: 1px solid #DDE1E5;
      background: #FFFFFF ;
      font-family: TT Norms;
      font-size: 14px;
      font-weight: bold;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: center;
      color: #535C69;
      width: 100%;
    }

    .functions:hover{
      color: #FFFFFF;
      background: #6266EA;
    }
    a{
      text-decoration: none;
      width: 100%;
    }
  </style>  