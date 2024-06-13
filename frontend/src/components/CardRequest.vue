<template>
  <div class="all-request">
    <div class="verticalStatus" :class="statusClass"></div>
      <div class="main_card">
      <div class="mark_container">
        
        <div class="mark" v-if="!Mark" @click="Mark = true"></div>
        <div class="mark_active" v-else @click="Mark = false">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
          </svg>
        </div>
        <div class="status-select" @click="statusDrop = true" tabindex="1" @blur="toggleStatusDropdown">
          <div>
            <p class="text_container" v-if="requestData.status === 'New'" style="background-color: #28CCF0;">Новые</p>
            <p class="text_container" v-else-if="requestData.status === 'Adopted'" style="background-color: #F7D37D;">Принят</p>
            <p class="text_container" v-else-if="requestData.status === 'Canceled'" style="background-color: #F97F7F;">Отменен</p>
            <p class="text_container" v-else-if="requestData.status === 'Done'" style="background-color: #00A490;">Завершен</p>
          </div>
          <img src="../../static/img/arrow-down.png" alt="">
          <div v-if="statusDrop" class="status-select_options">
            <p class="status-option" @click="set_status(requestData.id, 'Adopted')">Принят</p>
            <p class="status-option" @click="set_status(requestData.id, 'New')">Новые</p>
            <p class="status-option" @click="set_status(requestData.id, 'Done')">Завершен</p>
            <p class="status-option" @click="set_status(requestData.id, 'Canceled')">Отменен</p>
          </div>
        </div>
      </div>
      <p class="date_text">{{ requestData.data }}</p>
      <div class="container">
        <p class="client_text">NaN {{ requestData.client }}</p>
        <div class="client_container">
          <p class="client_text">client Phone NaN</p>
          <img src="../../static/img/copy.svg" alt="">
        </div>
        <div class="client_container">
          <p class="client_text">#{{ requestData.client }}</p>
          <img src="../../static/img/copy.svg" alt="">
        </div>
      </div>
      <div class="container">
        <div class="client_wrapper">
          <p class="client_subtext">Сотрудник</p>
          <p class="client_text">NaN {{ requestData.employee }}</p>
        </div>
        <div class="client_wrapper">
          <p class="client_subtext">Название услуги</p>
          <p class="client_text">NaN {{ requestData.usluga }}</p>
        </div>
        <div class="client_wrapper">
          <p class="client_subtext">Стоимость</p>
          <p class="client_text">NaN ₸</p>
        </div>
      </div>
      <div class="keys">
        <img src="../../static/img/cog.svg" alt="" class="">
        <img src="../../static/img/copy_2.svg" alt="" class="">
        <img src="../../static/img/delete.svg" alt="" class="">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  props: ['requestData'],
  data() {
      return {
        Mark: false,
        statusDrop: false,
      }
  },
  methods:{
    toggleStatusDropdown(){
      this.statusDrop = !this.statusDrop;
    },
    async set_status(id, status) {
      const formData = new FormData();
      formData.append('id', id);
      formData.append('status', status)
      axios.post('http://127.0.0.1:8000/api/set_status/', formData)
        .then(response => {
          console.log('Service deleted:', response.data);
        })
        .catch(error => {
          console.error('Error creating service:', error);
        });
    },
  },
  computed: {
    statusClass() {
      return {
        
        'done': this.requestData.status === 'Done',
        'new': this.requestData.status === 'New',
        'adopted': this.requestData.status === 'Adopted',
        'canceled': this.requestData.status === 'Canceled'
      };
    }
  }
}
</script>

<style scoped>
.status-select_options{
  position: absolute;
  background-color: white;
  filter: drop-shadow(0 0 10px rgb(215, 215, 215));
  border: solid 2px #F5F5F5;
  border-radius: 5px;
  top: 30px;
  z-index: 99;
}

.status-option{
  text-align: start;
  padding: 10px;
  width: 150px;
  color: #AFB6C1;
  font-family: TT Norms Medium;
}
.status-option:hover{
  color: #535C69;
  cursor: pointer;
}
.status-select{
  position: relative;
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}
.done{
  background-color: #00A490;
}
.new{
  background-color: #28CCF0;
}
.adopted{
  background-color: #F7D37D;
}
.canceled{
  background-color: #F97F7F;
}
.verticalStatus{
  height: 100%;
  width: 2px;
}
.client_container{
  display: flex;
  gap: 5px;
}
.all-request{
  display: flex;
  height: 170px;
  background-color: white;
  transition: all .2s ease;
}

.all-request:hover{
  background-color: #FAFAFA;
}
.main_card{
    width: 100%;
    padding: 20px 10px;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: 1fr;
    align-items: center;
    gap: 10px;
}
.mark_container{
  display: flex;
  align-items: center;
  gap: 20px;
}
.mark{
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  user-select:none;
}
.mark_active{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 16px;
  height: 16px;
  border-radius: 3px;
  border: 1px solid #C6CBD2;
  cursor: pointer;
  background: #6266EA;
  user-select:none;
}
.text_container{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14.16px;
  text-align: left;
  color: #FFFFFF;

  display: flex;
  justify-content: center;
  align-items: center;
  width: 66px;
  height: 25px;
  border-radius: 3px;
  background: #00A490;
}
p {
  margin: 0;
}
.date_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
}
.client_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;  
}
.container{
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.client_subtext{
  font-family: TT Norms light;
  font-size: 10px;
  line-height: 14px;
  text-align: left;
  color: #535C69;
}
.keys{
  display: flex;
  gap: 10px;
}
</style>