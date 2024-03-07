<template>
    <div class="main">
      <div class="content" v-if="employees.length>0 && employees_load">
        <router-link to="/lk/personal/employees" class="add">
          <div class="svg-plus">
            <svg width="1em" height="1em" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z"/>
              </svg>            
          </div>
          <p>Добавить сотрудника</p>
        </router-link>
      <div v-for="employee in employees" :key="employee.id">
        <CardEmployeesPage :employeeData="employee"/>
      </div>

      </div>
      <div v-else-if="employees.length==0 && employees_load" class="personal">
        <img src="../../static/img/plus-sotrudnik.svg" alt="" class="img_personal">
        <p class="header">Вот это скорость!</p>
        <p class="subheader">Мы видим, что вы завершили создание услуг. В этом разделе,предлагаем добавить ваших сотрудников и назначить им ранее созданные услуги. Если, у вас нет сотрудников, вы можете пропустить этот шаг и перейти к созданию своего филиала/компании.</p>
        <div class="pernosal_btns">
          <a href="#/lk" style="text-decoration:none"><button class="personal_btn skip-btn"> Пропустить</button></a>
          <a href="#/lk/personal/employees" style="text-decoration:none"><button class="personal_btn"> + Добавить сотрудника</button></a>
        </div>
      </div>
      <div v-else style="padding-top: 200px;">
      <!-- Показываем значок загрузки -->
        <i class="pi pi-spin pi-spinner" style="font-size: 2rem;  color: #6266EA"></i>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import CardEmployeesPage from '../components/CardEmployeesPage.vue';
  
  export default {
    components: { CardEmployeesPage },
    data() {
      return {
        employees: [], // Сюда будем сохранять полученных сотрудников
        employees_load: false,
      };
    },
    methods:{
      get_employee(){
              const user_id =  this.$store.state.registrationData.user_id;// Замените на актуальный user_id
  
      // Выполняем запрос к API Django
      axios.get(`http://127.0.0.1:8000/api/get_employees/?user_id=${user_id}`)
        .then(response => {
          this.employees = response.data; // Сохраняем полученные данные в переменной
          this.employees_load = true;
          this.employees.reverse();
          console.log(this.employees)
        })
        .catch(error => {
          console.error('Error fetching employees:', error);
        });
      },
    },
    mounted() {
      // Здесь нужно заменить 'STATIC_USER_ID' на актуальный user_id
      this.get_employee()
    }
  }
  </script>
  
  <style scoped>
  .main{
    overflow-y: scroll;
    height: 87vh;
  }
  .pernosal_btns{
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 10px;
  }

  .skip-btn {
    color: #535C69;
    background: #FFFFFF;
    border-radius: 3px;
    border: 1px solid #DDE1E5
  }
  .personal {
    height: 87vh;
    text-align: center;
    align-items: center;
    justify-content: center;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .img_personal {
    margin-bottom: 10px;
    width: 86px;
    height: 86px;
  }
  
  .header {
    color: #535C69;
    font-family: TT Norms Medium;
    font-size: 20px;
    font-weight: 500;
    line-height: 15px;
    letter-spacing: 0em;
    text-align: center;
  }
  
  .subheader {
    font-size: 16px;
    line-height: 18px;
    color: #AFB6C1;
    font-family: TT Norms Medium;
    font-weight: 500;
    letter-spacing: 0em;
    text-align: center;
    max-width: 500px;
  }
  .personal_btn{
    margin: 0 auto;
  }
  .content{
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(4, 1fr);
  }
  .add {
    text-decoration-line: initial;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    display: flex;
    height: 100%;
    width: 100%;
    gap: 10px;
    color: #6266EA;
    border-style: dashed;
    border-width: 2px;
    border-color: #D9D9D9;
    transition: 0.3s ease;
    padding: 20px;
    border-radius: 5px;
  }
  .svg-plus{
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 40px;
    width: 1em;
    height: 1em;
  }
  p{
    margin: 0;
  }
  .add:hover{
    background: #EFEFFF;
  }
  @media (max-width: 1340px){
    .content{
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (max-width: 1061px){
    .content{
      grid-template-columns: 1fr
    }
    .add{
      min-height: 135px;
    }
  }
  @media (max-width: 900px){
    .personal{
      height: 70vh;
    }
    .img_personal{
      width: 60px;
      height: 60px;
    }
  }
  @media (max-width: 768px){
    .main{
      padding: 20px;
    }
  }
  @media (max-width: 576px){
    .pernosal_btns{
      flex-direction: column;
      width: 100%;
    }
    .personal_btn{
      margin: 0;
      width: 100%;
    }
  }
  </style>