<template>
  <div class="main">
    <div class="transition">
      <router-link to="/lk/personal" class="employesss-link">Сотрудники</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Создание сотрудника</p>
    </div>
    <div class="create_employess">
      <!-- Form Elements -->
      <div class="form-container">
        <div class="form-row">
          <div class="form-column">
            <label for="firstName">Имя</label>
            <input type="text" id="firstName" placeholder="Введите имя">
          </div>
          <div class="form-column">
            <label for="lastName">Фамилия</label>
            <input type="text" id="lastName" placeholder="Введите фамилию">
          </div>
        </div>

        <div class="form-row">
          <div class="form-column">
            <label for="position">Должность</label>
            <input type="text" id="position" placeholder="Введите должность">
          </div>
          <div class="form-column">
            <label for="photo">Фото</label>
            <label class="custom-file-upload">
              <input type="file" accept="image/*"/>Прикрепите фото
            </label>
          </div>
        </div>
        
        <div class="dropdown-container">
          <label for="service">Услуга</label>
          <select id="service">
            <option value="" disabled selected style="display:none;">Выберете услугу</option>
            <option>Стрижка</option>
            <option>Стрижка + борода</option>
            <option>Укладка волос</option>
            <option>Чистка лица</option>
            <option>Окантовка</option>
            <option>Отец + сын</option>
          </select>
        </div>

        <div class="form-row">
          <div class="dropdown-container">
            <label>График работы</label>
            <div class="days-buttons">
              <button :class="{ 'form-btn-active': isDaySelected('Пн'), 'form-btn': !isDaySelected('Пн') }" @click="toggleDay('Пн')">Пн</button>
              <button :class="{ 'form-btn-active': isDaySelected('Вт'), 'form-btn': !isDaySelected('Вт') }" @click="toggleDay('Вт')">Вт</button>
              <button :class="{ 'form-btn-active': isDaySelected('Ср'), 'form-btn': !isDaySelected('Ср') }" @click="toggleDay('Ср')">Ср</button>
              <button :class="{ 'form-btn-active': isDaySelected('Чт'), 'form-btn': !isDaySelected('Чт') }" @click="toggleDay('Чт')">Чт</button>
              <button :class="{ 'form-btn-active': isDaySelected('Пт'), 'form-btn': !isDaySelected('Пт') }" @click="toggleDay('Пт')">Пт</button>
              <button :class="{ 'form-btn-active': isDaySelected('Сб'), 'form-btn': !isDaySelected('Сб') }" @click="toggleDay('Сб')">Сб</button>
              <button :class="{ 'form-btn-active': isDaySelected('Вс'), 'form-btn': !isDaySelected('Вс') }" @click="toggleDay('Вс')">Вс</button>
            </div>
            <div class="grafic">
              <p class="grafic_text">Сменный график:</p>
              <button :class="{ 'grafic-btn-active': selectedSchedule === '1x1', 'grafic-btn': selectedSchedule !== '1x1' }" @click="selectedSchedule = '1x1'; toggleAllDays()">1x1</button>
              <div class="dot"></div>
              <button :class="{ 'grafic-btn-active': selectedSchedule === '2x2', 'grafic-btn': selectedSchedule !== '2x2' }" @click="selectedSchedule = '2x2'; toggleAllDays()">2x2</button>
              <div class="dot"></div>
              <button :class="{ 'grafic-btn-active': selectedSchedule === '3x3', 'grafic-btn': selectedSchedule !== '3x3' }" @click="selectedSchedule = '3x3'; toggleAllDays()">3x3</button>
              <div class="dot"></div>
              <button :class="{ 'grafic-btn-active': selectedSchedule === '5x2', 'grafic-btn': selectedSchedule !== '5x2' }" @click="selectedSchedule = '5x2'; toggleAllDays()">5x2</button>
            </div>
          </div>
        </div>

        <div class="form-row">
          <div class="dropdown-container">
            <label for="workingHours">Рабочие часы</label>
            <div class="dropdown-container">
              <select id="workingHours">
                <option value="" disabled selected style="display:none;">Время работы</option>
                <option>9:00 - 19:00</option>
                <option>9:00 - 20:00</option>
                <option>9:00 - 21:00</option>
                <option>10:00 - 18:00</option>
                <option>10:00 - 19:00</option>
                <option>10:00 - 20:00</option>
                <option>10:00 - 22:00</option>
              </select>
            </div>
          </div>
          <div class="dropdown-container">
            <label for="break">Перерыв</label>
            <div class="dropdown-container">
              <select id="break">
                <option value="" disabled selected style="display:none;">Время перерыва</option>
                <option>13:00-14:00</option>
                <option>14:00-15:00</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- Buttons -->
      <div class="button-container">
        <button @click="saveAndExit" class="save-and-exit-button">Сохранить и выйти</button>
        <button @click="cancel" class="cancel-button">Отмена</button>
      </div>
    </div>
  </div>
</template>


  
<script>
export default {
  data() {
    return {
      selectedDays: [],
      selectedRecordType: 'individual',
      selectedPaymentFormat: 'sessionPayment',
      uploadedFile: null,
      groupCapacity: 0,
      maxGroupCapacity: 0,
      selectedSchedule: null, // Новое свойство для хранения выбранного графика работы
    };
  },
  methods: {
    isDaySelected(day) {
      return this.selectedDays.includes(day);
    },
    toggleDay(day) {
      if (this.selectedSchedule && this.selectedDays.length > 0) {
        // Сбрасываем выбранные дни и график, если график был выбран
        this.selectedDays = [];
        this.selectedSchedule = null;
      }

      if (!this.selectedDays.includes(day)) {
        this.selectedDays.push(day);
      } else {
        this.selectedDays = this.selectedDays.filter(selectedDay => selectedDay !== day);
      }
    },
    toggleAllDays() {
      if (this.selectedSchedule === '1x1') {
        this.selectedDays = ['Пн', 'Ср', 'Пт', 'Вс'];
      } else if (this.selectedSchedule === '2x2') {
        this.selectedDays = ['Пн', 'Вт', 'Пт', 'Сб'];
      } else if (this.selectedSchedule === '3x3') {
        this.selectedDays = ['Пн', 'Вт', 'Ср', 'Вс'];
      } else if (this.selectedSchedule === '5x2') {
        this.selectedDays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'];
      }
    },
    saveAndExit() {
      // Ваша текущая логика сохранения и выхода
    },
    cancel() {
      // Ваша текущая логика отмены
    },
  }
}
</script>
  
  <style scoped>
  .form-row {
    display: flex;
    gap: 10px;
  }

  .days-buttons {
    display: flex;
    gap: 10px;
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
  .form-container{
    display: flex;
    flex-direction: column;
    gap: 20px;
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
  .create_employess {
    width: 80%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
  }
  .form-column{
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: 100%;
  }

  .dropdown-container{
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .button-container {
    display: flex;
    gap: 10px;
    justify-content: flex-end;
    margin-top: 20px;
  }

  .save-and-exit-button {
    background-color: #EFEFFF;
    color: #6266EA;
    transition: background-color 0.3s, color 0.3s;
  }

  .save-and-exit-button:hover {
    background-color: #464AD9;
    color: #EFEFFF;
  }

  .cancel-button {
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1px solid #DDE1E5;
  }
  .custom-file-upload {
    height: 36px;
    display: flex;
    padding: 8px 10px;
    cursor: pointer;
    background-color: #F3F5F6;
    color: #D2D8DE;
    align-items: center;
    margin-bottom: 0;
    font-weight: 500;
  }
  
  .custom-file-upload input[type="file"] {
    display: none;
  }
  input::placeholder {
    font-family: "TT Norms";
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    color: #D2D8DE;
  }
  .form-btn-active {
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1px solid #6266EA;
  }
  .form-btn {
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1px solid #DDE1E5;
  }
  select {
    padding: 10px;
    font-family: TT Norms;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    border-radius: 3px;
  }
  
  select option {
    font-family: TT Norms;
    font-size: 14px;
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
  }
  label{
    font-weight: 700;
    margin: 0;
  }
  .grafic_text{
    font-size: 10px;
    font-weight: 400;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
    color:#535C69;
  }
  .grafic{
    display: flex;
    align-items: center;
  }
  .grafic-btn{
    background: #FFFFFF;
    color: #D2D8DE;
  }
  .grafic-btn-active {
    background-color: #FFFFFF;
    color: #6266EA;
    border-radius: 3px;
  }
  .dot {
    display: flex;
    align-items: center;
    height: 2px;
    width: 2px;
    background: #C6CBD2;
    border-radius: 5px;
  }
</style>
  