<template>
  <div style="height: 100%;">
    <div :class="{'service_card' : !deleteAction, 'service_card-deleting' : deleteAction}">
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
          <Kebab :buttons="buttons" :HasDelete="true" :HasDeviders="true" @Deleting="toggleModal"/>
        </div>
        <div class="line"></div>
        <div class="card-bottom">
          <div class="text-container">
            <p class="text-header">{{ employeeData.rank }}</p>
            <p class="text-subheader">Должность</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ employeeData.daystime }}</p>
              <p class="text-subheader">Рабочие часы</p>
            </div>
          </div>
          <div class="cards">
            <div class="text-container">
              <p v-if="employeeData.daystime!='undefined'" class="text-header">{{employeeData.daystime}}</p>
              <p v-else class="text-header">{{employeeData.daystime}}</p>
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
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
    <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
            <div class="modal-content">
              <p class="text-header">Удаление услуги</p>
              <p class="modal-subtext">Вы действительно хотите удалить сотрудника<br><span>{{ this.employeeData.firstname + ' ' + this.employeeData.secondname }}</span>?</p>
              <div class="btn_container">
                <button class="delete" @click="deleteEmployee">Удалить</button>
                <button class="exit" @click="toggleModal">Отмена</button>
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
      deleteAction: false,
      usluganame: "",
      buttons:[
        {btnname:'Редактировать', svg:'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="100px" height="100px"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>'},
      ],
    };
  },

  methods: {
    deleteEmployee() {
    const serviceId = this.employeeData.id // Получаем идентификатор услуги
    const formData = new FormData();
    formData.append('id', serviceId);
    axios.post('http://127.0.0.1:8000/api/deleteemployee/', formData)
      .then(response => {
          console.log('Service deleted:', response.data);
          this.deleteAction = true;
          setTimeout(() => {
            this.$parent.get_employee();
            this.deleteAction = false;
          }, 200);
          this.showModal = !this.showModal;
      })
      .catch(error => {
          console.error('Error deleting service:', error);
      });
    },

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
.modal-show{
    width: auto;
    height: auto;
    position: absolute;
    padding: 40px;
    border-radius: 10px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background: white;
    z-index: 99;
    opacity: 1;
    visibility: visible;
    transition: all .1s ease;
  }
  .modal-hide{
    width: auto;
    height: auto;
    position: absolute;
    padding: 40px;
    border-radius: 10px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    background: white;
    z-index: 99;
    opacity: 0;
    visibility: hidden;
    transition: all .1s ease;
  }
  .overlay-show {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
    z-index: 98;
    opacity: 1;
    visibility: visible;
    transition: all .1s ease;
  }
  .overlay-hide {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
    z-index: 98;
    opacity: 0;
    visibility: hidden;
    transition: all .1s ease;
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
    height: 100%;
    background-color: #FFF;
    border-radius: 5px;
    transition: filter .2s ease;
  }

  .service_card-deleting{
    scale: 0;
    opacity: 0;
    transition: all .2s ease;
  }

  .service_card:hover{
    filter: drop-shadow(0 0 10px rgb(228, 228, 228));
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