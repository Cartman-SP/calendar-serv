<template>
  <div style="height: 100%;">
    <div div :class="{'service_card' : !deleteAction, 'service_card-deleting' : deleteAction}">
      <div class="card-container">
        <div class="card-header">
          <div class="main">
            <p class="text-header">{{ FilialData.name || 'Название не указано' }}</p> <!-- Отображаем название услуги -->
          </div>
          <Kebab :buttons="buttons" :HasDelete="true" :HasDeviders="true" @Deleting="toggleModal"/>
        </div>
        <div class="card_img">
          <img :src="image" style="width:100%; height: 200px; object-fit: cover; border: none;" alt="">
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ FilialData.address || 'Адрес не указан' }}</p>
            <p class="text-subheader">Адрес</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header" style="display: flex; align-items: center; gap: 5px;">{{ FilialData.phone || 'Телефон не указан' }} 
                <svg @click="copyPhoneNumber" class="copy" width="12" height="13" viewBox="0 0 12 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_4198_16698)">
                <path d="M6.5 10.5C7.1628 10.4992 7.79822 10.2356 8.26689 9.7669C8.73556 9.29823 8.99921 8.66281 9 8.00001V3.62151C9.00078 3.35869 8.94938 3.09833 8.84879 2.85552C8.7482 2.61271 8.60041 2.39228 8.414 2.20701L7.293 1.08601C7.10773 0.899596 6.8873 0.75181 6.64449 0.651219C6.40168 0.550627 6.14132 0.499231 5.8785 0.500009H3.5C2.8372 0.500803 2.20178 0.76445 1.73311 1.23312C1.26444 1.70179 1.00079 2.33721 1 3.00001V8.00001C1.00079 8.66281 1.26444 9.29823 1.73311 9.7669C2.20178 10.2356 2.8372 10.4992 3.5 10.5H6.5ZM2 8.00001V3.00001C2 2.60218 2.15804 2.22065 2.43934 1.93935C2.72064 1.65804 3.10218 1.50001 3.5 1.50001C3.5 1.50001 5.9595 1.50701 6 1.51201V2.50001C6 2.76523 6.10536 3.01958 6.29289 3.20712C6.48043 3.39465 6.73478 3.50001 7 3.50001H7.988C7.993 3.54051 8 8.00001 8 8.00001C8 8.39783 7.84197 8.77936 7.56066 9.06067C7.27936 9.34197 6.89783 9.50001 6.5 9.50001H3.5C3.10218 9.50001 2.72064 9.34197 2.43934 9.06067C2.15804 8.77936 2 8.39783 2 8.00001ZM11 4.50001V10C10.9992 10.6628 10.7356 11.2982 10.2669 11.7669C9.79822 12.2356 9.1628 12.4992 8.5 12.5H4C3.86739 12.5 3.74022 12.4473 3.64645 12.3536C3.55268 12.2598 3.5 12.1326 3.5 12C3.5 11.8674 3.55268 11.7402 3.64645 11.6465C3.74022 11.5527 3.86739 11.5 4 11.5H8.5C8.89783 11.5 9.27936 11.342 9.56066 11.0607C9.84197 10.7794 10 10.3978 10 10V4.50001C10 4.3674 10.0527 4.24022 10.1464 4.14646C10.2402 4.05269 10.3674 4.00001 10.5 4.00001C10.6326 4.00001 10.7598 4.05269 10.8536 4.14646C10.9473 4.24022 11 4.3674 11 4.50001Z" fill="#D2D8DE"/>
                </g>
                <defs>
                <clipPath id="clip0_4198_16698">
                <rect width="12" height="12" fill="white" transform="translate(0 0.5)"/>
                </clipPath>
                </defs>
                </svg>
              </p>
              <p class="text-subheader">
                Телефон
              </p>
            </div>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ FilialData.work_hours || 'Часы не указаны'}}</p>
              <p class="text-subheader">Рабочие часы</p>
            </div>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ FilialData.active_days || 'График не указан' }}</p>
              <p class="text-subheader">График работы</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
    <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
              <div class="modal-content">
                <p class="text-header">Удаление услуги</p>
                <p class="modal-subtext">Вы действительно хотите удалить услугу<br><span>{{FilialData.name}}</span>?</p>
                <div class="btn_container">
                  <button class="delete" @click="deleteService">Удалить</button>
                  <button class="exit" @click="toggleModal">Отмена</button>
                </div>
              </div>
    </div>
  </div>

  
</template>

<script>
import Kebab from '../components/DropdownKebab.vue';
import axios from 'axios';

export default {
  props:['FilialData'],
  components: { Kebab },
  data() {
    return {
      deleteAction: false,
      buttons:[
        {btnname:'Редактировать', svg:'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="100px" height="100px"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>'},
      ],
      image: '',
      showModal: false,
    };
  },
  methods: {
    copyPhoneNumber() {
      // Ваша функция для копирования в буфер обмена
      var tempInput = document.createElement("input");
      tempInput.value = this.FilialData.phone;
      document.body.appendChild(tempInput);
      tempInput.select();
      document.execCommand("copy");
      document.body.removeChild(tempInput);
      alert("Номер телефона скопирован в буфер обмена: " + this.FilialData.phone);
    },
    deleteService() {
        const formData = new FormData();
        formData.append('id', this.FilialData.id);
        axios.post('http://127.0.0.1:8000/api/delete_branch/', formData)
            .then(response => {
                console.log('Service deleted:', response.data);
                this.deleteAction = true;
                setTimeout(() => {
                  this.$parent.getfilials();
                  this.deleteAction = false;
                }, 200);
                this.showModal = !this.showModal;
            })
            .catch(error => {
                console.error('Error deleting service:', error);
            });
    },
    get_image(){
      axios.get(`http://127.0.0.1:8000/api/get_image/?id=${this.FilialData.id}`)
        .then(response => {
          this.image = 'http://127.0.0.1:8000/' + response.data.image
          console.log(response)
        })
        .catch(error => {
          this.image = '../../static/img/Card.png'
          console.error('Error fetching employees:', error);
        });
    },
    toggleModal() { // добавлено
      this.showModal = !this.showModal;
    },
  },
  mounted(){
    this.get_image()
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
  .copy{
    width: 15px;
    height: 15px;
  }

  .copy:hover{
    cursor: pointer;
  }
  .copy path{
    fill: #AFB6C1;
  }

  .copy:hover path{
    fill: #535C69;
  }
  .text-header{
    font-family: 'TT Norms Medium';
    font-size: 16px;
    line-height: 18px;
    letter-spacing: 0em;
    color: #535C69;
    margin: 0;
    text-align: left;
  }
  .text-subheader{
    font-family: 'TT Norms Medium';
    font-size: 13px;
    line-height: 12px;
    letter-spacing: 0em;
    color: #AFB6C1;
    margin: 0;
    margin-bottom: 10px;
    text-align: left;
  }
  .service_card{
    height: 100%;
    background-color: #FFF;
    border-radius: 5px;
  }

  .service_card-deleting{
    scale: 0;
    opacity: 0;
    transition: all .2s ease;
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
    align-items: center;
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
  .cards{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  img{
    border-radius: 5px;
  }
  .delete{
    color: #F97F7F;
    background-color: rgba(249, 127, 127, 0.2);
  }
  .delete:hover{
    background: #F97F7F;
    color: #FFFFFF;
  }
</style>