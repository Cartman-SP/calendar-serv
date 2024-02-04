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
        <input type="file" accept="image/*"/>Прикрепите фото
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
            <select v-model="timeZone" class="dropdown">
              <option value="GPT+3">GPT +3</option>
              <option value="GPT+4">GPT +4</option>
            </select>
          </div>
  
          <div class="dropdown-item">
            <p class="normal-text">Валюта</p>
            <select v-model="currency" class="dropdown">
              <option value="tenge">Тенге</option>
              <option value="rubles">Рубли</option>
            </select>
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
            <button class="next-button">Продолжить</button>
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
      showModal: false,
      companyName: '',
      showContinueButtonClicked: false,
      timeZone: 'GPT+3',
      currency: 'tenge',
      name: '',
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
    onContinueButtonClick() {
      if (!this.isContinueDisabled) {
        this.showContinueButtonClicked = true;
      }
    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },
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
      font-family: "TT Norms";
      font-size: 32px;
      font-style: normal;
      font-weight: bold;
      line-height: 120%;
      text-align: left;
    }
    
    .days-highlight {
      color: #6266EA;
      font-family: "TT Norms";
      font-size: 32px;
      font-style: normal;
      font-weight: bold;
      line-height: 120%;
    }
    
    .normal-text {
      color:#535C69;
      font-family: "TT Norms";
      font-size: 13px;
      font-style: normal;
      font-weight: bold;
      line-height: normal;
      text-align: left;
    }
    
    .small-text {
      color:#D2D8DE;
      font-family: "TT Norms";
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
      font-family: "TT Norms";
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
      margin-left: auto;
    }
    .continue-button-container {
      display: flex;
      flex-direction: column;
    }
    .steps-container{
      display: flex;
    }
    .continue-button{
      margin-left: auto;
    }
    .steps{
      display: flex;
    }
    .dropdown-item{
      margin-bottom: 20px;
    }
    input:focus {
      outline: none;
    }
    
    .custom-file-upload input[type="file"]:focus {
      outline: none;
    }
  </style>