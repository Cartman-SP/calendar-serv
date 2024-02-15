<template>
  <div class="sidebar">
    <div class="main_side">
      <router-link to="/lk/">
        <img src="../../static/img/SkedOnline.png" alt="" class="logotype">
      </router-link>
      <div class="content">
        <div class="top-group">
          <div class="cards-group">
            <router-link to="/lk/service" class="main_text" :class="{ active: $route.path === '/lk/service' }">
              <div class="main_menu">
                <img src="../../static/img/list.png" alt="" class="main_logo">
                <p class="main_text">Услуги</p>
              </div>
            </router-link>
            <router-link to="/lk/personal" class="main_text" :class="{ active: $route.path === '/lk/personal' }">
              <div class="main_menu">
                <img src="../../static/img/group.png" alt="" class="main_logo">
                <p class="main_text">Сотрудники</p>
              </div>
            </router-link>
            <router-link to="/lk/branch" class="main_text" :class="{ active: $route.path === '/lk/branch' }">
              <div class="main_menu">
                <img src="../../static/img/briefcase.png" alt="" class="main_logo">
                <p class="main_text">Филиалы</p>
              </div>
            </router-link>
          </div>
          <div class="line"></div>
          <div class="cards-group">
            <router-link to="/lk/widgets" class="main_text" :class="{ active: $route.path === '/lk/widgets' }">
              <div class="main_menu">
                <img src="../../static/img/plug.png" alt="" class="main_logo">
                <p class="main_text">Виджеты</p>
              </div>
            </router-link>
            <router-link to="/lk/calendar" class="main_text" :class="{ active: $route.path === '/main/calendar' }">
              <div class="main_menu">
                <img src="../../static/img/calendar.png" alt="" class="main_logo">
                <p class="main_text">Календарь</p>
              </div>
            </router-link>
            <router-link to="/lk/clients" class="main_text" :class="{ active: $route.path === '/main/clients' }">
              <div class="main_menu">
                <img src="../../static/img/group.png" alt="" class="main_logo">
                <p class="main_text">Клиенты</p>
              </div>
            </router-link>
            <router-link to="/lk/statistics" class="main_text" :class="{ active: $route.path === '/main/statistics' }">
              <div class="main_menu">
                <img src="../../static/img/arrow.png" alt="" class="main_logo">
                <p class="main_text">Статистика</p>
              </div>
            </router-link>
          </div>
        </div>
            <div class="cards-group">
              <div class="bottom_menu">
                <div class="left">
                  <img src="../../static/img/send.png" alt="" class="main_logo">
                  <a href="#" class="main_text">Заявки</a>
                </div>
                <p>0</p>
              </div>
              <div class="bottom_menu" style="display: block; padding: 20px;">
                <div class="avatar-top">
                  <div class="left-container" style="display: flex; align-items: center;">
                    <img src="https://images.stopgame.ru/blogs/2021/09/22/c1808x1008/S_DK0TEoWfxyvD6WKtWv8Q/qXH-FKmm.jpg" alt="" class="avatar" style="width: 40px; height: 40px; object-fit: cover; border-radius: 100px;">
                    <div style="margin-left: 10px;">
                      <p id="bottom_header"> Никита </p>
                      <p id="bottom_subheader"> Владелец </p>
                    </div>
                  </div>  
                  <div class="dropdown_btn">
                    <button @click="toggleDropdown" class="dropdown" :style="{ 'background-color': showDropdown ? '#F3F6F8' : 'transparent' }">
                      <img v-if="!showDropdown" src="../../static/img/kebab.svg" alt="Open">
                      <img v-if="showDropdown" src="../../static/img/x.svg" alt="Close">
                    </button>
                  </div>
                </div>
                <div class="avatar-bottom">
                  <img src="../../static/img/Union.png" alt="">
                  <p id="bottom_sub_text">Название компании</p>
                </div>
                <div v-if="showDropdown" class="dropdown-menu">
                  <router-link to="/lk/settings" style="text-decoration:none">
                    <div class="dropdown-item">
                      <div class="dropdown-header">Настройка профиля</div>
                    </div>
                  </router-link>
                  <div class="line"></div>
                  <div class="dropdown-item">
                    <div class="dropdown-header">Тарифный план</div>
                  </div>
                  <div class="dropdown-item">
                    <div class="dropdown-subheader" @click="logout">Выйти из аккаунта</div>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDropdown: false,
    };
  },
  computed: {
      userData() {
        return this.$store.getters.getRegistrationData;
      },
    },

  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    logout() {
        // Вызываем действие clearRegistrationData для очистки данных из Vuex
        this.$store.dispatch('clearRegistrationData');
        this.$router.push('/');
      },
  },
};
</script>

<style scoped>
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
  font-family: TT Norms;
  font-size: 14px;
  font-weight: bold;
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
}
.bottom_menu{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 20px;
  margin: 10px 0;
  transition: all .2s ease;
  text-align: left;
  background-color: #FFFFFF;
  border-radius: 5px;
}

.bottom_menu p{
  background-color: #EFEFFF;
  border-radius: 20px;
  color: #535C69;
  font-size: 12px;
  padding: 5px;
}

#bottom_header{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: bold;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
  margin-bottom: 5px;
}
#bottom_subheader{
  font-family: TT Norms;
  font-size: 12px;
  font-weight: 300;
  line-height: 12px;
  letter-spacing: 0em;
  color: #535C69;
}
#bottom_sub_text{
  font-family: TT Norms;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: center;
  color:#AFB6C1;
}

.active .main_menu {
  background-color: white;
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
  transition: background-color 0.3s ease;
}
.dropdown:hover{
  border: 1px solid #535C69;
}
.dropdown-menu {
  width: 171px;
  height: 105px;
  background-color: white;
  position: absolute;
  bottom: 0;
  left: 280px;
  bottom: 50px;
  border: 1px solid #E4EAEF;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.dropdown-item {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.dropdown-header{
  font-family: TT Norms;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  color: #AFB6C1;
}
.dropdown-header:hover {
  font-weight: bold;
  color: #535C69;
}
.dropdown-subheader{
  font-family: TT Norms;
  font-size: 13px;
  font-weight: 500;
  line-height: 13px;
  letter-spacing: 0em;
  color: #F97F7F;
}
.dropdown-subheader:hover {
  font-weight: bold;
  color: #F97F7F;
}
</style>