<template>
    <div class="main">
      <div class="create_employess">
        <div class="transition">
          <a href="#/main/personal" class="employesss-link">Сотрудники</a>
          <div class="arrow-container">
            <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
          </div>
          <p class="creation_text">Создание сотрудника</p>
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
    }
}   
  </script>
  
  <style scoped>
  
  .transition{
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 50px;
  }
  .employesss-link{
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
  
  .create_employess {
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
  
  #employessCover {
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
  