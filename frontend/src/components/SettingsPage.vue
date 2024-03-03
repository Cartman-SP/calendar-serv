<template>
  <div class="main">
    <h2>Настройка профиля</h2>
    <div class="settings">
      <div class="forms">
        <div class="name">
          <div class="name-container">
            <label for="userName">Имя</label>
            <div class="input_container_top">
              <input type="text" id="userName" v-model="User.name">
              <button @click="saveName" class="button-save">Сохранить изменения</button>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="photo">
          <div class="photo-container">
            <label for="userPhoto">Фотография</label>
            <div class="input_container">
              <input type="file" accept="image/*" ref="fileInput"/>Нажмите, чтобы загрузить
              <button @click="saveImage" class="button-save">Сохранить изменения</button>
            </div>
            <p class="photo-info">до 5 МБ, PNG, JPG, JPEG. Для замены удалите миниатюру и загрузите заново</p>
          </div>
        </div>
        <div class="divider"></div>
        <div class="email">
          <div class="email-container"> 
            <label for="userMail">Email</label>
            <p><span class="email-header">Будьте внимательны!</span> Email является логином для входа в сервис, если вы измените Email, то при авторизации нужно использовать обновленный Email</p>
            <div class="input_container_mail">
              <input type="mail" id="userMail" :value="this.$store.state.registrationData.email" disabled>
              <div class="email-btn">
                <button @click="acceptMail">Подтвердить Email</button>
                <button @click="changeMail" class="button-change">Изменить email</button>
                <ChangeMailPage v-if="showMail"/>
              </div>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="phone">
          <div class="phone-container">
            <label for="userPhone">Телефон</label>
            <p>Получайте SMS-уведомления о новых заявках</p>
            <div class="input_container_phone">
              <input id="userphone" :value="'+'+User.phone.toString()" disabled>
              <div class="phone-btn">
                <button @click="acceptPhone">Подтвердить телефон</button>
                <button @click="changePhone" class="button-change">Изменить Телефон</button>
                <ChangePhonePage v-if="showPhone"/>
              </div>
            </div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="change">
          <label>Пароль</label>
          <p class="password">Был установлен {{when_changed}}</p>
          <button @click="showModals" type="button" class="button-change">Изменить пароль</button>
          <ChangePasswordPage v-if="showModal"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChangePasswordPage from './ChangePasswordPage.vue';
import ChangeMailPage from './ChangeMailPage.vue';
import ChangePhonePage from './ChangePhonePage.vue';
import axios from 'axios';  


export default {
  components: { ChangePasswordPage, ChangeMailPage, ChangePhonePage },
  data() {
    return {
      showModal: false,
      showMail: false,
      showPhone: false,
      when_changed: 'Недавно',
      User: {
        name: '',
        avatar: '',
        email: '',
        phone: '',
      }
    };
  },
  methods: {
    showModals() {
      this.showModal = true;
    },
    changeMail() {
      this.showMail = true;
    },
    changePhone() {
      this.showPhone = true;
    },

    get_profile(){
      axios.post('http://127.0.0.1:8000/api/getprofile/', { user_id:  this.$store.state.registrationData.user_id})
      .then(response => {
        this.avatar = "http://127.0.0.1:8000" + response.data.profile.avatar
        this.User.name = response.data.profile.name
        console.log(response.data)
        this.position = response.data.profile.name // сделать должность
        this.company = response.data.profile.company_name
        this.User.phone =response.data.phone
        if(response.data.password_set==0){
          this.when_changed = "сегодня"
        }else if(response.data.password_set==30){
          this.when_changed = `месяц назад`
        }else if(response.data.password_set>0){
          this.when_changed = `${response.data.password_set} дней назад`
        }else if(response.data.password_set<122){
          this.when_changed = `${Math.floor(response.data.password_set/30)} месяца назад`
        }else if(response.data.password_set>122){
          this.when_changed = `${Math.floor(response.data.password_set/30)} месяцев назад`
        }
        console.log()
      })
      .catch(error => {
        // Ошибка при получении данных
        console.error('Ошибка при получении данных о пользователе:', error);
      });
    },
    saveName() {
      axios.post('http://127.0.0.1:8000/api/change_name/', { 
          id: this.$store.state.registrationData.user_id,
          name: this.User.name 
        })
        .then(response => {
          console.log('Имя успешно сохранено:', response.data);
          window.location.reload();
        })
        .catch(error => {
          console.error('Ошибка при сохранении имени:', error);
        });
    },
    saveImage() {
      const formData = new FormData();
      formData.append('id', this.$store.state.registrationData.user_id);
      formData.append('avatar', this.$refs.fileInput.files[0]);

      axios.post('http://127.0.0.1:8000/api/change_avatar/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(response => {
          console.log('Изображение успешно сохранено:', response.data);
          window.location.reload();
        })
        .catch(error => {
          console.error('Ошибка при сохранении изображения:', error);
        });
    },
  },
  mounted(){  
    this.get_profile();
  }
};
</script>

<style scoped>

.settings {
  text-align: center;
  width: 40vw;
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
  width: 50%;
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
  font-size: 14px;
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
  width: auto;
  margin: 20px 0;
}
.custom-file-upload {
  width: 50%;
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
  color: #AFB6C1;
  font-family: TT Norms Medium;
  font-size: 10px;
  line-height: 10px;
  letter-spacing: 0em;
  margin: 5px 0;
}
span{
  font-weight: bold;
}
.input_container_mail input {
  position: relative;
  background-image: url(../../static/img/warning.svg);
  background-repeat: no-repeat;
  background-position: calc(100% - 15px) center;
}
.input_container_phone input {
  position: relative;
  background-image: url(../../static/img/warning.svg);
  background-repeat: no-repeat;
  background-position: calc(100% - 15px) center;
}

.input_container_mail:hover::after {
  content: "Email адрес не подтвержден";
  display: flex;
  height: 36px;
  width: auto;
  background-color: #FFFFFF;
  color: #7D838C;
  position: absolute;
  left: 30%;
  top: 515px; /* Положение псевдоэлемента относительно input */
  z-index: 15;
  padding: 0 10px;
  border-radius: 5px;
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  transition: all ease 0.3s;
  align-items: center;
  box-shadow: 0px 2px 8px 0px #7D879066;
}

.input_container_phone:hover::after {
  content: "Телефон не подтвержден";
  display: flex;
  height: 36px;
  width: auto;
  background-color: #FFFFFF;
  color: #7D838C;
  position: absolute;
  left: 30%;
  top: 67%; /* Положение псевдоэлемента относительно input */
  z-index: 15;
  padding: 0 10px;
  border-radius: 5px;
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  transition: all ease 0.3s;
  align-items: center;
  box-shadow: 0px 2px 8px 0px #7D879066;
}
</style>