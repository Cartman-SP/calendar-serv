<template>
  <div class="main">
    <div class="create_employess">
      <div class="transition">
        <a href="#/main/personal" class="employesss-link">Сотрудники</a>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <p class="creation_text">Создание сотрудника</p>
      </div>
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
          <div class="form-container">
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
          <div class="flex-row">
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

    <div class="navigation">
      <!-- Подключение других компонентов -->
      <SidebarPage/>
      <NavbarPage/>
    </div>
  </div>
</template>


  
<script>
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';

export default {
  components: { NavbarPage, SidebarPage },
  data() {
    return {
      // Добавлено новое свойство для хранения выбранных дней
      selectedDays: [],
      selectedRecordType: 'individual',
      selectedPaymentFormat: 'sessionPayment',
      uploadedFile: null,
      groupCapacity: 0,
      maxGroupCapacity: 0,
    };
  },
  methods: {
    // Добавлен новый метод для проверки выбран ли день
    isDaySelected(day) {
      return this.selectedDays.includes(day);
    },
    // Добавлен новый метод для изменения состояния выбранного дня
    toggleDay(day) {
      if (this.isDaySelected(day)) {
        this.selectedDays = this.selectedDays.filter(selectedDay => selectedDay !== day);
      } else {
        this.selectedDays.push(day);
      }
    },
    // Ваша текущая логика сохранения и выхода
    saveAndExit() {
      // ...
    },
    // Ваша текущая логика отмены
    cancel() {
      // ...
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
    margin-bottom: 50px;
  }

  .employesss-link {
    font-family: TT Norms;
    font-size: 20px;
    font-weight: 500;
    line-height: 24px;
    text-align: left;
    text-decoration: none;
    color: #AFB6C1;
  }

  .creation_text {
    color: #535C69;
    font-family: TT Norms;
    font-size: 20px;
    font-weight: 500;
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

  .navigation {
    display: flex;
    background-color:#FAFAFA;
  }

  .create_employess {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 530px;
    height: 549px;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
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
    width: 240px;
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
    font-size: 16px;
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
    font-size: 16px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
  }
  input{
    width: 240px;
  }
  label{
    font-weight: 700;
  }
</style>
  