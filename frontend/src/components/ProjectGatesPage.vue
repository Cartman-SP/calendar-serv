<template>
    <div class="main">
      <div class="transition">
        <router-link to="/dashboard/project" class="eidt-link">Мои проекты</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>
        <router-link to="/dashboard/project" class="eidt-link">{{ project }}</router-link>
        <div class="arrow-container">
          <img src="../../static/img/arrow-right.png" alt="Стрелка вправо" class="arrow-icon">
        </div>  
        <p class="creation_text">Доступы</p>
      </div>
      <div class="edit">
        <p class="edit_header">Добавление нового пользователя для проекта:</p>
        <div class="main_container">
          <div class="card_img">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 1C1.89543 1 1 1.89543 1 3V16C1 17.1046 1.89543 18 3 18H17C18.1046 18 19 17.1046 19 16V5C19 3.89543 18.1046 3 17 3H8C8 1.89543 7.10457 1 6 1H3Z" fill="white"/>
            </svg> 
          </div>
          <div class="main_text">
            <p class="main_header">Барбершоп на Сатпаева</p>
            <p class="main_subheader">ID {{ project }}</p>
          </div>
        </div>
        <div class="divider"></div>
        <div class="form">
          <label for="">Введите Email адрес пользователя</label>
          <input type="text" placeholder="Email">
          <p class="small_text">На этот адрес будет отправлено приглашение</p>
        </div>
        <div class="choice">
          <p class="choice_text">Выберите права для пользователя</p>
          <div class="choice_container">
            <div class="choice_pick" @click="activateChoice">
              <div class="circle">
                <div class="second_circle"></div>
              </div>
              <p class="pick_text">Владелец</p>
              <Tip :Tip="'Владелец — полная передача прав на проект'"/>
            </div>
            <div class="choice_pick" @click="activateChoice">
              <div class="circle">
                <div class="second_circle"></div>
              </div>
              <p class="pick_text">Администратор</p>
              <Tip :Tip="'Администратор — есть доступ ко всем разделам \n и может редактировать любые разделы'"/>
            </div>
          </div>
          <div class="choice_container">
            <div class="choice_pick" @click="activateChoice">
              <div class="circle">
                <div class="second_circle"></div>
              </div>
              <p class="pick_text">Менеджер</p>
              <Tip :Tip="'Менеджер — доступ к заявкам, календарю, \n статистики, клиентам'"/>
            </div>
            <div class="choice_pick" @click="activateChoice">
              <div class="circle">
                <div class="second_circle"></div>
              </div>
              <p class="pick_text">Сотрудник</p>
              <Tip :Tip="'Сотрудник — когда выбирают права сотрудник, \n то выбирают какой именно сотрудник'"/>
            </div>
          </div>
        </div>
        <div class="dropdown-item" v-if="selectedRole === 'Сотрудник'">
          <p class="normal-text">Выберите сотрудника</p>
          <SelectPage
          :options="['123','123']"
          :placeholderdata="'Выберите сотрудников'"
          @input="option => selectedEmployees = option"
          :class="{ 'select-error': selectedEmployeesError }"
          :searchable="true"
          />
        </div>
        <div class="send">
          <button class="send_btn">Отправить приглашение</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import SelectPage from '../components/SelectPage.vue';
  import Tip from '../components/TipComponent.vue';

  export default { 
    components: { SelectPage,Tip },
    props: ['project'],
    data() {
      return {
         selectedEmployees: false,
         selectedRole: null,
      };
    },
    methods: {
      activateChoice(event) {
        // Получите ссылку на текущий выбор
        const choice = event.currentTarget;


        // Удалите `active` класс из всех choice
        document.querySelectorAll('.choice_pick').forEach(choice => {
            choice.classList.remove('active');
            choice.querySelector('.second_circle').style.display = 'none';
            choice.querySelector('.pick_text').style.color = '#AFB6C1';
            choice.querySelector('.circle').style.borderColor = '#C6CBD2'; // возвращаем цвет границы Circle
        });

        // Добавьте `active` класс только к текущему выбору
        choice.classList.add('active');
        choice.querySelector('.second_circle').style.display = 'inline-block';
        choice.querySelector('.pick_text').style.color = '#6266EA';
        choice.querySelector('.circle').style.borderColor = '#6266EA'; // меняем цвет границы Circle

        const role = choice.querySelector('.pick_text').textContent;
      // Устанавливаем выбранную роль в переменную selectedRole
      this.selectedRole = role;

      // Если выбран "Сотрудник", устанавливаем selectedEmployees в true
      if (role === 'Сотрудник') {
        this.selectedEmployees = true;
      } else {
        this.selectedEmployees = false;
      }
    },
    }
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
    width: 40%;
    height: auto;
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .card_img{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 32px;
    width: 32px;
    border-radius: 30px;
    background: #F97F7F;
  }
  .main_container{
    display: flex;
    gap: 10px;
  }
  .main_header{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
  }
  .main_subheader{
    font-family: TT Norms Medium;
    font-size: 12px;
    line-height: 14px;
    letter-spacing: 0.03em;
    text-align: left;
    color: #AFB6C1;
  }
  p{
    margin: 0;
  }
  .edit_header{
    font-family: TT Norms Medium;
    font-size: 18px;
    line-height: 21px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;    
  }
  .divider {
    border-bottom: 1px solid rgba(50, 56, 74, 0.1); 
    width: auto;
    margin: 0;
  }
  .choice_container{
    display: flex;
    justify-content: space-between;
  }
  .choice_text{
    font-family: TT Norms Medium;
    font-size: 13px;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: left;
    color: #535C69;
  }
  .choice{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .choice_pick{
    width: 100%;
    display: flex;
    align-items: center;
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
  .pick_text{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 17px;
    letter-spacing: 0em;
    text-align: center;
    color: #535C69;    
    cursor: pointer;
  }
  .small_text{
    font-family: TT Norms Medium;
    font-size: 12px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
  }
  input{
    margin: 0;
  }
  .second_circle{
    background: #6266EA;
    width: 10px;
    height: 10px;
    border-radius: 25px;
    display: none;
  }
  .send_btn{
    color: #6266EA;
    background: #EFEFFF;
  }
  .send_btn:hover{
    background: #6266EA;
    color: #FFFFFF;
  }
  .send{
    display: flex;
    justify-content: end;
  }
  label{
    margin: 0;
  }
  .form{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .dropdown-item{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .normal-text {
    color:#535C69;
    font-family: TT Norms Medium;
    font-size: 13px;
    font-style: normal;
    line-height: normal;
    text-align: left;
  }
  </style>