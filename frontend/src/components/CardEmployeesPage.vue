<template>
  <div class="service_card">
    <div class="card-container">
      <div class="card-header">
        <div class="main">
          <img :src="get_img()" alt="Service Cover" class="img_head">
          <div class="head">
            <div class="text-container">
              <p class="text-header">{{ employeeData.firstname }}</p> <!-- Отображаем название услуги -->
              <p class="text-subheader">Имя</p>
            </div>
            <div class="text-container">
              <p class="text-header">{{ employeeData.secondname }}</p>
              <p class="text-subheader">Фамилия</p>
            </div>
          </div>
        </div>
        <div class="dropdown-container">
          <div class="dropdown_btn">
            <button @click="toggleDropdown" class="dropdown" :style="{ 'background-color': showDropdown ? '#F3F6F8' : 'transparent' }">
              <img v-if="!showDropdown" src="../../static/img/kebab.svg" alt="Open">
              <img v-if="showDropdown" src="../../static/img/x.svg" alt="Close">
            </button>
          </div>
          <div v-if="showDropdown" class="dropdown-menu">
            <router-link to="/#" style="text-decoration:none">
              <div class="dropdown-item">
                <div class="dropdown-header">Редактировать</div>
              </div>
            </router-link>
            <div class="lines"></div>
            <div class="dropdown-item" @click="toggleModal">
              <div class="dropdown-subheader">Удалить</div>
            </div>
          </div>
          <div v-if="showModal" class="modal">
            <div class="modal-content">
              <p class="text-header">Удаление услуги</p>
              <p class="modal-subtext">Вы действительно хотите удалить услугу<br><span>Стрижка?</span></p>
              <div class="btn_container">
                <button class="delete" @click="deleteService">Удалить</button>
                <button class="exit" @click="toggleModal">Отмена</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="line"></div>
      <div class="card-bottom">
        <div class="text-container">
          <p class="text-header">{{ employeeData.rank }}</p>
          <p class="text-subheader">Должность</p>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ employeeData.worktime }}</p>
            <p class="text-subheader">Рабочие часы</p>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p v-if="employeeData.timetable!='undefined'" class="text-header">{{employeeData.timetable.replace('x','/')}}</p>
            <p v-else class="text-header">{{employeeData.days}}</p>
            <p class="text-subheader">График работы</p>
          </div>
        </div>
      </div>
      <div class="service">
        <div class="usluga">
          <p class="usluga_text">Стрижка</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    employeeData: Object // Принимаем данные о сотруднике через props
  },
  data() {
    return {
      showDropdown: false,
      showModal: false,
    };
  },

  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    toggleModal() { // добавлено
      this.showModal = !this.showModal;
    },
    get_img(){
      return "http://127.0.0.1:8000"+this.employeeData.avatar
    }
  }
};
</script>


<style scoped>
.text-header{
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 14px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .text-subheader{
    font-family: TT Norms;
    font-size: 10px;
    font-weight: bold;
    line-height: 12px;
    letter-spacing: 0em;
    color: #AFB6C1;
    margin: 0;
    margin-bottom: 10px;
    text-align: left;
  }
  .line{
    width: 100%;
    height: 1px;
    background-color: #E4EAEF;
    margin: 20px 0;
  }
  .service_card{
    width: 23vw;
    height: auto;
    background-color: #FFF;
    border-radius: 5px;
  }
  .card-container{
    padding: 20px;
    padding-bottom: 45px;
  }
  .card-header{
    display: flex;
  }
  .main{
    display: flex;
    gap: 20px;
    width: 100%;
  }
  .dropdown-container{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .dropdown{
    color: #AFB6C1;
    font-size: 15px;
    font-weight: bold;
    background-color: white;
    width: 1em;
    height: 2em;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 3px;
    transition: background-color 0.3s ease;
  }
  .dropdown:hover{
    border: 1px solid #535C69;
  }
  .dropdown-menu {
    width: 15vh;
    height: auto;
    background-color: #FFFFFF;
    border: 1px solid #E4EAEF;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    text-align: left;
  }
  
  .dropdown-item {
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  
  .dropdown-header{
    font-family: TT Norms;
    font-size: 13px;
    font-weight: 500;
    line-height: 13px;
    letter-spacing: 0em;
    color: #AFB6C1;
  }
  .dropdown-header:hover {
    font-weight: bold;
    color: #535C69;
  }
  .dropdown-subheader{
    font-family: TT Norms;
    font-size: 13px;
    font-weight: 500;
    line-height: 13px;
    letter-spacing: 0em;
    color: #AFB6C1;
  }
  .dropdown-subheader:hover {
    font-weight: bold;
    color: #535C69;
  }
  .img_head{
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 100px;
  }
  .lines{
    width: 100%;
    height: 1px;
    background-color: #E4EAEF;
  }
  .dropdown_btn{
    display: flex;
    justify-content: right;
  }
  .modal{
    width: 36vw;
    height: auto;
    position: absolute;
    padding: 40px;
    border-radius: 10px;
    gap: 10px;
    left: 500px;
    top: 500px;
    background: white;
  }
  .delete{
    color: #F97F7F;
    background-color: rgba(249, 127, 127, 0.2);
    font-weight: bold;
  }
  .delete:hover{
    background: #F97F7F;
    color: #FFFFFF;
  }
  .exit{
    color: #535C69;
    border: 1px solid #DDE1E5;
    background: #FFFFFF;  
    font-weight: bold;
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
  span{
    color: #7D838C;
    font-weight: bold;
  }
  .modal-subtext{
    font-family: TT Norms;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    letter-spacing: 0em;
    text-align: left;
    color: #AFB6C1;
    margin: 0;
    margin-top: 10px;
  }
  .card-bottom{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 30px;
    margin-bottom: 20px;
  }
  .service{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .usluga{
    width: auto;
    color: #AFB6C1;
    background: #FAFAFA;
    padding: 5px 10px;
    border-radius: 100px;
    gap: 10px;
  }
  p{
    margin: 0;
  }
  .usluga_text{
    font-family: TT Norms;
    font-size: 10px;
    font-weight: 500;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
  }
</style>