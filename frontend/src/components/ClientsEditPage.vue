<template>
  <div class="main">
    <div class="transition">
      <router-link to="/dashboard/clients" class="employesss-link">Клиенты</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">ИМЯ ФАМИЛИЯ</p>
    </div>

    <div class="settings">
      <div class="forms">
        <div class="name">
          <div class="name-container">
            <label for="userName">{{clientData.firstname}}</label>
            <div class="input_container_top">
              <input type="text" placeholder="Введите имя">
            </div>
          </div>
        </div>
        <div class="second_name">
          <div class="name-container">
            <label for="">Фамилия</label>
            <div class="input_container_top">
              <input type="text" placeholder="Введите фамилию">
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="photo">
          <div class="photo-container">
            <label for="userPhoto">Фотография</label>
            <div class="input_container">
              <label class="custom-file-upload">
                <input type="file" accept="image/*" ref="fileInput" @change="handleFileUpload($event)"/><span :class="{'inputFile-empty' : !fileNameVariable, 'inputFile-file' : fileNameVariable}">{{ fileNameVariable || 'Нажмите, чтобы загрузить' }}</span>
              </label>
            </div>
            <p class="photo-info">до 5 МБ, PNG, JPG, JPEG. Для замены - загрузите заново</p>
          </div>
        </div>
        <div class="divider"></div>
        <div class="email">
          <div class="email-container">
            <label for="userMail">Email (необязательно)</label>
            <input type="mail" placeholder="client@mail.ru">
            <p class="email-header">Клиент еще не подтвердил свою почту</p>
          </div>
        </div>
        <div class="divider"></div>
        <div class="phone">
          <div class="phone-container">
            <label for="userPhone">Телефон</label>
            <input id="userphone" disabled placeholder="+7">
            <p class="email-header">Клиент еще не подтвердил свой номер телефона</p>
          </div>
        </div>
        <div class="divider"></div>
        <div class="change">
          <button type="button" class="button-change">Сохранить</button>
          <button type="button" class="button-back">Вернуться назад</button>
        </div>
      </div>
    </div>
    <MessageAlert :message="alertMessage" :color="alertColor"/>
  </div>
</template>

<script>
import MessageAlert from "../components/MessageAlert.vue";
export default {
  components: { MessageAlert },
  data() {
    return {
      clientData: {},
    }
  },
  methods:{
    getClientDataById(){ //Функция для получения данных о клиенте по id
      const id = this.$route.params.clientId;
      console.log('kek', id)
    }
  },
  mounted(){
    this.getClientData();
  }

}
</script>

<style scoped>
.main{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.transition {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.employesss-link {
  font-family: 'TT Norms Medium';
  font-size: 20px;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}
.creation_text {
  color: #535C69;
  font-family: 'TT Norms Medium';
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
.inputFile-empty{
  font-family: TT Norms;
  color: #D2D8DE;
}

.inputFile-file{
  font-family: TT Norms;
  color: #535C69;
}
.settings {
  text-align: center;
  width: fit-content;
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
  margin-bottom: 5px;
  font-family: TT Norms Medium;
  font-size: 13px;
  line-height: 15px;
  letter-spacing: 0em;
}

.input_container {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}
.input_container_mail {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}
.input_container_phone {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}
.input_container_top {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}

input {
  margin-bottom: 0;
  width: 100%;
}

.email-btn{
  display: flex;
  flex-direction: row;
  gap: 10px;
}

p{
  text-align: left;
  margin: 10px 0;
  width: 450px;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 17px;
  letter-spacing: 0em;
  color: rgba(83, 92, 105, 0.7);
}

.email-header{
  font-family: TT Norms Medium;
  font-size: 12px;
  font-weight: 500;
  line-height: 14.16px;
  text-align: left;
  color: #7D838C;
  margin-top: 5px;
  margin-bottom: 0;
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
  width: auto;
  margin: 20px 0;
}
.custom-file-upload {
  width: 100%;
  height: 36px;
  display: flex;
  padding: 8px 10px;
  cursor: pointer;
  background-color: #F3F5F6;
  color: #D2D8DE;
  align-items: center;
  margin-bottom: 0;
  font-weight: 500;
  background-image: url(../../static/img/paperclip.svg);
  background-repeat: no-repeat;
  background-position: calc(100% - 15px) center;
}

.custom-file-upload input[type="file"] {
  display: none;
}
.password{
  color: #7D838C;
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
}
h2{
  font-family: TT Norms Medium;
  margin: 0;
  padding-bottom: 20px;
  color: #535C69;
}
.photo-info{
  color: #D2D8DE;
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14.16px;
  text-align: left;
  
  margin: 5px 0;
}
span{
  font-weight: bold;
}
input::placeholder {
  font-family: 'TT Norms Medium';
  font-size: 13px;
  line-height: 17px;
  letter-spacing: 0em;
  color: #D2D8DE;
}
.name{
  margin-bottom: 20px;
}
.change{
  justify-content: end;
  display: flex;
  gap: 10px;
}
.button-back{
  background: #FFFFFF;
  border: 1px solid #DDE1E5;
  color: #535C69;
}
.button-back:hover{
  color: #6266EA;
}
</style>