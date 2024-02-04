<template>
  <div class="sidebar">
    <div class="main_side">
        <img src="../../static/img/SkedOnline.png" alt="" class="logotype">
        <div class="content">
          <div class="top-group">
            <div class="cards-group">
                <div class="main_menu">
                    <img src="../../static/img/list.png" alt="" class="main_logo">
                    <a href="#/main/service" class="main_text">Услуги</a>
                </div>
                <div class="main_menu">
                    <img src="../../static/img/group.png" alt="" class="main_logo">
                    <a href="#/main/personal" class="main_text">Сотрудники</a>
                </div>
                <div class="main_menu">
                    <img src="../../static/img/briefcase.png" alt="" class="main_logo">
                    <a href="#/main/branch" class="main_text">Филиалы</a>
                </div>
            </div>
            <div class="line"></div>
            <div class="cards-group">
              <div class="main_menu">
                <img src="../../static/img/plug.png" alt="" class="main_logo">
                <a href="#/main/widgets" class="main_text">Виджеты</a>
              </div>
              <div class="main_menu">
                <img src="../../static/img/calendar.png" alt="" class="main_logo">
                <a href="#" class="main_text">Календарь</a>
              </div>
              <div class="main_menu">
                <img src="../../static/img/group.png" alt="" class="main_logo">
                <a href="#" class="main_text">Клиенты</a>
              </div>
              <div class="main_menu">
                <img src="../../static/img/arrow.png" alt="" class="main_logo">
                <a href="#" class="main_text">Статистика</a>
              </div>
            </div>
          </div>
            <div class="cards-group">
              <div class="bottom_menu">
                <div class="left">
                  <img src="../../static/img/send.png" alt="" class="main_logo">
                  <a href="#" class="main_text">Заявки</a>
                </div>
                <p>12</p>
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
                  <button>...</button>
                </div>
                <div class="avatar-bottom">
                  <img src="../../static/img/Union.png" alt="">
                  <p id="bottom_sub_text">Барбершоп на</p>
                </div>
              </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.avatar-bottom{
  margin-top: 10px;
  background-color: #fafafa;
  padding: 2px;
}
#bottom_header{
  color: #535C69;
}

#bottom_header, #bottom_subheader, #bottom_sub_text{
  background-color: transparent;
  margin: 0;
  padding: 0;
}
.avatar-top, .avatar-bottom{
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sidebar{
  padding: 30px;
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
  font-weight: 500;
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
    padding: 15px 20px;
    transition: all .2s ease;
    background-color: transparent;
    border-radius: 5px;
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
  font-weight: bold;
  padding: 5px;
}
.bottom_header{
  font-family: TT Norms;
  font-size: 14px;
  font-weight: bold;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
}
.bottom_subheader{
  font-family: TT Norms;
  font-size: 12px;
  font-weight: 300;
  line-height: 12px;
  letter-spacing: 0em;
  color: #535C69;

}
.bottom_container{
  display: flex;
  flex-direction: row;
}
.bottom_sub_text{
  font-family: TT Norms;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  letter-spacing: 0em;
  text-align: center;
  color:#AFB6C1;

}
</style>