<template>
  <div class="main">
    <div class="transition">
      <router-link to="/lk/service" class="employesss-link">Услуги</router-link>
      <div class="arrow-container">
        <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
      </div>
      <p class="creation_text">Создание услуги</p>
    </div>
    <div class="main_group">

      <div class="create_service">
        <!-- 1. Название услуги -->
        <div>
          <label for="serviceName">Название услуги</label>
          <input type="text" id="serviceName" placeholder="Новая услуга" v-model="serviceName" :class="{ 'input-error': serviceNameError }">
        </div>
  
        <!-- 2. Стоимость, Длительность -->
        <div class="cost-duration-container">
          <div class="input-group">
            <label for="serviceCost">Стоимость</label>
            <input type="number" appearance-none id="serviceCost" placeholder="Введите стоимость" v-model="serviceCost" :class="{ 'input-error': serviceCostError }">
          </div>
  
          <div class="input-group">
            <label for="serviceDuration">Длительность</label>
            <SelectPage
            :options="['15 минут', '30 минут', '45 минут', '1 час','1 час 30 минут','2 часа','2 часа 30 минут']"
            class="select" @input="option => serviceDuration = option"
            :placeholderdata="'Выберите время'"
            :class="{ 'select-error': serviceDurationError }"
          />
          </div>
        </div>
  
        <!-- 3. Обложка услуги -->
        <div>
          <label for="serviceCover" class="file-label">Обложка услуги</label>
            <label class="custom-file-upload" :class="{'custom-file-upload-error' : serviceCoverError}">
              <input type="file" accept="image/*" @change="handleFileUpload($event)"/>Нажмите, чтобы добавить
            </label>
          <p class="text">до 5 МБ, PNG, JPG, JPEG</p>
        </div>
  
        <!-- 4. Тип индивидуальности -->
        <div>
          
          <div class="usluga-head">
            <label for="recordType">Тип записи</label>
            <Tip :Tip="'Индивидуальная запись <span> — сеанс бронируется одним клиентом или группой людей. Например, для записи к врачу или салон красоты, для бронирования квеста или других развлечений. </span> \n \n Групповая запись <span> — запись нескольких клиентов на один и тот же сеанс. Он остается доступным до тех пор, пока есть свободные места. Например, для записи на занятия фитнесом, йогой или для продажи билетов на мероприятия</span> \n \n Аренда <span> — клиент может выбрать любой доступный период почасовой илипоминутной аренды, а так же количество единиц оборудования, если требуется. Например для сдачи в аренду помещений, спортивного и развлекательного инвентаря, для записи в киберспортивные клубы. </span>'"/>
          </div>
          <div class="record-type-container">
            <button
              :class="{ 'active': selectedRecordType === 'individual', 'button-error': selectedRecordTypeError }"
              @click="selectRecordType('individual','Индивидуальная')"
              class="record-button"
            >
              Индивидуальная
            </button>
            <button
              :class="{ 'active': selectedRecordType === 'group', 'button-error': selectedRecordTypeError  }"
              @click="selectRecordType('group','Групповая')"
              class="record-button"
            >
              Групповая
            </button>
            <button
              :class="{ 'active': selectedRecordType === 'rental', 'button-error': selectedRecordTypeError  }"
              @click="selectRecordType('rental','Аренда')"
              class="record-button"
            >
              Аренда
            </button>
          </div>
    
          <!-- 5. Групповые параметры -->
          <div v-if="selectedRecordType === 'group'" class="group-parameters">
            <div class="usluga-head" v-if="selectedRecordType !== ''">
              <label for="groupCapacity">Количество мест</label>
              <Tip :Tip="'Выберите минимальное и максимальное количество мест, <br> которое соответствует вашей услуге'"/>
            </div>
            <div class="group-buttons">
              <div class="group-counter" :class="{'group-counter-error': GroupCapacityError}">
                <button @click="decreaseGroupCapacity" id="decrease">-</button>
                <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
                <input type="text" v-else placeholder="" :value="groupCapacity">
                <button @click="increaseGroupCapacity" id="increase">+</button>
              </div>
              <div class="group-counter" :class="{'group-counter-error': MaxGroupCapacityError}">
                <button @click="decreaseMaxGroupCapacity" id="decrease">-</button>
                <input type="text" v-if="maxGroupCapacity === 0" placeholder="До" :value="''">
                <input type="text" v-else placeholder="" :value="maxGroupCapacity">
                <button @click="increaseMaxGroupCapacity" id="increase">+</button>
              </div>
            </div>
          </div>
    
          <!-- 6. Групповые параметры для аренды -->
          <div v-if="selectedRecordType === 'rental'" class="group-parameters">
            <div class="usluga-head" v-if="selectedRecordType !== ''">
              <label for="groupCapacity">Количество единиц для аренды</label>
              <Tip :Tip="'Придумать описание, а, вообще, даня, верни 5к'"/>
            </div>
            <div class="group-buttons">
              <div class="group-counter" :class="{'group-counter-error': GroupCapacityError}">
                <button @click="decreaseGroupCapacity">-</button>
                <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
                <input type="text" v-else placeholder="" :value="groupCapacity">
                <button @click="increaseGroupCapacity">+</button>
              </div>
              <div class="group-counter" :class="{'group-counter-error': MaxGroupCapacityError}">
                <button @click="decreaseMaxGroupCapacity">-</button>
                <input type="text" v-if="maxGroupCapacity === 0" placeholder="До" :value="''">
                <input type="text" v-else placeholder="" :value="maxGroupCapacity">
                <button @click="increaseMaxGroupCapacity">+</button>
              </div>
            </div>
          </div>      
    
          <!-- 7. Формат оплаты -->
          <div class="usluga-head" v-if="selectedRecordType !== ''">
            <label>Формат оплаты</label>
            <Tip v-if="selectedRecordType === 'individual'" :Tip="'Оплата за сеанс <span> — стоимость услуги формируется за сеанс, независимо от количества выбранных мест. Доступна настройка оплаты за дополнительные места.</span> \n\n Оплата за место <span> — стоимость услуни формируется в зависимости от количества выбранных мест.</span> \n\n Аренда — <span> стоимость не отображается. Подойдет, если услуга бесплатная, или конечнаяили конечная стоимость формируется на месте.</span>'"/>
            <Tip v-if="selectedRecordType === 'group'" :Tip="'Оплата за время и единицу оборудования <span> — стоимость аренды формирутеся от выбранного периода и количества едениц оборудования.</span> \n\n Без стоимости <span> — стоимость не отображается. Подойдет, если услуга бесплатная, или конечная стоимость формируется на места</span>'"/>
            <Tip v-if="selectedRecordType === 'rental'" :Tip="'Оплата за время и единицу оборудования <span> — стоимость аренды формирутеся от выбранного периода и количества едениц оборудования.</span> \n\n Без стоимости <span> — стоимость не отображается. Подойдет, если услуга бесплатная, или конечная стоимость формируется на места</span>'"/>
            </div>
          <div class="record-type-container" v-if="selectedRecordType !== ''">
            <!-- Добавлены условия для всех типов записи -->
            <button
              v-if="selectedRecordType === 'individual'"
              :class="{ 'active': selectedPaymentFormat === 'sessionPayment', 'button-error': selectedPaymentFormatError }"
              @click="selectPaymentFormat('sessionPayment','Оплата за сеанс')"
              class="record-button"
            >
              Оплата за сеанс
            </button>
            <button
              v-if="selectedRecordType === 'individual'"
              :class="{ 'active': selectedPaymentFormat === 'spotPayment', 'button-error': selectedPaymentFormatError }"
              @click="selectPaymentFormat('spotPayment','Оплата за место')"
              class="record-button"
            >
              Оплата за место
            </button>
            <button
              v-if="selectedRecordType === 'individual'"
              :class="{ 'active': selectedPaymentFormat === 'freePayment', 'button-error': selectedPaymentFormatError }"
              @click="selectPaymentFormat('freePayment','Без стоимости')"
              class="record-button"
            >
              Без стоимости
            </button>
            <!-- Добавлены условия для групповой и аренды -->
            <button
              v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
              :class="{ 'active': selectedPaymentFormat === 'equipmentPayment', 'button-error': selectedPaymentFormatError }"
              @click="selectPaymentFormat('equipmentPayment','Оплата за время и единицу оборудования')"
              class="record-button"
            >
              Оплата за время и единицу оборудования
            </button>
            <button
              v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
              :class="{ 'active': selectedPaymentFormat === 'freePayment', 'button-error': selectedPaymentFormatError }"
              @click="selectPaymentFormat('freePayment','Без стоимости')"
              class="record-button"
            >
              Без стоимости
            </button>
          </div>
    
          <!-- 8. Кнопки -->
          <div class="button-container">
            <button @click="saveAndExit" class="save-and-exit-button">Сохранить и выйти</button>
            <button @click="cancel" class="cancel-button">Отмена</button>
          </div>
        </div>
      </div>
      <div class="adaptive_window">
        <img v-if="serviceCover" :src="coverDataUrl" alt="" style="width:auto;height:200px;border-radius:2px;">
        <div class="img_container" v-else>
          <img class="img_window"  src="../../static/img/service.svg" alt="">
        </div>
        <div v-if="serviceName">
          <p class="header">{{serviceName}}</p>
          <p class="descr">Название услуги</p>
        </div>
        <div v-else class="first">
          <div class="stripe" style="width: 143px;"></div>
          <div class="stripe" style="width: 97px;"></div>
        </div>
        <div v-if="serviceDuration.length > 0" >
          <p class="header">{{serviceDuration}}</p>
          <p class="descr">Длительность</p>
        </div>
        <div v-else class="first">
          <div class="stripe" style="width: 143px;"></div>
          <div class="stripe" style="width: 97px;"></div>
        </div>
        <div v-if="selectedRecordText">
          <p class="header">{{selectedRecordText}}</p>
          <p class="descr">Тип записи</p>
        </div>
        <div v-else class="first">
          <div class="stripe" style="width: 143px;"></div>
          <div class="stripe" style="width: 97px;"></div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center">
          <div v-if="selectedPaymentText">
            <p class="header">{{selectedPaymentText}}</p>
            <p class="descr">Формат оплаты</p>
          </div>
          <div v-else class="second">
            <div class="stripe" style="width: 109px;"></div>
            <div class="stripe" style="width: 63px;"></div>
          </div>
          <div v-if="serviceCost">
            <p class="header">{{serviceCost}} {{ costsign }}</p>
          </div>
          <div v-else class="third">
            <div class="circle"></div>
          </div>
        </div>
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

export default {
  components: { Tip, SelectPage, MessageAlert },
  data() {
    return {
      alertMessage: null,
      alertColor: '',

      selectedRecordType: '',
      selectedRecordTypeError: false,

      selectedPaymentFormat: '',
      selectedPaymentFormatError: false,

      groupCapacity: 0,
      maxGroupCapacity: 0,

      serviceName: '',
      serviceNameError: false,

      serviceCost: '',
      serviceCostError: false,

      serviceDuration: '',
      serviceDurationError: false,

      serviceCover: null,
      serviceCoverError: false,

      selectedPaymentText: '',
      selectedPaymentTextError: false,

      coverDataUrl: null,
      selectedRecordText: '',
      costsign: '₽',

      GroupCapacityError: false,
      MaxGroupCapacityError: false,
    };
  },
  watch: {
    serviceName() {
      this.alertMessage = null;
      this.serviceNameError = false;
    },
    serviceCost() {
      this.alertMessage = null;
      this.serviceCostError = false;
    },
    serviceDuration() {
      this.alertMessage = null;
      this.serviceDurationError = false;
    },
    serviceCover(){
      this.alertMessage = null;
      this.serviceCoverError = false;
    },
    selectedPaymentFormat() {
      this.alertMessage = null;
      this.selectedPaymentFormatError = false;
    },
    selectedRecordType() {
      this.alertMessage = null;
      this.selectedRecordTypeError = false;
    },
    groupCapacity(){
      this.alertMessage = null;
      this.GroupCapacityError = false;
    },
    maxGroupCapacity(){
      this.alertMessage = null;
      this.MaxGroupCapacityError = false;
    },
  },
  methods: {
    selectRecordType(type,text) {
      this.selectedRecordType = type;
      this.selectedRecordText = text;
      this.selectedPaymentFormat = '';
      this.selectedPaymentText = '';
    },
    selectPaymentFormat(format, text) {
      this.selectedPaymentFormat = format;
      this.selectedPaymentText = text;
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      this.serviceCover = file;
      this.readCoverDataUrl();
    },
    readCoverDataUrl() {
      if (!this.serviceCover) return;
      const reader = new FileReader();
      reader.onload = (e) => {
        this.coverDataUrl = e.target.result;
      };
      reader.readAsDataURL(this.serviceCover);
    },
    saveAndExit() {
      if (!this.groupCapacity || !this.maxGroupCapacity || !this.serviceName || !this.serviceCost || !this.serviceDuration || !this.selectedPaymentFormat || !this.selectedRecordText || !this.serviceCover) {
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Пожалуйста, заполните выделенные поля';
        this.alertColor = '#F97F7F';
        }, 100);

        if (!this.serviceName) {
          this.serviceNameError = true;
        }else{
          this.serviceNameError = false;
        }
        if (!this.serviceCost.toString()) {
          this.serviceCostError = true;
        }else{
          this.serviceCostError = false;
        }
        if (!this.serviceDuration.length) {
          this.serviceDurationError = true;
        }else{
          this.serviceDurationError = false;
        }
        if (!this.selectedRecordType) {
          this.selectedRecordTypeError = true;
        }else{
          this.selectedRecordTypeError = false;
        }
        if (!this.selectedPaymentFormat) {
          this.selectedPaymentFormatError = true;
        }else{
          this.selectedPaymentFormatError = false;
        }
        if (!this.serviceCover) {
          this.serviceCoverError = true;
        }else{
          this.serviceCoverError = false;
        }
        if (!this.groupCapacity) {
          this.GroupCapacityError = true;
        }else{
          this.GroupCapacityError = false;
        }
        if (!this.maxGroupCapacity) {
          this.MaxGroupCapacityError = true;
        }else{
          this.MaxGroupCapacityError = false;
        }
      }

      const formData = new FormData();
      formData.append('name', this.serviceName);
      formData.append('cost', this.serviceCost);
      formData.append('time', this.serviceDuration);
      formData.append('type', this.selectedRecordType);
      formData.append('place_ammount', this.groupCapacity);
      formData.append('rent_ammount', this.maxGroupCapacity);
      formData.append('pay_type', this.selectedPaymentText);
      formData.append('user', this.$store.state.registrationData.user_id);
      formData.append('serviceCover', this.serviceCover);

      axios.post('http://127.0.0.1:8000/api/uslugi/', formData)
        .then(response => {
          console.log('Service created:', response.data);
          this.alertMessage = 'Настройки успешно сохранены'
          this.alertColor = '#0BB6A1'
          setTimeout(() => {
            this.$router.go(-1);
          }, 2000)
        })
        .catch(error => {
          console.error('Error creating service:', error);
        });
    },
    cancel() {
      this.$router.go(-1);
    },
    decreaseGroupCapacity() {
      if (this.groupCapacity > 0) {
        this.groupCapacity--;
      }
    },
    increaseGroupCapacity() {
      this.groupCapacity++;
    },
    decreaseMaxGroupCapacity() {
      if (this.maxGroupCapacity > 0) {
        this.maxGroupCapacity--;
      }
    },
    increaseMaxGroupCapacity() {
      this.maxGroupCapacity++;
    },
  },
};

</script>


<style scoped>
.main{
  overflow: hidden;
}
.button-error{
  border: solid 1px #F97F7F !important;
}
.select-error >>> .selected{
  border: solid 1px #F97F7F !important;
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
.main_group{
  display: flex;
  gap: 40px;
}
.adaptive_window{
  background-color: #FFFFFF;
  width: 400px;
  height: auto;
  padding: 20px;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.header{
  font-family: 'TT Norms Medium';
  font-size: 22px;
  line-height: 22px;
  text-align: left;
  color: #535C69;
  margin: 0;
}
.first{
  width: 220px;
  height: 50px;
  border-radius: 2px;
  background: linear-gradient(90deg, #F6F6F6 0%, #F1F4F9 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 10px;
}
.stripe {
  height: 10px;
  background: linear-gradient(90deg, #EBEBEB 0%, #DAE2EE 100%);
  border-radius: 2px;
}
.second{
  width: 155px;
  height: 50px;
  border-radius: 2px;
  background: linear-gradient(90deg, #F6F6F6 0%, #F1F4F9 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 10px;
  padding: 10px;
}
.third{
  width: 92px;
  height: 36px;
  border-radius: 2px;
  background: linear-gradient(90deg, #F6F6F6 0%, #F1F4F9 100%);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding: 10px;
}
.circle{
  width: 16px;
  height: 16px;
  background: #E7ECF6;
  border-radius: 100px;
}
.descr{
  color: #AFB6C1;
  font-family: 'TT Norms Medium';
  font-size: 16px;
  line-height: 19px;
  text-align: left;
  margin: 5px 0 0 0;
}
.group-buttons{
  display: flex;
  flex-direction: row;
  justify-content: left;
  gap: 10px;
  margin-bottom: 10px;
}
.group-buttons button {
  border-radius: 0;
  width: 40px;
  height: 36px;
  font-size: 25px;
  font-family: 'TT Norms Light';
  background-color: #FFFFFF;
  color: #6266EA;
  cursor: pointer;
}

#decrease{
  border-radius: 3px 0 0 3px;
  border: solid 1px #C6CBD2;
  transition: all .2s ease;
}

#increase{
  border-radius: 0 3px 3px 0;
  border: solid 1px #C6CBD2;
  transition: all .2s ease;
}

#increase:hover, #decrease:hover{
  border: solid 1px #7D838C;
}

#increase:active, #decrease:active{
  border: solid 1px #6266EA;
}
.group-counter{
  display: flex;
  color: #535C69;
  align-items: center;
  border-radius: 3px;
}

.group-counter-error{
  display: flex;
  color: #535C69;
  align-items: center;
  border-radius: 3px;
  border: 1px solid #F97F7F !important;
}
.group-counter p{
  padding: 0 20px;
}
.group-counter input {
  border-radius: 0;
  border: solid 1px #C6CBD2;
  background-color: #FFFFFF;
  text-align: center;
  width: 55px;
  margin: 0;
  transition: all .2s ease;
}

.group-counter input:hover{
  border: solid 1px #7D838C;
}

.group-counter input:focus{
  border: solid 1px #6266EA;
}

.create_service {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 550px;
  height: fit-content;
  background-color: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
}

.cost-duration-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.input-group {
  display: flex;
  flex-direction: column;
  width: 49%;
}

#serviceCover {
  width: 0;
  height: 0;
  opacity: 0;
  position: absolute;
  z-index: -1;
}

.file-label {
  cursor: pointer;
}
.text {
  font-family: 'TT Norms Medium';
  font-size: 10px;
  line-height: 12px;
  letter-spacing: 0em;
  text-align: left;
  color: #D2D8DE;
}
.record-type-container {
  display: flex;
  gap: 20px;
  align-items: center;
  margin-bottom: 10px;
}

.record-button {
  font-family: 'TT Norms Medium';
  padding: 8px 12px;
  font-size: 13px;
  background-color: #F3F5F6;
  color: #D2D8DE;
  border: none;
  cursor: pointer;
  transition: background-color 0.2s, color 0.2s; /* Добавлено плавное переходное свойство */
}

.record-button:hover {
  background-color: #6266EA;
  color: #FFFFFF;
}

.record-button.active {
  background-color: #6266EA;
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
  transition: all .2s eases;
}

.cancel-button:hover{
  color: #6266EA;
}
input::placeholder {
  font-family: 'TT Norms Medium';
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
  font-weight: 500;
}

.custom-file-upload-error{
  border: 1px solid #F97F7F !important;
  border-radius: 3px;
}

.custom-file-upload input[type="file"] {
  display: none;
}
label{
  font-family: 'TT Norms Medium';
}
.transition {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 20px;
}

.employesss-link {
  font-family: 'TT Norms Medium';
  font-size: 20px;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}

.creation_text {
  color: #535C69;
  font-family: 'TT Norms Medium';
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
.input-error {
  border: 1px solid #F97F7F !important;
}
.img_window{
  width:58px;
  height:58px;
  border-radius:2px;
}
.img_container{
  align-items: center;
  max-width: 365px;
  height: 200px;
  display: flex;
  justify-content: center;
  background: linear-gradient(90deg, #F6F6F6 0%, #F1F4F9 100%);
  border-radius: 2px;
}
input{
  margin: 0;
}
</style>
