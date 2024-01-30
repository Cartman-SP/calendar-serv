<template>
    <div class="login">
      <div class="container">
        <div class="header">
          <div class="subheader">SKED</div>
          <div class="subtext">Онлайн запись — легко!</div>
        </div>
        <div class="Forma">
          <div class="login-prompt">
            Уже есть аккаунт? <span class="login-link">Войти</span>
          </div>
          <div class="registration-form">
            <h2>Регистрация</h2>
            <form>
                <div class="form-group">
                    <label for="username">Почта<span class="required-field">*</span></label>
                    <input type="email" id="username" name="username" placeholder="Usermail@gmail.com" required>
                </div>
                <label for="phone">Телефон<span class="required-field">*</span></label>
                <div class="form-group" style="display: flex;">      
                    <div class="card flex justify-content-center">
                        <DropdownComponent v-model="selectedCountry" :options="countries" optionLabel="name" placeholder="🇷🇺" class="w-full md:w-14rem">
                            <template #value="slotProps">
                                <div v-if="slotProps.value" class="flex align-items-center">
                                    <div>{{ slotProps.value.name }}</div>
                                </div>
                                <span v-else>
                                    {{ slotProps.placeholder }}
                                </span>
                            </template>
                            <template #option="slotProps">
                                <div class="flex align-items-center">
                                    <div>{{ slotProps.option.name }}</div>
                                </div>
                            </template>
                        </DropdownComponent>
                    </div>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                <div class="form-group">
                  <label for="password">Пароль</label>
                  <el-input
                  v-model="input"
                  type="password"
                  placeholder="Please input password"
                  show-password
                />
                </div>
                <button type="submit">Создать аккаунт</button>
                <p class="disclaimer">
                  Используя SKED, я соглашаюсь с обработкой <br> <span class="underlined">персональных данных</span> и <span class="underlined">договором публичной оферты</span>
                </p>
                <div class="social-icons">
                  <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Google">
                  <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Twitter">
                  <img class="logo" src="../../static/img/photo_2024-01-30_18-49-14.jpg" alt="Mail.ru">
                </div>
            </form>
          </div>
        </div>
      </div>
      <InputMaskComponent id="basic" v-model="value" mask="99-999999" placeholder="99-999999" />
    </div>
  </template>
  
  <script>
    export default {
        data() {
            return {
                selectedCountry: null,
                countries: [
                    { name: '🇷🇺', code: '' },
                    { name: '🇧🇾', code: '' },
                    { name: '🇰🇿', code: '' },
                    { name: '🇺🇦', code: '' },
                ]
            };
        }
    };
  </script>
  
  <style>
  .container {
    height: 100vh;
    padding: 0 30vw;
    display: flex;
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
  
  label {
    display: block;
    margin-bottom: 5px;
    color: var(--cold-text-title-200, #535C69);
    font-family: "TT Norms";
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: left;
  }
  
  .p-dropdown{
      background: #f3f5f6;
      border: none;
      transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s, outline-color 0.2s;
      border-radius: 6px;
      outline-color: transparent;
  }

  input {
    width: 100%;
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
    padding: 8px 10px;
    justify-content: space-between;
    align-items: center;
    align-self: stretch;
    border-radius: 3px;
    background:#F3F5F6;
    border: none;
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
  
  .input-container .toggle-password {
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
  
  }
  
  .disclaimer {
    color: var(--cold-text-muted-400, #AFB6C1);
    font-family: "TT Norms";
    font-size: 10px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    margin-top: 10px;
    text-align: left;
  }
  
  .disclaimer span {
    text-decoration-line: underline;
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
  
  </style>