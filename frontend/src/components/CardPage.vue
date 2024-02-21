<template>
  <div class="service_card">
    <div class="overlay" v-if="showModal"></div>
    <div class="card-container">
      <div class="card-header">
        <div class="main">
          <img :src="'http://127.0.0.1:8000/' + usluga.serviceCover" alt="Service Cover" class="img_head">
          <div class="head">
            <div class="text-container">
              <p class="text-header">{{ usluga.name }}</p> <!-- Отображаем название услуги -->
              <p class="text-subheader">Название услуги</p>
            </div>
            <div class="text-container">
              <p class="text-header">{{ usluga.time }}</p>
              <p class="text-subheader">Длительность</p>
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
          <div v-if="showDropdown" class="dropdown-menu" @click="closeDropdown">
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
      <div class="line"></div>
      <div class="card-bottom">
        <div class="text-container">
          <p class="text-header">{{ usluga.type.replace('individual','Индивидуальный').replace('group','Групповой').replace('rental','Аренда') }}</p>
          <p class="text-subheader">Тип записи</p>
        </div>
        <div class="bottom">
          <div class="text-container">
            <p class="text-header">{{ usluga.pay_type }}</p>
            <p class="text-subheader">Формат оплаты</p>
          </div>
          <p class="bottom-text">{{ usluga.cost }} Р</p> <!-- Отображаем стоимость услуги -->
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
      showDropdown: false,
      showModal: false,
    };
  },

  props: ['usluga'], // Принимаем объект Usluga через пропс

  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    toggleModal() { // добавлено
      this.showModal = !this.showModal;
    },
    closeDropdown() {
      this.showDropdown = false;
    },
    deleteService() {
    const serviceId = this.usluga.id; // Получаем идентификатор услуги
    console.log(this.usluga)
    const formData = new FormData();
    formData.append('id', serviceId);
    axios.post('http://127.0.0.1:8000/api/delete/', formData)
        .then(response => {
            console.log('Service deleted:', response.data);
            this.$parent.get_uslugi();
        })
        .catch(error => {
            console.error('Error deleting service:', error);
        });
},
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
    height: auto;
    background-color: #FFF;
    border-radius: 5px;
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
  .bottom{
    display: flex;
    justify-content: space-between;
  }
  .bottom-text{
    margin: 0;
    background-color:#EFEFFF;
    max-width: 110px;
    padding: 0 10px;
    height: 34px;
    white-space: nowrap;
    font-family: TT Norms;
    font-size: 14px;
    font-weight: bold;
    line-height: 24px;
    letter-spacing: 0em;
    color: #535C69;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 3px;
  }
  
  .dropdown-container{
    position: relative;
    display: inline-block;
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
    transition: all .2s ease;
    border: 1px solid white;
  }
  .dropdown:hover{
    border: 1px solid #535C69;
  }
  .dropdown-menu {
    position: absolute;
    right: 0;
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
  
  .dropdown-item{
    padding: 10px;
    font-family: TT Norms;
    font-size: 13px;
    font-weight: 500;
    line-height: 13px;
    letter-spacing: 0em;
    color: #AFB6C1;
    transition: all .2s ease;
  }

  .dropdown-item:hover {
    color: #535C69;
    cursor: pointer;
  }
  .img_head{
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 5px;
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
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6); /* Задний фон с прозрачностью 60% */
  }
</style>