    <template>
      <div class="main">
        <div v-if="firstemployye">
          <ModalEmployeesPage/>
        </div>
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
                <input type="text" v-model="firstname" id="firstName" placeholder="Введите имя" :class="{ 'input-error': firstnameError }">
              </div>
              <div class="form-column">
                <label for="lastName">Фамилия</label>
                <input type="text" v-model="secondname" id="lastName" placeholder="Введите фамилию" :class="{ 'input-error': secondnameError }">
              </div>
            </div>

            <div class="form-row">
              <div class="form-column">
                <label for="position">Должность</label>
                <input type="text" v-model="rank" id="position" placeholder="Введите должность" :class="{ 'input-error': rankError }">
              </div>
              <div class="form-column">
                <label for="photo">Фото</label>
                <label class="custom-file-upload" :class="{'custom-file-upload-error' : avatarError}" v-if="!fileNameVariable">
                  <input type="file" accept="image/*" @change="handleFileUpload($event)"/>Нажмите, чтобы добавить 
                </label>
                <label style="color: #535C69;" class="custom-file-upload" :class="{'custom-file-upload-error' : avatarError}" v-else>
                  <input type="file" accept="image/*" @change="handleFileUpload($event)"/>{{ fileNameVariable }}
                </label>
              </div>
            </div>
            
            <div class="dropdown-container">
              <label for="service">Услуга</label>
              <SelectPage
                :options="this.uslugi.map(item => 
                ({name: item.name, 
                  id: item.id}))"
                class="select"
                @input="handleSelectInput"
                :placeholderdata="'Выберите услугу'"
                :class="{ 'select-error': chipsError }"
              />
            </div>

            <div class="chips-block">
              <div class="chip" v-for="chip in chips" :key="chip.id">
                <svg @click="deleteChip(chip)" width="8" height="8" viewBox="0 0 6 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2.29294 3.00003L0.146484 5.14648L0.853591 5.85359L3.00004 3.70714L5.1465 5.85359L5.85361 5.14648L3.70715 3.00003L5.85359 0.853591L5.14648 0.146484L3.00004 2.29292L0.853605 0.146484L0.146499 0.853591L2.29294 3.00003Z" fill="white"/>
                </svg>
                <p>{{ chip.name }}</p>
              </div>
            </div>

            <div class="form-row">
              <div class="dropdown-container">
                <div class="usluga-head" v-if="selectedRecordType !== ''">
                  <label for="groupCapacity">График работы</label>
                  <Tip :Tip="'На основе выбранного графика, система автоматически \n сформирует график работы на месяц вперед'"/>
                </div>
                <div class="graffic_container">
                  <button class="graffic_btn" @click="toggleGraffic('weekly')" :class="{ 'graffic_btn-active': selectedRecordType === 'weekly', 'button-error' : selectedRecordTypeError }">Недельный график</button>
                  <button class="graffic_btn" @click="toggleGraffic('replaceable')" :class="{ 'graffic_btn-active': selectedRecordType === 'replaceable', 'button-error' : selectedRecordTypeError  }">Сменный график</button>
                </div>
                <div class="weekly" v-show="isGrafficActive('weekly')">
                  <p class="graffic_text">
                    Недельный график:
                  </p>
                  <div class="days-buttons">
                    <button :class="{ 'form-btn-active': isDaySelected('Пн'), 'form-btn': !isDaySelected('Пн'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Пн')">
                      Пн
                      <svg @click.stop="toggleTimeArea('Пн')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Вт'), 'form-btn': !isDaySelected('Вт'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Вт')">
                      Вт
                      <svg @click.stop="toggleTimeArea('Вт')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Ср'), 'form-btn': !isDaySelected('Ср'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Ср')">
                      Ср
                      <svg @click.stop="toggleTimeArea('Ср')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Чт'), 'form-btn': !isDaySelected('Чт'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Чт')">
                      Чт
                      <svg @click.stop="toggleTimeArea('Чт')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Пт'), 'form-btn': !isDaySelected('Пт'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Пт')">
                      Пт
                      <svg @click.stop="toggleTimeArea('Пт')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Сб'), 'form-btn': !isDaySelected('Сб'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Сб')">
                      Сб
                      <svg @click.stop="toggleTimeArea('Сб')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                    <button :class="{ 'form-btn-active': isDaySelected('Вс'), 'form-btn': !isDaySelected('Вс'), 'button-days-error' : selectedDaysError }" @click="toggleDay('Вс')">
                      Вс
                      <svg @click.stop="toggleTimeArea('Вс')" width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M8 4C8 6.20914 6.20914 8 4 8C1.79086 8 0 6.20914 0 4C0 1.79086 1.79086 0 4 0C6.20914 0 8 1.79086 8 4ZM4.2 1.8H3.4V3.96569L5.51716 6.08284L6.08284 5.51716L4.2 3.63431V1.8Z" fill="#D2D8DE"/>
                      </svg>
                    </button>
                  </div>
                </div>
                <div v-if="timeArea" class="form-column">
                  <label>Рабочие часы - {{ timeAreaDay }}</label>
                  <input type="text">
                </div>
                <div class="replaceable" v-show="isGrafficActive('replaceable')">
                  <p class="graffic_text">
                    Сменный график (Рабочий день х Выходной день):
                  </p>
                  <div class="days-buttons">
                    <button :class="{ 'form-btn-active': isDaySelected('1x1'), 'form-btn': !isDaySelected('1x1'), 'button-days-error' : selectedDaysError }" @click="toggleDay('1x1')">1x1</button>
                    <button :class="{ 'form-btn-active': isDaySelected('2х2'), 'form-btn': !isDaySelected('2х2'), 'button-days-error' : selectedDaysError }" @click="toggleDay('2х2')">2х2</button>
                    <button :class="{ 'form-btn-active': isDaySelected('3х3'), 'form-btn': !isDaySelected('3х3'), 'button-days-error' : selectedDaysError }" @click="toggleDay('3х3')">3х3</button>
                    <button :class="{ 'form-btn-active': isDaySelected('7х7'), 'form-btn': !isDaySelected('7х7'), 'button-days-error' : selectedDaysError }" @click="toggleDay('7х7')">7х7</button>
                    <button :class="{ 'form-btn-active': isDaySelected('1х2'), 'form-btn': !isDaySelected('1х2'), 'button-days-error' : selectedDaysError }" @click="toggleDay('1х2')">1х2</button>
                    <button :class="{ 'form-btn-active': isDaySelected('2х1'), 'form-btn': !isDaySelected('2х1'), 'button-days-error' : selectedDaysError }" @click="toggleDay('2х1')">2х1</button>
                    <button :class="{ 'form-btn-active': isDaySelected('15х15'), 'form-btn': !isDaySelected('15х15'), 'button-days-error' : selectedDaysError }" @click="toggleDay('15х15')">15х15</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="form-row">
              <div class="dropdown-container">
                <label for="workingHours">Рабочие часы</label>
                <div class="dropdown-container">
                  <SelectPage
                  :options="['9:00 — 19:00', '9:00 — 20:00', '9:00 — 21:00', '10:00 — 18:00','10:00 — 19:00','10:00 — 20:00', '10:00 — 22:00']"
                  @input="option => work_time = option"
                  :placeholderdata="'Выберите время'"
                  :class="{ 'select-error': work_timeError }"
                  />    
                </div>
              </div>
              <div class="dropdown-container">
                <label for="break">Перерыв</label>
                <div class="dropdown-container">
                  <SelectPage
                  :options="['13:00 — 14:00', '13:00 — 14:00', '13:00 — 14:00']"
                  @input="option => chill_time = option"
                  :placeholderdata="'Выберите время'"
                  :class="{ 'select-error': chill_timeError }"
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
        <MessageAlert :message="alertMessage" :color="alertColor"/>
      </div>
    </template>

<script>
    import axios from 'axios';
    import Tip from '../components/TipComponent.vue';
    import SelectPage from '../components/SelectPage.vue';
    import MessageAlert from "../components/MessageAlert.vue";
    import ModalEmployeesPage from "../components/ModalEmployeesPage.vue"
    export default {
      components: { Tip, SelectPage, MessageAlert, ModalEmployeesPage },
      data() {
        return {
          timeArea: false,
          timeAreaDay: '',
          firstemployye: false,
          selectedDays: [],
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
          work_time: '',
          chill_time: '',
          selectedServiceId: [],
          chips: [],
          selectedRecordType: 'weekly',
          alertMessage: null,

          firstnameError: false,
          secondnameError: false,
          rankError: false,
          avatarError: false,
          chipsError: false,
          selectedRecordTypeError: false,
          selectedDaysError: false,
          work_timeError: false,
          chill_timeError: false,

          fileNameVariable: '',
        };
      },
    
      methods: {
        toggleTimeArea(day){
          this.timeArea = true;
          this.timeAreaDay = day;
        },
        
        handleFileUpload(event) {
          const file = event.target.files[0];
          this.avatar = file; // сохраняем весь объект файла
          const fileName = file.name; // извлекаем название файла
          this.fileNameVariable = fileName; // сохраняем название файла в переменной
        },

        deleteChip(chip){
          let indexToRemove = this.chips.indexOf(chip);
          if (indexToRemove !== -1) {
            this.chips.splice(indexToRemove, 1);
          }
        },

        handleSelectInput(selected) {
          const existingChip = this.chips.find(chip => chip.name === selected.name && chip.id === selected.id);
          if (!existingChip) {
            this.chips.push({ name: selected.name, id: selected.id });
          }
        },
    async get_uslugi(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/uslugi/?variable=${this.$store.state.registrationData.user_id}`);
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
        isGrafficActive(type) {
          return this.selectedRecordType === type;
        },
        toggleGraffic(type) {
          this.selectedRecordType = type;
        },
        saveAndExit() {
          if (!this.firstname || !this.secondname || !this.rank || !this.avatar || !this.chips.length || !this.selectedRecordType || !this.selectedDays.length || !this.work_time || this.chill_time) {
            this.alertMessage = null;
            console.log(this.selectedDays.length, this.work_time, this.chill_time)
            setTimeout(() => {
              this.alertMessage = 'Пожалуйста, заполните выделенные поля';
            this.alertColor = '#F97F7F';
            }, 100);

            if (!this.firstname) {
              this.firstnameError = true;
            }else{
              this.firstnameError = false;
            }
            if (!this.secondname) {
              this.secondnameError = true;
            }else{
              this.secondnameError = false;
            }
            if (!this.rank) {
              this.rankError = true;
            }else{
              this.rankError = false;
            }
            if (!this.avatar) {
              this.avatarError = true;
            }else{
              this.avatarError = false;
            }
            if (!this.chips.length > 0) {
              this.chipsError = true;
            }else{
              this.chipsError = false;
            }
            if (!this.selectedRecordType) {
              this.selectedRecordTypeError = true;
            }else{
              this.selectedRecordTypeError = false;
            }
            if (this.selectedDays.length === 0) {
              this.selectedDaysError = true;
            }else{
              this.selectedDaysError = false;
            }
            if (!this.work_time.length > 0) {
              this.work_timeError = true;
            }else{
              this.work_timeError = false;
            }
            if (!this.chill_time.length > 0) {
              this.chill_timeError = true;
            }else{
              this.chill_timeError = false;
            }
          }


          let usl = ""
          for(let i=0;i<this.chips.length;i++){
            usl+=this.chips[i].id + ','
          }
          const formData = new FormData();
          const selectedDaysString = this.selectedDays.join(',');
          formData.append('firstname', this.firstname);
          formData.append('secondname',this.secondname);
          formData.append('rank',this.rank);
          formData.append('avatar',this.avatar)
          formData.append('serviceid', usl)
          formData.append('worktime',this.work_time);
          formData.append('timetable',this.selectedSchedule)
          formData.append('chilltime',this.chill_time);
          formData.append('days',selectedDaysString)
          formData.append('avatar', this.avatar);
          formData.append('user_id', this.$store.state.registrationData.user_id)
          axios.post('http://127.0.0.1:8000/api/employee/', formData)
            .then(response => {
              console.log('Employee created:', response.data);
              this.alertMessage = 'Настройки успешно сохранены'
              this.alertColor = '#0BB6A1'
              console.log(response)
              if(response.data){
              this.firstemployye = response.data
              }else{
              setTimeout(() => {
                this.$router.go(-1);
              }, 2000)}
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
  watch: {
    firstname() {
      this.alertMessage = null;
      this.firstnameError = false;
    },
    secondname() {
      this.alertMessage = null;
      this.secondnameError = false;
    },
    rank() {
      this.alertMessage = null;
      this.rankError = false;
    },
    avatar(){
      this.alertMessage = null;
      this.avatarError = false;
    },
    chips() {
      this.alertMessage = null;
      this.chipsError = false;
    },
    selectedRecordType() {
      this.alertMessage = null;
      this.selectedRecordTypeError = false;
    },
    selectedDays(){
      this.alertMessage = null;
      this.selectedDaysError = false;
    },
    work_time(){
      this.alertMessage = null;
      this.work_timeError = false;
    },
    chill_time(){
      this.alertMessage = null;
      this.chill_timeError = false;
    },
  },
}
</script>
  
  <style scoped>
  .button-days-error{
    border: 1px solid #F97F7F !important;
    border-radius: 3px;
  }
  .custom-file-upload-error{
    border: 1px solid #F97F7F !important;
    border-radius: 3px;
  }
  .input-error {
    border: 1px solid #F97F7F !important;
  }
  .button-error{
    border: solid 1px #F97F7F !important;
  }
  .select-error >>> .selected{
    border: solid 1px #F97F7F !important;
  }
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
        background-image: url(../../static/img/paperclip.svg);
        background-repeat: no-repeat;
        background-position: calc(100% - 15px) center;
      }
      
      .custom-file-upload input[type="file"] {
        display: none;
      }
      input::placeholder {
        font-family: "TT Norms Medium";
        font-size: 13px;
        font-weight: 500;
        line-height: 17px;
        letter-spacing: 0em;
        color: #D2D8DE;
      }
      .form-btn-active {
        position: relative;
        height: 50px;
        width: 50px;
        box-sizing: border-box;
        background-color: #FFFFFF;
        color: #535C69;
        border-radius: 3px;
        border: 1px solid #6266EA;
        background-color: rgba(98, 102, 234, 0.1);
      }

      .form-btn-active svg{
        position: absolute;
        z-index: 10;
        right: 2px;
        bottom: 2px;
      }

      .form-btn-active svg path{
        fill: #6266EA;
        transition: all .2s ease;
      }

      .form-btn {
        position: relative;
        height: 50px;
        width: 50px;
        box-sizing: border-box;
        background-color: #FFFFFF;
        color: #535C69;
        border-radius: 3px;
        border: 1px solid #DDE1E5;
        transition: all .2s ease;
      }

      .form-btn svg{
        position: absolute;
        right: 2px;
        bottom: 2px;
      }

      .form-btn svg path{
        fill: #D2D8DE;
        transition: all .2s ease;
      }

      .form-btn:hover{  
        border: 1px solid #535C69;
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
      .graffic_btn-active {
        background-color: #6266EA !important;
        color: #FFFFFF !important;
      }
      .graffic_container{
        display: flex;
        gap: 5px;
      }
      .graffic_btn{
        background: #F3F5F6;
        color: #D2D8DE;
      }
      .graffic_btn:hover{
        background-color: #6266EA;
        color: #FFFFFF;
      }

      .graffic_text{
        font-family: TT Norms Medium;
        font-size: 13px;
        line-height: 15px;
        letter-spacing: 0em;
        text-align: left;
        color: #535C69;
      }
    </style>
      