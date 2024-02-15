<template>
  <div class="main">
    <h2>Настройка профиля</h2>
    <div class="settings">
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
              <label class="custom-file-upload">
                <input type="file" accept="image/*"/>Нажмите, чтобы загрузить
              </label>
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
          <p class="password">Был установлен 3 месяца назад</p>
          <button @click="showModals" type="button" class="button-change">Изменить пароль</button>
          <ChangePasswordPage v-if="showModal"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChangePasswordPage from './ChangePasswordPage.vue';

export default {
  components: { ChangePasswordPage },
  data() {
    return {
      showModal: false,
    };
  },
  methods: {
    showModals() {
      this.showModal = true;
    }
  }
};
</script>

<style scoped>

.settings {
  text-align: center;
  width: 35vw;
  height: auto;
  background-color: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
}

.name-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

label {
  margin-right: 10px;
  margin-bottom: 20px;
  font-family: TT Norms;
  font-size: 13px;
  font-weight: bold;
  line-height: 15px;
  letter-spacing: 0em;
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
.custom-file-upload {
  width: 260px;
  height: 36px;
  display: flex;
  padding: 8px 10px;
  cursor: pointer;
  background-color: #F3F5F6;
  color: #D2D8DE;
  align-items: center;
  margin-bottom: 0;
  font-weight: 500;
}

.custom-file-upload input[type="file"] {
  display: none;
}
.password{
  color: #7D838C;
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
}
h2{
  margin: 0;
  padding-bottom: 20px;
}
</style>