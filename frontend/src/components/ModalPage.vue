<template>
  <div>
    <div class="overlay"></div>
    <div class="modal-container">
      <div class="image-container">
        <img src="../../static/img/woman_modal.svg" alt="" class="woman">
      </div>

      <div class="text-container" v-if="!showContinueButtonClicked">
        <div class="days-text-container">
          <p class="days-text">Завершив регистрацию<br>мы подарим вам <span class="days-highlight">365 дней</span> бесплатного пользования</p>
        </div>
        <div class="input_container">
          <p class="normal-text">Имя</p>
          <input type="text" placeholder="Введите имя" v-model="name" :class="{ 'input-error': nameError }">
        </div>
        <div class="input_container">
          <p class="normal-text">Фотография (необязательно)</p>
          <label class="custom-file-upload" :class="{'custom-file-upload-error' : serviceCoverError}" v-if="!fileNameVariable">
            <input type="file" accept="image/*" @change="handleFileUpload($event)"/>Прикрепите фото 
          </label>
          <label style="color: #535C69;" class="custom-file-upload" :class="{'custom-file-upload-error' : serviceCoverError}" v-else>
            <input type="file" accept="image/*" @change="handleFileUpload($event)"/>{{ fileNameVariable }}
          </label>
          <p class="small-text">до 5 МБ, PNG, JPG, JPEG. Для замены - загрузите заново</p>
        </div>
        <div class="input_container">
          <div style="display: flex; align-items: center; gap: 5px;">
            <p class="normal-text">Название компании</p>
            <Tip :Tip="'Придумать текст описания'"/>
          </div>
          <input maxlength="25" type="text" v-model="companyName" placeholder="Введите название" :class="{ 'input-error': companyNameError }">
          <p class="small-text">Для ввода доступно — <span class="remaining-characters">{{ remainingCharacters }}</span>/25</p>
        </div>
        <div class="steps-container">
          <div class="continue-button-container">
            <div class="steps-progress">
              <div class="divider"></div>
              <div class="divider-two"></div>
            </div>
            <p class="steps-text">Шаг 1 из 2</p>
          </div>
          <button class="continue-button" @click="onContinueButtonClick">Продолжить</button>
        </div>
      </div>

      <div class="form" v-else>
        <div class="form-container">
          <p class="days-text">Завершив регистрацию<br>мы подарим вам <span class="days-highlight">365 дней</span><br>бесплатного пользования</p>
          <div class="dropdown-container">
            <div class="dropdown-item">
              <p class="normal-text">Часовой пояс</p>
              <SelectPage
              :options="['0 — Лондон, Дублин', '+1 — Париж, Рим', '+2 — Афины, Каир', '+3 — Москва, Стамбул', '+4 — Дубай, Новосибирск', '+5 — Астана, Ташкент', '+6 — Омск, Бишкек', '+7 — Бангкок, Джакарта', '+8 — Гонконг, Сингапур', '-8 — Лос-Анджелес, Ванкувер', '-7 — Денвер, Эдмонтон', '-6 — Чикаго, Мехико', '-5 — Нью-Йорк, Монреаль', '-4 — Галифакс, Каракас', '-3 — Рио-де-Жанейро, Буэнос-Айрес']"
              @input="option => selectedTimeZone = option"
              :placeholderdata="'Выберите свой часовой пояс'"
              :class="{ 'select-error': selectedTimeZoneError }"
              />
            </div>
    
            <div class="dropdown-item">
              <p class="normal-text">Валюта</p>
              <SelectPage
              :options="['RUB — Российский рубль', 'BYN — Белорусский рубль', 'USD — Доллар США', 'EUR — Евро', 'KZT — Казахстанский тенге', 'UAH — Украинская гривна', 'AZN — Азербайджанский манат', 'AMD — Армянский драм', 'GEL — Грузинский лари', 'KGS — Киргизский сом', 'TJS — Таджикский сомони', 'UZS — Узбекский сум', 'ARS — Аргентинское песо', 'BRL — Бразильский реал', 'AED — Дирхам ОАЭ', 'INR — Индийская рупи', 'MDL — Молдавский лей', 'NGN — Нигерийская найра', 'ILS — Новый израильский шекель', 'THB — Тайский бат', 'TRY — Турецкая лира ', 'ZAR — Южноафриканский рэнд']"
              :placeholderdata="'Выберите основную валюту'"
              @input="option => selectedCurrency = option"
              :class="{ 'select-error': selectedCurrencyError }"
              />
            </div>

          </div>
          <div class="steps">
            <div class="second-steps-container">
              <div class="steps-progress">
                <div class="second-divider"></div>
                <div class="second-divider-two"></div>
              </div>
              <p class="steps-text">Шаг 2 из 2</p>
            </div>
            <div class="btn-container">
              <button class="back" @click="onBackClick">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1.3999 6.96667L4.8999 3.5V6.3H13.2999V7.7H4.8999V10.5L1.3999 6.96667Z" fill="#535C69"/>
                </svg>
              </button>
              <button class="next-button" @click="createProfile">Продолжить</button>
            </div>
          </div>
        </div>  
      </div>
      
    </div>
    <MessageAlert :message="alertMessage" :color="alertColor"/>
  </div>
  
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import axios from 'axios';
import MessageAlert from "../components/MessageAlert.vue";
import Tip from '../components/TipComponent.vue';

export default { 
  components: { SelectPage, MessageAlert, Tip },
  data() {
    return {
      alertMessage: null,
      alertColor: '',

      fileNameVariable: '',

      companyName: '',
      showContinueButtonClicked: false,
      name: '',
      selectedTimeZone: '',
      selectedCurrency: '',
      avatar: null,

      nameError: false,
      companyNameError: false,
      selectedTimeZoneError: false,
      selectedCurrencyError: false,
    };
  },
  computed: {
    remainingCharacters() {
      const maxLength = 25;
      return maxLength - this.companyName.length;
    },
  },
  watch: {
    name() {
      this.alertMessage = null;
      this.nameError = false;
    },
    companyName() {
      this.alertMessage = null;
      this.companyNameError = false;
    },
    selectedTimeZone(){
      this.alertMessage = null;
      this.selectedTimeZoneError = false;
    },
    selectedCurrency(){
      this.alertMessage = null;
      this.selectedCurrencyError = false;
    }
  },
  methods: {
    handleFileUpload(event) {
      this.avatar = event.target.files[0];
      const file = event.target.files[0];
      this.serviceCover = file; // сохраняем весь объект файла
      const fileName = file.name; // извлекаем название файла
      if (fileName.length > 40) {
        this.fileNameVariable = fileName.slice(0, 40) + '...' + fileName.slice(-4);
      }else{
        this.fileNameVariable = fileName.slice(0, 40);
      }
    },

    createProfile(){
      console.log(this.selectedTimeZone, this.selectedCurrency)
      if (!this.selectedTimeZone.length || !this.selectedCurrency.length) {
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Пожалуйста, заполните выделенные поля';
          this.alertColor = '#F97F7F';
        }, 100);

        if (!this.selectedTimeZone.length) {
          this.selectedTimeZoneError = true;
        }else{
          this.selectedTimeZoneError = false;
        }
        if (!this.selectedCurrency.length) {
          this.selectedCurrencyError = true;
        }else{
          this.selectedCurrencyError = false;
        }
      } else{
          const formData = new FormData();
          formData.append('name', this.name);
          formData.append('company', this.companyName);
          formData.append('timezone', this.selectedTimeZone)
          formData.append('avatar', this.avatar);
          formData.append('currency', this.selectedCurrency);
          formData.append('id', this.$store.state.registrationData.user_id);
          console.log(this.$store.state.registrationData.user_id)
          axios.post('http://127.0.0.1:8000/api/profile/', formData)
            .then(response => {
              console.log('Profile created:', response.data);
              let projectId = response.data.project
              console.log(response)
              console.log('response',projectId)
              this.$store.commit('setActiveProject', projectId);
              console.log('vuex',this.$store.state.activeProjectId)
              this.alertMessage = null;
              setTimeout(() => {
                this.alertMessage = '365 дней бесплатного тариф начислены в ваш аккаунт';
                this.alertColor = '#0BB6A1';
              }, 100);
              setTimeout(() => {
                window.location.reload();
              }, 3000);
            })
            .catch(error => {
              console.error('Error creating profile:', error);
            });
        }
    },

    onContinueButtonClick() {
      if (!this.name || !this.companyName) {
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Пожалуйста, заполните выделенные поля';
          this.alertColor = '#F97F7F';
        }, 100);

        if (!this.name) {
          this.nameError = true;
        }else{
          this.nameError = false;
        }
        if (!this.companyName) {
          this.companyNameError = true;
        }else{
          this.companyNameError = false;
        }
      } else{
        if (!this.isContinueDisabled) {
          this.showContinueButtonClicked = true;
        }
      }
    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },
  },
};
</script>


  <style scoped>
  .select-error >>> .selected{
    border: solid 1px #F97F7F !important;
  }
  .overlay {
    z-index: 98;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
  }
  
  .input-error {
    border: 1px solid #F97F7F !important;
  }
  .modal-container {
      position: absolute;
      z-index: 99;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      gap: 40px;
      align-items: center;
      width: 932px;
      height: 560px;
      background-color: #FAFAFA;
      border-radius: 25px;
      box-shadow: 0px 0px 15px 0px rgba(0, 0, 0, 0.10);
    }
    
    .image-container{
      width: 381px;
    }

    .text-container {
      width: 437px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 20px;
      box-sizing: border-box;
    }
    
    .days-text {
      color: #535C69;
      font-family: TT Norms Medium;
      font-size: 36px;
      font-weight: 500;
      line-height: 43px;
      letter-spacing: 0em;
      text-align: left;
    }
    
    .days-highlight {
      color: #6266EA;
      font-family: TT Norms Medium;
      font-size: 32px;
      font-style: normal;
      line-height: 120%;
    }
    
    .normal-text {
      color:#535C69;
      font-family: TT Norms Medium;
      font-size: 13px;
      font-style: normal;
      line-height: normal;
      text-align: left;
    }
    
    .small-text {
      color:#D2D8DE;
      font-family: TT Norms Medium;
      font-size: 12px;
      font-weight: 500;
      line-height: 14px;
      letter-spacing: 0em;
      text-align: left;
    }
    .small-text .remaining-characters {
      color: #6266EA;
    }
    .divider {
      border-bottom: 3px solid #6266EA; 
      width: 80px;
      border-radius: 100px;
    }
    .divider-two {
      border-bottom: 3px solid #D8DDE3;
      width: 50px;
      border-radius: 100px;
      margin: 10px 0;
    }
    .steps-progress{
      display: flex;
      gap: 10px;
    }
    .steps-text{
      text-align: left;
      font-family: TT Norms Medium;
      font-size: 10px;
      font-weight: 300;
      line-height: 10px;
      letter-spacing: 0em;
      color: #535C69;
      margin-bottom: 0;
    }
    input{
      color: #535C69;
      font-family: TT Norms Medium;
      font-size: 14px;
      font-weight: 500;
      line-height: 17px;
      letter-spacing: 0em;
      border: none;
    }
    input::placeholder {
      font-family: TT Norms Medium;
      font-size: 14px;
      font-weight: 500;
      line-height: 17px;
      letter-spacing: 0em;
      color: #D2D8DE;
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
      background-image: url(../../static/img/paperclip.svg);
      background-repeat: no-repeat;
      background-position: calc(100% - 15px) center;
    }
  
    .custom-file-upload input[type="file"] {
      display: none;
    }
    .form-container {
      width: 437px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 20px;
      box-sizing: border-box;
    }
    .form {
      width: 437px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 20px;
      box-sizing: border-box;
    }
    .second-divider {
      border-bottom: 3px solid #6266EA; 
      width: 122px;
      border-radius: 100px;
    }
    .second-divider-two {
      border-bottom: 3px solid #D8DDE3;
      width: 10px;
      border-radius: 100px;
    }
    .back{
      padding: 10px, 14px, 10px, 14px;
      border-radius: 3px;
      border: 1px solid #DDE1E5;
      gap: 5px;
      color: #535C69;
      background-color: #FFFFFF;
    }
    .btn-container{
      display: flex;
      gap: 10px;
    }
    .continue-button-container {
      display: flex;
      flex-direction: column;
    }
    .continue-button{
      background: #EFEFFF;
      color: #6266EA;
      transition: all 0.2s ease;
    }
    .continue-button:hover{
      background: #6266EA;
      color: #FFFFFF;
    }
    .steps-container{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .steps{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .dropdown-item{
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
      gap: 5px;
    }
    .input_container{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    input:focus {
      outline: none;
    }
    
    .custom-file-upload input[type="file"]:focus {
      outline: none;
    }
    select {
      padding: 8px 10px;
      font-family: TT Norms;
      font-size: 14px;
      line-height: 20px;
      color: #D2D8DE;
      border: none;
      background-color: #F3F5F6;
      margin-bottom: 10px;
      border-radius: 3px;
      height: 36px;
    }
    
    select option {
      font-family: TT Norms;
      font-size: 14px;
      line-height: 20px;
      color: #535C69;

    } 
    .selected {
      color: #535C69;
      font-family: TT Norms;
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: left;
    }
    select:active, select:focus{
      outline:none
    }
    p{
      margin: 0;
    }
    input{
      margin: 0;
      width: 100%;
    }
    .second-steps-container{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .image-container{
        display: block;
      }
    @media (max-width: 991px){
      .image-container{
        display: none;
      }
      .text-container{
        width: 100%;
      }
      .form-container{
        width: 100%;
      }
      .modal-container{
        width: 600px;
        padding: 60px;
      }
    }
    @media (max-width: 768px){
      .modal-container{
        padding: 30px;
        max-width: 390px;
        height: auto;
      }
      input{
        width: 100%;
      }
      .days-text{
        text-align: center;
        font-size: 20px;
        line-height: 20px;
        margin: 0;
      }
      .days-highlight{
        font-size: 20px;
        line-height: 20px;
      }
      .custom-file-upload{
        width: 100%;
      }
      .text-container{
        padding: 0;
      }
  }
  @media (max-width: 576px){
    .steps-container{
      flex-direction: column;
      gap: 10px;
    }
    .steps{
      flex-direction: column;
      gap: 10px;
    }
  }
  </style>