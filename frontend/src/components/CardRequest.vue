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
        <div class="status-select" @click="statusDrop = true">
          <div>
            <p class="text_container" v-if="requestData.status === 'New'" style="background-color: #28CCF0;">Новые</p>
            <p class="text_container" v-else-if="requestData.status === 'Adopted'" style="background-color: #F7D37D;">Принят</p>
            <p class="text_container" v-else-if="requestData.status === 'Canceled'" style="background-color: #F97F7F;">Отменен</p>
            <p class="text_container" v-else-if="requestData.status === 'Done'" style="background-color: #00A490;">Завершен</p>
          </div>
          <img :class="{'statusDropClosed' : !statusDrop, 'statusDropOpened' : statusDrop}" src="../../static/img/arrow-down.png" alt="">
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
        <p class="client_text">{{ client.firstname + ' ' + client.secondname }}</p>
        <div class="client_container">
          <p class="client_text">{{ client.phone }}</p>
          <img src="../../static/img/copy.svg" alt="">
        </div>
        <div class="client_container">
          <p class="client_text">#{{ client.id }}</p>
          <img src="../../static/img/copy.svg" alt="">
        </div>
      </div>
      <div class="container">
        <div class="client_wrapper">
          <p class="client_subtext">Сотрудник</p>
          <p class="client_text">{{ sotrudnik.firstname + ' ' + sotrudnik.secondname }}</p>
        </div>
        <div class="client_wrapper">
          <p class="client_subtext">Название услуги</p>
          <p class="client_text">{{ usluga.name }}</p>
        </div>
        <div class="client_wrapper">
          <p class="client_subtext">Стоимость</p>
          <p class="client_text">{{ usluga.cost }}</p>
        </div>
      </div>
      <div class="keys">
        <svg id="edit" @click="this.$router.push({ name: `edit`, params: { clientId: human.id, clientDataToEdit: human }})" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="16" height="16" fill="white"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M7.05788 0.400024C6.84974 0.400024 6.68102 0.56875 6.68102 0.776884V2.19817C6.09375 2.34332 5.53152 2.57563 5.01308 2.88734L4.01148 1.88314C3.94083 1.81232 3.84493 1.77249 3.7449 1.77242C3.64486 1.77236 3.54891 1.81207 3.47817 1.8828L1.8828 3.47817C1.81207 3.54891 1.77236 3.64486 1.77242 3.7449C1.77249 3.84493 1.81232 3.94083 1.88314 4.01148L2.88734 5.01308C2.57563 5.53152 2.34332 6.09375 2.19817 6.68102H0.776884C0.56875 6.68102 0.400024 6.84974 0.400024 7.05788V8.94217C0.400024 9.15031 0.56875 9.31903 0.776884 9.31903H2.19817C2.34332 9.90629 2.57563 10.4685 2.88734 10.987L1.88314 11.9886C1.81232 12.0592 1.77249 12.1551 1.77242 12.2552C1.77236 12.3552 1.81207 12.4511 1.8828 12.5219L3.47817 14.1172C3.54891 14.188 3.64486 14.2277 3.7449 14.2276C3.84493 14.2276 3.94083 14.1877 4.01148 14.1169L5.01308 13.1127C5.53152 13.4244 6.09375 13.6567 6.68102 13.8019V15.2232C6.68102 15.4313 6.84974 15.6 7.05788 15.6H8.94217C9.15031 15.6 9.31903 15.4313 9.31903 15.2232V13.8019C9.90629 13.6567 10.4685 13.4244 10.987 13.1127L11.9886 14.1169C12.0592 14.1877 12.1551 14.2276 12.2552 14.2276C12.3552 14.2277 12.4511 14.188 12.5219 14.1172L14.1172 12.5219C14.188 12.4511 14.2277 12.3552 14.2276 12.2552C14.2276 12.1551 14.1877 12.0592 14.1169 11.9886L13.1127 10.987C13.4244 10.4685 13.6567 9.90629 13.8019 9.31903H15.2232C15.4313 9.31903 15.6 9.15031 15.6 8.94217V7.05788C15.6 6.84974 15.4313 6.68102 15.2232 6.68102H13.8019C13.6567 6.09375 13.4244 5.53152 13.1127 5.01308L14.1169 4.01148C14.1877 3.94083 14.2276 3.84493 14.2276 3.7449C14.2277 3.64486 14.188 3.54891 14.1172 3.47817L12.5219 1.8828C12.4511 1.81207 12.3552 1.77236 12.2552 1.77242C12.1551 1.77249 12.0592 1.81232 11.9886 1.88314L10.987 2.88734C10.4685 2.57563 9.90629 2.34332 9.31903 2.19817V0.776884C9.31903 0.56875 9.15031 0.400024 8.94217 0.400024H7.05788ZM5.36201 8.00002C5.36201 6.54309 6.54309 5.36201 8.00002 5.36201C9.45696 5.36201 10.638 6.54309 10.638 8.00002C10.638 9.45696 9.45696 10.638 8.00002 10.638C6.54309 10.638 5.36201 9.45696 5.36201 8.00002Z" fill="#D2D8DE"/>
        </svg>

        <svg id="copy" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M9.33058 2.4H2.85124C2.59563 2.4 2.38843 2.60893 2.38843 2.86666V9.4C2.38843 9.65773 2.59563 9.86666 2.85124 9.86666H9.33058C9.58617 9.86666 9.79339 9.65773 9.79339 9.4V2.86666C9.79339 2.60893 9.58617 2.4 9.33058 2.4ZM2.85124 1C1.82883 1 1 1.83574 1 2.86666V9.4C1 10.4309 1.82883 11.2667 2.85124 11.2667H9.33058C10.353 11.2667 11.1818 10.4309 11.1818 9.4V2.86666C11.1818 1.83574 10.353 1 9.33058 1H2.85124Z" fill="#D2D8DE"/>
          <path fill-rule="evenodd" clip-rule="evenodd" d="M4.81812 12.2001V13.1334C4.81812 14.1644 5.64695 15.0001 6.66936 15.0001H13.1487C14.1711 15.0001 14.9999 14.1644 14.9999 13.1334V6.60006C14.9999 5.56913 14.1711 4.7334 13.1487 4.7334H12.2231V6.1334H13.1487C13.4043 6.1334 13.6115 6.34233 13.6115 6.60006V13.1334C13.6115 13.3911 13.4043 13.6001 13.1487 13.6001H6.66936C6.41375 13.6001 6.20655 13.3911 6.20655 13.1334V12.2001H4.81812Z" fill="#D2D8DE"/>
        </svg>

        <svg id="delete" @click="toggleModal" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M3.36363 1.77778C3.36363 1.34822 3.72994 1 4.18181 1H11.8182C12.2701 1 12.6364 1.34822 12.6364 1.77778C12.6364 2.20733 12.2701 2.55556 11.8182 2.55556H4.18181C3.72994 2.55556 3.36363 2.20733 3.36363 1.77778ZM2.81818 5.66667H2V4.11111H14V5.66667H13.1818V12.1481C13.1818 13.7232 11.8387 15 10.1818 15H5.81818C4.16132 15 2.81818 13.7232 2.81818 12.1481V5.66667ZM11.5455 5.66667H4.45455V12.1481C4.45455 12.8641 5.06508 13.4444 5.81818 13.4444H10.1818C10.9349 13.4444 11.5455 12.8641 11.5455 12.1481V5.66667Z" fill="#D2D8DE"/>
        </svg>
      </div>
    </div>
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
    <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
          <div class="modal-content">
            <p class="text-header">Удалить заявку #{{ target }}?</p>
            <p class="modal-subtext">Важно отметить, что заявку после <br> удаления невозможно восстановить</p>
            <div class="btn_container">
              <button class="btn-delete"  @click="delete_request(requestData.id)">Удалить</button>
              <button class="btn-exit" @click="this.showModal = !this.showModal">Отмена</button>
            </div>
          </div>
    </div>
    <MessageAlert :message="alertMessage" :color="alertColor"/>
  </div>
</template>

<script>
import MessageAlert from "../components/MessageAlert.vue";
import axios from 'axios';
import { mapMutations } from 'vuex';
export default {
  props: ['requestData'],
  components: { MessageAlert },
  data() {
      return {
        Mark: false,
        statusDrop: false,
        showModal: false,
        alertColor: '',
        alertMessage: '',

        client: {},
        sotrudnik: {},
        usluga: {},
      }
  },
  methods:{
    ...mapMutations(['setUpdateSidebar']),
      rerenderSidebar() {
        this.setUpdateSidebar();
      },
    toggleModal() {
      this.showModal = !this.showModal
      this.target = this.requestData.id;
    },
    toggleStatusDropdown(){
      this.statusDrop = !this.statusDrop;
    },
    async getusluga(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_uslugabyid/?variable=${id}`);
            this.usluga = response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Услуге:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async getemployee(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_employeebyid/?variable=${id}`);
            this.sotrudnik = response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Сотруднике:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async getclient(i) {
        try {
            const id = i;
            const response = await axios.get(`http://127.0.0.1:8000/api/get_clientbyid/?variable=${id}`);
            this.client = response.data;
        } catch (error) {
            console.error('Ошибка при получении данных о Клиенте:', error);
            throw error; // throw error, чтобы предоставить возможность обработки ошибки вверх по стеку вызовов
        }
    },
    async set_status(id, status) {
      if (this.requestData.status === status) {
        this.alertMessage = 'Данный статус уже установлен';
        this.alertColor = '#F97F7F';
        setTimeout(() => {
          this.alertMessage = '';
          this.alertColor = '#F97F7F';
        }, 3000);
      }else{
        const formData = new FormData();
        formData.append('id', id);  
        formData.append('status', status)
        axios.post('http://127.0.0.1:8000/api/set_status/', formData)
          .then(response => {
            console.error(response);
            this.$emit('changed', { id, status });
            this.rerenderSidebar();
            this.statusDrop = false;
          })
          .catch(error => {
            console.error('Error set_status:', error);
            this.statusDrop = false;
            this.alertMessage = 'Произошла ошибка при смене статуса заявки #' + id;
              this.alertColor = '#F97F7F';
              setTimeout(() => {
                this.alertMessage = '';
                this.alertColor = '#F97F7F';
              }, 3000);
          });
      }
      
    },
    async delete_request(id) {
      const formData = new FormData();
      formData.append('id', id);
      axios.post('http://127.0.0.1:8000/api/delete_request/', formData)
        .then(response => {
          console.log('Request deleted:', response.data);
          this.showModal = !this.showModal
          this.$emit('deleted')
        })
        .catch(error => {
          console.error('Error deleting request:', error);
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
  },
  mounted(){
    this.getclient(this.requestData.client);
    this.getemployee(this.requestData.employee);
    this.getusluga(this.requestData.usluga)
  }
}
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
.btn_container{
    margin-top: 30px;
    display: flex;
    gap: 10px;
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
  
.btn-delete{
  color: #F97F7F;
  background-color: rgba(249, 127, 127, 0.2);
}
.btn-delete:hover{
  background: #F97F7F;
  color: #FFFFFF;
}
.btn-exit{
  color: #535C69;
  border: 1px solid #DDE1E5;
  background: #FFFFFF;  
  transition: background-color 0.3s, border-color 0.3s, color 0.3s;
}
.btn-exit:hover{
  border: 1px solid #AFB6C1;
  background: #F5F5F5;
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

#edit path,#copy path,#delete path{
  fill: #D2D8DE;
  transition: all .2s ease;
}

#edit:hover path, #copy:hover path{
  fill: #535C69;
}

#delete:hover path{
  fill: #F97F7F;
}
.statusDropClosed{
  filter: brightness(100%);
  rotate: 0;
  transition: .3s ease all;
}

.statusDropOpened{
  filter: brightness(50%);
  rotate: 180deg;
  transition: .3s ease all;
}
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
    grid-template-columns: repeat(4, 1fr) 80px;
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
  cursor: pointer;
}
</style>