<template>
  <div class="reset">
    <div v-if="reset_page" class="container3">
      <div class="header">
        <div class="subheader2">SKED</div>
        <div class="subtext">Онлайн запись — легко!</div>
      </div>
      <div class="Forma">
        <div class="reset-prompt">
          Нет аккаунта? <router-link to="/register" class="login-link" style="text-decoration: none;">Зарегистрироваться</router-link>
        </div>


        <div class="reset-form" :class="{'modal-show' : isModalVisible, 'modal-hide' : !isModalVisible}">
          <h2>Восстановление<br>пароля</h2>
          <form v-if="step === 1" @submit.prevent="resetPassword">
            <div class="form-group">
              <p class="mail">Мы отправим код подтверждения<br>на указанную почту</p>
              <label for="username">Почта</label>
              <input v-model="email" autocomplete="new-password"  type="email" id="username" name="username" placeholder="Usermail@gmail.com" required>
            </div>
            <div class="reset-btn">
              <button type="submit" @click="send_email, step = 2">Восстановить пароль</button>
              <p class="error-btn" v-if="error">{{ error }}</p>
            </div>
          </form>

          <form v-if="step === 2" @submit.prevent="resetPassword">
            <div class="form-group">
              <p class="mail">Мы отправили код подтверждения<br>на указанную почту</p>
              <label for="username">Код подтверждения</label>
              <input v-model="code" autocomplete="new-password" type="text" id="code" name="code" placeholder="Введите код подтверждения" required>
            </div>
            <div class="form-group">
              <label for="username">Новый пароль</label>
              <input v-model="newPassword" autocomplete="new-password" type="password" id="newPassword" name="newPassword" placeholder="Введите код подтверждения" required>
            </div>
            <div class="reset-btn">
              <button type="submit" @click="newPass">Сменить пароль</button>
              <p class="error-btn" v-if="error">{{ error }}</p>
            </div>
          </form>
        </div>
      </div>
    </div>
    <RecoveryPage v-else :email="email"/>
  </div>
</template>

<script>
import axios from 'axios';
import RecoveryPage from './RecoveryPage.vue';
export default {
  components: { RecoveryPage },
  data() {
    return {
      email: '',
      reset_page: true,
      error: '',

      isModalVisible: false,
      step: 1,
    };
  },
  mounted(){
    this.opacityAnimation()
  },
  watch: {
    email(){
      this.error = ''
    },
  },
  methods: {
    opacityAnimation(){
      this.isModalVisible = false;
      setTimeout(() => {
        this.isModalVisible = true;
      }, 200);
    },
    send_email(){
            if (this.email.length === 0) {
              this.error = 'Пожалуйста, введите почту'
            } else{
              const apiUrl = 'http://127.0.0.1:8000/api/pass_reset/';

              const data = {
              email: this.email,
              };

              axios.post(apiUrl, data)
              .then(response => {
                  // Обработка успешного ответа от сервера
                  console.log('Ответ от сервера:', response.data);
                  this.reset_page = false
              })
              .catch(error => {
                  this.error = 'Аккаунта с такой почтой не существует'
                  console.error('Произошла ошибка при отправке запроса:', error);
              });
            }
        },
  },
};
</script>

    <style scoped>
    .modal-show{
      opacity: 1;
      transform: translateX(0);
      transition: all .8s ease;
    }

    .modal-hide{
      opacity: 0;
      transform: translateX(-20px);
      transition: all .8s ease;
    }

    .container3 {
      font-family: "TT Norms Medium";
      height: 100vh;
      padding: 0 30vw;
      display: flex;
      width: 100vw;
      justify-content: space-between;
      align-items: center;
    }
    
    .header{
      display: flex;
      flex-direction: column;
      text-align: left;
    }
    
    .subheader2 {
      text-align: left;
      color: #FFF;
      font-family: "TT Norms Bold";
      font-size: 64px;
      font-style: normal;
      line-height: normal;
    }
    
    .subtext {
      color: #FFF;
      font-family: "TT Norms Medium";
      font-size: 28px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
    }
    
    
    .Forma {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    
    .mail{
      color:#535C69;
      font-size: 13px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-bottom: 20px;
      text-align: left;
    }
    
    .reset-prompt {
      padding: 0 80px 0 0;
      text-align: left;
      width: 340px;
      color: var(--cold-text-ghost-500, #DDE1E5);
      font-family: "TT Norms Medium";
      font-size: 13px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-bottom: 10px;
    }
    
    .reset-link {
      color: #04C562;
      text-decoration: underline;
      cursor: pointer;
    }
    
    .reset-form {
      background: #fff;
      width: 340px;
      height: fit-content;
      margin: 0 auto;
      padding: 40px;
      border-radius: 5px;
      box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.10);
    }
    
    .form-group {
      margin-bottom: 20px;
    }
    
    .input-container {
      position: relative;
    }
    .reset-btn{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .reset-btn button{
      font-family: "TT Norms Medium";
      width: fit-content;
    }
    .error-btn{
      margin: 0;
      text-align: left;
      font-family: TT Norms Medium;
      font-size: 12px;
      line-height: 14px;
      letter-spacing: 0em;
      text-align: left;
      color: #F97F7F;
    }

    @media (max-width: 1641px){
      .container3{
        padding: 0 20vw;
      }
    }
    @media (max-width: 1280px){
      .container3{
        padding: 0 10vw;
      }
    }
    @media (max-width: 991px){
      .container3{
        padding: 0 10vw;
        flex-direction: column;
        height: 100vh;
        gap: 30px;
        align-items: center;
        justify-content: center;
      }
      .subheader2{
        text-align: center;
        font-size: 32px;
        color: #FFFFFF;
      }
    }
    </style>