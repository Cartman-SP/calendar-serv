<template>
  <div class="modal-container">
    <div class="image-container">
      <img src="../../static/img/woman.png" alt="" class="woman">
    </div>

    <div class="text-container" v-if="!showContinueButtonClicked">
      <p class="days-text">Завершив регистрацию<br>мы подарим вам <span class="days-highlight">365 дней</span><br>бесплатного пользования</p>
      <p class="normal-text">Имя</p>
      <input type="text" placeholder="Введите имя" v-model="name">
      <p class="normal-text">Фотография (необязательно)</p>
      <label class="custom-file-upload">
        <input type="file" accept="image/*" @change="onFileChange"/>Прикрепите фото
      </label>
      <p class="small-text">до 5 МБ, PNG, JPG, JPEG. Для замены - загрузите заново</p>
      <p class="normal-text">Название компании</p>
      <input maxlength="25" type="text" v-model="companyName" placeholder="Введите название">
      <p class="small-text">Для ввода доступно — <span class="remaining-characters">{{ remainingCharacters }}</span>/25</p>
      <div class="steps-container">
        <div class="continue-button-container">
          <div class="steps-progress">
            <div class="divider"></div>
            <div class="divider-two"></div>
          </div>
          <p class="steps-text">Шаг 1 из 2</p>
        </div>
        <button class="continue-button" @click="onContinueButtonClick" :disabled="isContinueDisabled">Продолжить</button>
      </div>
    </div>

    <div v-else>
      <div class="form-container">
        <p class="days-text">Завершив регистрацию<br>мы подарим вам <span class="days-highlight">365 дней</span><br>бесплатного пользования</p>
        <div class="dropdown-container">
          <div class="dropdown-item">
            <p class="normal-text">Часовой пояс</p>
            <SelectPage
            :options="['0 — Лондон, Дублин', '+1 — Париж, Рим', '+2 — Афины, Каир', '+3 — Москва, Стамбул', '+4 — Дубай, Новосибирск', '+5 — Астана, Ташкент', '+6 — Омск, Бишкек', '+7 — Бангкок, Джакарта', '+8 — Гонконг, Сингапур', '-8 — Лос-Анджелес, Ванкувер', '-7 — Денвер, Эдмонтон', '-6 — Чикаго, Мехико', '-5 — Нью-Йорк, Монреаль', '-4 — Галифакс, Каракас', '-3 — Рио-де-Жанейро, Буэнос-Айрес']"
            @input="option => selectedTimeZone = option"
            :placeholderdata="'Выберите свой часовой пояс'"
            class="select"
            />
          </div>
  
          <div class="dropdown-item">
            <p class="normal-text">Валюта</p>
            <SelectPage
            :options="['RUB — Российский рубль', 'BYN — Белорусский рубль', 'USD — Доллар США', 'EUR — Евро', 'KZT — Казахстанский тенге', 'UAH — Украинская гривна', 'AZN — Азербайджанский манат', 'AMD — Армянский драм', 'GEL — Грузинский лари', 'KGS — Киргизский сом', 'TJS — Таджикский сомони', 'UZS — Узбекский сум', 'ARS — Аргентинское песо', 'BRL — Бразильский реал', 'AED — Дирхам ОАЭ', 'INR — Индийская рупи', 'MDL — Молдавский лей', 'NGN — Нигерийская найра', 'ILS — Новый израильский шекель', 'THB — Тайский бат', 'TRY — Турецкая лира ', 'ZAR — Южноафриканский рэнд']"
            :placeholderdata="'Выберите основную валюту'"
            @input="option => selectedCurrency = option"
            class="select"
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
            <button class="back" @click="onBackClick">Назад</button>
            <button class="next-button" @click="createProfile">Продолжить</button>
          </div>
        </div>
      </div>  
    </div>
  </div>
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import axios from 'axios';

export default { 
  components: { SelectPage },
  data() {
    return {
      companyName: '',
      showContinueButtonClicked: false,
      name: '',
      selectedTimeZone: '',
      selectedCurrency: '',
      avatar: null,
    };
  },
  computed: {
    remainingCharacters() {
      const maxLength = 25;
      return maxLength - this.companyName.length;
    },
    isContinueDisabled() {
      return !this.companyName.trim() || !this.name.trim();
    },
  },
  methods: {
    createProfile(){
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
          console.log('Service created:', response.data);
          window.location.reload();
        })
        .catch(error => {
          console.error('Error creating service:', error);
        });
    },

    onContinueButtonClick() {
      if (!this.isContinueDisabled) {
        this.showContinueButtonClicked = true;
      }
    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },
    onSelectChange(type) {
      // Обрабатываем изменения в выбранных опциях
      // И применяем стиль к тексту в зависимости от типа элемента select
      if (type === 'timeZone') {
        // Для часового пояса
        // Можно выполнить другие действия, если необходимо
      } else if (type === 'currency') {
        // Для валюты
        // Можно выполнить другие действия, если необходимо
      }
    },
    onFileChange(event) {
      this.avatar = event.target.files[0];
    }
  },
};
</script>


  <style scoped>
  .modal-container {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      align-items: center;
      width: 932px;
      height: 560px;
      background-color: #FAFAFA;
      border-radius: 25px;
      box-shadow: 0px 0px 15px 0px rgba(0, 0, 0, 0.10);
    }
    
    .image-container,
    .text-container {
      width: 50%;
      box-sizing: border-box;
      padding: 20px;
    }
    
    .days-text {
      color: #535C69;
      font-family: TT Norms Medium;
      font-size: 32px;
      font-style: normal;
      line-height: 120%;
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
      font-size: 14px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
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
      font-family: TT Norms;
      font-size: 10px;
      font-weight: 300;
      line-height: 10px;
      letter-spacing: 0em;
      color: #535C69;
      margin-bottom: 0;
    }
    input{
      width: 340px;
      color: #535C69;
      font-family: TT Norms;
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
      width: 340px;
      height: 36px;
      display: flex;
      padding: 8px 10px;
      cursor: pointer;
      background-color: #F3F5F6;
      color: #D2D8DE;
      align-items: center;
    }
  
    .custom-file-upload input[type="file"] {
      display: none;
    }
    .form-container {
      width: 100%;
      box-sizing: border-box;
      padding: 20px;
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
    
  </style>