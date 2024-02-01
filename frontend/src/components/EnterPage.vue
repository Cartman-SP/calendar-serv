<template>
  <div class="login">
    <div class="container1">
      <div class="Forma">
        <div class="login-prompt">
          Нет аккаунта? <router-link to="/register" class="login-link">Зарегистрироваться</router-link>
        </div>
        <div class="registration-form">
          <h2>Вход</h2>
          <form @submit.prevent="loginUser">
            <div class="form-group">
              <label for="username">Почта или телефон</label>
              <input v-model="usernameOrEmail" id="username" name="username" placeholder="Usermail@gmail.com" required>
            </div>
            <div class="form-group">
              <label for="password">Пароль</label>
              <PasswordComponent v-model="passwordValue" toggleMask />
            </div>
            <div class="reset">
              <button type="submit">Войти</button>
              <router-link to="/reset" class="ResetPassword">Восстановить пароль</router-link>
            </div>
            <div class="social-icons">
              <!-- ... (ваш текущий код) ... -->
            </div>
          </form>
          <div id="error">{{ errorMessage }}</div>
        </div>
      </div>
      <div class="man">
        <img src="../../static/img/Man.png" alt="">
        <div class="man_head">
          <div class="man_header">Здравствуйте!</div>
          <div class="man_subheader">Зарегистрируйтесь или войдите, чтобы <br>получить полный доступ к безграничному <br> функционалу Calendar</div>
          <div class="man_button-container">
            <router-link to="/register" class="man_button">Регистрация</router-link>
          </div>
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
      usernameOrEmail: '',
      passwordValue: '',
      errorMessage: '', // Обновленное имя переменной для ошибки
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          username_or_email: this.usernameOrEmail,
          password: this.passwordValue,
        });

        // Сохраняем данные пользователя в хранилище Vuex
        this.$store.dispatch('saveRegistrationData', response.data);

        // Очищаем ошибку в случае успешной авторизации
        this.errorMessage = '';

        // Переход на другую страницу (например, после успешной авторизации)
        this.$router.push('/profile');
      } catch (error) {
        console.error('Ошибка входа', error);

        if (error.response && error.response.data && error.response.data.error) {
          // Если есть информация об ошибке в ответе сервера, устанавливаем её
          this.errorMessage = 'Ошибка входа: ' + error.response.data.error;
        } else {
          // Если нет информации об ошибке, устанавливаем общее сообщение
          this.errorMessage = 'Ошибка входа: произошла непредвиденная ошибка';
        }
      }
    },
  },
};
</script>

  
  <style>
  .container1{
    height: 100vh;
    padding: 0 0 0 30vw;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .login-prompt {
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
  
  .login-link {
    color: #04C562;
    text-decoration: underline;
    cursor: pointer;
  }
  
  h2 {
    color: var(--cold-text-headline-100, #212326);
    font-family: "TT Norms";
    font-size: 24px;
    font-style: normal;
    font-weight: 300;
    line-height: 100%;
    margin-bottom: 25px;
    text-align: left;
  }
  
  .registration-form {
    background: #fff;
    width: 340px;
    height: 475px;
    margin: 0 auto;
    padding: 40px;
    border-radius: 5px;
    box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.10);
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .p-dropdown{
      background: #f3f5f6;
      border: none;
      transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s, outline-color 0.2s;
      border-radius: 6px;
      outline-color: transparent;
  }
  .required-field {
    color: var(--required-field-color, #F97F7F);
    font-family: Montserrat;
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }
  
  #username::placeholder {
    color: var(--cold-text-title-200, #535C69);
    font-family: "TT Norms";
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }
  
  .input-container {
    position: relative;
  }
  
  .input-container input {
    width: 260px;
    padding: 10px;
    box-sizing: border-box;
    margin-bottom: 10px;
    color: var(--cold-text-title-200, #535C69);
    font-family: "TT Norms";
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    display: flex;
    height: 36px;
    padding-right: 40px;
    align-items: center;
    align-self: stretch;
    border-radius: 3px;
    background: var(--cold-text-soft-600, #F3F5F6);
  }
  
  .input-container{
    color: #535C69;
    position: absolute;
    right: 10px;
    top: 69%;
    transform: translateY(-50%);
    cursor: pointer;
  }
  
  button {
    color: var(--ffffff, #FFF);
    background:#6266EA;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    display: flex;
    height: 34px;
    padding: 10px 14px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    border-radius: 3px;
    transition: background-color 0.3s, color 0.3s
  }

  button:hover {
    background-color: #464AD9;
    color: #FFF;
  }

  .reset {
    display: flex;
    align-items: center;
  }

  .ResetPassword{
    color: var(--cold-text-subtitle-300, #7D838C);
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    margin-left: 15px;
    text-decoration: none;
    transition: color 0.3s;
  }

  .ResetPassword:hover {
    color: #464AD9;
  }
  
  .social-icons {
    margin: 10px;
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
  
  .logo{
    justify-content: center;
    padding: 10px;
  }

  .man{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background:#6266EA;
    height: 100vh;
    width: 40%;
  }

  .man img{
    width: 15vw;
    margin: 2vw;
  }

  .man_head {
    text-align: center;
    color: #FAFAFA;
  }

  .man_header{
    color:#FAFAFA;
    font-size: 24px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
  }
  .man_subheader{
    color:#FFF;
    width: 300px;
    text-align: center;
    font-size: 14px;
    font-style: normal;
    font-weight: 300;
    line-height: normal;
    margin: 0 auto;
  }
  .man_button {
    border: 1px solid #FAFAFA;
    padding: 20px 55px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
    text-decoration: none;
    color: white;
  }

  .man_button:hover {
    background-color: #FFF;
    color: #535C69;
  }

  .man_button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px; 
  }
  </style>