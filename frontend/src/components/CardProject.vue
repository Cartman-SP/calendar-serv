<template>
    <div class="service_card">
      <div class="card-container">
        <div class="main_container">
          <div class="card_img" v-if="CurrentProject">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 1C1.89543 1 1 1.89543 1 3V16C1 17.1046 1.89543 18 3 18H17C18.1046 18 19 17.1046 19 16V5C19 3.89543 18.1046 3 17 3H8C8 1.89543 7.10457 1 6 1H3Z" fill="white"/>
            </svg> 
          </div>
          <div v-else class="avatar" :style="{ 'background-color': Color }">
            <p class="avatar_text">{{ formatText(Name) }}</p>
          </div>
          <div class="main_text">
            <p class="main_header">{{ Name }}</p>
            <p class="main_subheader">ID {{ Id }}</p>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ Services }}</p>
            <p class="text-subheader">Количество услуг</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ Filials }}</p>
              <p class="text-subheader">Количество филиалов</p>
            </div>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ Employees }}</p>
            <p class="text-subheader">Сотрудников</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ Role }}</p>
              <p class="text-subheader">Ваша роль</p>
            </div>
          </div>
        </div>  
        <div class="bottom">
          <p class="text-subheader">Последнее изменение: {{ EditDate }} в {{ EditTime }}</p>
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
    props:{
      Name: String,
      Id: Number,
      Services: Number,
      Filials: Number,
      Employees: Number,
      Role: String,
      Color: String,
      EditDate: String,
      EditTime: String,
      CurrentProject: Boolean,
    },
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

      formatText(text) {
          return text
            .split(' ')
            .map(word => (word.length > 1 ? word.charAt(0).toUpperCase() : word.toUpperCase()))
            .join('');
      },
    }
  };
  </script>
  
  
  <style scoped>
  .avatar{
    height: 32px;
    width: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 30px;
  }
  .avatar_text{
    margin: -10px;
    font-family: 'TT Norms Medium';
    width: auto;
    height: auto;
    color: #FFFFFF;
    font-size: 14px;
  }
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