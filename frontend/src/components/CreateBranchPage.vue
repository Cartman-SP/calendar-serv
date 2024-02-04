<template>
  <div class="main">
    <div class="create_branch">
      <div class="transition">
        <a href="#/main/branch  " class="branchs-link">Филиалы</a>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <p class="creation_text">Создание филиала</p>
      </div>

      <!-- Форма создания филиала -->
      <form class="branch-form">
        <div class="one-group">
          <div class="form-group">
            <label for="country">Страна</label>
            <select id="country">
              <option value="Russia">Россия</option>
              <option value="Kazakhstan">Казахстан</option>
              <option value="Belarus">Беларусь</option>
              <option value="Ukraine">Украина</option>
            </select>
          </div>

          <div class="form-group">
            <label for="city">Город</label>
            <select id="city">
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
            <input type="file" accept="image/*"/>Нажмите, чтобы добавить
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
          <button class="btn">Продолжить</button>
        </div>
      </form>
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
  methods: {
    weeklySchedule() {
      this.isWeeklyActive = true;
      this.isShiftActive = false;
      // Логика для недельного графика
    },
    shiftSchedule() {
      this.isWeeklyActive = false;
      this.isShiftActive = true;
      // Логика для сменного графика
    },
  },
  data() {
    return {
      isWeeklyActive: true,  // Измененная строка
      isShiftActive: false,
    };
  },
};
</script>

<style scoped>
  .transition {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 50px;
  }

  .branchs-link {
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

  .create_branch {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 488px;
    height: 439px;
    color: #FFFFFF;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  input,
  select {
    padding: 10px;
    font-family: TT Norms;
    font-size: 16px;
    font-weight: 500;
    line-height: 20px;
    color: #AFB6C1;
    border-radius: 5px;
  }

  p {
    font-family: TT Norms;
    font-size: 12px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    color: #D2D8DE;
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
    margin-top: 20px; /* Устанавливаем отступ от верхней границы формы */
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
  }
  
  .custom-file-upload input[type="file"] {
    display: none;
  }
</style>
