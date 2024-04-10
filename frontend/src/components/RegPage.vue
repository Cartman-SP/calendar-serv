<template>
  <div class="reg">
    <div class="container2">
      <div class="header">
        <div class="subheader1">SKED</div>
        <div class="subtext">Онлайн запись — легко!</div>
      </div>
      <div class="Forma1">
        <div class="login-prompt">
          Уже есть аккаунт? <router-link class="login-link" :to="'/login'" style="text-decoration:none">Войти</router-link>
        </div>
        <div class="registration-form1" :class="{'modal-show' : isModalVisible, 'modal-hide' : !isModalVisible}">
          <div class="registers">
            <h2>Регистрация</h2>
          </div>
          <form @submit.prevent="registerUser">
            <div class="form-group">
              <label for="username">Почта<span class="required-field">*</span></label>
              <input v-model="email" autocomplete="new-password" type="email" id="username" name="username" placeholder="Usermail@gmail.com" required>
            </div>
            <label for="phone">Телефон<span class="required-field">*</span></label>
            <div class="form-group-phone" style="display: flex;">      
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
              <InputMaskComponent autocomplete="new-password" @input="handleInput" id="basic" v-model="value" :mask="computedMask" :placeholder="computedPlaceholder" />
            </div>
            <div class="form-group">
              <label for="password">Пароль</label>
              <div class="card flex justify-content-center">
                <PasswordComponent autocomplete="new-password" v-model="passwordValue" toggleMask />
              </div>
              <div id="error" v-if="PasswordError">Введите более 6 знаков, включая цифры и латинские буквы</div>
            </div>
            <button type="submit">Создать аккаунт</button>
            <div id="error"> {{ error }} </div>
            <p class="disclaimer">
              Используя SKED, я соглашаюсь с обработкой <br> <span class="underlined">персональных данных</span> и <span class="underlined">договором публичной оферты</span>
            </p>
            <div class="social-icons">
              <div class="google">
                <img class="logo_auth" src="../../static/img/google.svg" alt="Google">
                <p class="google_text">Войти с помощью Google</p>
              </div>
              <div class="yandex">
                <img class="logo_auth" src="../../static/img/yandex.svg" alt="Twitter">
              </div>
              <div class="mailru">
                <img class="logo_auth" src="../../static/img/mail.svg" alt="Mail.ru">
              </div>
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
      selectedCountry: null,
      value: '7 ', // Начальное значение для InputMaskComponent
      passwordValue: '', // Поле пароля
      countries: [
        { name: '🇷🇺', code: '+7' },
        { name: '🇧🇾', code: '+375' },
        { name: '🇰🇿', code: '+7' },
        { name: '🇺🇦', code: '+380' },
      ],
      email: '',
      error: '',
      PasswordError: false,

      isModalVisible: false,
    };
  },
  computed: {
    computedMask() {
      if (this.selectedCountry) {
        const countryCode = this.selectedCountry.code;
        if (countryCode === '+375' || countryCode === '+380') {
          return `${countryCode} (99) 999-99-99`;
        } else {
          return `${countryCode} (999) 999-99-99`;
        }
      } else {
        return '+7 (999) 999-99-99'; // Default mask
      }
    },
    computedPlaceholder() {
      return this.selectedCountry ? this.selectedCountry.code + ' |' : '+7 |';
    },
  },
  watch: {
    selectedCountry(newCountry) {
      if (newCountry) {
        this.value = newCountry.code + ' ' + this.value.replace(/^\s*\+\d\s*\|\s*/, '');
      }
    },
    passwordValue(){
      this.PasswordError = false;
    }
  },
  mounted(){
    this.opacityAnimation()
  },
  methods: {
    opacityAnimation(){
      this.isModalVisible = false;
      setTimeout(() => {
        this.isModalVisible = true;
      }, 200);
    },

    handleInput() {
      const countryCode = this.selectedCountry ? this.selectedCountry.code : '';
      this.value = countryCode + ' ' + this.value.replace(/^\s*\+\d\s*\|\s*/, '');
    },

    async registerUser() {
      if (this.passwordValue.length < 6) {
          this.PasswordError = true;
        }else{
          try {
            const response = await axios.post('http://127.0.0.1:8000/api/reg/', {
              password: this.passwordValue,
              phone: this.value,
              email: this.email
            });
            this.$store.dispatch('saveRegistrationData', response.data);
            this.$router.push('/dashboard');
          } catch (error) {
            console.error('Ошибка регистрации', error.response);

            if (error.response.data && typeof error.response.data === 'object') {
              console.error('Детали ошибки:', JSON.stringify(error.response.data, null, 2));
              // Устанавливаем значение свойства error для отображения в div
              this.error = error.response.data.error;
            } else {
              console.error('Детали ошибки:', error.response.data);
              // Устанавливаем значение свойства error для отображения в div
              this.error = error.response.data;
            }
          }
        }
    },
  },
};
</script>

  
  <style>
  .modal-show{
    opacity: 1;
    transform: translateX(0);
    transition: all .8s ease;
  }

  .modal-hide{
    transform: translateX(-20px);
    opacity: 0;
    transition: all .8s ease;
  }

  .p-password{
    display: block;
  }

  .container2 {
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
  
  .subheader1 {
    text-align: left;
    color: #FFF;
    font-family: TT Norms Medium;
    font-size: 64px;
    font-style: normal;
    line-height: normal;
  }
  
  .subtext {
    color: #FFF;
    font-family: TT Norms Medium;
    font-size: 28px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
  }
  
  
  .Forma1 {
    display: flex;
    flex-direction: column;
  }
  
  .login-prompt {
    padding: 0 80px 0 0;
    text-align: left;
    width: 340px;
    color: var(--cold-text-ghost-500, #DDE1E5);
    font-family: TT Norms Medium;
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
    font-family: TT Norms Medium;
    font-size: 24px;
    font-style: normal;
    font-weight: 300;
    line-height: 100%;
    text-align: left;
    margin: 0;
  }
  
  .registration-form1 {
    background: #fff;
    width: 340px;
    height: auto;
    margin: 0 auto;
    padding: 40px;
    border-radius: 5px;
    box-shadow: 0px 4px 20px 0px rgba(0, 0, 0, 0.10);
    display: flex;
    flex-direction: column;
    gap: 25px;
  }
  
  .form-group-phone{
    display: flex;
    gap: 5px;
  }
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    color: #535C69;
    font-family: TT Norms Medium;
    font-size: 13px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: left;
  }
  
  .p-dropdown{
      background: #f3f5f6;
      border: none;
      transition: background-color 0.3s, color 0.3s, border-color 0.3s, box-shadow 0.3s, outline-color 0.3s;
      border-radius: 6px;
      outline-color: transparent;
  }

  input {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    margin-bottom: 10px;
    color: #535C69;
    font-family: TT Norms Medium;
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
    font-family: TT Norms Medium;
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
    color:#AFB6C1;
    font-family: TT Norms Medium;
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
  
  /* button {
    color: var(--ffffff, #FFF);
    background:#6266EA;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    display: flex;
    height: 36px;
    padding: 10px 14px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    border-radius: 3px;
  } */
  
  .disclaimer {
    color: var(--cold-text-muted-400, #AFB6C1);
    font-family: TT Norms Medium;
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
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    margin: 0;
  }
  .google{
    display: flex;
    align-items: center;
    gap: 5px;
    border: 1px solid #DDE1E5;
    border-radius: 5px;
    height: 34px;
    padding: 10px;
    cursor:pointer;
  }
  .google:hover{
    border: 1px solid #535C69;
    transition: all ease 0.35s
  }
  .google_text{
    font-family: TT Norms Medium;
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    margin: 0;
  }
  .logo_auth{
    width: 20px;
    height: 20px;
    padding: 0;
  }
  .mailru{
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #DDE1E5;
    border-radius: 5px;
    height: 34px;
    width: 34px;
    cursor:pointer;
  }
  .mailru:hover{
    margin: 0;
    border: 1px solid #535C69;
    transition: all ease 0.35s
  }
  .yandex{
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #DDE1E5;
    border-radius: 5px;
    height: 34px;
    width: 34px;
    cursor:pointer;
  }
  .yandex:hover{
    border: 1px solid #535C69;
    transition: all ease 0.35s
  }
  input#username::placeholder {
    font-family: 'TT Norms Medium';
    font-size: 13px;
    line-height: 17px;
    letter-spacing: 0em;
    color: #D2D8DE;
  }
  @media (max-width: 1641px){
    .container2{
      padding: 0 20vw;
    }
  }
  @media (max-width: 1280px){
    .container2{
      padding: 0 10vw;
    }
  }
  @media (max-width: 991px){
    .container2{
      padding: 0 10vw;
      flex-direction: column;
      height: 100vh;
      gap: 30px;
      align-items: center;
      justify-content: center;
    }
    .Forma1{
      width: 100%;
    }
    .registration-form1{
      width: 100%;
    }
    .subheader1{
      text-align: center;
      font-size: 32px;
    }
  }
  </style>