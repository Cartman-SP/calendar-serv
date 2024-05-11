<template>
  <div class="calendar">
    <div class="calendar-block">
      <div class="date-block">
        <button style="width: 100%; margin-bottom: 20px;i">
          <svg style="rotate: 45deg;" width="15" height="15" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8.58578 10L4.29288 14.2929L5.70709 15.7071L10 11.4142L14.2929 15.7071L15.7071 14.2929L11.4142 10L15.7071 5.70712L14.2929 4.29291L10 8.58579L5.70712 4.29291L4.29291 5.70712L8.58578 10Z" fill="white"/>
          </svg>
          Создать запись
        </button>
        <CalendarDisplay v-model="date" inline showWeek>
          <template #header>
            <div class="date-picker">
              <div class="monthes">
                <svg width="13" height="12" viewBox="0 0 13 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M8.45518 1.57605L9.30371 2.42458L5.60297 6.12531L9.30371 9.82605L8.45518 10.6746L3.90592 6.12531L8.45518 1.57605Z" fill="#AFB6C1"/>
                </svg>
                <p class="month">Апрель 2024</p>
                <svg width="7" height="10" viewBox="0 0 7 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M1.54482 9.42395L0.696289 8.57542L4.39703 4.87469L0.696289 1.17395L1.54482 0.325422L6.09408 4.87469L1.54482 9.42395Z" fill="#AFB6C1"/>
                </svg>
              </div>
            </div>
          </template>
        </CalendarDisplay>


      </div>
      <div class="chooses">
        <div class="choose-block">
          <p class="header">Выбрать филиал</p>
          <SelectPage
          :options="['Пушкинский', 'Новый', 'Я люблю пельмени', 'Тест 2']"
          :searchable="true"
          :placeholderdata="'Выбрать филиал'"
          @input="option => selectedBranch = option"
          />
        </div>
        <div class="choose-block">
          <p class="header">Выбрать сотрудника</p>
          <SelectPage
        :options="['Кологривый','РЫНДЫЧ','влади дади','Шишадмин' ]"
        :placeholderdata="'Выбрать cотрудника'"
        :searchable="true"
        @input="option => selectedEmployee = option"
        />
        </div>
      </div>
    </div>
    <div class="schedule">
      <div class="dates">
        <div class="day">
          <h1 class="day-num">14</h1>
          <p class="day-name">пн</p>
        </div>
        <div class="day">
          <h1 class="day-num">15</h1>
          <p class="day-name">вт</p>
        </div>
        <div class="day">
          <h1 class="day-num">16</h1>
          <p class="day-name">ср</p>
        </div>
        <div class="day">
          <h1 class="day-num">17</h1>
          <p class="day-name">чт</p>
        </div>
        <div class="day">
          <h1 class="day-num">18</h1>
          <p class="day-name">пт</p>
        </div>
        <div class="day">
          <h1 class="day-num">19</h1>
          <p class="day-name">сб</p>
        </div>
        <div class="day">
          <h1 class="day-num">20</h1>
          <p class="day-name">вс</p>
        </div>
      </div>
      <div class="empty-row-up"></div>
      <div class="table-container">
        <div class="table-full">
          <div class="time-table">
            <p>06:00</p>
            <p>07:00</p>
            <p>08:00</p>
            <p>09:00</p>
            <p>10:00</p>
            <p>11:00</p>
            <p>12:00</p>
            <p>13:00</p>
            <p>14:00</p>
            <p>15:00</p>
            <p>16:00</p>
            <p>17:00</p>
            <p>18:00</p>
            <p>19:00</p>
            <p>20:00</p>
            <p>21:00</p>
            <p>22:00</p>
          </div>
          <div class="table">
            <div v-for="i in timeSlots" :key="i" class="table-row">
              <div class="cell" v-for="j in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']" :key="j" :style="{ 'background-color': i === 'Сб' || i === 'Вс' ? 'rgba(98, 102, 234, 0.02)' : 'white' }">
                <div v-for="e in events" :key="e.id" v-show="j === e.day">
                  <CalendarEvent :eventData="e" :color="'#FFCF7D'" v-if="j === e.day && i === e.time"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="empty-row-down"></div>
      <button @click="console.log(timeSlots)">log slots</button>
    </div>
  </div>
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import CalendarEvent from '../components/CalendarEvent.vue';

export default{
  components: {SelectPage, CalendarEvent},
  data(){
    return{
      events:[
        {
            id: '1',
            name: 'Ноготочки',
            day: 'Пн',
            time: '13:00 - 14:00',
            color: '#33B679',
          },
          {
            id: '2',
            name: 'Прическа XXL',
            day: 'Ср',
            time: '15:00 - 16:00',
            color: '#3DB4EE',
          },
          {
            id: '3',
            name: 'Прическа M',
            day: 'Вт',
            time: '11:00 - 12:00',
            color: '#B24ECD',
          }
        ]
    }
  },
  computed: {
    timeSlots() {
        const slots = [];
        for (let i = 6; i <= 22; i++) {
            const startTime = `${i < 10 ? '0' : ''}${i}:00`;
            const endTime = `${i + 1 < 10 ? '0' : ''}${i + 1}:00`;
            slots.push(`${startTime} - ${endTime}`);
        }
        return slots;
    }
  }
}
</script>

<style scoped>
.calendar{
  display: flex;
  justify-content: start;
  align-items: start;
  gap: 20px;
  width: 100%;
  overflow-x: scroll;
}
.chooses{
  background-color: white;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.header{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
  margin: 0;
  margin-bottom: 5px;
  text-align: left;
}
.monthes{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}

.month{
  font-family: TT Norms Medium;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0em;
  color: #535C69;
  margin: 0;
  margin-bottom: 1px;
  text-align: left;
}

.dates{
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

.day{
  max-width: 200px;
  display: flex;
  align-items: start;
  gap: 5px;
}

.day-num{
  font-family: TT Norms Medium;
  font-size: 40px;
  font-weight: 500;
  line-height: 28px;
  text-align: center;
  color: #535C69;
}

.day-name{
  font-family: TT Norms Medium;
  font-size: 20px;
  font-weight: 500;
  line-height: 16px;
  text-align: center;
  color: #AFB6C1;
}

.schedule{
  width: 100%;
}

.dates{
  margin-left: 50px;
}

.date-block{
  background-color: white;
  padding: 20px;
}

.calendar-block{
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: fit-content;
}

.table{
  display: grid;
  grid-template-rows: repeat(1, 90px);
  width: 100%;
}

.table-row{
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  width: 100%;
}

/* .table-row:nth-child(even){
  filter: brightness(97%);
} */

.table-container{
  display: flex;
  overflow-y: scroll;
  overflow-x: hidden;
  height: 70vh;
}

.table-full{
  width: 100%;
  display: flex;
}

.time-table{
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  grid-template-rows: repeat(16, 1fr);
}

.time-table p{
  font-family: TT Norms Medium;
  font-size: 14px;
  font-weight: 500;
  line-height: 10px;
  text-align: center;
  color: #AFB6C1;
  height: 90px;
  margin: 0;
  width: 50px;
}
.empty-row-up{
  margin-left: 50px;
  border: 1px solid #e7eaee;
  height: 20px;
  border-radius: 5px 5px 0 0;
  background-color: white;
}

.empty-row-down{
  margin-left: 50px;
  border: 1px solid #e7eaee;
  height: 20px;
  border-radius: 0 0 5px 5px;
  background-color: white;
}

.table-row > * {
  border: 1px solid #e7eaee;
  width: 100%;
  background-color: white;
}

.cell{
  align-items: center;
  display: grid; /* Используем display: grid */
  grid-template-columns: 1fr; /* Одна колонка */
  height: 90px;
  min-width: 150px;
  padding: 5px;
}

@media (max-width: 1641px){
  .calendar-block{
    display: none;
  }
}
</style>