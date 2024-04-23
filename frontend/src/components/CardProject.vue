<template>
  <div>
    <div class="service_card">
      <div class="card-container">
        <div class="main_container">
          <div class="main_wrapp">
            <div class="card_img" v-if="isActive">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 1C1.89543 1 1 1.89543 1 3V16C1 17.1046 1.89543 18 3 18H17C18.1046 18 19 17.1046 19 16V5C19 3.89543 18.1046 3 17 3H8C8 1.89543 7.10457 1 6 1H3Z" fill="white"/>
              </svg> 
            </div>
            <div v-else class="avatar" :style="{ 'background-color': ProjectData.colour }">
              <p class="avatar_text">{{ formatText(ProjectData.name) }}</p>
            </div>
            <div class="main_text">
              <p class="main_header">{{ ProjectData.name || 'NaN' }}</p>
              <p class="main_subheader">ID {{ ProjectData.id || 'NaN' }}</p>
            </div>
          </div>
          <div class="checkmark" v-if="!isActive" @click="toggleModal(ProjectData)">
            <svg width="15" height="15" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="white"/>
            </svg>
          </div>
          <div class="active-checkmark" v-else @click="deactivateProject">
            <svg width="15" height="15" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="white"/>
            </svg>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ ProjectData.services || 'NaN' }}</p>
            <p class="text-subheader">Количество услуг</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ ProjectData.filials || 'NaN' }}</p>
              <p class="text-subheader">Количество филиалов</p>
            </div>
          </div>
        </div>
        <div class="cards">
          <div class="text-container">
            <p class="text-header">{{ ProjectData.employees || 'NaN' }}</p>
            <p class="text-subheader">Сотрудников</p>
          </div>
          <div class="cards">
            <div class="text-container">
              <p class="text-header">{{ ProjectData.position || 'NaN' }}</p>
              <p class="text-subheader">Ваша роль</p>
            </div>
          </div>
        </div>  
        <div class="bottom">
          <p class="text-subheader">Последнее изменение: {{ ProjectData.editDate }} в {{ ProjectData.editTime }}</p>
          <div class="bottom_btns">
            <router-link to="/dashboard/project/edit">
              <button class="functions">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0,0,256,256" width="20" height="20"><g fill="#535c69" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(10.66667,10.66667)"><path d="M18,2l-2.41406,2.41406l4,4l2.41406,-2.41406zM14.07617,5.92383l-11.07617,11.07617v4h4l11.07617,-11.07617z"></path></g></g></svg>
                Редактировать</button>
            </router-link>
            <router-link :to="'/dashboard/project/gates/' + ProjectData.id" style="width:65%">
              <button class="functions">
                <svg width="20" height="20" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.7 3.15001C7.7 4.50311 8.7969 5.60001 10.15 5.60001C11.5031 5.60001 12.6 4.50311 12.6 3.15001C12.6 1.79691 11.5031 0.700012 10.15 0.700012C8.7969 0.700012 7.7 1.79691 7.7 3.15001Z" fill="#535C69"/>
                <path d="M2.1 2.80001H3.5V4.90001H5.6V6.30001H3.5V8.40001H2.1V6.30001H0V4.90001H2.1V2.80001Z" fill="#535C69"/>
                <path d="M13.3 9.10001C13.3 8.32681 12.6732 7.70001 11.9 7.70001H8.4C6.0804 7.70001 4.2 9.58042 4.2 11.9V12.6H13.3V9.10001Z" fill="#535C69"/>
              </svg>
                Доступы</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div :class="{'overlay-show' : showModal, 'overlay-hide' : !showModal}"></div>
      <div :class="{'modal-show' : showModal, 'modal-hide' : !showModal}">
            <div class="modal-content">
              <p class="text-header">Смена проекта</p>
              <p class="modal-subtext">Вы действительно хотите сменить <br> проект на <span>"{{ selectedProjectToChange.name }}"</span>?</p>
              <div class="btn_container">
                <button class="delete" @click="setActiveProject(selectedProjectToChange.id)">Да, сменить</button>
                <button class="exit" @click="toggleModal">Отмена</button>
              </div>
            </div>
      </div>
      <MessageAlert :message="alertMessage" :color="alertColor"/>
  </div>
  </template>
  
  <script>
  import MessageAlert from "../components/MessageAlert.vue";
  export default {
    components: {MessageAlert},
    props:['ProjectData'],
    data() {
      return {
        alertMessage: null,
        alertColor: '',
        selectedProjectToChange: '',

        showModal: false,
      };
    },
    computed: {
      isActive() {
        const a = this.$store.state.activeProjectId;
        if (a === this.ProjectData.id) {
          return true;
        } else{
          return false;
        }
      },
    },
    methods: {
      setActiveProject(projectId) {
        this.showModal = !this.showModal;
        this.$store.commit('setActiveProject', projectId);
        this.alertMessage = null;
        setTimeout(() => {
          this.alertMessage = 'Проект успешно изменен';
          this.alertColor = '#0BB6A1';
        }, 100);
      },
      deactivateProject() {
        this.$store.commit('deactivateProject');
      },

      toggleModal(project) {
        this.selectedProjectToChange = project;
        this.showModal = !this.showModal;
      },

      formatText(text) {
          return text
            .split(' ')
            .map(word => (word.length > 1 ? word.charAt(0).toUpperCase() : word.toUpperCase()))
            .join('');
      },
    }
  };
  </script>
  
  
  <style scoped>
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
  .btn_container{
    margin-top: 30px;
    display: flex;
    gap: 10px;
  }
  span{
    color: #7D838C;
  }
  .delete{
    color: #6266EA;
    background-color: #EFEFFF;
  }
  .delete:hover{
    background: #DBEAFF;
    color: #6266EA;
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
  .avatar{
    height: 32px;
    width: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 30px;
  }
  .avatar_text{
    margin: -10px;
    font-family: 'TT Norms Medium';
    width: auto;
    height: auto;
    color: #FFFFFF;
    font-size: 14px;
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
      font-size: 10px;
      line-height: 12px;
      letter-spacing: 0em;
      color: #AFB6C1;
      margin: 0;
      text-align: left;
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
    }
    .card-container{
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    p{
      margin: 0;
    }
    .cards{
      display: flex;
      gap: 10px;
      width: 100%;
    }
    .text-container{
      width: 50%;
    }
    img{
      border-radius: 5px;
    }
    .card_img{
      display: flex;
      align-items: center;
      justify-content: center;
      height: 32px;
      width: 32px;
      border-radius: 30px;
      background: #F97F7F;
    }
    .main_container{
      display: flex;
      justify-content: space-between;
      gap: 10px;
    }
    .main_header{
      font-family: 'TT Norms Medium';
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: left;
      color: #535C69;
    }
    .main_subheader{
      font-family: 'TT Norms Medium';
      font-size: 12px;
      line-height: 14px;
      letter-spacing: 0.03em;
      text-align: left;
      color: #AFB6C1;
    }
    .bottom{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .bottom_btns{
      display: flex;
      justify-content: space-between;
      gap: 20px;
    }
    .functions{
      padding: 20px 0;
      border: 1px solid #DDE1E5;
      background: #FFFFFF ;
      font-family: 'TT Norms Medium';
      font-size: 14px;
      line-height: 17px;
      letter-spacing: 0em;
      text-align: center;
      color: #535C69;
      width: 100%;
      transition: all .2s ease;
    }

    .functions svg path{
      fill: #535C69;
      transition: all .2s ease;
    }

    .functions:hover{
      border: 1px solid #6266EA;
      color: #FFFFFF;
      background: #6266EA;
    }

    .functions:hover svg path{
      fill: white;
    }


    a{
      text-decoration: none;
      width: 100%;
    }
    .main_wrapp{
      display: flex;
      gap: 10px;
    }
    .checkmark{
      width: 18px;
      height: 18px;
      background: #F3F5F6;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease
    }
    .checkmark:hover{
      background: #04C562;
      cursor: pointer;
    }

    .active-checkmark{
      width: 18px;
      height: 18px;
      background: #04C562;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease
    }
  </style>  