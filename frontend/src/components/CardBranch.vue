<template>
  <div class="service_card">
    <div class="card-container">
      <div class="card-header">
        <div class="main">
          <p class="text-header">{{ Name || 'Название не указано' }}</p> <!-- Отображаем название услуги -->
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
      <div class="card_img">
        <img src="../../static/img/Card.png" style="width:100%" alt="">
      </div>
      <div class="cards">
        <div class="text-container">
          <p class="text-header">{{ Address || 'Адрес не указан' }}</p>
          <p class="text-subheader">Адрес</p>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ Phone || 'Телефон не указан' }}</p>
            <p class="text-subheader">Телефон</p>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ WorkTime || 'Часы не указаны'}}</p>
            <p class="text-subheader">Рабочие часы</p>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ WorkDays || 'График не указан' }}</p>
            <p class="text-subheader">График работы</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Kebab from '../components/DropdownKebab.vue';

export default {
  props:['Name', 'Address', 'Phone', 'WorkTime', 'WorkDays'],
  components: { Kebab },
  data() {
    return {
      buttons:[
        {btnname:'Редактировать', svg:'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="100px" height="100px"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>'},
      ],
    };
  },
};
</script>


<style scoped>
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
    font-size: 10px;
    line-height: 12px;
    letter-spacing: 0em;
    color: #AFB6C1;
    margin: 0;
    margin-bottom: 10px;
    text-align: left;
  }
  .service_card{
    width: 17vw;
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
    align-items: center;
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
</style>