<template>
  <div class="service_card">
    <div class="card-container">
      <div class="card-header">
        <div class="main">
          <img src="../../static/img/Salon_2.png" alt="">
          <div class="main_container">
            <div class="main_header">
              <p class="text-header">Барбершоп «Викинг»</p>
              <div class="link_container">
                <svg width="10" height="10" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M3.5 2C2.67157 2 2 2.67157 2 3.5V16.5C2 17.3284 2.67157 18 3.5 18H16.5C17.3284 18 18 17.3284 18 16.5V11H19V16.5C19 17.8807 17.8807 19 16.5 19H3.5C2.11929 19 1 17.8807 1 16.5V3.5C1 2.11929 2.11929 1 3.5 1H9V2H3.5ZM11.8431 2H18V8.15685H17V3.70711L7.95406 12.753L7.24695 12.0459L16.2929 3H11.8431V2Z" fill="#398BFF"/>
                </svg>
                <a href="">calendar.com/user1/barbershop-viking</a>
              </div>
            </div>
            <div class="main_subheader">
              <div class="date">
                <img src="../../static/img/edit.png" alt="">
                <p class="id">12.05.2023</p>
              </div>
              <p class="id">id  12345678</p>
            </div>
          </div>
        </div>
        <div class="btns">
          <button class="play">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 18V2L18 10.2286L5 18Z" fill="#00A490"/>
            </svg>
          </button>
          <button class="btn_svg">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M9.99998 6C7.77205 6 5.59687 6.9496 3.9367 8.7223L2.74012 9.99998L3.9367 11.2777C5.60258 13.0565 7.67481 14 9.99998 14C12.3252 14 14.3974 13.0565 16.0633 11.2777L17.2599 9.99998L16.0633 8.7223C14.4031 6.9496 12.2279 6 9.99998 6ZM20 9.99998L17.5231 12.6448C15.5084 14.7961 12.9198 16 9.99998 16C7.08018 16 4.49163 14.7961 2.47691 12.6448L0 9.99998L2.47691 7.35518C4.4944 5.20094 7.18913 4 9.99998 4C12.8108 4 15.5056 5.20094 17.5231 7.35518L20 9.99998Z" fill="#6266EA"/>
              <path d="M10.0001 6.84607C9.68466 6.84607 9.36928 6.9512 9.0539 6.9512C9.57954 7.16146 10.0001 7.79223 10.0001 8.423C10.0001 9.26403 9.26415 9.99993 8.42312 9.99993C7.79235 9.99993 7.26671 9.57942 6.95133 9.05378C6.8462 9.36916 6.84619 9.68454 6.84619 9.99993C6.84619 11.7871 8.21286 13.1538 10.0001 13.1538C11.7872 13.1538 13.1539 11.7871 13.1539 9.99993C13.1539 8.21274 11.7872 6.84607 10.0001 6.84607Z" fill="#6266EA"/>
            </svg>
          </button>
          <button class="btn_svg">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M15.9667 1L9.00006 1.03317L11.783 3.8029L7.00008 8.5858V13.5858L2.29297 18.2929L3.70718 19.7071L9.00008 14.4142V9.41423L13.2006 5.21375L16.0001 8L15.9667 1Z" fill="#6266EA"/>
            </svg> 
          </button>
          <button>Редактировать</button>
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
      </div>
    </div>
  </div>
</template>

<script>
import Kebab from '../components/DropdownKebab.vue';
export default {
  components: { Kebab },
  data() {
    return {
      showDropdown: false,
      showModal: false,
      buttons:[
        {btnname:'Дублировать', svg:'<svg width="12" fill="white" height="14" viewBox="0 0 12 14" xmlns="http://www.w3.org/2000/svg"><path d="M8.83533 2.91667H6.00033V0.00933333L8.83533 2.91667ZM4.83366 4.08333V0H1.91699C1.45286 0 1.00774 0.184374 0.679555 0.512563C0.351367 0.840752 0.166992 1.28587 0.166992 1.75V11.0833H8.91699V4.08333H4.83366ZM10.0837 4.08917V12.2722H3.08366V14H11.8337V5.83333L10.0837 4.08917Z"/></svg>'
},
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
  }
};
</script>


<style scoped>
  .text-header{
    font-family: TT Norms Medium;
    font-size: 16px;
    line-height: 18px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .service_card{
    width: 100%;
    height: auto;
    background-color: #FFF;
    border-radius: 5px;
  }
  .card-container{
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .card-header{
    display: flex;
  }
  .main{
    display: flex;
    gap: 20px;
    width: 100%;
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
  p{
    margin: 0;
  }
  img{
    border-radius: 5px;
  }
  .link_container{
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .main_container{
    display: flex;
    flex-direction: column;
    gap: 35px;
  }
  .main_header{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .main_subheader{
    display: flex;
    gap: 15px;
  }
  .date{
    display: flex;
    gap: 5px;
  }
  .id{
    color: #D2D8DE;
    font-family: TT Norms Medium;
    font-size: 12px;
    font-weight: 700;
    line-height: 14px;
    letter-spacing: 0em;
    text-align: right;
  }
  a{
    text-decoration: none;
    color: #398BFF;
  }
  .btns{
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .btn_svg{
    background: #F5F6FF;
  }
  .play{
    background:#DCF4F2;
  }
  .play:hover{
    background: #0ABBA5;
    color: #FFFFFF;
  }
</style>