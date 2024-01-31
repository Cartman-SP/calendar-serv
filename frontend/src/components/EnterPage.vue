<template>
  <div class="login">
    <div class="container">
      <div class="Forma">
        <div class="login-prompt">
          Нет аккаунта? <a href="#/register" class="login-link" style="text-decoration:none">Зарегистрироваться</a>
        </div>
        <div class="registration-form">
          <h2>Вход</h2>
          <form>
            <div class="form-group">
              <label for="username">Почта или телефон</label>
              <input type="email" id="username" name="username" placeholder="Usermail@gmail.com" required>
            </div>
            <div class="form-group">
              <label for="password">Пароль</label>
              <div class="card flex justify-content-center">
                <PasswordComponent v-model="passwordValue" toggleMask />
              </div>
            </div>
            <div class="reset">
              <a href="#/main" style="text-decoration:none"><button type="submit">Войти</button></a>
              <a class="ResetPassword" href="#/reset"> Восстановить пароль </a>
            </div>
            <div class="social-icons">
              <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Google">
              <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Twitter">
              <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Mail.ru">
            </div>
          </form>
        </div>
      </div>
      <div class="man">
        <img src="../../static/img/Man.png" alt="">
        <div class="man_head">
          <div class="man_header">Здравствуйте!</div>
          <div class="man_subheader">Зарегистрируйтесь или войдите, чтобы <br>получить полный доступ к безграничному <br> функционалу Calendar</div>
          <div class="man_button-container">
            <a href="#/register" style="text-decoration:none">
              <button class="man_button">Регистрация</button>
          </a>
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
  
  <style>
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
  
  .input-containe{
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
    background:#6266EA;
    height: 100%;
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