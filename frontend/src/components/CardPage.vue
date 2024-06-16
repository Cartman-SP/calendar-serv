<template>
  <div style="height: 100%;">
    <div :class="{'service_card' : !deleteAction, 'service_card-deleting' : deleteAction}">
      <div class="card-container">
        <div class="card-header">
          <div class="main">
            <img :src="'http://127.0.0.1:8000/' + usluga.serviceCover" alt="No service cover" class="img_head">
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
          
          <Kebab :buttons="buttons" :HasDelete="true" :HasDeviders="true" @Deleting="toggleModal" @edit="this.$router.push({ path: `/dashboard/service/${usluga.id}/edit`, params: { serviceToEditId: usluga.id }})"/>
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
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
    <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
          <div class="modal-content">
            <p class="text-header">Удаление услуги</p>
            <p class="modal-subtext">Вы действительно хотите удалить услугу<br> <span>{{ this.usluga.name }}</span>?</p>
            <div class="btn_container">
              <button class="delete" @click="deleteService">Удалить</button>
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
  components: { Kebab },
  data() {
    return {
      showDropdown: false,
      showModal: false,
      deleteAction: false,
      buttons:[
      {btnname:'Редактировать',
        svg:'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="100px" height="100px"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>',
        action:'Edit',},
      ],
    };
  },

  props: ['usluga'],

  methods: {
    toggleModal() { // добавлено
      this.showModal = !this.showModal;
    },
    deleteService() {
    const serviceId = this.usluga.id;
    const formData = new FormData();
    formData.append('id', serviceId);
    axios.post('http://127.0.0.1:8000/api/delete/', formData)
        .then(response => {
            console.log('Service deleted:', response.data);
            this.deleteAction = true;
            setTimeout(() => {
              this.$parent.get_uslugi();
              this.deleteAction = false;
            }, 200);
            this.showModal = !this.showModal;
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
    font-family: TT Norms Medium;
    font-size: 18px;
    line-height: 18px;
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
    opacity: 1;
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
    gap: 10px;
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
    font-family: TT Norms Medium;
    font-size: 14px;
    line-height: 24px;
    letter-spacing: 0em;
    color: #535C69;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 3px;
  }
  .img_head{
    background-color: #f8f8f8;
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 5px;
  }
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
  @media (max-width: 568px){
    .bottom{
      flex-direction: column;
    }
    .bottom-text{
      max-width: 100%; 
    }
  }
</style>