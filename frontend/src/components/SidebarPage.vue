<template>
  <div class="sidebar">
    <div class="main_side">
      <router-link to="/lk/service">
        <img src="../../static/img/logo.svg"  id="desktopLink" alt="" class="logotype">
      </router-link>
      <div class="mobile-logo">
        <router-link to="/lk/service">
          <img src="../../static/img/LogoMobile.svg" id="mobileLogo" alt="" class="logotype">
        </router-link>
      </div>
      <div class="content">
        <div class="top-group">
          <div class="cards-group">
            <router-link to="/lk/service" class="main_text" :class="{ active: $route.path === '/lk/service'}">
              <div class="main_menu">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M10 12H19V14H10V12Z" fill="#6266EA"/>
                  <path d="M10 16H16V18H10V16Z" fill="#6266EA"/>
                  <path d="M1 13C1 12.4477 1.44772 12 2 12H7C7.55228 12 8 12.4477 8 13V18C8 18.5523 7.55228 19 7 19H2C1.44772 19 1 18.5523 1 18V13Z" fill="#6266EA"/>
                  <path d="M10 5H16V7H10V5Z" fill="#6266EA"/>
                  <path d="M10 1H19V3H10V1Z" fill="#6266EA"/>
                  <path d="M1 2C1 1.44772 1.44772 1 2 1H7C7.55228 1 8 1.44772 8 2V7C8 7.55228 7.55228 8 7 8H2C1.44772 8 1 7.55228 1 7V2Z" fill="#6266EA"/>
                </svg>
                  
                <p class="main_text">Услуги</p>
              </div>
            </router-link>
            <router-link :to="!uslugi.length > 0 ? '/lk/locked' : '/lk/personal'" class="main_text" :class="{ active: $route.path === '/lk/personal' }">
              <div :class="{'disabled-menu' : !uslugi.length > 0, 'main_menu' : uslugi.length > 0}">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M16 6.5C16 7.88071 14.8807 9 13.5 9C12.1193 9 11 7.88071 11 6.5C11 5.11929 12.1193 4 13.5 4C14.8807 4 16 5.11929 16 6.5Z" fill="#6266EA"/>
                  <path d="M7 11H2C0.895431 11 0 11.8954 0 13V18H13V17C13 13.6863 10.3137 11 7 11Z" fill="#6266EA"/>
                  <path d="M20 16C20 13.2386 17.7614 11 15 11H10C13 11 16 13.4558 16 17.2792V18H20V16Z" fill="#6266EA"/>
                  <path d="M9 5.5C9 7.433 7.433 9 5.5 9C3.567 9 2 7.433 2 5.5C2 3.567 3.567 2 5.5 2C7.433 2 9 3.567 9 5.5Z" fill="#6266EA"/>
                </svg>
                <p class="main_text">Сотрудники</p>
              </div>
            </router-link>
            <router-link :to="!employees.length > 0 || !uslugi.length > 0 ? '/lk/locked' : '/lk/branch'" class="main_text" :class="{ active: $route.path === '/lk/branch' }">
              <div :class="{'disabled-menu' : !employees.length > 0, 'main_menu' : employees.length > 0}">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M5 4V3.5C5 1.84315 6.34315 0.5 8 0.5H12C13.6569 0.5 15 1.84315 15 3.5V4H18C19.1046 4 20 4.89543 20 6V16C20 17.1046 19.1046 18 18 18H2C0.895431 18 0 17.1046 0 16V6C0 4.89543 0.895431 4 2 4H5ZM7 3.5C7 2.94772 7.44772 2.5 8 2.5H12C12.5523 2.5 13 2.94772 13 3.5V4H7V3.5ZM10 10C10.8284 10 11.5 9.32843 11.5 8.5C11.5 7.67157 10.8284 7 10 7C9.17157 7 8.5 7.67157 8.5 8.5C8.5 9.32843 9.17157 10 10 10Z" fill="#6266EA"/>
                </svg>
                <p class="main_text">Филиалы</p>
              </div>
            </router-link>
          </div>
          <div class="line"></div>
          <div class="cards-group">
            <router-link  :to="!employees.length > 0 || !uslugi.length > 0 || !filials.length > 0 ? '/lk/locked' : '/lk/widgets'" class="main_text" :class="{ active: $route.path === '/lk/widgets' }">
              <div :class="{'disabled-menu' : !filials.length > 0, 'main_menu' : filials.length > 0}">
                <svg width="16" height="16" viewBox="0 0 16 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M8 2.1C4.48183 2.1 1.6 4.98183 1.6 8.5C1.6 12.0182 4.48183 14.9 8 14.9V16.5C3.59817 16.5 0 12.9018 0 8.5C0 4.09817 3.59817 0.5 8 0.5C12.4018 0.5 16 4.09817 16 8.5C16 12.7506 14 15.7 11.2 15.7C8.8 15.7 7.2 13.46 7.2 10.9H6.39998C5.51632 10.9 4.79998 10.1836 4.79998 9.29997L4.79999 6.89998H5.93488V4.66746C5.93488 4.31809 6.21808 4.03489 6.56744 4.03489C6.91679 4.03489 7.19999 4.31809 7.19999 4.66746V6.89998H8.79999V4.66746C8.79999 4.31809 9.08319 4.03489 9.43256 4.03489C9.7819 4.03489 10.0651 4.31809 10.0651 4.66746V6.89998H11.2V9.29998C11.2 10.1836 10.4836 10.9 9.59999 10.9H8.8C8.8 13.3 10 14.1 11.2 14.1C12.8 14.1 14.4 12.3854 14.4 8.5C14.4 4.98183 11.5182 2.1 8 2.1Z" fill="#6266EA"/>
                </svg>
                <p class="main_text">Виджеты</p>
              </div>
            </router-link>
            <router-link to="/lk/calendar" class="main_text" :class="{ active: $route.path === '/main/calendar' }">
              <div class="main_menu">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M5 5V0H7V5H5Z" fill="#6266EA"/>
                  <path d="M13 5V0H15V5H13Z" fill="#6266EA"/>
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M2 19C1.44772 19 1 18.5523 1 18V3C1 2.44772 1.44772 2 2 2H4V6H8V2H12V6H16V2H18C18.5523 2 19 2.44772 19 3V18C19 18.5523 18.5523 19 18 19H2ZM17 17V8H3V17H17Z" fill="#6266EA"/>
                </svg>
                <p class="main_text">Календарь</p>
              </div>
            </router-link>
            <router-link to="/lk/clients" class="main_text" :class="{ active: $route.path === '/main/clients' }">
              <div class="main_menu">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M16 6.5C16 7.88071 14.8807 9 13.5 9C12.1193 9 11 7.88071 11 6.5C11 5.11929 12.1193 4 13.5 4C14.8807 4 16 5.11929 16 6.5Z" fill="#6266EA"/>
                  <path d="M7 11H2C0.895431 11 0 11.8954 0 13V18H13V17C13 13.6863 10.3137 11 7 11Z" fill="#6266EA"/>
                  <path d="M20 16C20 13.2386 17.7614 11 15 11H10C13 11 16 13.4558 16 17.2792V18H20V16Z" fill="#6266EA"/>
                  <path d="M9 5.5C9 7.433 7.433 9 5.5 9C3.567 9 2 7.433 2 5.5C2 3.567 3.567 2 5.5 2C7.433 2 9 3.567 9 5.5Z" fill="#6266EA"/>
                </svg>
                <p class="main_text">Клиенты</p>
              </div>
            </router-link>
            <router-link to="/lk/statistics" class="main_text" :class="{ active: $route.path === '/main/statistics' }">
              <div class="main_menu">
                <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M15.9667 1L9.00006 1.03317L11.783 3.8029L7.00008 8.5858V13.5858L2.29297 18.2929L3.70718 19.7071L9.00008 14.4142V9.41423L13.2006 5.21375L16.0001 8L15.9667 1Z" fill="#6266EA"/>
                </svg> 
                <p class="main_text">Статистика</p>
              </div>
            </router-link>
          </div>
        </div>
            <div class="cards-group">
              <div class="bottom_menu" id="zayavki" style="cursor:pointer">
                <div class="left">
                  <svg width="16" height="16" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2 16.4627C2 17.186 2.74418 17.67 3.40538 17.3768L20 10.0179L3.4069 2.6267C2.74553 2.3321 2 2.81616 2 3.54018V7.15049C2 8.19451 2.80304 9.06289 3.84388 9.14439L15 10.0179L3.84934 10.8603C2.80618 10.9391 2 11.8085 2 12.8546V16.4627Z" fill="#6266EA"/>
                  </svg> 
                  <a href="" id="main-text" class="main_text">Заявки</a>
                </div>
                <p class="number">{{ zayavki }}</p>
              </div>
              <div class="bottom_menu" id="bottom_avatar" style="display: block;">
                <div class="avatar-top">
                  <div class="left-container" style="display: flex; align-items: center;">
                    <img class="img_profile" :src="avatar">
                    <div class="names">
                      <p id="bottom_header"> {{ name }} </p>
                      <p id="bottom_subheader"> {{ position || 'Владелец' }}</p>
                    </div>
                  </div>  
                  <div class="dropdown_btn">
                    <button @click="toggleDropdown" class="dropdown" :style="{ 'background-color': showDropdown ? '#F3F6F8' : 'transparent' }">
                      <img v-if="!showDropdown" src="../../static/img/kebab.svg" alt="Open">
                      <img v-if="showDropdown" src="../../static/img/x.svg" alt="Close" style="width: 12px; height: 12px;">
                    </button>
                    <div :class="{'dropdown-menu-show' : showDropdown, 'dropdown-menu-hide' : !showDropdown}" @click="closeDropdown">
                    <router-link to="/lk/settings" style="text-decoration:none" class="dropdown-link">
                      <div class="dropdown-item">
                        <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" clip-rule="evenodd" d="M8.82231 0.5C8.56215 0.5 8.35124 0.710907 8.35124 0.971074V2.74768C7.61716 2.92912 6.91437 3.2195 6.26632 3.60914L5.01431 2.3539C4.92601 2.26537 4.80613 2.21558 4.68109 2.2155C4.55605 2.21542 4.4361 2.26505 4.34769 2.35347L2.35347 4.34769C2.26505 4.4361 2.21542 4.55605 2.2155 4.68109C2.21558 4.80613 2.26537 4.92601 2.3539 5.01431L3.60914 6.26632C3.2195 6.91437 2.92912 7.61716 2.74768 8.35124H0.971074C0.710907 8.35124 0.5 8.56215 0.5 8.82231V11.1777C0.5 11.4379 0.710907 11.6488 0.971074 11.6488H2.74768C2.92912 12.3828 3.2195 13.0856 3.60914 13.7337L2.3539 14.9857C2.26537 15.074 2.21558 15.1939 2.2155 15.3189C2.21542 15.444 2.26505 15.5639 2.35347 15.6523L4.34769 17.6465C4.4361 17.7349 4.55605 17.7846 4.68109 17.7845C4.80613 17.7844 4.92601 17.7346 5.01431 17.6461L6.26632 16.3909C6.91437 16.7805 7.61716 17.0709 8.35124 17.2523V19.0289C8.35124 19.2891 8.56215 19.5 8.82231 19.5H11.1777C11.4379 19.5 11.6488 19.2891 11.6488 19.0289V17.2523C12.3828 17.0709 13.0856 16.7805 13.7337 16.3909L14.9857 17.6461C15.074 17.7346 15.1939 17.7844 15.3189 17.7845C15.444 17.7846 15.5639 17.7349 15.6523 17.6465L17.6465 15.6523C17.7349 15.5639 17.7846 15.444 17.7845 15.3189C17.7844 15.1939 17.7346 15.074 17.6461 14.9857L16.3909 13.7337C16.7805 13.0856 17.0709 12.3828 17.2523 11.6488H19.0289C19.2891 11.6488 19.5 11.4379 19.5 11.1777V8.82231C19.5 8.56215 19.2891 8.35124 19.0289 8.35124H17.2523C17.0709 7.61716 16.7805 6.91437 16.3909 6.26632L17.6461 5.01431C17.7346 4.92601 17.7844 4.80613 17.7845 4.68109C17.7846 4.55605 17.7349 4.4361 17.6465 4.34769L15.6523 2.35347C15.5639 2.26505 15.444 2.21542 15.3189 2.2155C15.1939 2.21558 15.074 2.26537 14.9857 2.3539L13.7337 3.60914C13.0856 3.2195 12.3828 2.92912 11.6488 2.74768V0.971074C11.6488 0.710907 11.4379 0.5 11.1777 0.5H8.82231ZM6.70248 10C6.70248 8.17883 8.17883 6.70248 10 6.70248C11.8212 6.70248 13.2975 8.17883 13.2975 10C13.2975 11.8212 11.8212 13.2975 10 13.2975C8.17883 13.2975 6.70248 11.8212 6.70248 10Z" fill="#AFB6C1"/>
                        </svg> 
                        <p class="dropdown-header">Настройка профиля</p>
                      </div>
                    </router-link>
                    <router-link to="#" style="text-decoration:none" class="dropdown-link">
                      <div class="dropdown-item">
                        <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" clip-rule="evenodd" d="M17 4.00006H2.5L15 6.10352e-05L17 4.00006Z" fill="#AFB6C1"/>
                          <path d="M1 8.00012C1 6.89555 1.89543 6.00012 3 6.00012H17C18.1046 6.00012 19 6.89555 19 8.00012V11H15.6666C14.7222 11 14 11.65 14 12.5C14 13.35 14.7222 14 15.6666 14H19V17.0001C19 18.1047 18.1046 19.0001 17 19.0001H3C1.89543 19.0001 1 18.1047 1 17.0001V8.00012Z" fill="#AFB6C1"/>
                        </svg>
                        <p class="dropdown-header">Тарифный план</p>
                      </div>
                    </router-link>
                    <router-link to="#" style="text-decoration:none" class="dropdown-link">
                      <div class="dropdown-item" id="logout">
                        <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <g clip-path="url(#clip0_767_17838)">
                          <path d="M13.332 17.5H17.1578C17.3459 17.4995 17.4982 17.3472 17.4987 17.1592V2.84082C17.4982 2.65277 17.3459 2.50043 17.1578 2.5H13.332C12.6417 2.5 12.082 1.94035 12.082 1.25C12.082 0.559648 12.6417 0 13.332 0H17.1578C18.726 0.00183594 19.9968 1.27266 19.9987 2.84082V17.1591C19.9968 18.7273 18.726 19.9982 17.1578 20H13.332C12.6417 20 12.082 19.4404 12.082 18.75C12.082 18.0596 12.6416 17.5 13.332 17.5Z" fill="#F97F7F"/>
                          <path d="M1.2487 8.75L12.6154 8.7725L9.72707 5.88417C9.23875 5.39609 9.23855 4.60457 9.72663 4.11625C10.2147 3.62792 11.0062 3.62773 11.4946 4.11582L14.7271 7.34832C16.1916 8.81277 16.1916 11.1871 14.7271 12.6516L14.7271 12.6516L11.4946 15.8841C11.0062 16.3722 10.2147 16.372 9.72663 15.8837C9.23855 15.3954 9.23875 14.6039 9.72707 14.1158L12.5712 11.2725L1.2487 11.25C0.558353 11.2486 -0.000161171 10.6878 0.0012064 9.9975C0.00257301 9.30714 0.563354 8.74863 1.25371 8.75H1.2487Z" fill="#F97F7F"/>
                          </g>
                          <defs>
                          <clipPath id="clip0_767_17838">
                          <rect width="20" height="20" fill="white" transform="matrix(-1 0 0 1 20 0)"/>
                          </clipPath>
                          </defs>
                        </svg>
                        <div class="dropdown-subheader" @click="logout">Выйти из аккаунта</div>
                      </div>
                    </router-link>
                    </div>
                  </div>
                </div>
                <div class="avatar-bottom">
                  <img src="../../static/img/Union.png" alt="">
                  <p id="bottom_sub_text">{{ company }}</p>
                </div>
              </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';  
import { mapState } from 'vuex';


export default {
  data() {
    return {
      showDropdown: false,
      name: "",
      position: '',
      avatar: "",
      company:"",
      zayavki: '2', // сделать кол-во заявок

      uslugi: [],
      employees: [],
      filials: [],
    };
  },
  computed: {
      userData() {
        return this.$store.getters.getRegistrationData;
      },
      ...mapState(['updateSidebar']),
    },
    watch: {
      updateSidebar() {
        this.get_profile();
        this.getfilials();
        this.get_uslugi();
        this.get_employee();
      },
    },
  methods: {

    async getfilials(){
      axios.get(`http://127.0.0.1:8000/api/get_branch/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`)
        .then(response => {
            this.filials = response.data;
            this.filials.reverse();
            console.log(response);
        })
        .catch(error => {
            console.error('Ошибка при получении данных о пользователе:', error);
        });
    },

    async get_uslugi(){
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/uslugi/?variable=${this.$store.state.registrationData.user_id}&project=${this.$store.state.activeProjectId}`);
        this.uslugi = response.data;
        this.uslugi.reverse();
      } catch (error) {
        console.error('Error fetching uslugi:', error);
      }
    },
    async get_employee(){
              const user_id =  this.$store.state.registrationData.user_id;// Замените на актуальный user_id
  
      // Выполняем запрос к API Django
      axios.get(`http://127.0.0.1:8000/api/get_employees/?user_id=${user_id}&project=${this.$store.state.activeProjectId}`)
        .then(response => {
          this.employees = response.data; // Сохраняем полученные данные в переменной
          this.employees.reverse();
          console.log(this.employees);
        })
        .catch(error => {
          console.error('Error fetching employees:', error);
        });
    },
    get_profile(){
      console.log(this.updateSidebar)
      axios.post('http://127.0.0.1:8000/api/getprofile/', { user_id:  this.$store.state.registrationData.user_id})
      .then(response => {
        this.avatar = "http://127.0.0.1:8000" + response.data.profile.avatar
        console.log(this.avatar)
        this.name = response.data.profile.name
        // this.position = response.data.profile.name // сделать должность
        this.company = response.data.profile.company_name
      })
      .catch(error => {
        // Ошибка при получении данных
        console.error('Ошибка при получении данных о пользователе:', error);
      });
    },
 
    closeDropdown() {
      this.showDropdown = false;
    },
                                              
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    logout() {
        // Вызываем действие clearRegistrationData для очистки данных из Vuex
        this.$store.dispatch('clearRegistrationData');
        this.$router.push('/');
      },
  },
  mounted(){  
    this.get_profile();
    this.get_uslugi();
    this.get_employee();
    this.getfilials();
  }
};
</script>

<style scoped>
.disabled-menu{
    text-align: left;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 0px 20px;
    transition: all .2s ease;
    background-color: transparent;
    border-radius: 5px;
    margin-bottom: 10px;
    gap: 10px;
}

.disabled-menu:hover{
  background: white;
}

.disabled-menu p{
  color: #9da0a4;
}

.disabled-menu svg path{
  fill: #888cff;
}

.dropdown-link:hover .dropdown-item p{
  color: #535C69;
}

.dropdown-link .dropdown-item p{
  transition: all .2s ease;
}

.dropdown-link:hover .dropdown-item svg path{
  fill: #535C69;
}

.dropdown-link:hover #logout div{
  color: #f20808;
}

.dropdown-link:hover #logout svg path{
  fill: #f20808;
}

.dropdown-link .dropdown-item div{
  transition: all .2s ease;
}

.dropdown-link .dropdown-item svg path{
  transition: all .2s ease;
}

.dropdown-link:hover #logout p{
  transition: all .2s ease;
}

.dropdown-link:hover #logout svg path{
  transition: all .2s ease;
}
.avatar-bottom{
  margin-top: 10px;
  background-color: #fafafa;
  padding: 2px;
  display: flex;
  align-items: center;
  gap: 10px;
}
#bottom_header{
  color: #535C69;
}

#bottom_header, #bottom_subheader, #bottom_sub_text{
  
  background-color: transparent;
  margin: 0;
  padding: 0;
  user-select:none;
}
.avatar-top{
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sidebar{
  padding: 20px;
  height: 100vh;
}
.content{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}
.line{
  width: 100%;
  height: 1px;
  background-color: #E4EAEF;
}
.cards-group{
  margin: 20px 0;
}
.main_side {
    padding: 20px;
    background-color: #F3F6F8;
    width: 260px;
    border-radius: 10px;
    height: 100%;
    top: 0;
    left: 0;  
  }
.main_text{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: 0em;
  text-align: center;
  text-decoration: none;
  color: #535C69;
}

.main_menu{
    text-align: left;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 0px 20px;
    transition: all .2s ease;
    background-color: transparent;
    border-radius: 5px;
    margin-bottom: 10px;
    gap: 10px;
}

.main_menu:hover{
  background-color: white;
  cursor: pointer;
}

.main_logo {
    margin-right: 10px
}

.left{
  display: flex;
  align-items: center;
  gap: 10px;
}
.bottom_menu{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 20px;
  margin: 10px 0;
  transition: all .2s ease;
  text-align: left;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 5px;
}
.bottom_menu:hover{
  background-color: rgba(255, 255, 255, 1);
}

#bottom_header{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
  margin-bottom: 5px;
}
#bottom_subheader{
  font-family: TT Norms Light;
  font-size: 12px;
  font-weight: 300;
  line-height: 12px;
  letter-spacing: 0em;
  color: #535C69;
}
#bottom_sub_text{
  font-family: TT Norms Medium;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: left;
  color:#AFB6C1;
  width: 100%;
  display: flex;
  align-items: center;
}

.active .main_menu {
  background-color: white;
}
.dropdown{
  position: relative;
  display: inline-block;
  color: #AFB6C1;
  font-size: 15px;
  background-color: white;
  width: 1em;
  height: 2em;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
  border: 1px solid #ffffff;
  transition: all .2s ease;
}
.dropdown:hover{
  border: 1px solid #535C69;
}
.dropdown-menu-show {
  width: 170px;
  height: auto;
  background-color: white;
  position: absolute;
  transform: translate(40px, -35px);
  bottom: 0;
  border: 1px solid #E4EAEF;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  text-align: left;

  opacity: 1;
  visibility: visible;
  transition: all .2s ease;
}

.dropdown-menu-hide {
  width: 170px;
  height: auto;
  background-color: white;
  position: absolute;
  transform: translate(40px, -35px);
  bottom: 0;
  border: 1px solid #E4EAEF;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  text-align: left;

  opacity: 0;
  visibility: hidden;
  transition: all .2s ease;
}

.dropdown-item {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  height: 35px;
  display: flex;
  gap: 10px;
}

.dropdown-header{
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  color: #AFB6C1;
  width: 100%;
  background: #FFFFFF;
  margin: 0;
}
.dropdown-subheader{
  font-family: TT Norms Medium;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  color: #F97F7F;
}
.dropdown-subheader:hover {
  color: #F97F7F;
}
.img_profile{
  width: 45px;
  height: 45px;
  border-radius: 25px;
}
.number{

  background-color: #EFEFFF;
  border-radius: 10px;
  color: #535C69;
  width: 20px;
  height: 20px;
  font-size: 12px;
  text-align: center;
  padding-top: 3px;
}
.mobile-logo{
  display: flex;
  justify-content: center;
}
.names{
  margin-left: 10px;
}
#bottom_avatar{
  padding: 15px 20px;
}
#mobileLogo {
    display: none;
}

@media (max-width: 1024px){
  .content{
    height: 60%;
  }
}
@media (max-width: 991px){
  .content{
    height: 65%;
  }
}
@media (max-width: 768px){
  .disabled-menu{
    text-align: left;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    transition: all .2s ease;
    background-color: transparent;
    border-radius: 5px;
    margin-bottom: 10px;
    gap: 10px;
    width: 46px;
    height: 46px;
  }

  #desktopLink {
    display: none;
  }
  #mobileLogo {
    display: block;
    margin-bottom: 30px;
  }
  #main-text{
    display: none;
  }
  #bottom_avatar{
    padding: 0;
  }
  #zayavki{
    padding: 15px;
  }
  .content{
    height: 90%;
  }
  .main_text p{
    display: none;
  }
  .main_text a{
    display: none;
  }
  .line{
    display: none;
  }
  .number{
    display: none;
  }
  .names{
    display: none;
  }
  .dropdown{
    display: none;
  }
  .avatar-bottom{
    display: none;
  }
  .cards-group{
    margin: 0;
  }
  .sidebar{
    padding: 0;
  }
  .main_side{
    width: 66px;
    padding: 20px 10px;
  }
  .bottom_menu{
    padding: 0;
    display: flex;
    justify-content: center;
  }
  .main_menu{
    padding: 15px;
    justify-content: center;
  }
}
</style>