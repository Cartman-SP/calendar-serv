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
      <input type="text" id="serviceName" placeholder="Новая услуга">

      <!-- 2. Стоимость, Длительность -->
      <div class="cost-duration-container">
        <div class="input-group">
          <label for="serviceCost">Стоимость</label>
          <input type="number" id="serviceCost" placeholder="Введите стоимость">
        </div>

        <div class="input-group">
          <label for="serviceDuration">Длительность</label>
          <select id="serviceDuration" placeholder="Выберите время">
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
        <input type="file" accept="image/*"/>Нажмите, чтобы добавить
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

        <!-- Объект для кнопок "+" и "-" -->
        <div class="group-buttons">
          <div class="group-counter">
            <button @click="decreaseGroupCapacity">-</button>
            <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
            <input type="text" v-else placeholder="" :value="groupCapacity">
            <button @click="increaseGroupCapacity">+</button>
          </div>

          <!-- Объект для кнопок "+" и "-" -->
          <div class="group-counter">
            <button @click="decreaseMaxGroupCapacity">-</button>
            <input type="text" v-if="maxGroupCapacity === 0" placeholder="До" :value="''">
            <input type="text" v-else placeholder="" :value="maxGroupCapacity">
            <button @click="increaseMaxGroupCapacity">+</button>
          </div>
        </div>
      </div>

      <!-- 6. Групповые параметры -->
      <div v-if="selectedRecordType === 'rental'" class="group-parameters">
        <label for="groupCapacity">Количество единиц для аренды</label>

        <!-- Объект для кнопок "+" и "-" -->
        <div class="group-buttons">
          <div class="group-counter">
            <button @click="decreaseGroupCapacity">-</button>
            <input type="text" v-if="groupCapacity === 0" placeholder="От" :value="''">
            <input type="text" v-else placeholder="" :value="groupCapacity">
            <button @click="increaseGroupCapacity">+</button>
          </div>

          <!-- Объект для кнопок "+" и "-" -->
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
          v-if="selectedRecordType === 'individual'"
          :class="{ 'active': selectedPaymentFormat === 'sessionPayment' }"
          @click="selectPaymentFormat('sessionPayment')"
          class="record-button"
        >
          Оплата за сеанс
        </button>
        <button
          v-if="selectedRecordType === 'individual'"
          :class="{ 'active': selectedPaymentFormat === 'spotPayment' }"
          @click="selectPaymentFormat('spotPayment')"
          class="record-button"
        >
          Оплата за место
        </button>
        <button
          v-if="selectedRecordType === 'individual'"
          :class="{ 'active': selectedPaymentFormat === 'freePayment' }"
          @click="selectPaymentFormat('freePayment')"
          class="record-button"
        >
          Без стоимости
        </button>

        <!-- Добавлены условия для групповой и аренды -->
        <button
          v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
          :class="{ 'active': selectedPaymentFormat === 'equipmentPayment' }"
          @click="selectPaymentFormat('equipmentPayment')"
          class="record-button"
        >
          Оплата за время и единицу оборудования
        </button>
        <button
          v-if="selectedRecordType === 'group' || selectedRecordType === 'rental'"
          :class="{ 'active': selectedPaymentFormat === 'freePayment' }"
          @click="selectPaymentFormat('freePayment')"
          class="record-button"
        >
          Без стоимости
        </button>
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
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        // Ваш код для загрузки файла, например, отправка на сервер
        // В данном примере используется заглушка, вы должны заменить ее на свою логику
        this.uploadedFile = 'URL к загруженному файлу';
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
  background-color:#FAFAFA;
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
