<template>
  
  <div class="main">
    <div v-if="first">
      <ModalBranchPage/>
    </div>
    <div class="transition">
      <router-link to="/lk/branch" class="employesss-link">Филиалы</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Создание филиала</p>
    </div>
    <div class="create_branch">
      <!-- Форма создания филиала -->
      <form class="branch-form" v-if="!showContinueButtonClicked" enctype="multipart/form-data">
        <div class="one-group">
          <div class="form-group">
            <label for="country">Страна</label>
            <SelectPage
            :options="['Россия', 'Казахстан','Украина','Таджикистан','Кыргызстан']"
            class="select"
            @input="option => selectedCountry = option"
            :placeholderdata="'Выберите страну'"
            :class="{ 'select-error': selectedCountryError }"
            />
          </div>

          <div class="form-group">
            <label for="city">Город</label>
            <SelectPage
            :options="['Москва', 'Санкт-Петербург','Тула','Тверь','Великий Новгород']"
            class="select"
            @input="option => selectedCity = option"
            :placeholderdata="'Выберите город'"
            :class="{ 'select-error': selectedCityError }"
            />
          </div>
        </div>

        <div class="one-group">
          <div class="form-group">
            <label for="address">Адрес</label>
            <input type="text" id="address" v-model="selectedAdress" placeholder="Введите точный адрес"
            :class="{ 'input-error': selectedAdressError }">
          </div>
          <div class="form-group" style="flex-direction: row; gap: 5px;">      
                <div class="card flex justify-content-center">
                  <label>Регион</label>
                  <DropdownComponent v-model="selectedCountryPhone" :options="countries" optionLabel="name" placeholder="🇷🇺" class="w-full md:w-14rem">
                    <template #value="slotProps">
                      <div v-if="slotProps.value" class="flex align-items-center">
                        <div>{{ slotProps.value.name }}</div>
                      </div>
                      <span v-else>
                        {{ slotProps.placeholder }}
                      </span>
                    </template>
                    <template #option="slotProps">
                      <div class="flex align-items-center">
                        <div>{{ slotProps.option.name }}</div>
                      </div>
                    </template>
                  </DropdownComponent>
                </div>
                <div class="form-group">
                  <label>Телефон</label>
                  <InputMaskComponent :class="{'PhoneError' : PhoneError}" id="basic" v-model="value" :mask="computedMask" :placeholder="computedPlaceholder"/>
                </div>
                
          </div>
        </div>
        

        <div class="form-group">
          <label for="branchName">Название филиала</label>
          <input type="text" id="branchName" v-model="selectedName" placeholder="Введите название" maxlength="25"
          :class="{ 'input-error': selectedNameError }">
          <p class="character-limit">Название должно содержать не более 25 знаков</p>
        </div>

        <div class="form-group">
          <div class="usluga-head">
            <label for="upload-image ">Фото филиала</label>
            <Tip :Tip="'Мы рекомендуем загрузить наиболее удачные фотографии. \n Первая фотография будет размещена в шапке виджета, остальные \n фотографии будут видны в виджете вашим клиентам'"/>
          </div>
          <label class="custom-file-upload">
            <input type="file" accept="image/*" id="upload-image" @change="handleImageUpload" multiple> Нажмите, чтобы добавить
          </label>
          <p class="photo-info">до 5 МБ, PNG, JPG, JPEG. Для замены удалите миниатюру и загрузите заново</p>
        </div>

        <div class="upload">
          <div class="upload_img" v-for="(image, index) in uploadedImages" :key="index">
            <img class="upl_img" :src="image.url" :alt="image.name">
          </div>
        </div>

        <div class="form-group graffic">
          <div class="usluga-head">
            <label>График работы</label>
            <Tip :Tip="'График работы это график работы, логично \n (нет описания на фигме)'"/>
          </div>
          <div class="days">
              <button class="btn_day" :class="{ 'active': isBtnActive('Пн'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Пн')">Пн</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Вт'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Вт')">Вт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Ср'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Ср')">Ср</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Чт'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Чт')">Чт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Пт'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Пт')">Пт</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Сб'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Сб')">Сб</button>
              <button class="btn_day" :class="{ 'active': isBtnActive('Вс'),'button-days-error' : selectedDaysError}" @click="toggleBtn('Вс')">Вс</button>
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
          <button class="btn" @click="onContinueButtonClick">Продолжить</button>
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
              :class="{ 'select-error': selectedWorkHoursError }"
              />
            </div>
  
            <div class="form-group">
              <label for="city">Перерыв</label>
              <SelectPage
              :options="['9:00 — 19:00', '9:00 — 20:00', '9:00 — 21:00', '10:00 — 18:00','10:00 — 19:00','10:00 — 20:00', '10:00 — 22:00']"
              class="select"
              @input="option => selectedTimeout  = option"
              :placeholderdata="'Выберите время'"
              :class="{ 'select-error': selectedTimeoutError }"
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
            :class="{'select-error' : selectedBusinessError}"
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
            :class="{ 'select-error': chipsError }"
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
    <MessageAlert :message="alertMessage" :color="alertColor"/>
  </div>
</template>

<script>
import axios from 'axios';
import SelectPage from '../components/SelectPage.vue';
import MessageAlert from "../components/MessageAlert.vue";
import Tip from '../components/TipComponent.vue';
import ModalBranchPage from '../components/ModalBranchPage.vue';

export default {
  components: { SelectPage, MessageAlert, Tip, ModalBranchPage},
  data() {
    return {
      alertMessage: null,
      alertColor: '',
      selectedDays: [],
      selectedChoices: [],
      showContinueButtonClicked: false,
      businessTypes: ['qwdqwd', 'qwdqwdqdwqwd'],
      spheres: [],
      uploadedImages: [],
      selectedEmployeeId: [],
      chips: [],
      selectedPhone: '79672262425',
      first: false,
      selectedCountryPhone: null,
      value: '7 ', // Начальное значение для InputMaskComponent
      countries: [
        { name: '🇷🇺', code: '+7' },
        { name: '🇧🇾', code: '+375' },
        { name: '🇰🇿', code: '+7' },
        { name: '🇺🇦', code: '+380' },
      ],

      fileNameVariable: '',
      selectedCity: '',
      selectedCountry: '',
      selectedAdress: '',
      selectedName: '',
      selectedWorkHours: '',
      selectedTimeout: '', 

      chipsError: false,
      selectedNameError: false,
      selectedAdressError: false,
      selectedCountryError: false,
      selectedCityError: false, 
      selectedDaysError: false,
      selectedWorkHoursError: false,
      selectedTimeoutError: false, 
      selectedBusinessError: false,
      PhoneError: false,
    }
  },
  mounted(){
    this.get_workers()
    this.get_buisnessTypes()
    this.get_buisnesssphere()
  },
  computed: {
    computedMask() {
      if (this.selectedCountryPhone) {
        const countryCode = this.selectedCountryPhone.code;
        if (countryCode === '+375' || countryCode === '+380') {
          return `${countryCode} (99) 999-99-99`;
        } else {
          return `${countryCode} (999) 999-99-99`;
        }
      } else {
        return '+7 (999) 999-99-99'; // Default mask
      }
    },
    computedPlaceholder() {
      return this.selectedCountryPhone ? this.selectedCountryPhone.code + ' |' : '+7 |';
    },

    filteredChips() {
      // Начинаем с индекса 1 (второй элемент) и возвращаем оставшиеся элементы
      return this.chips.slice(1);
    }
  },
  watch: {
    selectedCountryPhone(newCountry) {
      if (newCountry) {
        this.value = newCountry.code + ' ' + this.value.replace(/^\s*\+\d\s*\|\s*/, '');
      }
    },
    selectedCountry() {
      this.alertMessage = null;
      this.selectedCountryError = false;
    },
    selectedCity() {
      this.alertMessage = null;
      this.selectedCityError = false;
    },
    selectedAdress() {
      this.alertMessage = null;
      this.selectedAdressError = false;
    },
    selectedName() {
      this.alertMessage = null;
      this.selectedNameError = false;
    },
    selectedDays(){
      this.alertMessage = null;
      this.selectedDaysError = false;
    },
    selectedWorkHours(){
      this.alertMessage = null;
      this.selectedWorkHoursError = false;
    },
    selectedTimeout(){
      this.alertMessage = null;
      this.selectedTimeoutError = false;
    },
    chips(){
      this.alertMessage = null;
      this.chipsError = false;
    },
    value(){
      this.alertMessage = null;
      this.PhoneError = false;
    },
    selectedBusiness(){
      this.alertMessage = null;
      this.selectedBusinessError = false;
    },
  },
  methods: {
    deleteChip(chip){
      let indexToRemove = this.chips.indexOf(chip);
      if (indexToRemove !== -1) {
        this.chips.splice(indexToRemove, 1);
      }
    },

    handleImageUpload(event) {
      const files = event.target.files;
      for (let i = 0; i < files.length; i++) {
        const reader = new FileReader();
        reader.onload = (e) => {
          const imageURL = e.target.result;
          const fileName = files[i].name;
          const fileFormat = fileName.split('.').pop(); // Получаем расширение файла
          this.uploadedImages.push({ name: fileName, format: fileFormat, url: imageURL });
        };
        reader.readAsDataURL(files[i]);
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
      return this.selectedDays.includes(day);
    },
    toggleBtn(day) {
      if (this.isBtnActive(day)) {
        this.selectedDays = this.selectedDays.filter(activeDay => activeDay !== day);
      } else {
        this.selectedDays.push(day);
      }
    },
    onContinueButtonClick() {
      console.log(this.value, this.selectedCountry, this.selectedCity, this.selectedAdress , this.selectedName)
      if (this.value.length < 3 || !this.selectedCountry.length || !this.selectedCity.length || !this.selectedAdress || !this.selectedName|| !this.selectedDays.length) {
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Пожалуйста, заполните выделенные поля';
          this.alertColor = '#F97F7F';
        }, 100);

        if (!this.selectedCountry.length) {
          this.selectedCountryError = true;
        }else{
          this.selectedCountryError = false;
        }

        if (!this.selectedCity.length) {
          this.selectedCityError = true;
        }else{
          this.selectedCityError = false;
        }

        if (!this.selectedAdress) {
          this.selectedAdressError = true;
        }else{
          this.selectedAdressError = false;
        }

        if (!this.selectedName) {
          this.selectedNameError = true;
        }else{
          this.sselectedNameError = false;
        }     
        
        if (this.selectedDays.length === 0) {
              this.selectedDaysError = true;
        }else{
              this.selectedDaysError = false;
        }

        if (this.value.length < 3) {
          this.PhoneError = true;
        }else{
          this.PhoneError = false;
        }

      } else {
        if (!this.isContinueDisabled) {
          this.showContinueButtonClicked = true;
        }
      }

    },
    onBackClick() {
      this.showContinueButtonClicked = false;
    },

    Finish() {
      // Создаем объект FormData
      const formData = new FormData();
    
      var ids = []
      for(let i=0;i<this.chips.length;i++){
        ids.push(this.chips[i].id);
      }
      var choices = []
      for(let i=0;i<this.selectedChoices.length;i++){
        choices.push(this.selectedChoices[i].id);
      }
      if (!this.selectedWorkHours.length || !this.selectedTimeout.length || this.chips.length === 1 || !this.selectedBusiness.length) {
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Пожалуйста, заполните выделенные поля';
          this.alertColor = '#F97F7F';
        }, 100);

        if (!this.selectedWorkHours.length) {
          this.selectedWorkHoursError = true;
        }else{
          this.selectedWorkHoursError = false;
        }
        if (!this.selectedTimeout.length) {
          this.selectedTimeoutError = true;
        }else{
          this.selectedTimeoutError = false;
        }
        if (this.chips.length === 1) {
          this.chipsError = true;
        }else{
          this.chipsError = false;
        }

        if (!this.selectedBusiness.length) {
          this.selectedBusinessError = true;
        }else{
          this.selectedBusinessError = false;
        }
      } else{
        formData.append('country', this.selectedCountry);
        formData.append('city', this.selectedCity);
        formData.append('address', this.selectedAdress);
        formData.append('name', this.selectedName);
        formData.append('active_days', this.selectedDays);
        formData.append('work_hours', this.selectedWorkHours);
        formData.append('timeout', this.selectedTimeout);
        formData.append('choices', ids); // Преобразуем массив в строку JSON
        formData.append('business', this.selectedBusiness);
        formData.append('chips', choices);
        formData.append('user_id', this.$store.state.registrationData.user_id)
        formData.append('phone', this.selectedPhone)
        formData.append('project', this.$store.state.activeProjectId)
        // Добавляем каждое изображение в FormData
        for (let i = 0; i < this.uploadedImages.length; i++) {
          // Преобразовываем изображение в объект типа File
          const file = this.dataURItoBlob(this.uploadedImages[i].url);
          formData.append('images[]', file, this.uploadedImages[i].name); // Передаем файл, его имя и формат
        }
      
        console.log(formData);
        // Отправка данных на сервер для создания филиала
        axios.post('http://127.0.0.1:8000/api/createbranch/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data' // Указываем тип содержимого как multipart/form-data
          }
        })
          .then(response => {
          this.alertMessage = 'Настройки успешно сохранены'
          this.alertColor = '#0BB6A1'
          console.log(response)
          if(response.data.answer){
          this.first = response.data.answer
          }else{
          setTimeout(() => {
            this.$router.go(-1);
          }, 2000)}
          })
          .catch(error => {
            console.error('Ошибка при отправке данных филиала:', error);
          });
      }      
      
},

// Метод для преобразования Data URI в Blob объект
dataURItoBlob(dataURI) {
  const byteString = atob(dataURI.split(',')[1]);
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  return new Blob([ab], { type: 'image/jpeg' }); // Укажите нужный MIME тип, если изображения не JPEG
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
.PhoneError{
  border: 1px solid #F97F7F !important;
  border-radius: 3px;
}
.button-days-error{
  border: 1px solid #F97F7F !important;
  border-radius: 3px;
}
.select-error >>> .selected{
  border: solid 1px #F97F7F !important;
}
.input-error {
  border: 1px solid #F97F7F !important;
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
  .create_branch {
    width: 600px;
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
    font-size: 13px;
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
    background-image: url(../../static/img/paperclip.svg);
    background-repeat: no-repeat;
    background-position: calc(100% - 15px) center;
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
    flex-wrap: wrap;
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
    object-fit: cover;
  }
  .graffic_label{
    margin: 0;
  }
  .graffic{
    display: flex;
    flex-direction: column;
    gap: 5px;
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
  input:focus {
    outline: none;
    border: 1px solid #6266EA;
  }
  .second-steps-container{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  @media (max-width: 1280px){
    .create_branch{
      width: 100%;
    }
  }
  @media (max-width: 768px){
    .main{
      margin: 20px;
    }
    .days{
      flex-wrap: wrap;
    }
  }
  @media (max-width: 568px){
    .main{
      height: 89vh;
      overflow: scroll;
    }
    .employesss-link{
      font-size: 16px;
    }
    .creation_text{
      font-size: 16px;
    }
    .one-group{
      flex-direction: column;
    }
    .form-btn{
      flex-direction: column;
      gap: 10px;
    }
    .steps-progress{
      justify-content: flex-start;
    }
    .divider{
      margin: 10px 0;
    }
    .btn{
      width: 100%;
    }
    .steps{
      flex-direction: column;
      gap: 10px;
    }
    .btn-container{
      flex-direction: column;
      margin: 0;
      width: 100%;
    }
  }
</style>