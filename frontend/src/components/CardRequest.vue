<template>
  <div class="main_card">
    <div class="mark_container">
      <div class="mark" v-if="!Mark" @click="Mark = true"></div>
      <div class="mark_active" v-else @click="Mark = false">
        <svg width="14" height="14" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M16.2556 6.15492L9.05226 14.4665L4.29285 9.7071L5.70706 8.29289L8.94764 11.5335L14.7443 4.84506L16.2556 6.15492Z" fill="#FFFFFF"/>
        </svg>
      </div>
      <div class="text_container">
        <p class="mark_text">{{ requestData.status }}</p>
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
      <div class="client_wrapper">
        <p class="client_subtext">Сотрудник</p>
        <p class="client_text">Егор Барбержопер</p>
      </div>
      <div class="client_wrapper">
        <p class="client_subtext">Название услуги</p>
        <p class="client_text">Стрижка и оформление бороды</p>
      </div>
      <div class="client_wrapper">
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
  props: ['requestData'],
  data() {
      return {
        Mark: false,
      }
  },
}
</script>

<style scoped>
.client_container{
  display: flex;
  gap: 5px;
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
}
</style>