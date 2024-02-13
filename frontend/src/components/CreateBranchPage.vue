<template>
  
  <div class="main">
    <div class="transition">
      <router-link to="/lk/branch" class="employesss-link">Филиалы</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Создание филиала</p>
    </div>
    <div class="create_branch">
      <!-- Форма создания филиала -->
      <form class="branch-form" v-if="!showContinueButtonClicked">
        <div class="one-group">
          <div class="form-group">
            <label for="country">Страна</label>
            <select id="country">
              <option value="" disabled selected style="display:none;">Выберите страну</option>
              <option value="Russia">Россия</option>
              <option value="Kazakhstan">Казахстан</option>
              <option value="Belarus">Беларусь</option>
              <option value="Ukraine">Украина</option>
            </select>
          </div>

          <div class="form-group">
            <label for="city">Город</label>
            <select id="city">
              <option value="" disabled selected style="display:none;">Выберите город</option>
              <option value="SaintPetersburg">Санкт-Петербург</option>
              <option value="Moscow">Москва</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label for="address">Адрес</label>
          <input type="text" id="address" placeholder="Введите точный адрес">
        </div>

        <div class="form-group">
          <label for="branchName">Название филиала</label>
          <input type="text" id="branchName" placeholder="Введите название" maxlength="25">
          <p class="character-limit">Название должно содержать не более 25 знаков</p>
        </div>

        <div class="form-group">
          <label for="branchPhoto">Фото филиала</label>
          <label class="custom-file-upload">
            <input type="file" accept="image/*" multiple/>Загрузите несколько фотографий
          </label>
          <p class="photo-info">до 5 МБ, PNG, JPG, JPEG. Для замены удалите миниатюру и загрузите заново</p>
        </div>

        <div class="form-group">
          <label>График работы</label>
          <div class="schedule-buttons">
            <button :class="{ 'active': isWeeklyActive }" @click="weeklySchedule">Недельный график</button>
            <button :class="{ 'active': isShiftActive }" @click="shiftSchedule">Сменный график</button>
          </div>
        </div>
        <div class="form-btn">
          <div class="continue-button-container">
            <div class="steps-progress">
              <div class="divider"></div>
              <div class="divider-two"></div>
            </div>
            <p class="steps-text">Шаг 1 из 2</p>
          </div>
          <button class="btn" @click="onContinueButtonClick" :disabled="isContinueDisabled">Продолжить</button>
        </div>
      </form>
      <div v-else>
        <div class="form-container">
          <div class="one-group">
            <div class="form-group">
              <label for="country">Рабочие часы</label>
              <select id="country">
                <option value="" disabled selected style="display:none;">Выберите время</option>
                <option value="Russia">Россия</option>
                <option value="Kazakhstan">Казахстан</option>
                <option value="Belarus">Беларусь</option>
                <option value="Ukraine">Украина</option>
              </select>
            </div>
  
            <div class="form-group">
              <label for="city">Перерыв</label>
              <select id="city">
                <option value="" disabled selected style="display:none;">Выберите время</option>
                <option value="SaintPetersburg">Санкт-Петербург</option>
                <option value="Moscow">Москва</option>
              </select>
            </div>
          </div>
          <label>Выберите тип бизнеса</label>
          <div class="dropdown-container">
            <label for="service">Сфера бизнеса</label>
            <select id="service">
              <option value="" disabled selected style="display:none;">Выберете сферу бизнеса</option>
              <option>Салон красоты</option>
              <option>Барбершоп</option>
              <option>Маникюрный салон</option>
              <option>Парикмахерская</option>
              <option>Брови и ресницы</option>
              <option>Тату салон</option>
              <option>Другое</option>
            </select>
          </div>
          <div class="dropdown-container">
            <label for="service">Выберете сотрудников для этого филиала</label>
            <select id="service">
              <option value="" disabled selected style="display:none;">Выберете сотрудников</option>
            </select>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      isWeeklyActive: false,
      isShiftActive: false
    }
  },
  methods: {
    weeklySchedule() {
      this.isWeeklyActive = true;
      this.isShiftActive = false;
    },
    shiftSchedule() {
      this.isShiftActive = true;
      this.isWeeklyActive = false;
    },
    onContinueButtonClick() {
      if (!this.isContinueDisabled) {
        this.showContinueButtonClicked = true;
      }
    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },
  }
}
</script>

<style scoped>
  .create_branch {
    position: absolute;
    width: 488px;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  input {
    padding: 8px 10px;
    font-family: TT Norms;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
    height: 36px;
  }

  select{
    border-radius: 3px;
  }

  p {
    font-family: TT Norms;
    font-size: 12px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    color: #D2D8DE;
    margin: 0;
  }

  .schedule-buttons {
    display: flex;
    gap: 10px;
    
  }

  .schedule-buttons button {
    background-color: #F3F5F6;
    color: #D2D8DE;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }

  .schedule-buttons button:hover {
    background-color: #6266EA;
    color: #EFEFFF;
  }

  .schedule-buttons button.active {
    background-color: #6266EA;
    color: #EFEFFF;
  }

  .one-group {
    display: flex;
    flex-direction: row;
    gap: 10px;
  }

  .form-btn {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }

  .btn {
    background-color: #EFEFFF;
    color: #6266EA;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }

  .btn:hover {
    background-color: #6266EA;
    color: #EFEFFF;
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
    width: 100%;
    height: 36px;
    display: flex;
    padding: 8px 10px;
    cursor: pointer;
    background-color: #F3F5F6;
    color: #D2D8DE;
    align-items: center;
    font-weight: 500;
  }
  
  .custom-file-upload input[type="file"] {
    display: none;
  }
  label{
    font-weight: bold;
  }
  .photo-info{
    color: #AFB6C1;
    font-size: 10px;
    font-weight: 500;
    line-height: 10px;
    letter-spacing: 0em;
  }
  .transition {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  .employesss-link {
    font-family: TT Norms;
    font-size: 20px;
    font-weight: bold;
    line-height: 24px;
    text-align: left;
    text-decoration: none;
    color: #AFB6C1;
  }
  
  .creation_text {
    color: #535C69;
    font-family: TT Norms;
    font-size: 20px;
    font-weight: bold;
    line-height: 24px;
    letter-spacing: 0em;
    text-align: left;
    margin: 0;
  }
  
  .arrow-container {
    display: flex;
    align-items: center;
  }
  
  .arrow-icon {
    height: 50%;
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
    margin-top: 10px;
  }
  .continue-button-container {
    display: flex;
    flex-direction: column;
  }
  .form-btn{
    display: flex;
    justify-content: space-between;
    align-items: center;
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
  .steps{
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .form-container {
    width: 100%;
    box-sizing: border-box;
  }
  select {
    padding: 10px;
    font-family: TT Norms;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
    border-radius: 3px;
  }
  
  select option {
    font-family: TT Norms;
    font-size: 16px;
    font-weight: bold;
    line-height: 20px;
    color: #535C69;
  }
  select#service {
    width: 100%;
    padding: 10px;
    font-family: TT Norms;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
  }
</style>
