<template>
    <div class="main_side">
        <img src="../../static/img/SkedOnline.png" alt="" class="logotype">
        <div class="main_application">
            <div class="main_first_application">
                <div class="main_menu" style="margin-top: 45px;">
                    <img src="../../static/img/list.png" alt="" class="main_logo">
                    <a href="#/main/service/" class="main_text">Услуги</a>
                </div>
                <div class="main_menu" style="margin-top: 25px;">
                    <img src="../../static/img/group.png" alt="" class="main_logo">
                    <a href="#" class="main_text">Сотрудники</a>
                </div>
                <div class="main_menu" style="margin-top: 25px;">
                    <img src="../../static/img/briefcase.png" alt="" class="main_logo">
                    <a href="#" class="main_text">Филиалы</a>
                </div>
            </div>
            <div class="main_second_application">
              <div class="main_menu" style="margin-top: 45px;"> 
                <img src="../../static/img/plug.png" alt="" class="main_logo">
                <a href="#" class="main_text">Виджеты</a>
              </div>
              <div class="main_menu" style="margin-top: 25px;">
                <img src="../../static/img/calendar.png" alt="" class="main_logo">
                <a href="#" class="main_text">Календарь</a>
              </div>
              <div class="main_menu" style="margin-top: 25px;">
                <img src="../../static/img/group.png" alt="" class="main_logo">
                <a href="#" class="main_text">Клиенты</a>
              </div>
            </div>
            <div class="_main_third_application" style="margin-top: 45px;">
              <div class="main_menu">
                <img src="../../static/img/arrow.png" alt="" class="main_logo">
                <a href="#" class="main_text">Статистика</a>
              </div>
            </div>
        </div>
        <DataTestPage/>
      </div>
</template>

<script>
import DataTestPage from './DataTestPage.vue'

export default {
  components: { DataTestPage },
}
</script>

<style scoped>
.main_side {
    margin: 30px;
    background-color: #F3F6F8;
    height: 100vh;
    width: 260px;
    border-radius: 10px;
    top: 0;
    left: 0;  
  }

.main_text{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: 500;
  line-height: 21px;
  letter-spacing: 0em;
  text-align: center;
  text-decoration: none;

}

.main_menu{
    padding-left: 60px;
    text-align: left;
}

.main_logo {
    margin-right: 10px
}

.logotype{
    margin-top: 25px;

}
</style>