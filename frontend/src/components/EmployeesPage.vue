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
            <input type="file" id="photo" accept="image/*">
          </div>
        </div>

        <div class="form-row">
          <div class="dropdown-container">
            <label for="service">Услуга</label>
            <select id="service">
              <option>Стрижка</option>
              <option>Стрижка + борода</option>
              <option>Укладка волос</option>
              <option>Чистка лица</option>
              <option>Окантовка</option>
              <option>Отец + сын</option>
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-container">
            <label>График работы</label>
            <div class="days-buttons">
              <button class="form-btn">Пн</button>
              <button class="form-btn">Вт</button>
              <button class="form-btn">Ср</button>
              <button class="form-btn">Чт</button>
              <button class="form-btn">Пт</button>
              <button class="form-btn">Сб</button>
              <button class="form-btn">Вс</button>
            </div>
          </div>
        </div>

        <div class="form-row">
          <div class="dropdown-container">
            <label for="workingHours">Рабочие часы</label>
            <div class="dropdown-container">
              <select id="workingHours">
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
        selectedRecordType: 'individual',
        selectedPaymentFormat: 'sessionPayment',
        uploadedFile: null,
        groupCapacity: 0,
        maxGroupCapacity: 0,
      };
    },
    methods: {
      selectRecordType(type) {
        this.selectedRecordType = type;
      },
      selectPaymentFormat(format) {
        this.selectedPaymentFormat = format;
      },
      saveAndExit() {
        // Логика сохранения и выхода
      },
      cancel() {
        // Переход на предыдущую страницу
        this.$router.go(-1);
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

  .form-btn {
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1px solid #DDE1E5;
  }

  .form-btn:focus {
    outline: none; /* Remove default focus outline */
    border-color: #6266EA; /* Border color when the button is focused */
    box-shadow: 0 0 5px rgba(98, 102, 234, 0.5); /* Optional: Add a subtle box shadow */
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
    background-color: white;
  }

  .create_employess {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 488px;
    height: 439px;
    color: #FFFFFF;
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
    transition: background-color 0.3s, color 0.3s; /* Плавный переход при ховере */
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

</style>
  