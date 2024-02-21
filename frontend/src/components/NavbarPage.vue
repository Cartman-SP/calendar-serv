<template>
    <div class="nav">
        <div class="search">
            <input type="text" placeholder="Найти">
        </div>
        <div class="actions">
            <div class="buttons-menu">
                <a @click="showGatesNotifications">
                    <img src="../../static/img/icon-file.png" alt="1">
                </a>
                <a @click="showPlusNotifications">
                    <img src="../../static/img/icon-plus.png" alt="2">
                </a>
                <a href="">
                    <img src="../../static/img/icon-ring.png" alt="3">
                </a>
                <a @click="showNotifications">
                    <img src="../../static/img/icon-bell.png" alt="4">
                </a>
            </div>
            <div class="rate">
                <img src="../../static/img/icon-wallet.png" alt="231">
                <div class="text">
                    <p>Тариф</p>
                    <h4>Пробный</h4>
                </div>
            </div>
        </div>
        <!-- Дополнительный блок для уведомлений -->
        <div  v-if="showGatesNotificationPanel" class="gates">
          <div class="gates_svg">
            <svg width="32" height="32" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12L10 7.24L14 12L6 12Z" fill="white"/>
            </svg>
          </div>
            
          <div class="gates-panel">
            <p class="teg_head">Быстрое проектов</p>
            <div class="wrapper">
              <div class="teg">
                <div class="teg_svg">
                  <svg width="16" height="16" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 0C0.895431 0 0 0.895431 0 2V15C0 16.1046 0.89543 17 2 17H16C17.1046 17 18 16.1046 18 15V4C18 2.89543 17.1046 2 16 2H7C7 0.895431 6.10457 0 5 0H2Z" fill="white"/>
                  </svg>
                </div>  
                <div class="wrapper_name">
                  <p class="wrapper_head">Барбершоп на Сатпаева</p>
                  <p class="wrapper_subhead">ID 124568 (Владелец)</p>
                </div>
              </div>
              <input type="search" placeholder="Найти проект">
              <div class="teg">
                <div class="avatar">
                  <p class="avatar_text">АР</p>
                </div>
                <div class="wrapper_name">
                  <p class="wrapper_descr">Аренда роликов</p>
                  <p class="wrapper_subhead">ID 254987 (Владелец)</p>
                </div>
              </div>
            </div>
            <router-link to="/lk/project" style="text-decoration:none">
              <div class="bottom">
                <svg width="14" height="14" viewBox="0 0 18 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2 0C0.895431 0 0 0.895431 0 2V15C0 16.1046 0.89543 17 2 17H16C17.1046 17 18 16.1046 18 15V4C18 2.89543 17.1046 2 16 2H7C7 0.895431 6.10457 0 5 0H2Z" fill="#AFB6C1"/>
                </svg>
                <p class="bottom_text">Всего проектов (0)</p>
              </div>
            </router-link>
          </div>
        </div>
        <div v-if="showPlusNotificationPanel" class="plus-panel">
          <p class="header">Быстрое создание</p>
          <router-link to="/lk/" style="text-decoration:none">
            <div class="create">
              <img src="../../static/img/plus/send.svg" alt="">
              <p class="subheader">Заявки</p>
            </div>
          </router-link>
          <router-link to="/lk/service/create" style="text-decoration:none">
            <div class="create">
              <img src="../../static/img/plus/list.svg" alt="">
              <p class="subheader">Услуги</p>
            </div>
          </router-link>
          <router-link to="/lk/personal/employees" style="text-decoration:none">
            <div class="create">
              <img src="../../static/img/plus/default.svg" alt="">
              <p class="subheader">Сотрудника</p>
            </div>
          </router-link>
          <router-link to="/lk/branch/createbranch" style="text-decoration:none">
            <div class="create">
              <img src="../../static/img/plus/case.svg" alt="">
              <p class="subheader">Филиала</p>
            </div>
          </router-link>
        </div>
        <div v-if="showNotificationPanel" class="notification-panel">
          <p class="header">Уведомления</p>
          <p class="subheader">У вас нет новых уведомлений</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showNotificationPanel: false,
            showPlusNotificationPanel: false,
            showGatesNotificationPanel: false,
        };
    },
    methods: {
        showNotifications() {
            this.showNotificationPanel = !this.showNotificationPanel;
        },
        showPlusNotifications() {
            this.showPlusNotificationPanel = !this.showPlusNotificationPanel;
        },
        showGatesNotifications() {
            this.showGatesNotificationPanel = !this.showGatesNotificationPanel;
        },
    },
};
</script>

<style scoped>
img{
    width: 16px;
}
.nav{
    margin-bottom: 20px;
    height: 4vw;
    width: 100%;
    display: flex;
    background-color: #F3F6F8;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
    border-radius: 10px;
}

.search input{
    background-color: #ffffff;
    color:#D2D8DE;
    margin: 0;
    width: 15vw;
    font-weight: bold;
}

.search input:focus{
    outline: solid 1px #6266EA;
}

.actions, .buttons-menu, .rate{
    display: flex;
    align-items: center;
}
.buttons-menu{
  margin-right: 20px;
}

.buttons-menu a{
    background-color: white;
    width: 40px;
    height: 40px;
    border-radius: 20px;
    margin: 0 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.rate{
    text-align: left;
    background-color: white;
    height: 50px;
    padding: 20px;
    border-radius: 25px;
}

.text{
    margin-left: 20px;
}

.rate p{
    margin: 0;
    color: #D2D8DE;
    font-size: 10px;
}

.rate h4{
    margin: 0;
    color: #52565F;
    font-size: 14px;
}
.notification-panel {
    width: 260px;
    height: 84px;
    background-color: #ffffff;
    position: absolute;
    top: 110px;
    right: 120px;
    border-radius: 5px;
    padding: 20px;
    text-align: center;
}

.header{
  font-family: TT Norms;
  font-size: 15px;
  font-weight: bold;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color:#535C69;
  margin-bottom: 20px;
}
.subheader{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0em;
  text-align: left;
  color:#AFB6C1;
}
.plus-panel {
  width: 260px;
  height: 230px;
  background-color: #ffffff;
  position: absolute;
  top: 110px;
  right: 240px;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
}
.create{
  display: flex;
  gap: 10px;
  padding: 10px;
}
.create:hover {
  background-color: #FAFAFA;
  cursor: pointer;
}
.create:hover p {
  color: #535C69;
  font-weight: bold;
}
a{
  cursor: pointer;
}
.wrapper_head{
  font-family: TT Norms;
  font-size: 13px;
  font-weight: bold;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #6266EA;
}
.wrapper_subhead{
  font-family: TT Norms;
  font-size: 12px;
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0.03em;
  text-align: left;
  color: #AFB6C1;
}
p{
  margin: 0;
}
.teg{
  display: flex;
  gap: 10px;
  align-items: center;
}
.teg_svg{
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #6266EA;
  background: #F97F7F;
  border-radius: 30px;
  height: 36px;
  width: 36px;
}
.wrapper_descr{
  font-family: TT Norms;
  font-size: 13px;
  font-weight: bold;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color: #535C69;
}
.teg_head{
  font-family: TT Norms;
  font-size: 15px;
  font-weight: bold;
  line-height: 15px;
  letter-spacing: 0em;
  text-align: left;
  color:#535C69;
}
input{
  margin: 0;
}
.avatar{
  height: 32px;
  width: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #28CCF0;
  border-radius: 30px;
}
.avatar_text{
  width: 16px;
  height: 16px;
  font-weight: bold;
  color: #FFFFFF;
  font-size: 13px;
}
.gates-panel {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 330px;
  height: 480px;
  background-color: #ffffff;
  position: absolute;
  top: 110px;
  right: 270px;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
}
.wrapper{
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
  padding: 10px;
}
.bottom{
  display: flex;
  gap: 5px;
  padding: 10px;
}
.bottom_text:hover{
  color: #535C69;
}
.bottom_text{
  font-family: TT Norms;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
}
</style>