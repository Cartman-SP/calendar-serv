<template>
  <div class="main">
    <div class="create_service">
      <div class="transition">
        <a href="#/main/service" class="services-link">Услуги</a>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <p class="creation_text">Создание услуг</p>
      </div>

      <!-- 1. Название услуги -->
      <label for="serviceName">Название услуги</label>
      <input type="text" id="serviceName" v-model="serviceName" placeholder="Новая услуга">

      <!-- 2. Стоимость, Длительность -->
      <div class="cost-duration-container">
        <div class="input-group">
          <label for="serviceCost">Стоимость</label>
          <input type="number" id="serviceCost" v-model="serviceCost" placeholder="Введите стоимость">
        </div>

        <div class="input-group">
          <label for="serviceDuration">Длительность</label>
          <select id="serviceDuration" v-model="serviceDuration" placeholder="Выберите время">
            <option value="15m">15м</option>
            <option value="30m">30м</option>
            <option value="45m">45м</option>
            <option value="60m">60м</option>
          </select>
        </div>
      </div>

      <!-- 3. Обложка услуги -->
      <label for="serviceCover" class="file-label">Обложка услуги</label>
      <div class="file-input-container" :style="{ background: uploadedFile ? `url(${uploadedFile}) center/cover no-repeat` : '#F3F5F6' }">
        <input type="file" id="serviceCover" accept=".png, .jpg, .jpeg" capture="environment" @change="handleFileChange">
        <label for="serviceCover" class="placeholder-text subtext">Нажмите, чтобы добавить</label>
      </div>
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
      <label for="paymentFormat">Формат оплаты</label>
      <div class="record-type-container">
        <!-- Добавлены условия для индивидуальной записи -->
        <button
          :class="{ 'active': selectedPaymentFormat === 'sessionPayment' }"
          @click="selectPaymentFormat('sessionPayment')"
          class="record-button"
        >
          Оплата за сеанс
        </button>
        <button
          :class="{ 'active': selectedPaymentFormat === 'equipmentPayment' }"
          @click="selectPaymentFormat('equipmentPayment')"
          class="record-button"
        >
          Оплата за оборудование
        </button>
        <!-- ... (другие кнопки) -->
      </div>

      <!-- 7. Кнопки -->
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
import axios from 'axios';
import NavbarPage from './NavbarPage.vue';
import SidebarPage from './SidebarPage.vue';

export default {
  components: { NavbarPage, SidebarPage },
  data() {
    return {
      serviceName: '',
      serviceCost: 0,
      serviceDuration: '',
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
      const formData = new FormData();

      // Добавляем поля данных
      formData.append('user_id', this.$store.getters.getRegistrationData.user_id);
      formData.append('name', this.serviceName);
      formData.append('cost', parseFloat(this.serviceCost));
      formData.append('duration', this.serviceDuration);
      formData.append('record_type', this.selectedRecordType);
      formData.append('payment_type', this.selectedPaymentFormat);

      // Добавляем изображение, если оно было загружено
      if (this.uploadedFile) {
        const blob = this.dataURItoBlob(this.uploadedFile);
        formData.append('cover', blob, 'cover.png');
      }

      // Отправляем запрос
      axios.post('http://127.0.0.1:8000/api/create_service/', formData)
        .then(response => {
          console.log(response.data);
          // Обработка успешного ответа, например, переход на другую страницу
        })
        .catch(error => {
          console.error('Ошибка при отправке данных:', error);
        });
    },

    cancel() {
      this.$router.go(-1);
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.uploadedFile = e.target.result;
        };
        reader.readAsDataURL(file);
      }
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
    dataURItoBlob(dataURI) {
      const [type, data] = dataURI.split(',');
      const byteString = atob(data);
      const buffer = new ArrayBuffer(byteString.length);
      const array = new Uint8Array(buffer);
      for (let i = 0; i < byteString.length; i++) {
        array[i] = byteString.charCodeAt(i);
      }
      return new Blob([buffer], { type: type });
    },
  },
};
</script>



<style scoped>

.group-buttons{
  display: flex;
  flex-direction: row;
  justify-content: left;
  gap: 10px;
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
.transition{
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 50px;
}
.services-link{
  font-family: TT Norms;
  font-size: 20px;
  font-weight: 500;
  line-height: 24px;
  text-align: left;
  text-decoration: none;
  color: #AFB6C1;
}
.creation_text{
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

.create_service {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 488px;
  height: 439px;
  color: #FFFFFF;
}

.cost-duration-container {
  display: flex;
  gap: 20px; /* Расстояние между элементами */
  align-items: center; /* Выравнивание по центру по вертикали */
}

.input-group {
  display: flex;
  flex-direction: column;
}

.file-input-container {
  position: relative;
  width: 100%;
  height: 36px;
  padding-left: 10px;
  display: flex;
  align-items: center;
  justify-content: left;
  text-align: left;
  background-color: #F3F5F6;
}

.file-input-container label {
  cursor: pointer;
  z-index: 2;
  font-size: 16px;
  color: #AFB6C1;
}

.file-input-container p {
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
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

.placeholder-text {
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  text-align: left;
  color: #AFB6C1;
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
  gap: 20px; /* Расстояние между элементами */
  align-items: center; /* Выравнивание по центру по вертикали */
}

.record-button {
  padding: 8px 12px;
  font-size: 14px;
  background-color: #F3F5F6;
  color: #D2D8DE;
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
  border: 1px solid #DDE1E5
}

.subtext{
  margin: 0;
}
</style>
