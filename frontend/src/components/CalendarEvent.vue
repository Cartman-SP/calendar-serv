<template>
  <div class="event-container">
    <div class="event" :style="{ borderColor: color }" @blur="about = false, colorEditor = false" @click="about = true, colorEditor = false" tabindex="1"  @contextmenu.prevent="colorEditor = true, about = false">
        <p class="event-name" v-text-ellipsis="eventName">{{ eventName }}</p>
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

    <div v-if="colorEditor" class="color-editor">
      <button class="deleteBtn">
        <svg data-v-62f0bed8="" style="margin-right: 5px;" width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path data-v-62f0bed8="" fill-rule="evenodd" clip-rule="evenodd" d="M3.44318 2.05556C3.44318 1.6797 3.7637 1.375 4.15909 1.375H10.8409C11.2363 1.375 11.5568 1.6797 11.5568 2.05556C11.5568 2.43142 11.2363 2.73611 10.8409 2.73611H4.15909C3.7637 2.73611 3.44318 2.43142 3.44318 2.05556ZM2.96591 5.45833H2.25V4.09722H12.75V5.45833H12.0341V11.1296C12.0341 12.5078 10.8589 13.625 9.4091 13.625H5.59091C4.14116 13.625 2.96591 12.5078 2.96591 11.1296V5.45833ZM10.6023 5.45833H4.39773V11.1296C4.39773 11.7561 4.93194 12.2639 5.59091 12.2639H9.4091C10.0681 12.2639 10.6023 11.7561 10.6023 11.1296V5.45833Z" fill="#F97F7F"></path></svg>
        Удалить
      </button>
      <div class="colors-row">
        <div class="color-circle" style="background-color: #F97F7F;"></div>
        <div class="color-circle" style="background-color: #F4511E;"></div>
        <div class="color-circle" style="background-color: #FFCF7D;"></div>
        <div class="color-circle" style="background-color: #33B679;"></div>
        <div class="color-circle" style="background-color: #158048;"></div>
      </div>
      <div class="colors-row" style="margin-top: 10px;">
        <div class="color-circle" style="background-color: #3DB4EE;"></div>
        <div class="color-circle" style="background-color: #5062C7;"></div>
        <div class="color-circle" style="background-color: #7986CB;"></div>
        <div class="color-circle" style="background-color: #B24ECD;"></div>
        <div class="color-circle" style="background-color: #616161;"></div>
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
          colorEditor: false,

          eventName: 'q24432wd',
        };
    },
    methods: {
      adjustText() {
        const containerWidth = document.querySelector('.event').clientWidth;
        const eventName = this.eventName;
        const eventNameElement = document.querySelector('.event-name');

        if (eventNameElement.scrollWidth > containerWidth) {
          eventNameElement.innerHTML = eventName + '...'; // Добавим многоточие, если текст не помещается
        } else {
          eventNameElement.innerHTML = eventName; // Оставим текст без изменений
        }
      }
    },
    mounted() {
      this.adjustText();
      window.addEventListener('resize', this.adjustText);
    },
    beforeUnmount() {
      window.removeEventListener('resize', this.adjustText);
    }
}
</script>

<style scoped>
.color-circle{
  width: 30px;
  height: 30px;
  border-radius: 15px;
  cursor: pointer;
}
.colors-row{
  display: flex;
  gap: 15px;
  align-items: center;
  justify-content: space-between;
}
.deleteBtn{
  background-color: white;
  font-family: TT Norms Medium;
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  text-align: left;
  color: #AFB6C1;
}
.color-editor{
  position: absolute;
  background-color: white;
  padding: 20px;
}
.about{
  position: absolute;
  background-color: white;
  filter: drop-shadow(0 0 10px rgb(233, 233, 233));
}
.event-container{
  position: relative;
  width: 100%;
}
.event{
  margin: 5px;
  padding: 15px;
  border: solid 1px #FFCF7D;
  border-radius: 5px;
  background-color: white;
  transition: all .2s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.event:hover{
    filter: drop-shadow(0 0 10px rgb(233, 233, 233));
}
.event-name{
  overflow: hidden;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.event-name, .event-time{
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  font-family: TT Norms Medium;
  font-size: 18px;
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
  font-size: 10px;
  font-weight: 500;
  line-height: 10px;
  text-align: left;
  color: #AFB6C1;
  margin: 0;
}
.about-header{
  font-family: TT Norms Medium;
  font-size: 14px;
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