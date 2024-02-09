<template>
    <div class="nav">
        <div class="search">
            <input type="text" placeholder="Найти">
        </div>
        <div class="actions">
            <div class="buttons-menu">
                <a href="">
                    <img src="../../static/img/icon-file.png" alt="1">
                </a>
                <a @click="showPlusNotifications" style="cursor: pointer;">
                    <img src="../../static/img/icon-plus.png" alt="2">
                </a>
                <a href="">
                    <img src="../../static/img/icon-ring.png" alt="3">
                </a>
                <a @click="showNotifications" style="cursor: pointer;">
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
        };
    },
    methods: {
        showNotifications() {
            this.showNotificationPanel = !this.showNotificationPanel;
        },
        showPlusNotifications() {
            this.showPlusNotificationPanel = !this.showPlusNotificationPanel;
        },
    },
};
</script>

<style scoped>
img{
    width: 20px;
}
.nav{
    margin: 30px 30px 30px 0px;
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
}

.rate h4{
    margin: 0;
    color: #52565F;
}
.notification-panel {
    width: 260px;
    height: 84px;
    background-color: #ffffff;
    position: absolute;
    top: 110px;
    right: 120px;
    border-radius: 5px;
    padding: 10px;
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
  padding: 10px;
  text-align: center;
}
.create{
  display: flex;
  gap: 10px;
}
.create:hover {
  background-color: #FAFAFA;
  cursor: pointer;
}
.create:hover p {
  color: #535C69;
  font-weight: bold;
}
</style>