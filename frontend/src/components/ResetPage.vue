<template>
  <div class="reset">
    <div class="container">
      <div class="header">
        <div class="subheader">SKED</div>
        <div class="subtext">Онлайн запись — легко!</div>
      </div>
      <div class="Forma">
        <div class="reset-prompt">
          Нет аккаунта? <router-link to="/register" class="login-link" style="text-decoration: none;">Зарегистрироваться</router-link>
        </div>
        <div class="reset-form">
          <h2>Восстановление<br>пароля</h2>
          <form @submit.prevent="resetPassword">
            <div class="form-group">
              <p class="mail">Мы отправим код подтверждения<br>на указанную почту или номер</p>
              <label for="username">Почта</label>
              <input v-model="email" type="email" id="username" name="username" placeholder="Usermail@gmail.com" required>
            </div>
            <div class="reset">
              <button type="submit">Восстановить пароль</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
    };
  },
  methods: {
    async resetPassword() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/password_reset/', {
          email: this.email,
        });

        // Обработка успешного ответа
        console.log(response.data);

        // Возможно, вы захотите обновить интерфейс или перенаправить пользователя после успешного сброса пароля
      } catch (error) {
        // Обработка ошибок
        console.error('Error:', error.response.data);
      }
    },
  },
};
</script>

    <style>
    .container {
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
    
    .subheader {
      text-align: left;
      color: #FFF;
      font-family: "TT Norms Bold";
      font-size: 64px;
      font-style: normal;
      line-height: normal;
    }
    
    .subtext {
      color: #FFF;
      font-family: "TT Norms";
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
      font-family: "TT Norms";
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
      height: 350px;
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
    </style>