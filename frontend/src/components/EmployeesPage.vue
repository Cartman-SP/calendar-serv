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
            <input type="text" v-model="firstname" id="firstName" placeholder="Введите имя">
          </div>
          <div class="form-column">
            <label for="lastName">Фамилия</label>
            <input type="text" v-model="secondname" id="lastName" placeholder="Введите фамилию">
          </div>
        </div>

        <div class="form-row">
          <div class="form-column">
            <label for="position">Должность</label>
            <input type="text" v-model="rank" id="position" placeholder="Введите должность">
          </div>
          <div class="form-column">
            <label for="photo">Фото</label>
            <label class="custom-file-upload">
              <input type="file" @change="handleFileUpload" accept="image/*"/>Прикрепите фото
            </label>
          </div>
        </div>
        
        <div class="dropdown-container">
          <label for="service">Услуга</label>
          <SelectPage
          :options="['Стрижка', 'Стрижка и борода', 'Укладка волос', 'Чистка лица','Оконтовка','Отец + сын']"
          :default="'Выберете услугу'"
          class="select"
          />
        </div>

        <div class="chips-block">
          <div class="chip" v-for="chip in chips" :key="chip">
            <svg width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
            </svg>
            <p>{{ chip }}</p>
          </div>
        </div>

        <div class="form-row">
          <div class="dropdown-container">
            <div class="usluga-head" v-if="selectedRecordType !== ''">
              <label for="groupCapacity">График работы</label>
              <Tip :Tip="'На основе выбранного графика, система автоматически \n сформирует график работы на месяц вперед'"/>
            </div>
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
              <SelectPage
              :options="['9:00 — 19:00', '9:00 — 20:00', '9:00 — 21:00', '10:00 — 18:00','10:00 — 19:00','10:00 — 20:00', '10:00 — 22:00']"
              :default="'Выберете время'"
              class="select"
              />
            </div>
          </div>
          <div class="dropdown-container">
            <label for="break">Перерыв</label>
            <div class="dropdown-container">
              <SelectPage
              :options="['13:00 — 14:00', '13:00 — 14:00', '13:00 — 14:00']"
              :default="'Выберите время'"
              class="select"
              />
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
import axios from 'axios';
import Tip from '../components/TipComponent.vue';
import SelectPage from '../components/SelectPage.vue';


export default {
  components: { Tip, SelectPage },
  data() {
    return {
      selectedDays: [],
      selectedRecordType: 'individual',
      selectedPaymentFormat: 'sessionPayment',
      uploadedFile: null,
      groupCapacity: 0,
      mxGroupCapacity: 0,
      sealectedSchedule: null, // Новое свойство для хранения выбранного графика работы
      uslugi: [],
      firstname: "",
      secondname: "",
      rank: "",
      avatar: null,
      work_time: "",
      chill_time: "",
      selectedServiceId: null, // Добавленная переменная для хранения выбранного id услуги
      
      chips: ['говно', 'залупа', 'пенис', 'хер+давалка', 'хуй', 'блядина', 'головка', 'шлюха']
    };
  },
  methods: {

    handleFileUpload(event) {
      const file = event.target.files[0];
      this.avatar = file;
    },
    async get_uslugi(){
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/uslugi/');
        this.uslugi = response.data;
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    
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
      const formData = new FormData();
      const selectedDaysString = this.selectedDays.join(',');
      formData.append('firstname', this.firstname);
      formData.append('secondname',this.secondname);
      formData.append('rank',this.rank);
      formData.append('avatar',this.avatar)
      formData.append('serviceid', this.selectedServiceId)
      formData.append('worktime',this.work_time);
      formData.append('timetable',this.selectedSchedule)
      formData.append('chilltime',this.chill_time);
      formData.append('days',selectedDaysString)
      formData.append('avatar', this.avatar);
      formData.append('user_id', this.$store.state.registrationData.user_id)
      axios.post('http://127.0.0.1:8000/api/employee/', formData)
        .then(response => {
          console.log('Service created:', response.data);
          this.$router.go(-1);
        })
        .catch(error => {
          console.error('Error creating service:', error);
        });
    },
    cancel() {
      // Ваша текущая логика отмены
    },
  },
  mounted(){
    this.get_uslugi()
  },
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
  .usluga-head{
    display: flex;
    justify-content: start;
    gap: 10px;
    align-items: center;
    margin-bottom: 5px;
  }

  .usluga-head label{
    margin: 0;
  }
  .input-group {
    display: flex;
    flex-direction: column;
    width: 49%;
  }
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
    font-family: TT Norms Medium;
    font-size: 20px;
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
  .create_employess {
    width: 500px;
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
    transition: background-color 0.2s, color 0.2s;
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
    font-family: "TT Norms Medium";
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    color: #D2D8DE;
  }
  .form-btn-active {
    box-sizing: border-box;
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1.5px solid #6266EA;
    background-color: rgba(98, 102, 234, 0.1);
  }
  .form-btn {
    box-sizing: border-box;
    background-color: #FFFFFF;
    color: #535C69;
    border-radius: 3px;
    border: 1.5px solid #DDE1E5;
    transition: all .2s ease;
  }

  .form-btn:hover{  
    border: 1.5px solid #535C69;
  }

  select {
    padding: 10px;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
    border-radius: 3px;
  }
  
  select option {
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #535C69;
  }
  select#service {
    width: 100%;
    padding: 10px;
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 20px;
    color: #D2D8DE;
    border: none;
    background-color: #F3F5F6;
  }
  label{
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
  