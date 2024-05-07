<template>
  <div class="event-container">
    <div class="event" :style="{ borderColor: color }" @blur="about = false" @click="about = true" tabindex="1">
        <p class="event-name">Стрижка1231231231231212123</p>
        <p class="event-time">7:30</p>
    </div>
    <div v-if="about" class="about">
      <div class="left">
        <div class="text-block">
          <p class="about-subHeader">Услуга</p>
          <p class="about-header">Стрижка + оформление бороды</p>
        </div>
        <div class="text-block">
          <p class="about-subHeader">Специалист</p>
          <p class="about-header">Паскуда Николаевич</p>
        </div>
        <div class="text-block-row">
          <div class="text-block">
            <p class="about-subHeader">Стоимость</p>
            <p class="about-header">9000 тнг</p>
          </div>
          <div class="text-block">
            <p class="about-subHeader">Время записи</p>
            <p class="about-header">17 апреля - 18:30</p>
          </div>
        </div>
        <router-link class="more" :to="'/'">Подробнее</router-link>
      </div>
      <div class="right">
        <svg class="close-icon" @click="about = false" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="20" height="20" rx="10" fill="#FAFAFA"/>
        <path d="M9.15143 9.99994L6.57568 12.5757L7.42421 13.4242L9.99996 10.8485L12.5757 13.4242L13.4242 12.5757L10.8485 9.99994L13.4242 7.42421L12.5757 6.57568L9.99996 9.15141L7.42423 6.57568L6.5757 7.42421L9.15143 9.99994Z" fill="#AFB6C1"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props:['color', 'eventData'],
    data() {
        return {
          about: false,
        };
    },
}
</script>

<style scoped>
.about{
  position: absolute;
  background-color: white;
  filter: drop-shadow(0 0 10px rgb(233, 233, 233));
}
.event-container{
  position: relative;
}
.event{
  margin: 5px;
  padding: 10px;
  border: solid 1px #FFCF7D;
  border-radius: 5px;
  width: 100%;
  background-color: white;
  transition: all .2s ease;
  cursor: pointer;
}



.event:hover{
    filter: drop-shadow(0 0 10px rgb(233, 233, 233));
}
.event-name{
  max-width: 6vw;
}

.event-name, .event-time{
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 16px;
  text-align: left;
  margin: 0;
  color: #535C69;
}

.about{
  border-radius: 5px;
  padding: 10px;
  min-width: 200px;
  width: fit-content;
  display: flex;
  align-items: start;
  justify-content: space-between;
  opacity: 1;
  transition: all .2s ease;
}

.about-subHeader{
  font-family: TT Norms Medium;
  font-size: 8px;
  font-weight: 500;
  line-height: 10px;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
}
.about-header{
  font-family: TT Norms Medium;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  text-align: left;
  color: #535C69;
  margin: 0;
}

.text-block{
  display: flex;
  flex-direction: column;
  gap: 0px;
}

.left{
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.text-block-row{
  display: flex;
  align-items: center;
  gap: 30px;
}

.more{
  font-family: TT Norms Medium;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  text-align: left;
  color: #AFB6C1;
  text-decoration: none;
}

.close-icon:hover{
  cursor: pointer;
}
.close-icon:hover path{
  fill: #AFB6C1;
  transition: all .2s ease;
}
.close-icon:hover path{
  fill: #F4511E;
  transition: all .2s ease;
}
</style>