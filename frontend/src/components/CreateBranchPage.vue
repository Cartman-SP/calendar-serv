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
            <SelectPage
            :options="['Россия', 'Казахстан','Украина','Таджикистан','Кыргызстан']"
            class="select"
            @input="option => selectedCountry = option"
            :placeholderdata="'Выберите страну'"
            />
          </div>

          <div class="form-group">
            <label for="city">Город</label>
            <SelectPage
            :options="['Москва', 'Санкт-Петербург','Тула','Тверь','Великий Новгород']"
            class="select"
            @input="option => selectedCity = option"
            :placeholderdata="'Выберите город'"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="address">Адрес</label>
          <input type="text" id="address" v-model="selectedAdress" placeholder="Введите точный адрес">
        </div>

        <div class="form-group">
          <label for="branchName">Название филиала</label>
          <input type="text" id="branchName" v-model="selectedName" placeholder="Введите название" maxlength="25">
          <p class="character-limit">Название должно содержать не более 25 знаков</p>
        </div>

        <div class="form-group">
          <label for="branchPhoto">Фото филиала</label>
          <label class="custom-file-upload">
            <input type="file" accept="image/*" multiple/>Загрузите несколько фотографий
          </label>
          <p class="photo-info">до 5 МБ, PNG, JPG, JPEG. Для замены удалите миниатюру и загрузите заново</p>
        </div>

        <div class="upload">
          <div class="upload_img">
            <img class="upl_img" src="../../static/img/salon.png" alt="">
          </div>
          <div class="upload_img">
            <img class="upl_img" src="../../static/img/salon.png" alt="">
          </div>
          <div class="upload_img">
            <img class="upl_img" src="../../static/img/salon.png" alt="">
          </div>
        </div>

        <div class="form-group graffic">
          <label class="graffic_label">График работы</label>
          <div class="days">
              <button class="btn_day" :class="{ 'active': isBtnActive('Пн') }" @click="toggleBtn('Пн')">Пн</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Вт') }" @click="toggleBtn('Вт')">Вт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Ср') }" @click="toggleBtn('Ср')">Ср</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Чт') }" @click="toggleBtn('Чт')">Чт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Пт') }" @click="toggleBtn('Пт')">Пт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Сб') }" @click="toggleBtn('Сб')">Сб</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Вс') }" @click="toggleBtn('Вс')">Вс</button>
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
      <div class="next-page" v-else>
        <div class="form-container">
          <div class="one-group">
            <div class="form-group">
              <label for="country">Рабочие часы</label>
              <SelectPage
              :options="['9:00 — 19:00', '9:00 — 20:00', '9:00 — 21:00', '10:00 — 18:00','10:00 — 19:00','10:00 — 20:00', '10:00 — 22:00']"
              class="select"
              @input="option => selectedWorkHours  = option"
              :placeholderdata="'Выберите время'"
              />
            </div>
  
            <div class="form-group">
              <label for="city">Перерыв</label>
              <SelectPage
              :options="['9:00 — 19:00', '9:00 — 20:00', '9:00 — 21:00', '10:00 — 18:00','10:00 — 19:00','10:00 — 20:00', '10:00 — 22:00']"
              class="select"
              @input="option => selectedTimeout  = option"
              :placeholderdata="'Выберите время'"
              />
            </div>
          </div>
          <div class="types-container">
            <label style="margin-bottom:10px">Выберите тип бизнеса</label>
            <div class="types">
              <div v-for="t in businessTypes" :key="t.name" class="choice" @click="activateChoice(t)">
                <div class="circle">
                  <div class="second_circle"></div>
                </div>
                <p class="choice_text">{{ t.name }}</p>
              </div>
            </div>
          </div>
          <div class="dropdown-container">
            <label for="service">Сфера бизнеса</label>
            <SelectPage
            :options="this.spheres.map(item => item.name)"
            class="select"
            @input="option => selectedBusiness = option"
            :placeholderdata="'Выберите сферу бизнеса'"
            />
          </div>
          <div class="dropdown-container">
            <label for="service">Выберите сотрудников для этого филиала</label>
            <SelectPage
            :options="this.employees.map(item => ({
                        name: item.firstname + ' ' + item.secondname,
                        id: item.id,
                      }))"

            class="select"
            @input="handleSelectInput"
            :placeholderdata="'Выберите сотрудников'"
            />
          </div>
          <div class="chips-block">
            <div class="chip" v-for="chip in filteredChips" :key="chip.id">
              <svg @click="deleteChip(chip)" width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
              </svg>
              <p>{{ chip.name }}</p>
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
              <button class="back" @click="onBackClick">Вернуться</button>
              <button class="btn" @click="Finish">Завершить</button>
            </div>
          </div>
        </div>  
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SelectPage from '../components/SelectPage.vue';

export default {
  components: { SelectPage },
  data() {
    return {
      activeDays: [],
      selectedChoices: [],
      showContinueButtonClicked: false,
      businessTypes: ['qwdqwd', 'qwdqwdqdwqwd'],
      spheres: [],

      selectedEmployeeId: [], 
      chips: [],
    }
  },
  mounted(){
    this.get_workers()
    this.get_buisnessTypes()
    this.get_buisnesssphere()
  },
  computed: {
    filteredChips() {
      // Начинаем с индекса 1 (второй элемент) и возвращаем оставшиеся элементы
      return this.chips.slice(1);
    }
  },

  methods: {
    deleteChip(chip){
      let indexToRemove = this.chips.indexOf(chip);
      if (indexToRemove !== -1) {
        this.chips.splice(indexToRemove, 1);
      }
    },

    get_workers(){
      axios.post('http://127.0.0.1:8000/api/getworkers/', { user_id:  this.$store.state.registrationData.user_id})
      .then(response => {
        console.log(response.data)
        this.employees = response.data;
      })
      .catch(error => {
        // Ошибка при получении данных
        console.error('Ошибка при получении данных о пользователе:', error);
      });
    },
    get_buisnessTypes(){
      axios.get('http://127.0.0.1:8000/api/get_buisnessTypes/')
      .then(response => {
        console.log(response.data)
        this.businessTypes = response.data
      })
      .catch(error => {
        // Ошибка при получении данных
        console.error('Ошибка при получении данных о пользователе:', error);
      });
    },

    get_buisnesssphere(){
      axios.get('http://127.0.0.1:8000/api/get_buisnessSphere/')
      .then(response => {
        console.log(response.data)
        this.spheres = response.data
      })
      .catch(error => {
        // Ошибка при получении данных
        console.error('Ошибка при получении данных о пользователе:', error);
      });
    },

    handleSelectInput(selected) {
      const existingChip = this.chips.find(chip => chip.name === selected.name && chip.id === selected.id);
      if (!existingChip) {
        this.chips.push({ name: selected.name, id: selected.id });
      }
    },


    isBtnActive(day) {
      return this.activeDays.includes(day);
    },
    toggleBtn(day) {
      if (this.isBtnActive(day)) {
        this.activeDays = this.activeDays.filter(activeDay => activeDay !== day);
      } else {
        this.activeDays.push(day);
      }
    },
    onContinueButtonClick() {
      if (!this.isContinueDisabled) {
        this.showContinueButtonClicked = true;
      }
    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },

    Finish(){
      const chipsIds = this.chips
  .filter(chip => chip.id) // Фильтруем массив, оставляя только элементы с существующим id
  .map(chip => chip.id)
  .join(', ');
      const data = {
    country: this.country,
    city: this.city,
    address: '',  
    name: this.name,
    active_days: this.active_days.join(', '),
    work_hours: this.work_hours,
    timeout: this.timeout,
    choices: this.selectedChoicesIds,  // Массив с выбранными идентификаторами
    business: this.business,
    chips: chipsIds
};

// Отправка данных на сервер
axios.post('http://127.0.0.1:8000/api/createbranch/', data)
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
    },

    activateChoice(t) {
      // Получите ссылку на текущий выбор
      const choice = event.currentTarget;
      // Проверьте, есть ли у выбранного выбора уже класс active
      const isActive = choice.classList.contains('active');

      // Удалите `active` класс из всех choice
      document.querySelectorAll('.choice').forEach(choice => {
        choice.classList.remove('active');
      });

      // Если у выбранного выбора уже есть класс active, удаляем его и возвращаемся к изначальному состоянию
      if (isActive) {
        choice.querySelector('.second_circle').style.display = 'none';
        choice.querySelector('.choice_text').style.color = '#AFB6C1';
        choice.querySelector('.circle').style.borderColor = '#C6CBD2'; // возвращаем цвет границы Circle
      } else {
        // Если класса нет, добавляем его и меняем стиль в соответствии с задачей
        choice.classList.add('active');
        choice.querySelector('.second_circle').style.display = 'inline-block';
        choice.querySelector('.choice_text').style.color = '#6266EA';
        choice.querySelector('.circle').style.borderColor = '#6266EA'; // меняем цвет границы Circle

        // Добавляем значение в массив выбранных элементов
        this.selectedChoices.push(t);
      }
    },
  }
}
</script>

<style scoped>
.chip svg:hover path{
    fill: rgb(250, 148, 148);
  }
  .chips-block{
    width: 100%;
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
  }

  .chip{
    display: flex;
    gap: 5px;
    align-items: center;
    justify-content: start;
    background-color: #6266EA;
    height: 20px;
    padding: 0 15px;
    border-radius: 10px;
    transition: all .2s ease;
  }

  .chip:hover{
    background-color: #5357c7;
    cursor: pointer;
  }

  .chip p{
    margin: 0;
    color: white;
    font-family: 'TT Norms';
    font-size: 12px;
    margin-top: -1.5px;
  }
  .create_branch {
    width: 50%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0;
  }

  input {
    padding: 8px 10px;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #535C69;
    border: none;
    background-color: #F3F5F6;
    margin-bottom: 10px;
    height: 36px;
    margin-bottom: 5px;
  }

  select{
    border-radius: 3px;
  }

  p {
    font-size: 12px;
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
    font-family: "TT Norms Medium";
    font-size: 14px;
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
  .photo-info{
    color: #AFB6C1;
    font-size: 10px;
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
    font-family: TT Norms Medium;
    font-size: 20px;
    line-height: 24px;
    text-align: left;
    text-decoration: none;
    color: #AFB6C1;
  }
  
  .creation_text {
    color: #535C69;
    font-family: TT Norms Medium;
    font-size: 20px;
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
    margin: 10px 0;
  }
  .steps-progress{
    display: flex;
    gap: 5px;
  }
  .steps-text{
    text-align: left;
    font-family: TT Norms Medium;
    font-size: 10px;
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
  .branch-form{
    display: flex;
    flex-direction: column;
    gap: 10px;
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
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
    box-sizing: border-box;
  }
  select {
    padding: 10px;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #535C69;
    border: none;
    background-color: #F3F5F6;
    border-radius: 3px;
  }
  
  select option {
    font-family: TT Norms Medium;
    font-size: 16px;
    line-height: 20px;
    color: #535C69;
  }
  select#service {
    width: 100%;
    padding: 10px;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #535C69;
    border: none;
    background-color: #F3F5F6;
  }
  .types{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  .choice{
    display: flex;
    gap: 5px;
  }
  .circle{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 18px;
    height: 18px;
    border: 1px solid #C6CBD2;
    background: #F3F5F6;
    border-radius: 15px;
    cursor: pointer;
  }
  .choice_text{
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
    color: #AFB6C1;
    cursor: pointer;
  }
  .back{
    color: #D2D8DE;
    background: #FFFFFF;
    border: 1px solid #DDE1E5;
  }
  .second_circle{
    background: #6266EA;
    width: 10px;
    height: 10px;
    border-radius: 25px;
    display: none;
  }
  .choice.active .circle {
    border-color: #6266EA; /* добавили изменение цвета границы для активного choice */
  }
  .upload{
    display: flex;
    gap: 10px;
  }
  .upload_img {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 64px;
    height: 64px;
    border-radius: 5px;
    overflow: hidden;
    position: relative;
  }
  .upl_img {
    width: 100%;
    height: 100%;
  }
  .graffic_label{
    margin: 0;
  }
  .graffic{
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  .btn_day{
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: left;
    box-sizing: border-box;
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1.5px solid #DDE1E5;
    transition: all .2s ease;
  }

  .btn_day:hover{
    border: 1.5px solid #535C69;
  }
  .days{
    display: flex;
    gap: 10px;
  }
  .btn_day.active {
    box-sizing: border-box;
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1.5px solid #6266EA;
    background-color: rgba(98, 102, 234, 0.1);
  }
</style>