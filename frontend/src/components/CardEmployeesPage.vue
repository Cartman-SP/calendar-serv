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
        <Kebab :buttons="buttons" :HasDelete="true" :HasDeviders="true"/>
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
        <div class="usluga" v-for="u in usluganame" :key="u">
          <p class="usluga_text">{{u}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Kebab from '../components/DropdownKebab.vue';

export default {
  
  props: {
    employeeData: Object // Принимаем данные о сотруднике через props
  },
  components: { Kebab },
  data() {
    return {
      showDropdown: false,
      showModal: false,
      usluganame: "",
      buttons:[
        {btnname:'Редактировать', svg:'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="100px" height="100px"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>'},
      ],
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
    },
    get_usluga(){
      console.log(this.employeeData.serviceid)
      axios.get('http://127.0.0.1:8000/api/get_usluga_name/', {
      params: {
        usluga_id: this.employeeData.serviceid // ваш ID услуги, который вы хотите получить
      }
    })
    .then(response => {
      this.usluganame = response.data.usluga_name;
    })
    .catch(error => {
      console.error('Error fetching usluga name:', error);
    });
    }
  },
  mounted() {
    this.get_usluga();
  },

  
};
</script>


<style scoped>
.text-header{
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 14px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .text-subheader{
    font-family: TT Norms Medium;
    font-size: 10px;
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
    width: 100%;
    height: 100%;
    background-color: #FFF;
    border-radius: 5px;
    transition: all .2s ease;
  }

  .service_card:hover{
    filter: drop-shadow(0 0 10px rgb(228, 228, 228));
    cursor: pointer;
  }
  .card-container{
    padding: 20px;
  }
  .card-header{
    display: flex;
  }
  .main{
    display: flex;
    gap: 20px;
    width: 100%;
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
  span{
    color: #7D838C;
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
    font-family: TT Norms Medium;
    font-size: 10px;
    font-weight: 500;
    line-height: 12px;
    letter-spacing: 0em;
    text-align: left;
  }
</style>