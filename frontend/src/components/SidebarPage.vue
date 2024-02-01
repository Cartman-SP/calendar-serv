<template>
    <div class="main_side">
        <img src="../../static/img/SkedOnline.png" alt="" class="logotype">
        <div class="main_application">
            <div class="main_first_application">
                <div class="main_menu" style="margin-top: 45px;">
                    <img src="../../static/img/list.png" alt="" class="main_logo">
                    <a href="#" class="main_text">Услуги</a>
                </div>
                <div class="main_menu" style="margin-top: 25px;">
                    <img src="../../static/img/list.png" alt="" class="main_logo">
                    <a href="#" class="main_text">Сотрудники</a>
                </div>
                <div class="main_menu" style="margin-top: 25px;">
                    <img src="../../static/img/list.png" alt="" class="main_logo">
                    <a href="#" class="main_text">Филиалы</a>
                </div>
            </div>
            <div class="main_second_application">
              <div class="main_menu" style="margin-top: 45px;"> 
                <img src="../../static/img/list.png" alt="" class="main_logo">
                <a href="#" class="main_text">Виджеты</a>
              </div>
              <div class="main_menu" style="margin-top: 25px;">
                <img src="../../static/img/list.png" alt="" class="main_logo">
                <a href="#" class="main_text">Календарь</a>
              </div>
              <div class="main_menu" style="margin-top: 25px;">
                <img src="../../static/img/list.png" alt="" class="main_logo">
                <a href="#" class="main_text">Клиенты</a>
              </div>
            </div>
            <div class="_main_third_application" style="margin-top: 45px;">
              <div class="main_menu">
                <img src="../../static/img/list.png" alt="" class="main_logo">
                <a href="#" class="main_text">Статистика</a>
              </div>
            </div>
        </div>
      </div>
</template>

<script>
export default {

}
</script>

<style>
.main_side {
    position: fixed;
    background-color: #F0F0FD;
    height: 100vh;
    width: 260px;
    border-radius: 10px;
    top: 0;
    left: 0;  
  }

.main_menu{
    padding-left: 60px;
}

.main_logo {
    background-color: #6266EA;  /* Задний фон цвета #6266EA */
    margin-right: 10px
}

.logotype{
    margin-top: 50px;

}
</style>