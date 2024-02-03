<template>
  <div class="main">
    <div class="settings">
      <h2>Настройка профиля</h2>
      <div class="forms">
        <div class="name">
          <div class="name-container">
            <label for="userName">Имя</label>
            <div class="input-container">
              <input type="text" id="userName">
              <button @click="saveName" class="button-save">Сохранить изменения</button>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="photo">
          <div class="photo-container">
            <label for="userPhoto">Фотография</label>
            <div class="input-container">
              <input type="file" id="userPhoto" accept=".png, .jpeg, .jpg">
              <button @click="saveName" class="button-save">Сохранить изменения</button>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="email">
          <div class="email-container"> 
            <label for="userMail">Email</label>
            <p><span class="email-header">Будьте внимательны!</span> Email является логином для входа в сервис, если вы измените Email, то при авторизации нужно использовать обновленный Email</p>
            <div class="input-container">
              <input type="mail" id="userMail">
              <div class="email-btn">
                <button @click="acceptMail">Подтвердить Email</button>
                <button @click="changeMail" class="button-change">Изменить email</button>
              </div>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="phone">
          <div class="phone-container">
            <label for="userPhone">Телефон</label>
            <p>Получайте SMS-уведомления о новых заявках</p>
            <div class="input-container">
              <input type="number" id="userphone">
              <div class="phone-btn">
                <button @click="acceptPhone">Подтвердить телефон</button>
                <button @click="changePhone" class="button-change">Изменить Телефон</button>
              </div>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="change">
          <label>Пароль</label>
          <p>Был установлен 3 месяца назад</p>
          <button @click="showModals" class="button-change">Изменить пароль</button>
        </div>
      </div>
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
  components: { NavbarPage, SidebarPage},
  data() {
    return {
    };
  },
  methods: {
    showModals() {
      
    }
  }
};
</script>

<style scoped>
.navigation {
  display: flex;
  background-color: white;
}

.settings {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 635px;
}

.name-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.label-container {
  display: flex;
  align-items: center;
}

label {
  margin-right: 10px;
  margin-bottom: 20px;
}

.input-container {
  display: flex;
  align-items: center;
}

input {
  margin-bottom: 0;
  margin-right: 10px;
}

.email-btn{
  display: flex;
  flex-direction: row;
  gap: 10px;
}

p{
  text-align: left;
  margin-bottom: 25px;
  width: 450px;
  font-family: TT Norms;
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 300;
  line-height: 17px;
  letter-spacing: 0em;
  color: rgba(83, 92, 105, 0.7);
}

.email-header{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 700;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: rgba(83, 92, 105, 0.7);
}
.phone-btn{
  display: flex;
  flex-direction: row;
  gap: 10px;
}

.button-save {
  background-color: #EFEFFF;
  color: #6266EA;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}
.button-save:hover {
  background-color: #DBDDFF;
  color: #6266EA;
}
.button-change {
  background-color: #EFEFFF;
  color: #6266EA;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.button-change:hover {
  background-color: #DBDDFF;
  color: #6266EA;
}
.divider {
  border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
  width: 590px;
  margin: 10px 0;
}

</style>