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
        <label for="serviceName">Название услуги</label>
        <input type="text" id="serviceName" placeholder="Новая услуга" v-model="serviceName" :class="{ 'input-error': serviceNameError }">
  
        <!-- 2. Стоимость, Длительность -->
        <div class="cost-duration-container">
          <div class="input-group">
            <label for="serviceCost">Стоимость</label>
            <input type="number" id="serviceCost" placeholder="Введите стоимость" v-model="serviceCost" :class="{ 'input-error': serviceCostError }">
          </div>
  
          <div class="input-group">
            <label for="serviceDuration">Длительность</label>
            <select id="serviceDuration" placeholder="Выберите время" v-model="serviceDuration">
              <option value="" disabled selected style="display:none;">Выберите время</option>
              <option value="15m">15м</option>
              <option value="30m">30м</option>
              <option value="45m">45м</option>
              <option value="60m">60м</option>
            </select>
          </div>
        </div>
  
        <!-- 3. Обложка услуги -->
        <label for="serviceCover" class="file-label">Обложка услуги</label>
        <label class="custom-file-upload">
          <input type="file" accept="image/*" @change="handleFileUpload($event)"/>Нажмите, чтобы добавить
        </label>
        <p class="text">до 5 МБ, PNG, JPG, JPEG</p>
  
        <!-- 4. Тип индивидуальности -->
        <label for="recordType">Тип записи</label>
        <div class="record-type-container">
          <button
            :class="{ 'active': selectedRecordType === 'individual' }"
            @click="selectRecordType('individual')"
            class="record-button"
          >
            Индивидуальная
          </button>
          <button
            :class="{ 'active': selectedRecordType === 'group' }"
            @click="selectRecordType('group')"
            class="record-button"
          >
            Групповая
          </button>
          <button
            :class="{ 'active': selectedRecordType === 'rental' }"
            @click="selectRecordType('rental')"
            class="record-button"
          >
            Аренда
          </button>
        </div>
  
        <!-- 5. Групповые параметры -->
        <div v-if="selectedRecordType === 'group'" class="group-parameters">
          <label for="groupCapacity">Количество мест</label>
          <div class="group-buttons">
            <div class="group-counter">
              <button @click="decreaseGroupCapacity">-</button>
              <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
              <input type="text" v-else placeholder="" :value="groupCapacity">
              <button @click="increaseGroupCapacity">+</button>
            </div>
            <div class="group-counter">
              <button @click="decreaseMaxGroupCapacity">-</button>
              <input type="text" v-if="maxGroupCapacity === 0" placeholder="До" :value="''">
              <input type="text" v-else placeholder="" :value="maxGroupCapacity">
              <button @click="increaseMaxGroupCapacity">+</button>
            </div>
          </div>
        </div>
  
        <!-- 6. Групповые параметры для аренды -->
        <div v-if="selectedRecordType === 'rental'" class="group-parameters">
          <label for="groupCapacity">Количество единиц для аренды</label>
          <div class="group-buttons">
            <div class="group-counter">
              <button @click="decreaseGroupCapacity">-</button>
              <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
              <input type="text" v-else placeholder="" :value="groupCapacity">
              <button @click="increaseGroupCapacity">+</button>
            </div>
            <div class="group-counter">
              <button @click="decreaseMaxGroupCapacity">-</button>
              <input type="text" v-if="maxGroupCapacity === 0" placeholder="До" :value="''">
              <input type="text" v-else placeholder="" :value="maxGroupCapacity">
              <button @click="increaseMaxGroupCapacity">+</button>
            </div>
          </div>
        </div>      
  
        <!-- 7. Формат оплаты -->
        <label for="paymentFormat" v-if="selectedRecordType !== ''">Формат оплаты</label>
        <div class="record-type-container" v-if="selectedRecordType !== ''">
          <!-- Добавлены условия для всех типов записи -->
          <button
            v-if="selectedRecordType === 'individual'"
            :class="{ 'active': selectedPaymentFormat === 'sessionPayment' }"
            @click="selectPaymentFormat('sessionPayment','Оплата за сеанс')"
            class="record-button"
          >
            Оплата за сеанс
          </button>
          <button
            v-if="selectedRecordType === 'individual'"
            :class="{ 'active': selectedPaymentFormat === 'spotPayment' }"
            @click="selectPaymentFormat('spotPayment','Оплата за место')"
            class="record-button"
          >
            Оплата за место
          </button>
          <button
            v-if="selectedRecordType === 'individual'"
            :class="{ 'active': selectedPaymentFormat === 'freePayment' }"
            @click="selectPaymentFormat('freePayment','Без стоимости')"
            class="record-button"
          >
            Без стоимости
          </button>
          <!-- Добавлены условия для групповой и аренды -->
          <button
            v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
            :class="{ 'active': selectedPaymentFormat === 'equipmentPayment' }"
            @click="selectPaymentFormat('equipmentPayment','Оплата за время и единицу оборудования')"
            class="record-button"
          >
            Оплата за время и единицу оборудования
          </button>
          <button
            v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
            :class="{ 'active': selectedPaymentFormat === 'freePayment' }"
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
      <div class="adaptive_window">
        <img src="../../static/img/service.png" alt="" style="width:auto;height:200px;border-radius:2px;  ">
        <div>
          <p class="header">Стрижка</p>
          <p class="descr">Название услуги</p>
        </div>
        <div class="first">
          <div class="stripe" style="width: 143px;"></div>
          <div class="stripe" style="width: 97px;"></div>
        </div>
        <div class="first">
          <div class="stripe" style="width: 143px;"></div>
          <div class="stripe" style="width: 97px;"></div>
        </div>
        <div class="second">
          <div class="stripe" style="width: 109px;"></div>
          <div class="stripe" style="width: 63px;"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedRecordType: '',
      selectedPaymentFormat: '',
      groupCapacity: 0,
      maxGroupCapacity: 0,
      serviceName: '',
      serviceNameError: false,
      serviceCost: '',
      serviceCostError: false,
      serviceDuration: '',
      serviceCover: null,
      paymentFormat: '',
      selectedPaymentText: '',
    };
  },
  methods: {
    selectRecordType(type) {
      this.selectedRecordType = type;
      this.selectedPaymentFormat = '';
    },
    selectPaymentFormat(format, text) {
      this.selectedPaymentFormat = format;
      this.selectedPaymentText = text;
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      this.serviceCover = file;
    },
    saveAndExit() {
      if (!this.serviceName.trim()) {
        this.serviceNameError = true;
        return;
      }
      this.serviceNameError = false;

      if (typeof this.serviceCost === 'string' && this.serviceCost.trim() === '') {
          this.serviceCostError = true;
          return;
      }
      this.serviceCostError = false;

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
.main_group{
  display: flex;
  gap: 40px;
}
.adaptive_window{
  background-color: #FFFFFF;
  width: 49vh;
  height: auto;
  padding: 20px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.header{
  font-family: TT Norms;
  font-size: 22px;
  font-weight: 500;
  line-height: 22px;
  text-align: left;
  color: #535C69;
  margin: 20px 0 0 0;
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
.descr{
  color: #AFB6C1;
  font-family: TT Norms;
  font-size: 16px;
  font-weight: 500;
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
  height: 36px;
  background-color: #FFFFFF;
  color: #6266EA;
  border: none;
  cursor: pointer;
}
.group-counter{
  display: flex;
  color: #535C69;
  align-items: center;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
}
.group-counter p{
  padding: 0 20px;
}
.group-counter input {
  background-color: #FFFFFF;
  text-align: center;
  width: 55px;
  margin: 0;
}

.create_service {
  width: 110vh;
  height: 60vh;
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
  width: 48%;
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
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
}
.record-type-container {
  display: flex;
  gap: 20px;
  align-items: center;
  margin-bottom: 10px;
}

.record-button {
  padding: 8px 12px;
  font-size: 14px;
  background-color: #F3F5F6;
  color: #AFB6C1;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s; /* Добавлено плавное переходное свойство */
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
  border: 1px solid #DDE1E5
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
select {
  padding: 8px 10px;
  font-family: TT Norms;
  font-size: 14px;
  line-height: 20px;
  color: #D2D8DE;
  border: none;
  background-color: #F3F5F6;
  margin-bottom: 10px;
  border-radius: 3px;
  height: 36px;
}

select option {
  font-family: TT Norms;
  font-size: 14px;
  font-weight: bold;
  line-height: 20px;
  color: #535C69;
}
label{
  font-weight: bold;
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
.input-error {
  border: 1px solid #F97F7F !important;
}
</style>
