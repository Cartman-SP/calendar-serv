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
          :options="['Пушкинский', 'Новый', 'Я люблю пельмени', 'Тест']"
          :searchable="true"
          :placeholderdata="'Выбрать филиал'"
          @input="option => selectedBranch = option"
          />
        </div>
        <div class="choose-block">
          <p class="header">Выбрать сотрудника</p>
          <SelectPage
        :options="['Кологривый','РЫНДЫЧ','влади дади','Шишадмин' ]"
        :placeholderdata="'Выбрать Сотрудника'"
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
      <div class="table">
        <div class="cell" v-for="i in 7" :key="i">
          <CalendarEvent :color="'#FFCF7D'"/>
        </div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
        <div class="cell" v-for="i in 7" :key="i"></div>
      </div>
    </div>
  </div>
</template>

<script>
import SelectPage from '../components/SelectPage.vue';
import CalendarEvent from '../components/CalendarEvent.vue';
export default{
  components: {SelectPage, CalendarEvent}
}
</script>

<style scoped>
.calendar{
  display: flex;
  justify-content: start;
  align-items: start;
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
  min-width: 150px;
  max-width: 200px;
  display: flex;
  align-items: start;
  gap: 5px;
}

.day-num{
  font-family: TT Norms Medium;
  font-size: 28px;
  font-weight: 500;
  line-height: 28px;
  text-align: center;
  color: #535C69;
}

.day-name{
  font-family: TT Norms Medium;
  font-size: 16px;
  font-weight: 500;
  line-height: 16px;
  text-align: center;
  color: #AFB6C1;
}

.schedule{
  width: 100%;
  margin-left: 20px;
}

.date-block{
  background-color: white;
  padding: 20px;
}

.calendar-block{
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.table{
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(16, 1fr);
  background-color: white;
  max-height: 80vh;
  width: 100%;
  overflow: scroll;
}
.empty-row-up{
  border: 1px solid #e7eaee;
  width: 100%;
  height: 20px;
  border-radius: 5px 5px 0 0;
  background-color: white;
}

.table > * {
  border: 1px solid #e7eaee;
  width: 100%;
  height: 70px;
}

.cell{
  align-items: center;
  display: flex;
  width: 100%;
  height: 100%;
}

</style>