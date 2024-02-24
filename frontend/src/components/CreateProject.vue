<template>
    <div class="main">
      <div class="overlay" v-if="showModal"></div>
      <div class="transition">
        <router-link to="/lk/project" class="eidt-link">Мои проекты</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <p class="creation_text">Новый проект</p>
      </div>
      <div class="edit">
        <div class="head_container">
          <p class="header_text">Создание проекта</p>
          <p class="subheader_text">Название проекта не должно превышать 25 знаков</p>
        </div>
        <div class="form">
          <div class="form_container">
            <label for="">Название проекта</label>
            <input maxlength="25" type="text" placeholder="Введите название проекта" v-model="companyName">
            <p class="small-text">Для ввода доступно — <span class="remaining-characters">{{ remainingCharacters }}</span>/25</p>
          </div>
          <div class="form_container">
            <label for="service">Часовой пояс</label>
            <SelectPage
            :options="['GMT +4', 'GMT +3']"
            :default="'Выберите свой часовой пояс'"
            class="select"
            />
          </div>
          <div class="form_container">
            <label for="service">Валюта</label>
            <SelectPage
            :options="['Р', 'Т']"
            :default="'Выберите основную валюту'"
            class="select"
            />
          </div>
        </div>
        <div class="picker">
          <p class="color_text">Цвет иконки проекта</p>
          <div class="color_container">
            <div class="color" style="background:#F3F5F6"></div>
            <div class="color" style="background:#7DCD37"></div>
            <div class="color" style="background:#28CCF0"></div>
            <div class="color" style="background:#9D8FF1"></div>
            <div class="color" style="background:#FB88C0"></div>
            <div class="color" style="background:#F97F7F"></div>
            <div class="color" style="background:#F7D37D"></div>
          </div>
        </div>
  
        <div class="bottom">
          <div class="bottom_container">
            <button class="save">Сохранить</button>
            <router-link to="/lk/project/" style="text-decoration:none; width:100%">
              <button class="back">Вернуться</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import SelectPage from '../components/SelectPage.vue';

  export default {
  components: { SelectPage },
    data() {
      return {
        companyName: '',
        showModal: false,
      };
    },
    computed: {
      remainingCharacters() {
        const maxLength = 25;
        return maxLength - this.companyName.length;
      },
    },
  };
  </script>
  
  <style scoped>
  .transition {
    display: flex;
    flex-direction: row;
    gap: 10px;
    margin-bottom: 20px;
  }
  .eidt-link {
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
  .edit {
    width: 50%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .form{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .head_container{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .form_container{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .header_text{
    font-family: TT Norms Medium;
    font-size: 18px;
    line-height: 21px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
    margin: 0;
  }
  .subheader_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    font-weight: 500;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    margin: 0;
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
  input{
    margin: 0;
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
  .color_text{
    font-family: TT Norms Medium;
    font-size: 12px;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    color: #52565F;
  }
  .color_container{
    display: flex;
    gap: 5px;
  }
  .color{
    width: 24px;
    height: 24px;
    border-radius: 3px;
    cursor: pointer;
    transition: all .2s ease;
  }

  .color:hover{
    filter: brightness(90%);
  }
  .bottom_container{
    display: flex;
    gap: 10px;
    width: 50%;
  }
  .bottom{
    display: flex;
    justify-content: space-between;
  }
  .save{
    background: #EFEFFF;
    color: #6266EA;
    width: 100%;
    font-family: TT Norms Medium;
  }
  .back{
    font-family: TT Norms Medium;
    color: #535C69;
    background: #FFFFFF;
    border: 1px solid #DDE1E5;
    width: 100%;
  }

  .back:hover{
    color: #6266EA;
  }
  .save:hover{
    color: #FFFFFF;
    background: #6266EA;
  }
  .delete{
    color: #F97F7F;
    background: #F97F7F33;
  }
  .delete:hover{
    background: #F97F7F;
    color: #FFFFFF;
  }
  .small-text {
    color:#D2D8DE;
    font-family: "TT Norms Medium";
    font-size: 14px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    text-align: left;
    margin: 0;
  }
  .small-text .remaining-characters {
    color: #6266EA;
  }
  .modal{
    width: 36vh;
    height: auto;
    position: absolute;
    padding: 40px;
    border-radius: 10px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background: white;
  }
  .delete_edit{
    color: #F97F7F;
    background-color: rgba(249, 127, 127, 0.2);
  }
  .delete:hover{
    background: #F97F7F;
    color: #FFFFFF;
  }
  .exit{
    color: #535C69;
    border: 1px solid #DDE1E5;
    background: #FFFFFF;  
    transition: background-color 0.3s, border-color 0.3s, color 0.3s;
  }
  .exit:hover{
    border: 1px solid #AFB6C1;
    background: #F5F5F5;
  }
  .btn_container{
    margin-top: 30px;
    display: flex;
    gap: 10px;
  }
  .text-header{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 14px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .modal-subtext{
    font-family: TT Norms Medium;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    margin: 0;
    margin-top: 10px;
  }
  .modal_span{
    color: #7D838C;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
  }
  </style>