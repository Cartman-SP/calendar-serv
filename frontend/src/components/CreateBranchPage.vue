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
      <form class="branch-form">
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
          <button class="btn">Продолжить</button>
        </div>
      </form>
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
    }
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
  }

  input,
  select {
    padding: 8px 10px;
    font-family: TT Norms;
    font-size: 16px;
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
  
  select option {
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 20px;
    color: #535C69;
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
</style>
