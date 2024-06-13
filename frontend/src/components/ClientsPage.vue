<template>
  <div class="clients">
    <p class="head">Клиенты</p>
    <div class="clients_main">
      <div class="add">
        <div class="delete" :class="{'delete-active' : clientsToDelete.length>0}" @click="toggleModal">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M11.2 11.9V4.9H2.80002V11.9C2.80002 12.6732 3.42683 13.3 4.20002 13.3H9.80002C10.5732 13.3 11.2 12.6732 11.2 11.9Z" fill="#4C5D6E33" fill-opacity="1"/>
          <path d="M5.21307 0.773901L4.55002 2.1H1.40002V3.5H12.6V2.1H9.45002L8.78698 0.7739C8.54983 0.299603 8.06506 0 7.53478 0H6.46527C5.93499 0 5.45022 0.299604 5.21307 0.773901Z" fill="#4C5D6E33" fill-opacity="1"/>
          </svg>
        </div>
        <button class="client_add" @click="this.$router.push('/dashboard/clients/create')">
          <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9.00006 11V17H11.0001V11H17V9H11.0001V3H9.00006V9H3V11H9.00006Z" fill="#6266EA"/>
          </svg>
          Добавить клиента</button>
      </div>
      <div class="people">

        <div class="people_nav">
          <div class="mark" v-if="!Mark" @click="toggleAllClients"></div>
          <div class="mark_active" v-else @click="toggleAllClients">
            <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
            </svg>
          </div>
          <p class="people_nav_text">Email</p>
          <p class="people_nav_text">Добавлен</p>
          <p class="people_nav_text">Телефон</p>
          <p class="people_nav_text">Действия</p>
        </div>
        <div class="divider"></div>
        <div class="client-table" style="padding-top: 10px;">
          <div class="people_main" v-for="human in clients" :key="human.id">
            <div class="mark" v-if="!(clientsToDelete.includes(human.id))" @click="addToDel(human.id)"></div>
            <div class="checkmark_active" v-else @click="addToDel(human.id)">
              <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
              </svg>
            </div>
            <div class="people_container" @click="this.$router.push({ path: `/dashboard/clients/${human.id}/info`, params: { clientId: human.id, clientDataToEdit: human }})">
              <img src="../../static/img/data.png" alt="" class="circle">
              <div class="cont">
                <div class="wrapper">
                  <p class="people_head">{{ human.firstname + ' ' + human.secondname }}</p>
                  <img class="edit" src="../../static/img/discover.svg" alt="">
                </div>
                <p class="people_nav_texts">{{ human.mail }}</p>
              </div>
            </div>
            <p class="people_nav_text">{{ human.date }}</p>
            <div class="people_nav_text">
              <div class="copy">
                <p>{{ human.phone }}</p>
                <img src="../../static/img/copy.svg" alt="">
              </div>
            </div>
            <div class="people_nav_text">
              <div class="keys">
                <svg id="edit" @click="this.$router.push({ name: `edit`, params: { clientId: human.id, clientDataToEdit: human }})" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect width="16" height="16" fill="white"/>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M7.05788 0.400024C6.84974 0.400024 6.68102 0.56875 6.68102 0.776884V2.19817C6.09375 2.34332 5.53152 2.57563 5.01308 2.88734L4.01148 1.88314C3.94083 1.81232 3.84493 1.77249 3.7449 1.77242C3.64486 1.77236 3.54891 1.81207 3.47817 1.8828L1.8828 3.47817C1.81207 3.54891 1.77236 3.64486 1.77242 3.7449C1.77249 3.84493 1.81232 3.94083 1.88314 4.01148L2.88734 5.01308C2.57563 5.53152 2.34332 6.09375 2.19817 6.68102H0.776884C0.56875 6.68102 0.400024 6.84974 0.400024 7.05788V8.94217C0.400024 9.15031 0.56875 9.31903 0.776884 9.31903H2.19817C2.34332 9.90629 2.57563 10.4685 2.88734 10.987L1.88314 11.9886C1.81232 12.0592 1.77249 12.1551 1.77242 12.2552C1.77236 12.3552 1.81207 12.4511 1.8828 12.5219L3.47817 14.1172C3.54891 14.188 3.64486 14.2277 3.7449 14.2276C3.84493 14.2276 3.94083 14.1877 4.01148 14.1169L5.01308 13.1127C5.53152 13.4244 6.09375 13.6567 6.68102 13.8019V15.2232C6.68102 15.4313 6.84974 15.6 7.05788 15.6H8.94217C9.15031 15.6 9.31903 15.4313 9.31903 15.2232V13.8019C9.90629 13.6567 10.4685 13.4244 10.987 13.1127L11.9886 14.1169C12.0592 14.1877 12.1551 14.2276 12.2552 14.2276C12.3552 14.2277 12.4511 14.188 12.5219 14.1172L14.1172 12.5219C14.188 12.4511 14.2277 12.3552 14.2276 12.2552C14.2276 12.1551 14.1877 12.0592 14.1169 11.9886L13.1127 10.987C13.4244 10.4685 13.6567 9.90629 13.8019 9.31903H15.2232C15.4313 9.31903 15.6 9.15031 15.6 8.94217V7.05788C15.6 6.84974 15.4313 6.68102 15.2232 6.68102H13.8019C13.6567 6.09375 13.4244 5.53152 13.1127 5.01308L14.1169 4.01148C14.1877 3.94083 14.2276 3.84493 14.2276 3.7449C14.2277 3.64486 14.188 3.54891 14.1172 3.47817L12.5219 1.8828C12.4511 1.81207 12.3552 1.77236 12.2552 1.77242C12.1551 1.77249 12.0592 1.81232 11.9886 1.88314L10.987 2.88734C10.4685 2.57563 9.90629 2.34332 9.31903 2.19817V0.776884C9.31903 0.56875 9.15031 0.400024 8.94217 0.400024H7.05788ZM5.36201 8.00002C5.36201 6.54309 6.54309 5.36201 8.00002 5.36201C9.45696 5.36201 10.638 6.54309 10.638 8.00002C10.638 9.45696 9.45696 10.638 8.00002 10.638C6.54309 10.638 5.36201 9.45696 5.36201 8.00002Z" fill="#D2D8DE"/>
                </svg>
                <svg id="delete" @click="addToDel(human.id), toggleModal()" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M3.36363 1.77778C3.36363 1.34822 3.72994 1 4.18181 1H11.8182C12.2701 1 12.6364 1.34822 12.6364 1.77778C12.6364 2.20733 12.2701 2.55556 11.8182 2.55556H4.18181C3.72994 2.55556 3.36363 2.20733 3.36363 1.77778ZM2.81818 5.66667H2V4.11111H14V5.66667H13.1818V12.1481C13.1818 13.7232 11.8387 15 10.1818 15H5.81818C4.16132 15 2.81818 13.7232 2.81818 12.1481V5.66667ZM11.5455 5.66667H4.45455V12.1481C4.45455 12.8641 5.06508 13.4444 5.81818 13.4444H10.1818C10.9349 13.4444 11.5455 12.8641 11.5455 12.1481V5.66667Z" fill="#D2D8DE"/>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
    <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
          <div class="modal-content">
            <p class="text-header">Удаление услуги</p>
            <p v-if="clientsToDelete.length > 1" class="modal-subtext">Вы действительно хотите удалить выбранных клиентов?</p>
            <p v-else class="modal-subtext">Вы действительно хотите удалить клиента <br> <span>{{ target }}</span>?</p>
            <div class="btn_container">
              <button class="btn-delete"  @click="deleteSelectedClients">Удалить</button>
              <button class="btn-exit" @click="toggleModal">Отмена</button>
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
      Mark: false,
      showModal: false,
      clients: {},
      clientsToDelete: [],
      target: 'Client name',
    }
  },
  methods:{
    toggleModal() {
      if (this.clientsToDelete.length>0) {
        this.showModal = !this.showModal
        if (this.clientsToDelete.length == 1) {
          let targetClient = this.clients.find(client => client.id === this.clientsToDelete[0]);
          this.target = targetClient.firstname + ' ' + targetClient.secondname;
        }
      }
      
    },
    async get_client(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/get_client/?project=${this.$store.state.activeProjectId}`);
        this.clients = response.data;
        this.$store.commit('addClients', response.data)
      } catch (error) {
        console.error('Error fetching clients:', error);
      }
    },
    addToDel(id) {
      const index = this.clientsToDelete.indexOf(id);
      if (index === -1) {
        this.clientsToDelete.push(id);
      } else {
        this.clientsToDelete.splice(index, 1);
      }
    },
    toggleAllClients() {
      const clientIds = Object.keys(this.clients).map(Number);
      const allClientsSelected = clientIds.every(id => this.clientsToDelete.includes(id));

      if (allClientsSelected) {
        this.clientsToDelete = [];
        this.Mark = false;
      } else {
        this.clientsToDelete = [...new Set([...this.clientsToDelete, ...clientIds])];
        this.Mark = true;
      }
    },
    deleteSelectedClients(){
      for(let i of this.clientsToDelete){
        console.log(i)
        this.deleteClient(i)
      }
      this.clientsToDelete = [];
      this.toggleModal();
    },
    async deleteClient(clientId) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/client/delete/', {
          id: clientId
        }, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        });
        if (response.data.message) {
          this.get_client();
        }
      } catch (error) {
        console.error('Произошла ошибка при удалении клиента:', error);
      }
    }
  },
  mounted(){
    this.get_client();
  }
}
</script>

<style scoped>
span{
    color: #7D838C;
  }
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

.client-table{
  height: fit-content;
  overflow-y: scroll;
  max-height: 65vh;
}
#edit, #delete{
  cursor: pointer;
}

#edit path, #delete path{
  fill: #D2D8DE;
  transition: all .2s ease;
}

#edit:hover path{
  fill: #AFB6C1;
}

#delete:hover path{
  fill: #F97F7F;
}


.head{
  font-family: TT Norms Medium;
  font-size: 20px;
  line-height: 23.6px;
  text-align: left;
  color: #535C69;
}
.clients{
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.clients_main{
  height: fit-content;
  max-height: 100%;
  background: #FFFFFF;
  padding: 20px;
  border-radius: 5px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.delete{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 3px;
  border: 1px solid #F3F5F6;
}

.delete-active{
  cursor: pointer;
  border: 1px solid #D2D8DE;
  transition: all .2s ease;
}

.delete svg path{
  fill: #4C5D6E33;
  transition: all .2s ease;
}

.delete-active svg path{
  fill: #F97F7F;
}
.add{
  display: flex;
  justify-content: space-between;
}
.client_add{
  background: #EFEFFF;
  color: #6266EA;
  transition: all 0.3s ease;
}
.client_add:hover{
  background: #464AD9;
  color: #FFFFFF;
}
.status{
  display: flex;
  gap: 50px;
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
.people_nav_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #AFB6C1;
  display: flex;
  align-items: center;
  justify-content: start;
}
.people_nav_texts{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #AFB6C1;
  cursor: pointer;
}
.people_nav{
  align-items: center;
  display: grid;
  grid-template-columns: .2fr repeat(3, 1fr) .2fr;  
  grid-template-rows: 1fr;
  padding: 0 10px;
  margin-bottom: 10px;
}
.people_main{
  align-items: center;
  display: grid;
  grid-template-columns: .2fr repeat(3, 1fr) .2fr; 
  grid-template-rows: 1fr;
  padding: 10px;
  border-bottom: 1px solid #F5F5F5;
  transition: all .1s ease;
}
.people_main:hover{
  background-color: #FAFAFA;
}
p{
  margin: 0;
}
.divider {
  border-bottom: 1px solid #F5F5F5; 
  width: auto;
  margin: 0;
}
.checkmark_active{
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
.people_head{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16.52px;
  text-align: left;
  color: #535C69;
  cursor: pointer;
}
.checkmark{
  display: flex;
  align-items: center;
  gap: 50px;
}
.wrapper{
  display: flex;
  gap: 5px;
}
.people_container{
  display: flex;
  gap: 10px;
}
.circle{
  width: 32px;
  height: 32px;
  border-radius: 30px;
}
.copy{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}
.keys{
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
.edit{
  cursor: pointer;
}
</style>