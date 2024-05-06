<template>
  <div class="main_card">
    <div class="mark_container">
      <div class="mark" v-if="!Mark" @click="Mark = true"></div>
      <div class="mark_active" v-else @click="Mark = false">
        <img src="../../static/img/checkmark.svg" alt="">
      </div>
      <div class="text_container">
        <p class="mark_text">Завершен</p>
      </div>
    </div>
    <p class="date_text">29.04.2024 , 10:49</p>
    <div class="container">
      <p class="client_text">Куричев Иван</p>
      <div class="client_container">
        <p class="client_text">+7 707 877 55 66</p>
        <img src="../../static/img/copy.svg" alt="">
      </div>
      <div class="client_container">
        <p class="client_text">#245353453</p>
        <img src="../../static/img/copy.svg" alt="">
      </div>
    </div>
    <div class="container">
      <div class="client_container">
        <p class="client_subtext">Сотрудник</p>
        <p class="client_text">Егор Барбержопер</p>
      </div>
      <div class="client_container">
        <p class="client_subtext">Название услуги</p>
        <p class="client_text">Стрижка и оформление бороды</p>
      </div>
      <div class="client_container">
        <p class="client_subtext">Стоимость</p>
        <p class="client_text">8000 ₸</p>
      </div>
    </div>
    <div class="keys">
      <img src="../../static/img/cog.svg" alt="" class="">
      <img src="../../static/img/copy_2.svg" alt="" class="">
      <img src="../../static/img/delete.svg" alt="" class="">
    </div>
  </div>
</template>

<script>
export default {
  data() {
      return {
        Mark: false,
      }
  },
}
</script>

<style scoped>
.main_card{
    width: 100%;
    padding: 20px 10px;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: 1fr;
    align-items: center;
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
  background: var(--color-global);
  user-select:none;
}
.text_container{
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
.mark_text{
  font-family: TT Norms Medium;
  font-size: 12px;
  line-height: 14.16px;
  text-align: left;
  color: #FFFFFF;
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
  justify-content: center;
}
</style>