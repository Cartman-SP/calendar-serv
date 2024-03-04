<template>
    <div class="service_card">
      <div class="card-container">
        <div class="main_container">
          <div class="main_wrapp">
            <div class="card_img" v-if="ProjectData.currentProject">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 1C1.89543 1 1 1.89543 1 3V16C1 17.1046 1.89543 18 3 18H17C18.1046 18 19 17.1046 19 16V5C19 3.89543 18.1046 3 17 3H8C8 1.89543 7.10457 1 6 1H3Z" fill="white"/>
              </svg> 
            </div>
            <div v-else class="avatar" :style="{ 'background-color': ProjectData.colour }">
              <p class="avatar_text">{{ formatText(ProjectData.name) }}</p>
            </div>
            <div class="main_text">
              <p class="main_header">{{ ProjectData.name }}</p>
              <p class="main_subheader">ID {{ ProjectData.id }}</p>
            </div>
          </div>
          <div class="checkmark">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="white"/>
            </svg>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ ProjectData.services }}</p>
            <p class="text-subheader">Количество услуг</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ ProjectData.filials }}</p>
              <p class="text-subheader">Количество филиалов</p>
            </div>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ ProjectData.employees }}</p>
            <p class="text-subheader">Сотрудников</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ ProjectData.position }}</p>
              <p class="text-subheader">Ваша роль</p>
            </div>
          </div>
        </div>  
        <div class="bottom">
          <p class="text-subheader">Последнее изменение: {{ ProjectData.editDate }} в {{ ProjectData.editTime }}</p>
          <div class="bottom_btns">
            <router-link to="/lk/project/edit">
              <button class="functions">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="20" height="20"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>
                Редактировать</button>
            </router-link>
            <router-link to="/lk/project/gates" style="width:65%">
              <button class="functions">
                <svg width="20" height="20" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.7 3.15001C7.7 4.50311 8.7969 5.60001 10.15 5.60001C11.5031 5.60001 12.6 4.50311 12.6 3.15001C12.6 1.79691 11.5031 0.700012 10.15 0.700012C8.7969 0.700012 7.7 1.79691 7.7 3.15001Z" fill="#535C69"/>
                <path d="M2.1 2.80001H3.5V4.90001H5.6V6.30001H3.5V8.40001H2.1V6.30001H0V4.90001H2.1V2.80001Z" fill="#535C69"/>
                <path d="M13.3 9.10001C13.3 8.32681 12.6732 7.70001 11.9 7.70001H8.4C6.0804 7.70001 4.2 9.58042 4.2 11.9V12.6H13.3V9.10001Z" fill="#535C69"/>
              </svg>
                Доступы</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props:['ProjectData'],
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
      font-family: 'TT Norms Medium';
      font-size: 16px;
      line-height: 18px;
      letter-spacing: 0em;
      color: #535C69;
      margin: 0;
      text-align: left;
    }
    .text-subheader{
      font-family: 'TT Norms Medium';
      font-size: 10px;
      line-height: 12px;
      letter-spacing: 0em;
      color: #AFB6C1;
      margin: 0;
      text-align: left;
    }
    .service_card{
      width: 100%;
      height: 100%;
      background-color: #FFF;
      border-radius: 5px;
      transition: all .2s ease;
    }

    .service_card:hover{
      cursor: pointer;
      filter: drop-shadow(0 0 10px rgb(228, 228, 228));
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
      justify-content: space-between;
      gap: 10px;
    }
    .main_header{
      font-family: 'TT Norms Medium';
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: left;
      color: #535C69;
    }
    .main_subheader{
      font-family: 'TT Norms Medium';
      font-size: 12px;
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
      padding: 20px 0;
      border: 1px solid #DDE1E5;
      background: #FFFFFF ;
      font-family: 'TT Norms Medium';
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: center;
      color: #535C69;
      width: 100%;
      transition: all .2s ease;
    }

    .functions svg path{
      fill: #535C69;
      transition: all .2s ease;
    }

    .functions:hover{
      border: 1px solid #6266EA;
      color: #FFFFFF;
      background: #6266EA;
    }

    .functions:hover svg path{
      fill: white;
    }


    a{
      text-decoration: none;
      width: 100%;
    }
    .main_wrapp{
      display: flex;
      gap: 10px;
    }
    .checkmark{
      width: 22px;
      height: 22px;
      background: #F3F5F6;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s ease
    }
    .checkmark:hover{
      background: #04C562;
    }
  </style>  