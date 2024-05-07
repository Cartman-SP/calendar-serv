<template>
    <div class="main">
      <div class="transition">
        <router-link to="/dashboard/project" class="eidt-link">Мои проекты</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <router-link to="/dashboard/project" class="eidt-link">Барбершоп на Сатпаева</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>  
        <p class="creation_text">Доступы</p>
      </div>
      
      <div class="edit">
        <div class="edit_top">
            <button class="basket">
                <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 17V7H4V17C4 18.1046 4.89543 19 6 19H14C15.1046 19 16 18.1046 16 17Z" fill="#AFB6C1"/>
                <path d="M7.44721 1.10557L6.5 3H2V5H18V3H13.5L12.5528 1.10557C12.214 0.428004 11.5215 0 10.7639 0H9.23607C8.47852 0 7.786 0.428005 7.44721 1.10557Z" fill="#AFB6C1"/>
                </svg>
            </button>
            <button class="send">
                <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#6266EA"/>
                </svg>
                Отправить приглашение
            </button>
        </div>
        <div class="edit_main">
            <div class="edit_wrapper">
              <p class="edit_text">Email</p>
              <p class="edit_text">Статус</p>
              <p class="edit_text">Роль</p>
              <p class="edit_text">Действия</p>
            </div>
            <div class="divider"></div>
            <div class="bottom">
              <div class="edit_container">
                <div class="edit_bottom">
                  <div class="img_container">
                    <img class="avatar" src="../../static/img/service_2.png" alt="">
                    <div class="name_container">
                      <p class="name_head">
                        Никита Половинко
                      </p>
                      <p class="name_sub">
                        nikitapolovinko@gmail.com
                      </p>
                    </div>
                  </div>
                  <div class="center">
                    <p class="edit_text">Отправлено приглашение</p>
                  </div>
                  <div class="center">
                    <p class="edit_text">Владелец</p>
                  </div>
                  <div class="btns">
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8.82231 0.5C8.56215 0.5 8.35124 0.710907 8.35124 0.971074V2.74768C7.61716 2.92912 6.91437 3.2195 6.26632 3.60914L5.01431 2.3539C4.92601 2.26537 4.80613 2.21558 4.68109 2.2155C4.55605 2.21542 4.4361 2.26505 4.34769 2.35347L2.35347 4.34769C2.26505 4.4361 2.21542 4.55605 2.2155 4.68109C2.21558 4.80613 2.26537 4.92601 2.3539 5.01431L3.60914 6.26632C3.2195 6.91437 2.92912 7.61716 2.74768 8.35124H0.971074C0.710907 8.35124 0.5 8.56215 0.5 8.82231V11.1777C0.5 11.4379 0.710907 11.6488 0.971074 11.6488H2.74768C2.92912 12.3828 3.2195 13.0856 3.60914 13.7337L2.3539 14.9857C2.26537 15.074 2.21558 15.1939 2.2155 15.3189C2.21542 15.444 2.26505 15.5639 2.35347 15.6523L4.34769 17.6465C4.4361 17.7349 4.55605 17.7846 4.68109 17.7845C4.80613 17.7844 4.92601 17.7346 5.01431 17.6461L6.26632 16.3909C6.91437 16.7805 7.61716 17.0709 8.35124 17.2523V19.0289C8.35124 19.2891 8.56215 19.5 8.82231 19.5H11.1777C11.4379 19.5 11.6488 19.2891 11.6488 19.0289V17.2523C12.3828 17.0709 13.0856 16.7805 13.7337 16.3909L14.9857 17.6461C15.074 17.7346 15.1939 17.7844 15.3189 17.7845C15.444 17.7846 15.5639 17.7349 15.6523 17.6465L17.6465 15.6523C17.7349 15.5639 17.7846 15.444 17.7845 15.3189C17.7844 15.1939 17.7346 15.074 17.6461 14.9857L16.3909 13.7337C16.7805 13.0856 17.0709 12.3828 17.2523 11.6488H19.0289C19.2891 11.6488 19.5 11.4379 19.5 11.1777V8.82231C19.5 8.56215 19.2891 8.35124 19.0289 8.35124H17.2523C17.0709 7.61716 16.7805 6.91437 16.3909 6.26632L17.6461 5.01431C17.7346 4.92601 17.7844 4.80613 17.7845 4.68109C17.7846 4.55605 17.7349 4.4361 17.6465 4.34769L15.6523 2.35347C15.5639 2.26505 15.444 2.21542 15.3189 2.2155C15.1939 2.21558 15.074 2.26537 14.9857 2.3539L13.7337 3.60914C13.0856 3.2195 12.3828 2.92912 11.6488 2.74768V0.971074C11.6488 0.710907 11.4379 0.5 11.1777 0.5H8.82231ZM6.70248 10C6.70248 8.17883 8.17883 6.70248 10 6.70248C11.8212 6.70248 13.2975 8.17883 13.2975 10C13.2975 11.8212 11.8212 13.2975 10 13.2975C8.17883 13.2975 6.70248 11.8212 6.70248 10Z" fill="#AFB6C1"/>
                    </svg>
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M16 17V7H4V17C4 18.1046 4.89543 19 6 19H14C15.1046 19 16 18.1046 16 17Z" fill="#AFB6C1"/>
                      <path d="M7.44721 1.10557L6.5 3H2V5H18V3H13.5L12.5528 1.10557C12.214 0.428004 11.5215 0 10.7639 0H9.23607C8.47852 0 7.786 0.428005 7.44721 1.10557Z" fill="#AFB6C1"/>
                    </svg>
                  </div>
                </div>
              </div>
              <div class="edit_container">
                <div class="edit_bottom">
                  <div class="img_container">
                    <img class="avatar" src="../../static/img/service_2.png" alt="">
                    <div class="name_container">
                      <p class="name_head">
                        Никита Половинко
                      </p>
                      <p class="name_sub">
                        nikitapolovinko@gmail.com
                      </p>
                    </div>
                  </div>
                  <div class="center">
                    <p class="edit_active">Активен</p>
                  </div>
                  <div class="center">
                    <p class="edit_text">Администратор</p>
                  </div>
                  <div class="btns">
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8.82231 0.5C8.56215 0.5 8.35124 0.710907 8.35124 0.971074V2.74768C7.61716 2.92912 6.91437 3.2195 6.26632 3.60914L5.01431 2.3539C4.92601 2.26537 4.80613 2.21558 4.68109 2.2155C4.55605 2.21542 4.4361 2.26505 4.34769 2.35347L2.35347 4.34769C2.26505 4.4361 2.21542 4.55605 2.2155 4.68109C2.21558 4.80613 2.26537 4.92601 2.3539 5.01431L3.60914 6.26632C3.2195 6.91437 2.92912 7.61716 2.74768 8.35124H0.971074C0.710907 8.35124 0.5 8.56215 0.5 8.82231V11.1777C0.5 11.4379 0.710907 11.6488 0.971074 11.6488H2.74768C2.92912 12.3828 3.2195 13.0856 3.60914 13.7337L2.3539 14.9857C2.26537 15.074 2.21558 15.1939 2.2155 15.3189C2.21542 15.444 2.26505 15.5639 2.35347 15.6523L4.34769 17.6465C4.4361 17.7349 4.55605 17.7846 4.68109 17.7845C4.80613 17.7844 4.92601 17.7346 5.01431 17.6461L6.26632 16.3909C6.91437 16.7805 7.61716 17.0709 8.35124 17.2523V19.0289C8.35124 19.2891 8.56215 19.5 8.82231 19.5H11.1777C11.4379 19.5 11.6488 19.2891 11.6488 19.0289V17.2523C12.3828 17.0709 13.0856 16.7805 13.7337 16.3909L14.9857 17.6461C15.074 17.7346 15.1939 17.7844 15.3189 17.7845C15.444 17.7846 15.5639 17.7349 15.6523 17.6465L17.6465 15.6523C17.7349 15.5639 17.7846 15.444 17.7845 15.3189C17.7844 15.1939 17.7346 15.074 17.6461 14.9857L16.3909 13.7337C16.7805 13.0856 17.0709 12.3828 17.2523 11.6488H19.0289C19.2891 11.6488 19.5 11.4379 19.5 11.1777V8.82231C19.5 8.56215 19.2891 8.35124 19.0289 8.35124H17.2523C17.0709 7.61716 16.7805 6.91437 16.3909 6.26632L17.6461 5.01431C17.7346 4.92601 17.7844 4.80613 17.7845 4.68109C17.7846 4.55605 17.7349 4.4361 17.6465 4.34769L15.6523 2.35347C15.5639 2.26505 15.444 2.21542 15.3189 2.2155C15.1939 2.21558 15.074 2.26537 14.9857 2.3539L13.7337 3.60914C13.0856 3.2195 12.3828 2.92912 11.6488 2.74768V0.971074C11.6488 0.710907 11.4379 0.5 11.1777 0.5H8.82231ZM6.70248 10C6.70248 8.17883 8.17883 6.70248 10 6.70248C11.8212 6.70248 13.2975 8.17883 13.2975 10C13.2975 11.8212 11.8212 13.2975 10 13.2975C8.17883 13.2975 6.70248 11.8212 6.70248 10Z" fill="#AFB6C1"/>
                    </svg>
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M16 17V7H4V17C4 18.1046 4.89543 19 6 19H14C15.1046 19 16 18.1046 16 17Z" fill="#AFB6C1"/>
                      <path d="M7.44721 1.10557L6.5 3H2V5H18V3H13.5L12.5528 1.10557C12.214 0.428004 11.5215 0 10.7639 0H9.23607C8.47852 0 7.786 0.428005 7.44721 1.10557Z" fill="#AFB6C1"/>
                    </svg>
                  </div>
                </div>
              </div>
              <div class="edit_container">
                <div class="edit_bottom">
                  <div class="img_container">
                    <img class="avatar" src="../../static/img/service_2.png" alt="">
                    <div class="name_container">
                      <p class="name_head">
                        Никита Половинко
                      </p>
                      <p class="name_sub">
                        nikitapolovinko@gmail.com
                      </p>
                    </div>
                  </div>
                  <div class="center">
                    <p class="edit_active">Активен</p>
                  </div>
                  <div class="center">
                    <p class="edit_text">Менеджер</p>
                  </div>
                  <div class="btns">
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8.82231 0.5C8.56215 0.5 8.35124 0.710907 8.35124 0.971074V2.74768C7.61716 2.92912 6.91437 3.2195 6.26632 3.60914L5.01431 2.3539C4.92601 2.26537 4.80613 2.21558 4.68109 2.2155C4.55605 2.21542 4.4361 2.26505 4.34769 2.35347L2.35347 4.34769C2.26505 4.4361 2.21542 4.55605 2.2155 4.68109C2.21558 4.80613 2.26537 4.92601 2.3539 5.01431L3.60914 6.26632C3.2195 6.91437 2.92912 7.61716 2.74768 8.35124H0.971074C0.710907 8.35124 0.5 8.56215 0.5 8.82231V11.1777C0.5 11.4379 0.710907 11.6488 0.971074 11.6488H2.74768C2.92912 12.3828 3.2195 13.0856 3.60914 13.7337L2.3539 14.9857C2.26537 15.074 2.21558 15.1939 2.2155 15.3189C2.21542 15.444 2.26505 15.5639 2.35347 15.6523L4.34769 17.6465C4.4361 17.7349 4.55605 17.7846 4.68109 17.7845C4.80613 17.7844 4.92601 17.7346 5.01431 17.6461L6.26632 16.3909C6.91437 16.7805 7.61716 17.0709 8.35124 17.2523V19.0289C8.35124 19.2891 8.56215 19.5 8.82231 19.5H11.1777C11.4379 19.5 11.6488 19.2891 11.6488 19.0289V17.2523C12.3828 17.0709 13.0856 16.7805 13.7337 16.3909L14.9857 17.6461C15.074 17.7346 15.1939 17.7844 15.3189 17.7845C15.444 17.7846 15.5639 17.7349 15.6523 17.6465L17.6465 15.6523C17.7349 15.5639 17.7846 15.444 17.7845 15.3189C17.7844 15.1939 17.7346 15.074 17.6461 14.9857L16.3909 13.7337C16.7805 13.0856 17.0709 12.3828 17.2523 11.6488H19.0289C19.2891 11.6488 19.5 11.4379 19.5 11.1777V8.82231C19.5 8.56215 19.2891 8.35124 19.0289 8.35124H17.2523C17.0709 7.61716 16.7805 6.91437 16.3909 6.26632L17.6461 5.01431C17.7346 4.92601 17.7844 4.80613 17.7845 4.68109C17.7846 4.55605 17.7349 4.4361 17.6465 4.34769L15.6523 2.35347C15.5639 2.26505 15.444 2.21542 15.3189 2.2155C15.1939 2.21558 15.074 2.26537 14.9857 2.3539L13.7337 3.60914C13.0856 3.2195 12.3828 2.92912 11.6488 2.74768V0.971074C11.6488 0.710907 11.4379 0.5 11.1777 0.5H8.82231ZM6.70248 10C6.70248 8.17883 8.17883 6.70248 10 6.70248C11.8212 6.70248 13.2975 8.17883 13.2975 10C13.2975 11.8212 11.8212 13.2975 10 13.2975C8.17883 13.2975 6.70248 11.8212 6.70248 10Z" fill="#AFB6C1"/>
                    </svg>
                    <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M16 17V7H4V17C4 18.1046 4.89543 19 6 19H14C15.1046 19 16 18.1046 16 17Z" fill="#AFB6C1"/>
                      <path d="M7.44721 1.10557L6.5 3H2V5H18V3H13.5L12.5528 1.10557C12.214 0.428004 11.5215 0 10.7639 0H9.23607C8.47852 0 7.786 0.428005 7.44721 1.10557Z" fill="#AFB6C1"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
      };
    },
  };
  </script>
  
  <style scoped>
  .transition {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 20px;
  }
  .eidt-link {
    font-family: TT Norms Medium;
    font-size: 20px;
    line-height: 24px;
    text-align: left;
    text-decoration: none;
    color: #AFB6C1;
  }
  .creation_text {
    color: #535C69;
    font-family: TT Norms Medium;
    font-size: 20px;
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
  .edit {
    width: 60%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    gap: 40px;
  }
  .edit_top{
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .basket{
    height: 34px;
    width: 34px;
    border: 1px solid #F3F5F6;
    background: #FFFFFF;
    padding: 0;
  }
  .send{
    background: #EFEFFF;
    color: #6266EA;
  }
  .send:hover{
    background: #6266EA;
    color: #FFFFFF;   
  }
  .edit_wrapper{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 1fr;
  }
  .edit_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
  }
  .divider {
    border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
    width: auto;
    margin: 10 0;
  }
  .avatar{
    height: 32px;
    width: 32px;
    border-radius: 100px;
  }
  .name_head{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
  }
  .name_sub{
    font-family: TT Norms Medium;
    font-size: 12px;
    line-height: 14px;
    letter-spacing: 0.03em;
    text-align: left;
    color: #AFB6C1;
  }
  .img_container{
    display: flex;
    gap: 10px;
    align-items: center;
  }
  p{
    margin: 0;
  }
  .edit_bottom{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 1fr;
  }
  .btns{
    display: flex;
    gap: 10px;
    align-items: center;
  }
  .bottom{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .center{
    display: flex;
    align-items: center;
  }
  .edit_active{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #04C562;
  }
  .edit_container:hover{
    background: #F3F6F8;
    transition: all 0.5;
  }
  </style>